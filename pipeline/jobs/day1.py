# ============================================================
# jobs/day1.py - Tanggal 1: Cleansing + Update Key Shipper
# File ini hanya orkestasi, logic ada di utils/
# ============================================================

from config.settings import GSHEET
from utils.gsheet import clear_range, read_sheet
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

    print("\n[1/1] Cleansing tracker...")

    tracker_list = [
        "tracker_gj",
        "tracker_sum",
        "tracker_wj",
        "tracker_cj",
        "tracker_ej",
    ]

    for tracker_key in tracker_list:

        tracker = GSHEET[tracker_key]

        tracker_id = tracker["sheet_id"]
        tabs = tracker["tabs"]
        clear_ranges = tracker.get("clear_ranges", {})

        print(f"\nClearing tracker: {tracker_key}")

        for tab_key, ranges in clear_ranges.items():

            tab_name = tabs.get(tab_key)

            if not tab_name:
                print(f"[SKIP] Tab '{tab_key}' tidak ditemukan")
                continue

            for rng in _iter_ranges(ranges):

                try:

                    print(f"  -> Clear {tab_name} | {rng}")

                    clear_range(
                        tracker_id,
                        tab_name,
                        rng
                    )

                    print("  [SUCCESS]")

                except Exception as e:

                    print(f"  [FAILED]")
                    print(repr(e))

    print("\nDay 1 selesai!")
 


if __name__ == "__main__":
    run()
