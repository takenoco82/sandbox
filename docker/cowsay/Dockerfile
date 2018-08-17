# 使用するベースイメージを指定する
FROM debian:wheezy

# イメージ内で実行するシェルのコマンドを指定する
RUN apt-get update && apt-get install -y cowsay fortune
# ホストからイメージのファイルシステムにコピーする必要がある
COPY entrypoint.sh /

# docker runに渡される任意の引数を扱う実行ファイルを指定する
ENTRYPOINT ["/entrypoint.sh"]
