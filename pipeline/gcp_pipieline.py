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

# TODO: Replace this with your actual feature processing
# For example, select only columns A, B, and C
selected_columns = df.columns[:5]  # change this logic
processed_df = df[selected_columns]
print(f"Selected columns: {list(selected_columns)}")

# 5. Upload to BigQuery
table_ref = f"{PROJECT}.{DATASET_ID}.{OUTPUT_TABLE}"

job = bq_client.load_table_from_dataframe(
    processed_df,
    table_ref,
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")  # overwrite table
)
job.result()
print(f"Uploaded {processed_df.shape[0]} rows to {table_ref}")