# ============================================================
# jobs/day1.py - Tanggal 1: Cleansing + Update Key Shipper
# File ini hanya orkestasi, logic ada di utils/
# ============================================================

from config.settings import GSHEET
from utils.gsheet import clear_range, open_by_key, read_sheet
from utils.transform import get_last_month_range
import pandas as pd


def _iter_ranges(value):
    if isinstance(value, dict):
        return list(value.values())
    if isinstance(value, (list, tuple)):
        return list(value)
    if isinstance(value, str):
        return [value]
    return []


def _ranges_for_tab(clear_ranges, tab_key):
    if isinstance(clear_ranges, dict):
        return _iter_ranges(clear_ranges.get(tab_key, []))
    return _iter_ranges(clear_ranges)



# =================== Buat Cleaning Data Tracker dan Sanggahan ========================== #
def run():

    # STEP 1: Cleansing Tracker
    print("\n[1/3] Cleansing tracker...")

    tracker_id = GSHEET["tracker_gj"]["sheet_id"]

    # Clear Raw Data [All]
    raw_all_tab = GSHEET["tracker"]["tabs"]["raw_data_cost"]
    raw_all_ranges = _iter_ranges(GSHEET["tracker"].get("clear_ranges", {}).get("raw_data_cost", []))
    for rng in raw_all_ranges:
        clear_range(tracker_id, raw_all_tab, rng)

    raw_int_tab = GSHEET["tracker"]["tabs"]["raw_data_int_comp"]
    raw_int_ranges = _iter_ranges(GSHEET["tracker"].get("clear_ranges", {}).get("raw_data_int_comp", []))
    for rng in raw_cost_ranges:
        clear_range(tracker_id, raw_cost_tab, rng)

    raw_cost_tab = GSHEET["tracker"]["tabs"]["raw_data_otif"]
    raw_cost_ranges = _iter_ranges(GSHEET["tracker"].get("clear_ranges", {}).get("raw_data_otif", []))
    for rng in raw_cost_ranges:
        clear_range(tracker_id, raw_cost_tab, rng)

    raw_cost_tab = GSHEET["tracker"]["tabs"]["hub"]
    raw_cost_ranges = _iter_ranges(GSHEET["tracker"].get("clear_ranges", {}).get("hub", []))
    for rng in raw_cost_ranges:
        clear_range(tracker_id, raw_cost_tab, rng)

    raw_cost_tab = GSHEET["tracker"]["tabs"]["staff_list"]
    raw_cost_ranges = _iter_ranges(GSHEET["tracker"].get("clear_ranges", {}).get("staff_list", []))
    for rng in raw_cost_ranges:
        clear_range(tracker_id, raw_cost_tab, rng)

    raw_cost_tab = GSHEET["tracker"]["tabs"]["mapping_area"]
    raw_cost_ranges = _iter_ranges(GSHEET["tracker"].get("clear_ranges", {}).get("mapping_area", []))
    for rng in raw_cost_ranges:
        clear_range(tracker_id, raw_cost_tab, rng)

 


if __name__ == "__main__":
    run()
