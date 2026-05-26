# ============================================================
# jobs/day1.py - Cleansing Tracker
# ============================================================

import time

from config.settings import GSHEET
from utils.gsheet import clear_range


def _iter_ranges(value):

    if isinstance(value, dict):
        return list(value.values())

    if isinstance(value, (list, tuple)):
        return list(value)

    if isinstance(value, str):
        return [value]

    return []


# ================= SAFE CLEAR ================= #
def safe_clear(sheet_id, tab_name, rng):

    try:

        print(f"  -> Clear {tab_name} | {rng}")

        clear_range(sheet_id, tab_name, rng)

        print("  [SUCCESS]")

    except Exception as e:

        print("  [FAILED]")
        print(e)

    # IMPORTANT: avoid quota exceeded
    time.sleep(2)


# ================= MAIN RUN ================= #
def run():

    print("\n=== DAY 1 - CLEANSING TRACKER ===")

    tracker_conf = GSHEET["tracker"]

    tracker_id = tracker_conf["sheet_id"]

    tabs = tracker_conf["tabs"]

    clear_ranges = tracker_conf.get("clear_ranges", {})

    # Loop semua tab yang ada di clear_ranges
    for tab_key, ranges in clear_ranges.items():

        # Ambil nama tab dari config tabs
        tab_name = tabs.get(tab_key)

        if not tab_name:
            print(f"[SKIPPED] tab config tidak ditemukan: {tab_key}")
            continue

        # Normalize ranges
        normalized_ranges = _iter_ranges(ranges)

        for rng in normalized_ranges:

            safe_clear(
                tracker_id,
                tab_name,
                rng
            )

    print("\n=== DAY 1 SELESAI ===")


if __name__ == "__main__":
    run()
