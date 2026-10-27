# NumPy Study Notes
link: https://www.youtube.com/playlist?list=PLZPZq0r_RZOMldEsyG8-3BebUNbTFVfmY

Japanese version: [README.md](README.md)

The code is in [main.py](main.py). Each `# video◯` comment matches a section below.

## Setup (uv)
```
uv add numpy
uv run python main.py
```
- `uv add numpy` adds NumPy to pyproject.toml and installs it into .venv.
- `uv run` runs the command inside .venv, so there is no need to activate it.

## video1: Python list vs NumPy array
- Multiplying a Python list by 2 repeats its items. Multiplying a NumPy array by 2 doubles each element.

```python
[1, 2, 3, 4] * 2            # [1, 2, 3, 4, 1, 2, 3, 4]
np.array([1, 2, 3, 4]) * 2  # [2 4 6 8]
```

## video2: Data types (dtype)
- `astype()` returns a **new array** with the converted type. The original array is unchanged.
- `array.dtype` shows the type, and `array.nbytes` shows the memory used in bytes.

| Type | Range |
|---|---|
| int8 | -128 to 127 |
| int16 | -32,768 to 32,767 |
| int32 | about ±2.1 billion |
| int64 | about ±9.2 quintillion |

- When unsure, keep the default (int64 / float64). Make the type smaller only if memory becomes a problem.
- Going out of range does not raise an error. The value wraps around (for example, int8: 127 + 1 becomes -128).
- `astype(int)` on floats **truncates toward zero**.

## video3: Multidimensional arrays and indexing
- `ndim` is the number of dimensions. `shape` is the size of each dimension, as a tuple.
- Chained indexing like `array[0][0][0]` is slower. Multidimensional indexing like `array[0, 0, 0]` is faster.

## video4: reshape
- You can change the shape as long as the number of elements stays the same. `-1` means "calculate this size automatically".

```python
array.reshape(1, -1)   # make it a single row
```

## video5: Slicing
- Use `array[rows, columns]` with `start:stop`. The stop value is not included.

```python
array[2:, 2:]   # from the 3rd row and the 3rd column onward
```

## video6: Arithmetic and math functions
- An operation with a scalar applies to every element (`+ - * / **`).
- An operation between two arrays is element-wise.
- A comparison operator returns an array of True/False values, which can be used to replace values.

```python
scores[scores < 60] = 0
```

| Function | Meaning |
|---|---|
| `np.sqrt` | square root |
| `np.round` | round to the nearest integer (exactly .5 goes to the even number) |
| `np.floor` | round down to the smaller integer |
| `np.ceil` | round up to the larger integer |
| `np.pi` | the value of pi |

- `floor` always rounds down, even for negative numbers (-2.3 becomes -3).

## video7: Broadcasting
- Arrays with different shapes can still be combined, because dimensions of size 1 are stretched automatically.

```python
np.array([[1, 2, 3, 4]]) * np.array([[1], [2], [3], [4]])   # (1,4) * (4,1) -> (4,4)
```

- If you get a shape mismatch error, print the `shape` of both arrays first.

## video8: Array creation functions
| Function | Description |
|---|---|
| `np.zeros(shape)` | all zeros |
| `np.ones(shape)` | all ones |
| `np.full(shape, value)` | filled with a given value |
| `np.eye(n)` | identity matrix |
| `np.empty(shape)` | uninitialized; the contents are random leftovers, and it is the fastest |
| `np.arange(start, stop, step)` | evenly spaced values (stop is excluded) |
| `np.linspace(start, stop, num)` | `num` evenly spaced points between start and stop (stop is included) |

- Use `empty` only when you are sure you will overwrite every element. When unsure, use `zeros`.

## video9: Aggregate functions
| Function | Meaning |
|---|---|
| `np.sum` | sum |
| `np.mean` | mean |
| `np.std` | standard deviation |
| `np.var` | variance |
| `np.min` / `np.max` | minimum / maximum |
| `np.argmin` / `np.argmax` | index of the minimum / maximum |

- `axis=0` works down each column. `axis=1` works across each row.
- `np.std` uses the population formula by default (divide by n). Use `ddof=1` for the sample formula (divide by n-1).

## video10: Filtering
- Build an array of True/False values from a condition, then use `array[condition]` to pick only the matching values.
- Combine conditions with `&` (and) and `|` (or). `and` and `or` do not work, and each condition must be wrapped in `()`.

```python
teenagers = ages[ages < 18]
evens = ages[ages % 2 == 0]
```

### where
```python
np.where(ages >= 18, ages, -1)   # np.where(condition, value_if_true, value_if_false)
```
- `where` replaces values **while keeping the array length**. `ages[ages >= 18]` changes the length.

## video11: Random numbers
```python
rng = np.random.default_rng()
rng.integers(low=1, high=7, size=(3, 2))          # 1 to 6 (high is excluded)
rng.integers(1, 6, endpoint=True)                 # 1 to 6 (high is included)
np.random.uniform(low=-1, high=1, size=(3, 2))    # floats in [low, high)
rng.shuffle(array)                                # shuffle in place (changes the original)
rng.choice(fruits, size=(3, 2))                   # pick items at random
```
- `integers` excludes `high`. Pass `endpoint=True` to include it.
- `uniform` with `low == high` always returns that value, because the range has zero width.
- **seed**: the starting point of the random sequence. The same seed produces the same sequence, so results can be reproduced.
  `np.random.default_rng(42)` is the recommended modern way, and `np.random.seed(1)` is the legacy way.

## video12: Saving and loading arrays
```python
# a single array
np.save("data", array)        # saved as data.npy
array = np.load("data.npy")   # load needs the .npy extension

# multiple arrays
np.savez("dataz", array1, array2)              # dataz.npz
np.savez_compressed("dataz", array1, array2)   # compressed version
arrays = np.load("dataz.npz")
arrays["arr_0"], arrays["arr_1"]               # named arr_0, arr_1, ... in the order saved
```
- `np.save` **adds the `.npy` extension automatically**, but `np.load` does not. Write `.npy` when loading.
- `.npy` is a binary format. It looks garbled in a text editor, which is normal. Do not save it from the editor.

## Mistakes I ran into
| Problem | Cause | Fix |
|---|---|---|
| `Invalid argument` for `main.py\` | A stray `\` at the end of the command | `uv run python main.py` |
| Warning showing `(fastapi-practice)` | Another project's venv was still activated | `deactivate` (it still works with `uv run`) |
| `NameError: name 'load'` | Forgot the `#` on a comment line | `# load` |
| `FileNotFoundError` from `np.load` | Forgot the `.npy` extension | `np.load("data.npy")` |
| Windows paths | `\n` and `\t` become escape characters | `"C:\\Users\\..."`, `r"C:\Users\..."`, or `/` |

## Phrases for explaining in English
- "It returns a new array and does not change the original."
- "The values are broadcast, so the shapes don't need to match exactly."
- "I used a boolean mask to filter the elements."
- "If I set the same seed, I get the same random numbers every time."
- "`np.save` adds the `.npy` extension, but `np.load` doesn't, so I have to write it myself."
