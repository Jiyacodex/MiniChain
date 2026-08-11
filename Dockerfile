FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py genesis.json ./
COPY minichain/ ./minichain/

EXPOSE 9000 8545

ENTRYPOINT ["python", "main.py"]
CMD ["--host", "0.0.0.0", "--port", "9000"]
