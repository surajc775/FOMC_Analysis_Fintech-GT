# FOMC_Analysis_Fintech-GT

This repository does the following:
- Downloads all official documents from the Fed's website and converts them into text
- Analyzes word frequencies and trends
## Installation

- Navigate to a command prompt
- Make a virtual environment with python using python's `venv` command
- Activate it, then install all required packages using the command `pip install -r requirements.txt`

## How to Run

- Download the PDFs using `fomcscraper.py`
- Convert the PDFs into text (stored in pickle files) and eliminate all punctuation and stop words (i.e. common English words) using `data_processing.py`
- Aggregate word frequencies by word and by date with `word_frequency.py`
- Create CSV files from Counter objects
