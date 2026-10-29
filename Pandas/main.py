import pandas as pd 
import sys

sys.stdout.reconfigure(encoding="utf-8")

# video1
print(pd.__version__)

# video2 Series
data = [True, False, True]
data = ["A", "B", "C"]
data = [101, 102, 104, 200, 202]

# series = pd.Series(data, index=["appartment #1", "appartment #2", "appartment #3"])
series = pd.Series(data, index=["a", "b", "c", "d", "e"])

series.loc["c"] = 200

print(series.loc["a"])
print(series)
print(series.iloc[0])
print(series[series < 200])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

series.loc["Day 3"] += 500

print(series)
print(series.loc["Day 3"])
print(series[series > 2000])

# video3 dataFrame
data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}, {"Name": "Eugene", "Age": 60, "Job": "Manager"}], index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_row])

print(df)
print(df.loc["Employee 1"])
print(df.iloc[2])

# video4 read csv and json file

# df = pd.read_csv("data.csv", index_col="名前")
df = pd.read_csv("data.csv")
# df = pd.read_csv("data.csv", index_col="名前")

# df = pd.read_json("data.json")
print(df.to_string())

# video5 selection

# by column
# print(df["高さ"].to_string())
# print(df["重さ"].to_string())
# print(df[["高さ", "重さ"]].to_string())

# by row

# print(df.loc["ピカチュウ", ["高さ", "重さ"]])
# print(df.iloc[0:11:2, 0:3])

# pokemon = input("Enter a Pokemon name: ")

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")


# video6 filtering
tall_pokemon = df[df["高さ"] >= 2]

heavy_pokemon = df[df["重さ"] >= 100]

legendary_pokemon = df[df["伝説"] == 1]

water_pokemon = df[(df["タイプ1"] == "みず") | 
                    (df["タイプ2"] == "みず")]

ff_pokemon = df[(df["タイプ1"] == "ほのお") &
                    (df["タイプ2"] == "ひこう")]
print(tall_pokemon)
print(heavy_pokemon)
print(legendary_pokemon)
print(water_pokemon)
print(ff_pokemon)

# video7 aggregate functions
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

# Single column
print(df["高さ"].mean(numeric_only=True))
print(df["高さ"].sum(numeric_only=True))
print(df["高さ"].min(numeric_only=True))
print(df["高さ"].max(numeric_only=True))
print(df["高さ"].count())

# grouping
group = df.groupby("タイプ1")

print(group["高さ"].mean())
print(group["高さ"].sum())
print(group["高さ"].min())
print(group["高さ"].max())
print(group["高さ"].count())

# video8 Data cleaning

# 1. Drop irrelevant columns
# df = df.drop(columns=["伝説", "番号"])

# 2. Handle missing data
# df = df.dropna(subset=["タイプ2"])
df = df.fillna({"タイプ1": "None"})

# 3. Fix inconsistent values
df["タイプ1"] = df["タイプ1"].replace({"くさ": "草", "いわ": "岩", "じめん": "地面"})

# 4. Standarize text
# df["名前"] = df["名前"].str.lower()

# 5. Fix data types
df["伝説"] = df["伝説"].astype(bool)

# 6. Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())
