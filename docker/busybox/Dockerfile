FROM busybox:latest

RUN echo "This should work"
# /bin/bashがないので次のコマンドで失敗する
# docker run -it {↑のコマンド終了時のイメージID} でデバッグできる
RUN /bin/bash -c echo "This won't"
