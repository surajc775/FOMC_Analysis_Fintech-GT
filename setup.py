import os

settings = {
    "data_dir": "data",
    "pdf_dir": "pdfs",
    "pkl_dir": "pkl",
    "results_dir": "results",
}

with open(".env", "w") as f:
    for setting, value in settings.items():
        f.write(f"{setting}={value}\n")