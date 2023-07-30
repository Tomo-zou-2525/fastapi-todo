# PYTHONをインストール
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリを指定
WORKDIR /src

# PIPを使用してPOETRYをインストール
RUN pip install poetry

# POETRYの定義ファイルをローカルからコピー（存在している場合）
COPY pyproject.toml* poetry.lock* ./

# POETRYで定義ファイルに記載されているライブラリをインストール（pyproject.tomlが存在している場合）
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# uvicornサーバを起動
ENTRYPOINT [ "poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]