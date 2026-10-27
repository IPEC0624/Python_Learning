# NumPy学習
link: https://www.youtube.com/playlist?list=PLZPZq0r_RZOMldEsyG8-3BebUNbTFVfmY

English version: [README_en.md](README_en.md)

コードは [main.py](main.py) の `# video◯` のコメントに対応しています。

## セットアップ (uv)
```
uv add numpy
uv run python main.py
```
- `uv add numpy`: pyproject.toml に追加して .venv にインストールする。
- `uv run` は .venv の中で実行するので activate は不要。

## video1 : list と NumPy array の違い
- Pythonのlistは `*2` すると中身が繰り返される。NumPy arrayは要素ごとに2倍になる。

```python
[1, 2, 3, 4] * 2            # [1, 2, 3, 4, 1, 2, 3, 4]
np.array([1, 2, 3, 4]) * 2  # [2 4 6 8]
```

## video2 : データ型 (dtype)
- `astype()` で型を変換した**新しい配列**を返す(元の配列は変わらない)。
- `array.dtype` で型、`array.nbytes` で使用メモリ(バイト)が分かる。

| 型 | 範囲 |
|---|---|
| int8 | -128 〜 127 |
| int16 | -32,768 〜 32,767 |
| int32 | 約 ±21億 |
| int64 | 約 ±922京 |

- 迷ったらデフォルト(int64 / float64)でよい。メモリが問題になったら型を小さくする。
- 範囲を超えるとエラーにならず値が一周する(例: int8で127+1 → -128)。
- 小数→整数の `astype(int)` は**0に向かって切り捨て**。

## video3 : 多次元配列とインデックス
- `ndim` は次元数、`shape` は各次元の大きさ(タプル)。
- `array[0][0][0]` (チェーン)は遅い。`array[0, 0, 0]` (多次元インデックス)のほうが速い。

## video4 : reshape
- 要素数が同じなら形を変えられる。`-1` は自動計算。

```python
array.reshape(1, -1)   # 1行にする
```

## video5 : スライス
- `array[行, 列]` で `開始:終了` を指定する(終了は含まない)。

```python
array[2:, 2:]   # 3行目以降・3列目以降
```

## video6 : 算術演算と数学関数
- スカラーとの演算は全要素に適用される(`+ - * / **`)。
- 配列同士の演算は要素ごと(Element-wise)。
- 比較演算子はTrue/Falseの配列を返し、それを使って値を置き換えられる。

```python
scores[scores < 60] = 0
```

| 関数 | 意味 |
|---|---|
| `np.sqrt` | 平方根 |
| `np.round` | 最も近い整数へ(ちょうど.5は偶数へ) |
| `np.floor` | 小さいほうの整数へ(切り捨て) |
| `np.ceil` | 大きいほうの整数へ(切り上げ) |
| `np.pi` | 円周率 |

- floor は負の数でも「下」へ丸める(-2.3 → -3)。

## video7 : ブロードキャスト
- shapeが違う配列でも、大きさ1の次元が自動で引き伸ばされて計算できる。

```python
np.array([[1, 2, 3, 4]]) * np.array([[1], [2], [3], [4]])   # (1,4) * (4,1) → (4,4)
```

- shapeが合わないエラーが出たら、まず両方の `shape` を print する。

## video8 : 配列を作る関数
| 関数 | 内容 |
|---|---|
| `np.zeros(shape)` | すべて0 |
| `np.ones(shape)` | すべて1 |
| `np.full(shape, value)` | 指定した値 |
| `np.eye(n)` | 単位行列 |
| `np.empty(shape)` | 初期化しない(中身は不定・最速) |
| `np.arange(start, stop, step)` | 等間隔(stopは含まない) |
| `np.linspace(start, stop, num)` | 区間をnum個に分割(stopを含む) |

- `empty` は全要素を後で必ず書き込むときだけ使う。迷ったら `zeros`。

## video9 : 集計関数
| 関数 | 意味 |
|---|---|
| `np.sum` | 合計 |
| `np.mean` | 平均 |
| `np.std` | 標準偏差 |
| `np.var` | 分散 |
| `np.min` / `np.max` | 最小・最大 |
| `np.argmin` / `np.argmax` | 最小・最大の位置 |

- `axis=0` は列ごと、`axis=1` は行ごと。
- `np.std` のデフォルトは母集団(nで割る)。標本(n-1で割る)は `ddof=1`。

## video10 : フィルタリング
- 条件でTrue/Falseの配列を作り、`array[条件]` で該当する値だけを取り出す。
- 条件の組み合わせは `&`(かつ)、`|`(または)。`and` / `or` は使えず、各条件を `()` で囲む。

```python
teenagers = ages[ages < 18]
evens = ages[ages % 2 == 0]
```

### where
```python
np.where(ages >= 18, ages, -1)   # np.where(条件, Trueのときの値, Falseのときの値)
```
- 配列の**長さを保ったまま**値を置き換える。`ages[ages >= 18]` は長さが変わる。

## video11 : 乱数
```python
rng = np.random.default_rng()
rng.integers(low=1, high=7, size=(3, 2))          # 1〜6 (highは含まない)
rng.integers(1, 6, endpoint=True)                 # 1〜6 (highを含む)
np.random.uniform(low=-1, high=1, size=(3, 2))    # [low, high) の小数
rng.shuffle(array)                                # 並び替え(元の配列を直接変更)
rng.choice(fruits, size=(3, 2))                   # ランダムに選ぶ
```
- `integers` は `high` を含まない(`endpoint=True` で含める)。
- `low == high` の `uniform` は幅が0なので常にその値になる。
- **seed(シード)**: 乱数の出発点。同じシードなら同じ乱数の並びになり、結果を再現できる。
  `np.random.default_rng(42)` (推奨の新しい方式) / `np.random.seed(1)` (古い方式)

## video12 : 配列の保存と読み込み
```python
# 1つの配列
np.save("data", array)        # data.npy として保存される
array = np.load("data.npy")   # load には .npy が必要

# 複数の配列
np.savez("dataz", array1, array2)              # dataz.npz
np.savez_compressed("dataz", array1, array2)   # 圧縮版
arrays = np.load("dataz.npz")
arrays["arr_0"], arrays["arr_1"]               # 保存した順に arr_0, arr_1 ...
```
- `np.save` は拡張子 `.npy` を**自動で付ける**が、`np.load` は付けない。読み込むときは `.npy` を書く。
- `.npy` はバイナリ形式。エディタで開くと文字化けするが正常。開いたまま保存しない。

## つまずいたところ
| 問題 | 原因 | 対処 |
|---|---|---|
| `main.py\` で `Invalid argument` | コマンドの末尾に余計な `\` を付けた | `uv run python main.py` |
| `(fastapi-practice)` の警告 | 別プロジェクトのvenvがactivateされたまま | `deactivate`(`uv run` ならそのままでも動く) |
| `NameError: name 'load'` | コメントの `#` を忘れた | `# load` |
| `FileNotFoundError` (np.load) | `.npy` を付け忘れた | `np.load("data.npy")` |
| Windowsのパス | `\n` や `\t` が特殊文字になる | `"C:\\Users\\..."`、`r"C:\Users\..."`、または `/` |
