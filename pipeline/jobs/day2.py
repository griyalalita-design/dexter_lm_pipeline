import copy
import time
from datetime import datetime, timedelta

import pandas as pd

from utils.metabase import tarik_metabase, get_token
from utils.gsheet import read_sheet, write_sheet
from config.settings import METABASE_CONFIG, GSHEET
from utils.transform import (
    transform_attempt,
    transform_n0_completion,
    transform_n1_completion,
    transform_completion_timeslot,
    transform_lnd,
    transform_rsvn_completed,
    transform_poda,
    transform_pu_rot,
    transform_td6,
    transform_rdo_rtd,
)


SHIPPER_GROUPS = {
    "agg_fsbd": [
        "FSBD Key Shipper",
        "Aggregator Keyshipper",
    ],
    "b2c_cc_agg_fsbd": [
        "B2C Cold Chain Sameday",
        "B2C Cold Chain Next Day",
        "FSBD Key Shipper",
        "Aggregator Keyshipper",
    ],
    "b2b_all_b2c_cc": [
        "B2B Dry Reguler",
        "B2B Sameday Reguler",
        "B2B Sameday Premium",
        "B2C Cold Chain Sameday",
        "B2C Cold Chain Next Day",
    ],
    "b2b_dry_cc_next": [
        # "B2B Dry Reguler",
        "B2C Cold Chain Next Day",
    ],
    "b2b_sds_dry_cold_prem": [
        "B2B Sameday Premium",
        # "B2C Cold Chain Sameday",
    ],
    "b2b_sds_dry_cold_reg": [
        "B2B Sameday Reguler",
        "B2C Cold Chain Sameday",
    ],
    "b2br_key_shipper": [
        "B2B Dry Reguler",
        "B2B Sameday Reguler",
        "B2B Sameday Premium",
        "FSBD Key Shipper",
        "Aggregator Keyshipper",
    ],
    "sds_cc": [
        "B2B Sameday Reguler",
        "B2B Sameday Premium",
        "B2C Cold Chain Sameday",
        "B2C Cold Chain Next Day",
    ],
    "aggregator": [
        "Aggregator Keyshipper",
    ],
}


LM_REPORT_PLAN = [
    # Attempt Rate N0
    {"report_key": "attempt_n0", "segment_key": "agg_fsbd"},
    {"report_key": "attempt_n0", "segment_key": "b2c_cc_agg_fsbd"},
    {"report_key": "attempt_n0", "segment_key": "laz_shop_tt"},

    # Completion N0
    {"report_key": "n0_completion", "segment_key": "b2b_all_b2c_cc"},
    {"report_key": "n0_completion", "segment_key": "b2b_dry_cc_next"},
    {"report_key": "n0_completion", "segment_key": "tt"},

    # Completion N1
    {"report_key": "n1_completion"},

    # Others
    {"report_key": "completion_within_timeslot"},
    {"report_key": "lnd_b2b_all_b2c_cc"},
    {"report_key": "no_rsvn_completed"},
    {"report_key": "no_rsvn_completed", "segment_key": "b2br_key_shipper"},
    {"report_key": "no_rsvn_completed", "segment_key": "sds_cc"},
    {"report_key": "poda_val_sho_laz"},
    {"report_key": "pu_rot"},
    {"report_key": "td6", "segment_key": "4pl"},
    {"report_key": "td6", "segment_key": "aggregator"},
    {"report_key": "td6", "segment_key": "shop_laz"},
    {"report_key": "rdo_rtd_b2b"},
]


def get_previous_month_period():
    today = datetime.today()
    first_day_this_month = today.replace(day=1)
    last_day_prev_month = first_day_this_month - timedelta(days=1)
    first_day_prev_month = last_day_prev_month.replace(day=1)

    start_date = first_day_prev_month.strftime("%Y-%m-%d")
    end_date = last_day_prev_month.strftime("%Y-%m-%d")
    period_str = f"{start_date}~{end_date}"

    return start_date, end_date, period_str


