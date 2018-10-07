# Directory Traversal

ディレクトリトラバーサルの脆弱性を持ったサイトを構築します。

## 環境構築方法

0. 予め、docker, docker-composeをinstallしてきて下さい
1. localで環境を構築します。`./run.sh`
  * 環境を ` Ctrl+C` で落としそこなった場合は、`docker-compose kill` を試して下さい。
2. `http://0.0.0.0:5001/` にアクセスし、サイトの機能を試してみましょう
