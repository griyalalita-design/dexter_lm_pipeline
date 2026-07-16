# jobs/day6.py
from utils.gsheet import read_sheet, write_sheet
from config.settings import GSHEET


def run():
    # print("====== Kita Kerjain Day 10 Buat RDO ya =========")

    # df_rdo = read_sheet(
    #     GSHEET["rdo_comp"]["sheet_id"],
    #     GSHEET["rdo_comp"]["tabs"]["main"]
    # )

    # print("===== Ambil data dari RDO done =====")

    # print("====== Kita Kerjain Day 10 Buat PODA ya =========")

    # df_poda_agg = read_sheet(
    #     GSHEET["poda_agg"]["sheet_id"],
    #     GSHEET["poda_agg"]["tabs"]["main"]
    # )

    # print("===== Ambil data dari PODA done =====")

    
    print("====== Kita Kerjain Day 10 Buat OVER MP ya =========")

    df_over_mp_fte = read_sheet(
        GSHEET["over_mp_fte"]["sheet_id"],
        GSHEET["over_mp_fte"]["tabs"]["main"]
    )

    print("===== Ambil data dari OVER MP done =====")

    # print("====== Kita Kerjain Day 10 Buat Vol ya =========")

    # df_vol = read_sheet(
    #     GSHEET["vol"]["sheet_id"],
    #     GSHEET["vol"]["tabs"]["main"]
    # )

    # print("===== Ambil data dari vol done =====")

    
    # print("====== Kita Kerjain Day 10 Buat lm_cost ya =========")

    # df_lm_cost = read_sheet(
    #     GSHEET["lm_cost"]["sheet_id"],
    #     GSHEET["lm_cost"]["tabs"]["main"]
    # )

    # print("===== Ambil data dari LM Cost done =====")

    # print("====== Kita Kerjain Day 10 Buat Hub MP ya =========")

    # df_hub_mp = read_sheet(
    #     GSHEET["hub_mp_cost"]["sheet_id"],
    #     GSHEET["hub_mp_cost"]["tabs"]["main"]
    # )

    # print("===== Ambil data dari Hub MP done =====")


    

    # print("===== Mulai input RDO ke Tracker dulu ya =====")
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_gj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_gj"]["tabs"]["raw_data_otif"],
    #     df=df_rdo,
    #     start_cell="I5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_sum"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_sum"]["tabs"]["raw_data_otif"],
    #     df=df_rdo,
    #     start_cell="I5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_wj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_wj"]["tabs"]["raw_data_otif"],
    #     df=df_rdo,
    #     start_cell="I5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_cj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_cj"]["tabs"]["raw_data_otif"],
    #     df=df_rdo,
    #     start_cell="I5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_ej"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_ej"]["tabs"]["raw_data_otif"],
    #     df=df_rdo,
    #     start_cell="I5",
    #     include_header=False
    # )
    # print("===== Done Input RDO ke Tracker =====")


    # print("===== Mulai input PODA ke Tracker dulu ya =====")
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_gj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_gj"]["tabs"]["raw_data_int_comp"],
    #     df=df_poda_agg,
    #     start_cell="P5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_sum"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_sum"]["tabs"]["raw_data_int_comp"],
    #     df=df_poda_agg,
    #     start_cell="Z5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_wj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_wj"]["tabs"]["raw_data_int_comp"],
    #     df=df_poda_agg,
    #     start_cell="P5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_cj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_cj"]["tabs"]["raw_data_int_comp"],
    #     df=df_poda_agg,
    #     start_cell="P5",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_ej"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_ej"]["tabs"]["raw_data_int_comp"],
    #     df=df_poda_agg,
    #     start_cell="P5",
    #     include_header=False
    # )
    # print("===== Done Input PODA ke Tracker =====")

    print("===== Mulai input OVER MP ke Tracker dulu ya =====")
    write_sheet(
        spreadsheet_id=GSHEET["tracker_gj"]["sheet_id"],
        sheet_name=GSHEET["tracker_gj"]["tabs"]["raw_data_cost"],
        df=df_over_mp_fte,
        start_cell="AA6",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_sum"]["sheet_id"],
        sheet_name=GSHEET["tracker_sum"]["tabs"]["raw_data_cost"],
        df=df_over_mp_fte,
        start_cell="AA6",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_wj"]["sheet_id"],
        sheet_name=GSHEET["tracker_wj"]["tabs"]["raw_data_cost"],
        df=df_over_mp_fte,
        start_cell="AA6",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_cj"]["sheet_id"],
        sheet_name=GSHEET["tracker_cj"]["tabs"]["raw_data_cost"],
        df=df_over_mp_fte,
        start_cell="AA6",
        include_header=False
    )
    write_sheet(
        spreadsheet_id=GSHEET["tracker_ej"]["sheet_id"],
        sheet_name=GSHEET["tracker_ej"]["tabs"]["raw_data_cost"],
        df=df_over_mp_fte,
        start_cell="AA6",
        include_header=False
    )
    print("===== Done Input OVER MP ke Tracker =====")

    # print("===== Mulai input vol ke Tracker dulu ya =====")
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_gj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_gj"]["tabs"]["raw_data_cost"],
    #     df=df_vol,
    #     start_cell="v6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_sum"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_sum"]["tabs"]["raw_data_cost"],
    #     df=df_vol,
    #     start_cell="v6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_wj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_wj"]["tabs"]["raw_data_cost"],
    #     df=df_vol,
    #     start_cell="v6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_cj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_cj"]["tabs"]["raw_data_cost"],
    #     df=df_vol,
    #     start_cell="v6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_ej"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_ej"]["tabs"]["raw_data_cost"],
    #     df=df_vol,
    #     start_cell="v6",
    #     include_header=False
    # )
    # print("===== Done Input Vol ke Tracker =====")

    # print("===== Mulai input LM Cost ke Tracker dulu ya =====")
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_gj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_gj"]["tabs"]["raw_data_cost"],
    #     df=df_lm_cost,
    #     start_cell="H6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_sum"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_sum"]["tabs"]["raw_data_cost"],
    #     df=df_lm_cost,
    #     start_cell="H6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_wj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_wj"]["tabs"]["raw_data_cost"],
    #     df=df_lm_cost,
    #     start_cell="H6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_cj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_cj"]["tabs"]["raw_data_cost"],
    #     df=df_lm_cost,
    #     start_cell="H6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_ej"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_ej"]["tabs"]["raw_data_cost"],
    #     df=df_lm_cost,
    #     start_cell="H6",
    #     include_header=False
    # )
    # print("===== Done Input LM Cost ke Tracker =====")

    # print("===== Mulai input Hub MP Cost ke Tracker dulu ya =====")
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_gj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_gj"]["tabs"]["raw_data_cost"],
    #     df=df_hub_mp,
    #     start_cell="O6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_sum"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_sum"]["tabs"]["raw_data_cost"],
    #     df=df_hub_mp,
    #     start_cell="O6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_wj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_wj"]["tabs"]["raw_data_cost"],
    #     df=df_hub_mp,
    #     start_cell="O6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_cj"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_cj"]["tabs"]["raw_data_cost"],
    #     df=df_hub_mp,
    #     start_cell="O6",
    #     include_header=False
    # )
    # write_sheet(
    #     spreadsheet_id=GSHEET["tracker_ej"]["sheet_id"],
    #     sheet_name=GSHEET["tracker_ej"]["tabs"]["raw_data_cost"],
    #     df=df_hub_mp,
    #     start_cell="O6",
    #     include_header=False
    # )
    # print("===== Done Input LM Cost ke Tracker =====")

if __name__ == "__main__":
    run()
