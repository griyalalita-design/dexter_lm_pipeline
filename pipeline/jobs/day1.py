# ============================================================
# jobs/day1.py - Tanggal 1: Cleansing Tracker
# ============================================================

from config.settings import GSHEET
from utils.gsheet import clear_range
import time


def _iter_ranges(value):
    """
    Handle:
    - string
    - list
    - tuple
    - None
    """
    if isinstance(value, (list, tuple)):
        return list(value)

    if isinstance(value, str):
        return [value]

    return []


def clear_tracker(tracker_key):
    """
    Clear tracker berdasarkan config settings.py
    """

    tracker = GSHEET[tracker_key]

    tracker_id = tracker["sheet_id"]
    tabs = tracker["tabs"]
    clear_ranges = tracker.get("clear_ranges", {})

    print(f"\nClearing tracker: {tracker_key}")

    # looping semua config clear range
    for tab_key, ranges in clear_ranges.items():

        # skip kalau tab tidak ada
        if tab_key not in tabs:
            print(f"[SKIP] Tab mapping '{tab_key}' tidak ditemukan")
            continue

        tab_name = tabs[tab_key]

        for rng in _iter_ranges(ranges):

            try:
                print(f"  -> Clear {tab_name} | {rng}")

                clear_range(
                    tracker_id,
                    tab_name,
                    rng
                )

                print(f"  [SUCCESS]")

                # kasih delay biar ga kena quota
                time.sleep(1)

            except Exception as e:

                print(f"  [FAILED] {tab_name} | {rng}")
                print(f"  Error: {repr(e)}")

                # delay juga pas gagal
                time.sleep(2)


def run():

    print("=== DAY 1 - CLEANSING TRACKER ===")

    tracker_list = [
        "tracker_gj",
        "tracker_sum",
        "tracker_wj",
        "tracker_cj",
        "tracker_ej",
    ]

    for tracker_key in tracker_list:

        try:
            clear_tracker(tracker_key)

        except Exception as e:

            print(f"\n[ERROR TRACKER] {tracker_key}")
            print(repr(e))

    print("\n=== DAY 1 SELESAI ===")


if __name__ == "__main__":
    run()
