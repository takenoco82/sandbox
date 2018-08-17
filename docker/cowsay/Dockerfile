FROM debian:wheezy

RUN apt-get update && apt-get install -y cowsay fortune
# ホストからイメージのファイルシステムにコピーする必要がある
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
