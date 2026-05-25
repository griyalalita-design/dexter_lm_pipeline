# ============================================================
# jobs/day1.py - Tanggal 1: Cleansing + Update Key Shipper
# File ini hanya orkestasi, logic ada di utils/
# ============================================================

from config.settings import GSHEET
from utils.gsheet import clear_range, open_by_key, read_sheet, copy_range
from utils.transform import get_last_month_range
import pandas as pd



def _iter_ranges(ranges):
    if isinstance(ranges, str):
        yield ranges
        return

    for rng in ranges or []:
        if rng:
            yield rng


def clear_tracker_day1_ranges(tracker_key: str) -> None:
    tracker = GSHEET["tracker_key"]
    tracker_id = tracker["sheet_id"]
    tabs = tracker["tabs"]
    clear_config = tracker.get("clear_ranges", {})

    # Clear Raw Data [All]
    raw_all_tab = tabs.get("raw_data_all")
    raw_all_ranges = _iter_ranges(clear_config.get("raw_data_all", []))
    if raw_all_tab:
        for rng in raw_all_ranges:
            clear_range(tracker_id, raw_all_tab, rng)

    # Clear Raw Data [Cost]
    raw_cost_tab = tabs["raw_data_cost"]
    raw_cost_ranges = _iter_ranges(clear_config.get("raw_data_cost", []))
    for rng in raw_cost_ranges:
        clear_range(tracker_id, raw_cost_tab, rng)

    # Clear Raw Data [Int & Comp]
    raw_int_comp_tab = tabs["raw_data_int_comp"]
    raw_int_comp_ranges = _iter_ranges(clear_config.get("raw_data_int_comp", []))
    for rng in raw_int_comp_ranges:
        clear_range(tracker_id, raw_int_comp_tab, rng)

    # Clear Raw Data [OTIF]
    raw_otif_tab = tabs["raw_data_otif"]
    raw_otif_ranges = _iter_ranges(clear_config.get("raw_data_otif", []))
    for rng in raw_otif_ranges:
        clear_range(tracker_id, raw_otif_tab, rng)

    # Clear [Upload] Hub
    hub_tab = tabs["hub"]
    hub_ranges = _iter_ranges(clear_config.get("hub", []))
    for rng in hub_ranges:
        clear_range(tracker_id, hub_tab, rng)

    # Clear List Staff
    staff_list_tab = tabs["staff_list"]
    staff_list_ranges = _iter_ranges(clear_config.get("staff_list", []))
    for rng in staff_list_ranges:
        clear_range(tracker_id, staff_list_tab, rng)

    # Clear Mapping Area
    mapping_area_tab = tabs["mapping_area"]
    mapping_area_ranges = _iter_ranges(clear_config.get("mapping_area", []))
    for rng in mapping_area_ranges:
        clear_range(tracker_id, mapping_area_tab, rng)

# =================== Buat Cleaning Data Tracker dan Sanggahan ========================== #
def run():
    # _, _, bulan = get_last_month_range()
    # print(f"=== DAY 1 - Persiapan data bulan {bulan} ===")

    # STEP 1: Cleansing Tracker
    print("\n[1/3] Cleansing tracker...")
    #     """
    # Tanggal 1
    # - Cleansing tracker (Raw Data [All], Raw Data [Cost])
    # - Cleansing sanggahan
    # - Copy data PNS -> Keyshipper sheet
    # """

    # 1) Cleansing tracker tabs (keep header + formula columns)
    clear_tracker_day1_ranges("tracker_gj")
    clear_tracker_day1_ranges("tracker_sum")
    clear_tracker_day1_ranges("tracker_wj")
    clear_tracker_day1_ranges("tracker_cj")
    clear_tracker_day1_ranges("tracker_ej")



    print("\nDay 1 selesai! Tracker")


if __name__ == "__main__":
    run()
