# ============================================================
# utils/transform.py — Semua transformasi data pake pandas
# TIDAK ada API calls di sini, murni transformasi aja
# ============================================================

import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


def get_last_month_range():
    """
    Hitung range bulan lalu.
    Contoh: kalau sekarang April 2026, return (2026-03-01, 2026-03-31, 'Maret')
    """
    today = date.today()
    start_day = (today.replace(day=1) - relativedelta(months=1))
    end_day = today.replace(day=1) - relativedelta(days=1)
    bulan_names = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    bulan_name = bulan_names[first_day.month]
    return start_day, end_day, bulan_name


def categorize_shippers(df_pns: pd.DataFrame):
    """
    Bagi shipper dari Key Shipper ke kategori Day 2.

    Returns:
        dict dengan keys: "b2b_cc", "key_shipper", "lazada_shopee"
        masing-masing berisi list Global ID (int).
    """
    required_cols = ["Global ID", "Shipper Service Category"]
    missing_cols = [c for c in required_cols if c not in df_pns.columns]
    if missing_cols:
        raise ValueError(
            f"Kolom wajib tidak ditemukan di key shipper sheet: {missing_cols}. "
            "Pastikan header: 'Global ID' dan 'Shipper Service Category'."
        )

    df = df_pns.copy()
    df["Shipper Service Category"] = df["Shipper Service Category"].astype(str).str.strip()
    df["Global ID"] = pd.to_numeric(df["Global ID"], errors="coerce")
    df = df[df["Global ID"].notna()]
    df["Global ID"] = df["Global ID"].astype(int)

    b2b_cc_categories = ["B2BR", "B2BR Sameday", "LTL Reguler"]
    key_shipper_category = "FS / BD Key Shipper"

    b2b_cc = (
        df[df["Shipper Service Category"].isin(b2b_cc_categories)]["Global ID"]
        .dropna()
        .astype(int)
        .drop_duplicates()
        .tolist()
    )

    key_shipper = (
        df[df["Shipper Service Category"] == key_shipper_category]["Global ID"]
        .dropna()
        .astype(int)
        .drop_duplicates()
        .tolist()
    )


    print(f"Shipper B2B+CC: {len(b2b_cc)}")
    print(f"Key Shipper: {len(key_shipper)}")

    return {
        "b2b_cc": b2b_cc,
        "key_shipper": key_shipper,
    }

def transform_attempt(df_raw):
    """
    Attempt Rate N0
    Tracker Output:
    Row Labels (dest_hub_name)
    Sum of n0_delivery_attempt_flag
    Sum of vol
    """

    if df_raw.empty:
        return df_raw

    tracker_df = (
        df_raw
        .groupby("dest_hub_name", as_index=False)
        .agg({
            "n0_delivery_attempt_flag": "sum",
            "vol": "sum"
        })
        .sort_values("dest_hub_name")
    )

    return tracker_df





def check_anomaly(df: pd.DataFrame, numeric_cols: list) -> pd.DataFrame:
    """
    Check anomaly di data: DIV/0, N/A, atau nilai kosong.

    Args:
        df           : DataFrame yang mau dicek
        numeric_cols : list kolom numerik yang mau dicek

    Returns:
        DataFrame berisi baris-baris yang anomaly
    """
    anomaly_rows = pd.DataFrame()

    for col in numeric_cols:
        if col not in df.columns:
            continue
        # Check DIV/0 atau string error
        mask_error = df[col].astype(str).str.contains("#DIV|#N/A|#REF|#VALUE", na=False)
        # Check null
        mask_null = df[col].isnull()
        # Check nol (ga ada performance)
        mask_zero = df[col] == 0

        anomaly = df[mask_error | mask_null | mask_zero].copy()
        if len(anomaly) > 0:
            anomaly["anomaly_col"] = col
            anomaly_rows = pd.concat([anomaly_rows, anomaly])

    if len(anomaly_rows) > 0:
        print(f"Ditemukan {len(anomaly_rows)} baris anomaly!")
    else:
        print("Tidak ada anomaly ditemukan.")

    return anomaly_rows.drop_duplicates()
