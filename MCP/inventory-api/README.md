# MCP server学習　
link: https://youtu.be/6bQj2o5Ul8M?si=xM4WaQO3Qs51z39K
    : https://youtu.be/VgH1GKSCXJQ?si=yUwUK8Q-wfbCYflW

## FastAPI
FastAPIの3大特長
圧倒的に高速

Node.jsやGo言語に匹敵するトップクラスの処理速度を誇ります。

直感的で書く量が少ない

Pythonの「型ヒント（Type Hints）」を活用しており、コード量を減らしつつバグを未然に防げます。

自動でAPIドキュメントが生成される

コードを書くだけで、ブラウザからAPIをテストできる画面が勝手に作成されます。

### 型定義だけで「入力チェック（バリデーション）」が自動化できる

### APIドキュメントの自動生成 (Swagger UI)
FastAPIでアプリを起動して、ブラウザで /docs にアクセスするだけで、インタラクティブなWeb APIドキュメントが自動生成されます。

できること:

どんなエンドポイント（URL）があるか一覧表示

どんなパラメーターを送る必要があるかの確認

ブラウザ上で実際にリクエストを送信してテスト（Try it out ボタン）

## UV
1. uv add （新しい依存関係の追加）

指定したパッケージを pyproject.toml の dependencies（または --dev で開発用依存関係）に書き加えます。

自動的に uv.lock を更新し、現在の仮想環境（.venv）に該当パッケージをインストールします。

npm でいう npm install <package> や Poetry でいう poetry add に相当します。

2. uv sync （環境の同期・完全再現）

pyproject.toml および uv.lock の定義を読み取り、現在の仮想環境（.venv）をその通りに仕立て上げます。

もし手動で削除したパッケージが仮想環境に残っている場合、uv sync はそれを自動的にアンインストール（削除）して完全な同期状態を作ります。

npm でいう npm ci や Poetry でいう poetry install に相当します。

### 挙動の違い

uv sync（通常）
uv.lock に記載された固定バージョンを厳密に維持して環境を同期します。他のメンバーと全く同じ環境を再現したい時に使います。

uv sync --upgrade（アップグレード実行）
uv.lock の固定を無視し、pyproject.toml で許容されている範囲内で最新のパッケージを探して uv.lock を書き換えた上で仮想環境にインストールします。