def build_shipper_group_values():
    print("\n[1/4] Read Key Shipper...")

    df = read_sheet(
        GSHEET["key_shipper"]["sheet_id"],
        GSHEET["key_shipper"]["tabs"]["main"],
    )

    df.columns = df.columns.astype(str).str.strip()

    required_cols = ["Type", "Shipper ID"]
    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Kolom tidak ditemukan di key_shipper: {missing_cols}")

    df["Type"] = df["Type"].astype(str).str.strip()

    df["Shipper ID"] = (
        pd.to_numeric(df["Shipper ID"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
    )

    result = {}

    for group_key, type_list in SHIPPER_GROUPS.items():
        ids = (
            df[df["Type"].isin(type_list)]["Shipper ID"]
            .dropna()
            .drop_duplicates()
            .tolist()
        )

        result[group_key] = ids
        print(f"{group_key}: {len(ids)} shipper_id | sample: {ids[:5]}")

    return result


def render_params(param_templates, runtime_values):
    rendered = []

    for param in param_templates or []:
        p = copy.deepcopy(param)

        if "value_key" in p:
            key = p.pop("value_key")
            p["value"] = runtime_values[key]

        elif isinstance(p.get("value"), str) and p["value"] in runtime_values:
            p["value"] = runtime_values[p["value"]]

        rendered.append(p)

    return rendered


def run_report(report_key, runtime_values, token, segment_key=None):
    cfg = METABASE_CONFIG["lm"][report_key]

    common_params = render_params(
        cfg.get("common_params_template", []),
        runtime_values,
    )

    segment_params = []
    if segment_key:
        segment_params = render_params(
            cfg.get("shipper_params_template", {}).get(segment_key, []),
            runtime_values,
        )

    final_params = common_params + segment_params
    desc = f"{report_key}_{segment_key}" if segment_key else report_key

    print(f"\n[RUN] {desc}")
    print(f"URL: {cfg['url']}")
    print(f"Total params: {len(final_params)}")

    df_result = tarik_metabase(
        url=cfg["url"],
        parameters=final_params,
        token=token,
        desc=desc,
    )

    print(f"{desc} shape: {df_result.shape}")
    print(f"{desc} shape: {df_result.shape}")
    
    print("\nColumns:")
    for col in df_result.columns:
        print(f" - {col}")


    if not df_result.empty:
        print(df_result.head(5).to_string(index=False))
    else:
        print(f"WARNING: {desc} hasil kosong")

    time.sleep(2)

    return df_result


def should_skip_report(report_key):
    if report_key not in METABASE_CONFIG["lm"]:
        return True

    url = METABASE_CONFIG["lm"][report_key].get("url", "")
    return not url or "PASTE_" in url


def run():
    print("=== LM DAY 2 START ===")

    start_date, end_date, period_str = get_previous_month_period()

    print(f"\n[0/4] Period")
    print(f"start_date : {start_date}")
    print(f"end_date   : {end_date}")
    print(f"period_str : {period_str}")

    print("\n[1/4] Get Metabase token...")
    token = get_token()
    print("Token loaded:", bool(token))

    shipper_runtime = build_shipper_group_values()

    runtime_values = {
        "start_date": start_date,
        "end_date": end_date,
        "period_str": period_str,
        "start_end": start_date,
        "driver_list": [
            "CDA Driver", "Driver", "Freelance CDA Driver", "Freelance Driver",
            "Junior Coldchain Driver", "Captain Sameday", "Freelance Sameday Driver",
            "Freelance Sameday Rider", "Junior Sameday Rider", "On-call Driver",
            "Rider", "Rider Bulky", "Sameday Rider", "Senior Sameday Rider",
            "SPH Driver", "SPH Leader", "SPH Rider", "SPH+(Plus) Rider",
        ],
        **shipper_runtime,
    }

    results = {}

    print("\n[2/4] Pull selected LM reports...")

    for item in LM_REPORT_PLAN:
        report_key = item["report_key"]
        segment_key = item.get("segment_key")
        result_name = f"{report_key}_{segment_key}" if segment_key else report_key

        if should_skip_report(report_key):
            print(f"SKIP {result_name}: report_key tidak ada atau URL kosong")
            continue

        try:
            results[result_name] = run_report(
                report_key=report_key,
                runtime_values=runtime_values,
                token=token,
                segment_key=segment_key,
            )
        except Exception as e:
            print(f"\n[FAILED] {result_name}")
            print(repr(e))
            results[result_name] = pd.DataFrame()

    print("\n[3/4] Summary raw result shapes:")
    for key, df in results.items():
        print(f"- {key}: {df.shape}")

    print("\n[4/4] Transform tracker outputs...")

    tracker_results = {}

    if "attempt_n0_agg_fsbd" in results:
        tracker_results["attempt_n0_agg_fsbd"] = transform_attempt(results["attempt_n0_agg_fsbd"])

    if "attempt_n0_b2c_cc_agg_fsbd" in results:
        tracker_results["attempt_n0_b2c_cc_agg_fsbd"] = transform_attempt(results["attempt_n0_b2c_cc_agg_fsbd"])

    if "attempt_n0_laz_shop_tt" in results:
        tracker_results["attempt_n0_laz_shop_tt"] = transform_attempt(results["attempt_n0_laz_shop_tt"])

    if "n0_completion_b2b_all_b2c_cc" in results:
        tracker_results["n0_completion_b2b_all_b2c_cc"] = transform_n0_completion(results["n0_completion_b2b_all_b2c_cc"])

    if "n0_completion_b2b_dry_cc_next" in results:
        tracker_results["n0_completion_b2b_dry_cc_next"] = transform_n0_completion(results["n0_completion_b2b_dry_cc_next"])

    if "n0_completion_tt" in results:
        tracker_results["n0_completion_tt"] = transform_n0_completion(results["n0_completion_tt"])

    print("\nSummary tracker output shapes:")
    for key, df in tracker_results.items():
        print(f"- {key}: {df.shape}")

    TRACKER_WRITE_MAP = {
        "attempt_n0_agg_fsbd": [
            {"tracker_key": "tracker_sum", "tab_key": "raw_data_otif", "start_cell": "AT5"},
        ],
        "attempt_n0_b2c_cc_agg_fsbd": [
            {"tracker_key": "tracker_gj", "tab_key": "raw_data_otif", "start_cell": "BD5"},
            {"tracker_key": "tracker_wj", "tab_key": "raw_data_otif", "start_cell": "BD5"},
        ],
        "attempt_n0_laz_shop_tt": [
            {"tracker_key": "tracker_gj", "tab_key": "raw_data_otif", "start_cell": "BJ5"},
        ],
        "n0_completion_b2b_all_b2c_cc": [
            {"tracker_key": "tracker_sum", "tab_key": "raw_data_otif", "start_cell": "AN5"},
        ],
        "n0_completion_b2b_dry_cc_next": [
            {"tracker_key": "tracker_gj", "tab_key": "raw_data_otif", "start_cell": "AX5"},
            {"tracker_key": "tracker_wj", "tab_key": "raw_data_otif", "start_cell": "AX5"},
        ],
        "n0_completion_tt": [
            {"tracker_key": "tracker_wj", "tab_key": "raw_data_otif", "start_cell": "BJ5"},
        ],
    }

    print("\n[WRITE] Dump tracker outputs...")

    for result_key, destinations in TRACKER_WRITE_MAP.items():
        if result_key not in tracker_results:
            print(f"[SKIP] {result_key}: not found in tracker_results")
            continue

        df_to_write = tracker_results[result_key]

        for dest in destinations:
            tracker_key = dest["tracker_key"]
            tab_key = dest["tab_key"]
            start_cell = dest["start_cell"]

            tracker_cfg = GSHEET[tracker_key]
            sheet_id = tracker_cfg["sheet_id"]
            sheet_name = tracker_cfg["tabs"][tab_key]

            print(f"Writing {result_key} -> {tracker_key} | {sheet_name} | {start_cell}")

            write_sheet(
                spreadsheet_id=sheet_id,
                sheet_name=sheet_name,
                df=df_to_write,
                start_cell=start_cell,
                include_header=False,
            )

    print("\n=== LM DAY 2 DONE ===")

    return {
        "raw": results,
        "tracker": tracker_results,
    }


if __name__ == "__main__":
    run()
