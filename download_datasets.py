import os
import requests
import zipfile
import json
from datasets import load_dataset

# Base directory to save the data
DATA_DIR = "data"

def download_and_extract_zip(url, target_dir):
    """Downloads a zip file and extracts it."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    zip_filename = os.path.join(target_dir, url.split("/")[-1])
    
    print(f"Downloading {url}...")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    
    with open(zip_filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    
    print(f"Extracting {zip_filename}...")
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(target_dir)
    
    os.remove(zip_filename)
    print(f"Extracted to {target_dir}")

def download_medical_questions_pairs():
    """Downloads the Curai Health Medical Questions Pairs dataset from Hugging Face."""
    print("Downloading Curai Health Medical Questions Pairs dataset...")
    pairs_path = os.path.join(DATA_DIR, "medical_questions_pairs")
    if not os.path.exists(pairs_path):
        os.makedirs(pairs_path)

    dataset = load_dataset("curaihealth/medical_questions_pairs")
    dataset.save_to_disk(pairs_path)
    print("Curai Health Medical Questions Pairs dataset downloaded and saved to disk.")

# def download_synthea():
#     """Downloads pre-generated Synthea samples."""
#     print("Downloading Synthea data...")
#     # Updated to a working sample file from the Synthea project
#     synthea_url = "https://synthea.mitre.org/downloads/sample_data_csv_synthea.zip"
#     synthea_path = os.path.join(DATA_DIR, "synthea")
#     download_and_extract_zip(synthea_url, synthea_path)

def download_openfda():
    """Downloads a sample from OpenFDA."""
    print("Downloading data from OpenFDA...")
    openfda_path = os.path.join(DATA_DIR, "openfda")
    if not os.path.exists(openfda_path):
        os.makedirs(openfda_path)

    # Example: Adverse drug events
    # See API docs: https://open.fda.gov/apis/drug/ade/
    url = "https://api.fda.gov/drug/event.json?limit=100"
    
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    output_file = os.path.join(openfda_path, "adverse_events.json")
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"OpenFDA data saved to {output_file}")

def download_open_patients():
    """Downloads the Open-Patients dataset from Hugging Face."""
    print("Downloading Open-Patients dataset...")
    open_patients_path = os.path.join(DATA_DIR, "open_patients")
    if not os.path.exists(open_patients_path):
        os.makedirs(open_patients_path)

    dataset = load_dataset("ncbi/Open-Patients")
    dataset.save_to_disk(open_patients_path)
    print("Open-Patients dataset downloaded and saved to disk.")

def download_symptom2disease():
    """Downloads the Symptom2Disease dataset from Kaggle."""
    print("Downloading Symptom2Disease dataset from Kaggle...")
    symptom_path = os.path.join(DATA_DIR, "symptom2disease")
    if not os.path.exists(symptom_path):
        os.makedirs(symptom_path)

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        api = KaggleApi()
        api.authenticate()
        # The dataset slug is 'niyarrbarman/symptom2disease'
        api.dataset_download_files('niyarrbarman/symptom2disease', path=symptom_path, unzip=True)
        print(f"Symptom2Disease dataset downloaded and extracted to {symptom_path}")
    except Exception as e:
        print("\nCould not download the Kaggle dataset.")
        print("Please make sure you have the Kaggle API set up.")
        print("1. Install the Kaggle library: pip install kaggle")
        print("2. Get your 'kaggle.json' API token from your Kaggle account page (go to Settings -> API -> Create New Token).")
        print("3. Place the 'kaggle.json' file in the '~/.kaggle/' directory.")
        print(f"Original error: {e}")


if __name__ == "__main__":
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    print("Starting dataset download...")

    # You can comment out the datasets you don't need.
    download_medical_questions_pairs()
    # download_synthea()
    download_openfda()
    download_open_patients()
    download_symptom2disease()

    print("All datasets downloaded.") 