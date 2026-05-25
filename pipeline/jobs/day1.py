# ============================================================
# jobs/day1.py - Tanggal 1: Cleansing Tracker
# ============================================================

from config.settings import GSHEET
from utils.gsheet import clear_range


def _iter_ranges(ranges):
    """
    Handle:
    - string tunggal
    - list range
    - None
    """
    if isinstance(ranges, str):
        yield ranges
        return

    for rng in ranges or []:
        if rng:
            yield rng


def clear_tracker_day1_ranges(tracker_key: str) -> None:
    """
    Clear configured ranges for a tracker.
    """

    tracker = GSHEET.get(tracker_key)

    if not tracker:
        print(f"[ERROR] Tracker config '{tracker_key}' tidak ditemukan")
        return

    tracker_id = tracker.get("sheet_id")
    tabs = tracker.get("tabs", {})
    clear_config = tracker.get("clear_ranges", {})

    print(f"\nClearing tracker: {tracker_key}")

    # Loop semua clear config
    for config_key, ranges in clear_config.items():

        tab_name = tabs.get(config_key)

        if not tab_name:
            print(f"[WARNING] Tab mapping '{config_key}' tidak ditemukan")
            continue

        for rng in _iter_ranges(ranges):
            try:
                print(f"  -> Clear {tab_name} | {rng}")
                clear_range(tracker_id, tab_name, rng)

            except Exception as e:
                print(f"  [FAILED] {tab_name} | {rng}")
                print(f"  Error: {e}")


# ==========================
# MAIN RUNNER
# ==========================

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
        clear_tracker_day1_ranges(tracker_key)

    print("\n=== DAY 1 SELESAI ===")


if __name__ == "__main__":
    run()
