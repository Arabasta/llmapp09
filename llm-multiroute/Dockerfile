FROM python:3.12-alpine3.23 AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM alpine:3.23

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apk add --no-cache --virtual .python-rundeps \
        ca-certificates \
        gdbm \
        krb5-libs \
        libbz2 \
        libffi \
        libintl \
        libncursesw \
        libnsl \
        libpanelw \
        libssl3 \
        libtirpc \
        libuuid \
        readline \
        sqlite-libs \
        tzdata \
        xz-libs \
        zlib

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY app ./app

RUN rm -rf \
        /usr/local/bin/pip \
        /usr/local/bin/pip3 \
        /usr/local/bin/pip3.12 \
        /usr/local/lib/python3.12/site-packages/pip \
        /usr/local/lib/python3.12/site-packages/pip-26.2.1.dist-info \
    && adduser -D -u 10001 appuser \
    && mkdir -p /app/metrics \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
