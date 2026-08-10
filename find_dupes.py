import pandas as pd
df = pd.read_excel("BioVFM Datasets.xlsx", sheet_name="Website")
names = [str(n).strip() for n in df["Name"].dropna()]
valid_names = [n for n in names if n not in ["", "0"]]

seen = set()
duplicates = []
for name in valid_names:
    if name in seen:
        duplicates.append(name)
    else:
        seen.add(name)

print("Duplicate Names:")
for dup in set(duplicates):
    print(f"- {dup} (appears {valid_names.count(dup)} times)")
