# jobs/day6.py
from utils.gsheet import read_sheet, write_sheet
from config.settings import GSHEET


def run():
    print("====== Kita Kerjain Day 10 Buat RDO ya =========")

    df_rdo = read_sheet(
        GSHEET["rdo_comp"]["sheet_id"],
        GSHEET["rdo_comp"]["tabs"]["main"]
    )

    print("===== Ambil data dari RDO done =====")

    print("===== Mulai input ke Tracker dulu ya =====")
    write_sheet(
        spreadsheet_id=GSHEET["tracker_gj"]["sheet_id"],
        sheet_name=GSHEET["tracker_gj"]["tabs"]["raw_data_otif"],
        df=df_rdo,
        start_cell="I5",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_sum"]["sheet_id"],
        sheet_name=GSHEET["tracker_sum"]["tabs"]["raw_data_otif"],
        df=df_rdo,
        start_cell="I5",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_wj"]["sheet_id"],
        sheet_name=GSHEET["tracker_wj"]["tabs"]["raw_data_otif"],
        df=df_rdo,
        start_cell="I5",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_cj"]["sheet_id"],
        sheet_name=GSHEET["tracker_cj"]["tabs"]["raw_data_otif"],
        df=df_rdo,
        start_cell="I5",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_ej"]["sheet_id"],
        sheet_name=GSHEET["tracker_ej"]["tabs"]["raw_data_otif"],
        df=df_rdo,
        start_cell="I5",
        include_header=False
    )
    print("===== Done Input ke Tracker =====")



if __name__ == "__main__":
    run()
