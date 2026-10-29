# Pandas学習
link: https://www.youtube.com/playlist?list=PLZPZq0r_RZONoiL6kRbNM9nPiUM0eErWG

English version: [README_en.md](README_en.md)

コードは [main.py](main.py) の `# video◯` のコメントに対応しています。データは [data.csv](data.csv) (ポケモン150匹)を使います。

## セットアップ (uv)
```
uv add pandas
uv run python main.py
```
- `uv add pandas`: pyproject.toml に追加して .venv にインストールする。
- `uv run` は .venv の中で実行するので activate は不要。
- プロジェクト名を `pandas` にすると `uv add pandas` が失敗する(自分自身への依存になる)。このプロジェクトは `pandas-practice` という名前にしている。`src/pandas` というフォルダ名も本物のpandasを隠してしまうので使わない。

## video1 : pandas のバージョン確認
```python
import pandas as pd
print(pd.__version__)
```

## video2 : Series
- Series は1列のデータ。各値に**ラベル(index)**が付く。
- リストから作ると index は `0, 1, 2…`。`index=[...]` でラベルを指定できる。辞書から作るとキーが index になる。

```python
series = pd.Series([101, 102, 104, 200, 202], index=["a", "b", "c", "d", "e"])
calories = pd.Series({"Day 1": 1750, "Day 2": 2100, "Day 3": 1700})
```

| 書き方 | 意味 |
|---|---|
| `series.loc["a"]` | **ラベル**で取り出す |
| `series.iloc[0]` | **位置**(0始まりの番号)で取り出す |
| `series.loc["c"] = 200` | ラベルを指定して値を書き換える |
| `series[series < 200]` | 条件に合う値だけ取り出す |

## video3 : DataFrame
- DataFrame は表(行と列)。辞書から作ると、キーが列名になる。

```python
data = {"Name": ["Spongebob", "Patrick", "Squidward"], "Age": [30, 35, 50]}
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
```

| やりたいこと | 書き方 |
|---|---|
| 列を追加 | `df["Job"] = ["Cook", "N/A", "Cashier"]` |
| 行を追加 | 新しい DataFrame を作り `pd.concat([df, new_row])` |
| 行を取り出す(ラベル) | `df.loc["Employee 1"]` |
| 行を取り出す(位置) | `df.iloc[2]` |

- 行の追加は、元の `df` を書き換えず**新しい DataFrame を返す**。`df = pd.concat(...)` と代入し直す。

## video4 : CSV / JSON の読み込み
```python
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", index_col="名前")   # 名前列を index にする
df = pd.read_json("data.json")
print(df.to_string())                            # 省略せず全行を表示
```
- `index_col="名前"` にすると、`名前` は列ではなく index になる。以降 `df["名前"]` は使えず、`df.loc["ピカチュウ"]` で行を取り出す。
- 名前が重複していると、`df.loc["カイリュー"]` は1行ではなく複数行を返す。

## video5 : 選択 (Selection)
```python
df["高さ"]                       # 1列 (Series)
df[["高さ", "重さ"]]             # 複数列 (DataFrame)。[] が二重になる
df.loc["ピカチュウ", ["高さ", "重さ"]]   # 行ラベル, 列ラベル
df.iloc[0:11:2, 0:3]             # 行0〜10を2つおき, 列0〜2 (終了は含まない)
```
- `loc` は**ラベル**、`iloc` は**位置**で指定する。`loc` のスライスは終了を含み、`iloc` は含まない。
- 存在しないラベルは `KeyError`。`try / except KeyError` で「見つからない」と表示できる。

## video6 : フィルタリング
```python
tall_pokemon  = df[df["高さ"] >= 2]
legendary     = df[df["伝説"] == 1]
water_pokemon = df[(df["タイプ1"] == "みず") | (df["タイプ2"] == "みず")]
ff_pokemon    = df[(df["タイプ1"] == "ほのお") & (df["タイプ2"] == "ひこう")]
```
- 条件でTrue/Falseの列を作り、`df[条件]` で該当する行だけ取り出す。
- 条件の組み合わせは `&`(かつ)、`|`(または)。`and` / `or` は使えず、各条件を `()` で囲む。
- `df["重さ" >= 100]` のように `[]` の位置を間違えると、文字列と数値を比べて `TypeError` になる。正しくは `df["重さ"] >= 100`。

## video7 : 集計と groupby
```python
df.mean(numeric_only=True)       # 数値列だけ平均
df["高さ"].sum()
df["高さ"].min(), df["高さ"].max()
df["高さ"].count()               # 欠損(NaN)を除いた個数

group = df.groupby("タイプ1")    # タイプ1ごとにまとめる
group["高さ"].mean()
```
- `numeric_only=True` で数値列だけ集計する(文字列の列があると集計できないため)。
- `count()` は NaN を数えない。`len(df)` は行数。
- `groupby` はグループごとの `mean / sum / min / max / count` を返す。

## video8 : データクリーニング
| 手順 | 書き方 |
|---|---|
| 1. 不要な列を消す | `df.drop(columns=["伝説", "番号"])` |
| 2. 欠損値を処理 | `df.dropna(subset=["タイプ2"])` / `df.fillna({"タイプ1": "None"})` |
| 3. 表記ゆれを直す | `df["タイプ1"].replace({"くさ": "草", ...})` |
| 4. 文字を統一 | `df["名前"].str.lower()` |
| 5. 型を直す | `df["伝説"].astype(bool)` |
| 6. 重複を消す | `df.drop_duplicates()` |

- `dropna(subset=["タイプ2"])` は `タイプ2` が空の行を**すべて消す**。ピカチュウやミュウツーのようにタイプ2を持たないポケモンも消えるので注意。消したくないときは `fillna` で埋める。
- `drop_duplicates()` は**全部の列が同じ行**だけを消す。`番号` が違えば、同じ名前でも別の行。名前だけで判定するなら `drop_duplicates(subset=["名前"])`。
- どの処理も新しい DataFrame を返すので、`df = ...` と代入し直す。

## つまずいたところ
| 問題 | 原因 | 対処 |
|---|---|---|
| `uv add pandas` が失敗 | プロジェクト名が `pandas` で、自分自身への依存になった | 名前を `pandas-practice` に変更 |
| `ParserError: Expected 1 fields in line 7, saw 3` | CSVに全角カンマ `、` と半角カンマ `,` が混ざっていた | 全角カンマを `,` に置換 |
| `TypeError: '>=' not supported between 'str' and 'int'` | `"1 .7"` や目に見えないゼロ幅スペースが混ざり、数値列が文字列になった | 該当の値を直す。または `pd.to_numeric(..., errors="coerce")` |
| `KeyError: 'ピカチュウ'` | 名前が index ではなく列だった | `index_col="名前"` を付ける |
| `KeyError: '名前'` | `index_col="名前"` にしたのに `df["名前"]` を使った | index になった列は `df["名前"]` で選べない |
| `UnicodeEncodeError: 'charmap'` | Windowsのコンソールが UTF-8 ではない | `sys.stdout.reconfigure(encoding="utf-8")` |
| ミュウツーが消えた | `dropna(subset=["タイプ2"])` が `タイプ2` の空の行を全部消した | `fillna` で埋めるか、`dropna` を外す |
| `(pyuv add pandas)` / `VIRTUAL_ENV ... will be ignored` の警告 | 別プロジェクトのvenvがactivateされたまま | `deactivate`(`uv run` ならそのままでも動く) |
