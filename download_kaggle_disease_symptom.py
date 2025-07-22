import os
import zipfile
import subprocess

KAGGLE_DATASET = "dhivyeshrk/diseases-and-symptoms-dataset"
OUTPUT_DIR = os.path.join("data", "disease_symptom_kaggle")

os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"Downloading Kaggle dataset: {KAGGLE_DATASET}")
subprocess.run([
    "kaggle", "datasets", "download", "-d", KAGGLE_DATASET, "-p", OUTPUT_DIR
], check=True)

# Find the zip file
zip_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.zip')]
if not zip_files:
    raise FileNotFoundError("No zip file found after Kaggle download.")

zip_path = os.path.join(OUTPUT_DIR, zip_files[0])
print(f"Extracting {zip_path} ...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(OUTPUT_DIR)

print(f"Cleaning up zip file {zip_path} ...")
os.remove(zip_path)

print(f"Done! Dataset extracted to {OUTPUT_DIR}") 