from pathlib import Path

import pandas as pd

pliki = Path("excel_data").rglob("*.xlsx")

output_df_list = []
for p in pliki:
    temp_df = pd.read_excel(p)
    temp_df["Nazwa pliku"] = p.as_posix()
    output_df_list.append(temp_df)

if output_df_list:
    output_df = pd.concat(output_df_list, axis=1)
    output_df.to_excel("excel_data/output.xlsx", index=False)
else:
    print("Brak plików do scalenia")
