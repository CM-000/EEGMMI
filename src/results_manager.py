import pandas as pd
from pathlib import Path

RESULTS_FILE = "results/experiment_results.xlsx"


def save_results(result_row):

    """
    Append experiment results to the master spreadsheet.
    """

    results_path = Path(RESULTS_FILE)

    if results_path.exists():

        df = pd.read_excel(
            results_path,
            engine="openpyxl"
        )

        df = pd.concat(
            [df, pd.DataFrame([result_row])],
            ignore_index=True
        )

    else:

        results_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df = pd.DataFrame([result_row])

    print()
    print("Writing to:")
    print(results_path.resolve())

    df.to_excel(
        results_path,
        index=False,
        engine="openpyxl"
    )

    print("Excel save complete.")