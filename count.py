import pandas as pd
xls = pd.ExcelFile("BioVFM Datasets.xlsx")
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    if "Name" in df.columns:
        names = [str(n).strip() for n in df["Name"].dropna()]
        valid_names = [n for n in names if n not in ["", "0"]]
        print(f"[{sheet}] Unique valid names: {len(set(valid_names))}")
