# Pandas Study Notes
link: https://www.youtube.com/playlist?list=PLZPZq0r_RZONoiL6kRbNM9nPiUM0eErWG

Japanese version: [README.md](README.md)

The code is in [main.py](main.py). Each `# video◯` comment matches a section below. The data is [data.csv](data.csv) (150 Pokémon).

## Setup (uv)
```
uv add pandas
uv run python main.py
```
- `uv add pandas` adds pandas to pyproject.toml and installs it into .venv.
- `uv run` runs the command inside .venv, so there is no need to activate it.
- If the project itself is named `pandas`, `uv add pandas` fails, because the project would depend on itself. This project is named `pandas-practice`. Do not name a folder `src/pandas` either, because it would hide the real pandas.

## video1: Check the pandas version
```python
import pandas as pd
print(pd.__version__)
```

## video2: Series
- A Series is a single column of data. Each value has a **label (index)**.
- A Series made from a list has the index `0, 1, 2…`. Pass `index=[...]` to set the labels. A Series made from a dictionary uses the keys as the index.

```python
series = pd.Series([101, 102, 104, 200, 202], index=["a", "b", "c", "d", "e"])
calories = pd.Series({"Day 1": 1750, "Day 2": 2100, "Day 3": 1700})
```

| Code | Meaning |
|---|---|
| `series.loc["a"]` | get by **label** |
| `series.iloc[0]` | get by **position** (a number starting from 0) |
| `series.loc["c"] = 200` | change the value at a label |
| `series[series < 200]` | pick only the values that match a condition |

## video3: DataFrame
- A DataFrame is a table (rows and columns). When made from a dictionary, the keys become the column names.

```python
data = {"Name": ["Spongebob", "Patrick", "Squidward"], "Age": [30, 35, 50]}
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
```

| Goal | Code |
|---|---|
| Add a column | `df["Job"] = ["Cook", "N/A", "Cashier"]` |
| Add rows | build a new DataFrame, then `pd.concat([df, new_row])` |
| Get a row (label) | `df.loc["Employee 1"]` |
| Get a row (position) | `df.iloc[2]` |

- Adding rows **returns a new DataFrame** and does not change the original. Assign it back with `df = pd.concat(...)`.

## video4: Reading CSV / JSON
```python
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", index_col="名前")   # use the 名前 column as the index
df = pd.read_json("data.json")
print(df.to_string())                            # print every row without truncating
```
- With `index_col="名前"`, `名前` becomes the index and is no longer a column. `df["名前"]` stops working, and you get a row with `df.loc["ピカチュウ"]` instead.
- If a name appears more than once, `df.loc["カイリュー"]` returns several rows instead of one.

## video5: Selection
```python
df["高さ"]                       # one column (a Series)
df[["高さ", "重さ"]]             # several columns (a DataFrame); note the double []
df.loc["ピカチュウ", ["高さ", "重さ"]]   # row label, column labels
df.iloc[0:11:2, 0:3]             # every 2nd row from 0 to 10, columns 0 to 2 (stop excluded)
```
- `loc` uses **labels** and `iloc` uses **positions**. A `loc` slice includes the stop value, and an `iloc` slice does not.
- A label that does not exist raises `KeyError`. Use `try / except KeyError` to print "not found".

## video6: Filtering
```python
tall_pokemon  = df[df["高さ"] >= 2]
legendary     = df[df["伝説"] == 1]
water_pokemon = df[(df["タイプ1"] == "みず") | (df["タイプ2"] == "みず")]
ff_pokemon    = df[(df["タイプ1"] == "ほのお") & (df["タイプ2"] == "ひこう")]
```
- Build a column of True/False values from a condition, then use `df[condition]` to keep only the matching rows.
- Combine conditions with `&` (and) and `|` (or). `and` and `or` do not work, and each condition must be wrapped in `()`.
- Misplacing the brackets, as in `df["重さ" >= 100]`, compares a string with a number and raises `TypeError`. The correct form is `df["重さ"] >= 100`.

## video7: Aggregation and groupby
```python
df.mean(numeric_only=True)       # mean of the numeric columns only
df["高さ"].sum()
df["高さ"].min(), df["高さ"].max()
df["高さ"].count()               # number of values, not counting missing ones (NaN)

group = df.groupby("タイプ1")    # group the rows by タイプ1
group["高さ"].mean()
```
- `numeric_only=True` aggregates only the numeric columns, because text columns cannot be averaged.
- `count()` does not count NaN. `len(df)` gives the number of rows.
- `groupby` returns `mean / sum / min / max / count` for each group.

## video8: Data cleaning
| Step | Code |
|---|---|
| 1. Drop irrelevant columns | `df.drop(columns=["伝説", "番号"])` |
| 2. Handle missing data | `df.dropna(subset=["タイプ2"])` / `df.fillna({"タイプ1": "None"})` |
| 3. Fix inconsistent values | `df["タイプ1"].replace({"くさ": "草", ...})` |
| 4. Standardize text | `df["名前"].str.lower()` |
| 5. Fix data types | `df["伝説"].astype(bool)` |
| 6. Remove duplicates | `df.drop_duplicates()` |

- `dropna(subset=["タイプ2"])` **removes every row** where `タイプ2` is empty. Pokémon with only one type, such as Pikachu and Mewtwo, disappear too. Use `fillna` to fill the gap instead.
- `drop_duplicates()` removes only rows where **every column is the same**. Two rows with the same name but different `番号` are different rows. To compare by name only, use `drop_duplicates(subset=["名前"])`.
- Each step returns a new DataFrame, so assign it back with `df = ...`.

## Mistakes I ran into
| Problem | Cause | Fix |
|---|---|---|
| `uv add pandas` failed | The project was named `pandas`, so it depended on itself | Rename it to `pandas-practice` |
| `ParserError: Expected 1 fields in line 7, saw 3` | The CSV mixed full-width commas `、` and normal commas `,` | Replace the full-width commas with `,` |
| `TypeError: '>=' not supported between 'str' and 'int'` | Values like `"1 .7"` or invisible zero-width spaces turned a numeric column into strings | Fix those values, or use `pd.to_numeric(..., errors="coerce")` |
| `KeyError: 'ピカチュウ'` | The name was a column, not the index | Add `index_col="名前"` |
| `KeyError: '名前'` | Used `df["名前"]` after setting `index_col="名前"` | A column that became the index cannot be selected with `df["名前"]` |
| `UnicodeEncodeError: 'charmap'` | The Windows console was not using UTF-8 | `sys.stdout.reconfigure(encoding="utf-8")` |
| Mewtwo disappeared | `dropna(subset=["タイプ2"])` removed every row with an empty `タイプ2` | Fill with `fillna`, or remove the `dropna` line |
| Warning `VIRTUAL_ENV ... will be ignored` | Another project's venv was still activated | `deactivate` (it still works with `uv run`) |

## Phrases for explaining in English
- "`loc` selects by label, and `iloc` selects by position."
- "I used a boolean mask to filter the rows."
- "Each cleaning step returns a new DataFrame, so I assign it back to `df`."
- "`drop_duplicates` only removes rows that are identical in every column."
- "`dropna` removed every row with a missing value in that column."
