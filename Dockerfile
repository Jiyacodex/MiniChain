FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev libffi-dev libgmp-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py genesis.json ./
COPY minichain/ ./minichain/

RUN useradd --create-home --uid 1000 minichain \
    && chown -R minichain:minichain /app
USER minichain

EXPOSE 9000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import socket; socket.create_connection(('127.0.0.1', 8545), timeout=3)"

ENTRYPOINT ["python", "main.py"]
CMD ["--host", "0.0.0.0", "--port", "9000"]
