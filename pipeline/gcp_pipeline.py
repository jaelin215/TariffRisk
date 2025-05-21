import os
import yaml
from pathlib import Path
import pandas as pd
from google.cloud import storage, bigquery

# Define base path relative to this file
config_path = Path(__file__).resolve().parent.parent / "config" / "config.yaml"

# 1. Load Config
with open(config_path, "r") as f:
    config = yaml.safe_load(f)['gcp']

PROJECT = config["project"]
BUCKET_NAME = config["bucket"]
INPUT_FILE = config["input_file"]
DATASET_ID = config["dataset"].split(".")[-1]
OUTPUT_TABLE = config["output_table"]
LOCAL_FILE = "local_copy.xlsx"  # local download target

# 2. Set up Clients
storage_client = storage.Client(project=PROJECT)
bq_client = bigquery.Client(project=PROJECT)

# 3. Download Excel from GCS
bucket = storage_client.bucket(BUCKET_NAME)
blob = bucket.blob(INPUT_FILE)
blob.download_to_filename(LOCAL_FILE)
print(f"Downloaded {INPUT_FILE} from GCS to {LOCAL_FILE}")

# 4. Read and Process Excel
df = pd.read_excel(LOCAL_FILE)
print(f"Loaded {df.shape[0]} rows.")

# Clean column names to be BigQuery-compliant
original_columns = df.columns.tolist()
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r'[^\w]', '_', regex=True)  # replaces non-alphanum with _
    .str.replace('_+', '_', regex=True)      # collapses multiple underscores
    .str.strip('_')                          # removes leading/trailing underscores
)
print("Loaded", len(df), "rows.")
print("Selected columns:", df.columns.tolist())

# Upload to BigQuery
dataset_id = config['dataset'].split(".")[-1]
table_id = f"{config['project']}.{dataset_id}.{config['output_table']}"

job = bq_client.load_table_from_dataframe(df, table_id)
job.result()  # Wait for the job to complete
print(f"✅ Uploaded to {table_id}")