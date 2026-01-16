import pandas as pd

df=pd.read_csv(r"C:\Users\91886\CampusX\penguins_size.csv")
df.dropna(inplace=True)
df.to_csv(r"C:\Users\91886\CampusX\penguins_size_cleaned.csv",index=False)
print("Data.csv")