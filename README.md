# FOMC_Analysis_Fintech-GT

This repository does the following:

- Downloads all official documents from the Fed's website and converts them into text
- Analyzes word frequencies and trends

## Installation

- Navigate to a command prompt
- Make a virtual environment with python using python's `venv` command
- Activate it, then install all required packages using the command `pip install -r requirements.txt`

## How to Run

### Required (you need to run these for everything else to work)

Perform the following in the order shown

1. Run `setup.py` to configure the `.env` file, should contain names for different directories
2. Download the PDFs using `fomcscraper.py`
3. Convert the PDFs into text (stored in pickle files) and eliminate all punctuation and stop words (i.e. common English words) using `data_processing.py`
4. Aggregate word frequencies by word and by date with `word_frequency.py`
5. Cache the document types as a python dictionary by running `generate_doctype.py`

### Optional (choose whatever you want from here)

- Separate results by document type (e.g. Beige Books, Blue Books) using `split_doctype.py`
- Create CSV files from Counter objects with `counter_csv.py`
