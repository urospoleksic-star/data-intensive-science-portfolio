# Cross-Domain LOS/NLOS Classification using Deep CORAL

Please see the main repository README for a project summary. 
Open `CrossDomainLOSNLOSClassifier.ipynb` to view the full pipeline.

## Data Pipeline
Because the raw data contains tens of thousands of complex CIR signals across 31 CSV files, the raw data is not hosted here. 

To recreate the `full_dataset.csv` used in the notebook:
1. Download the raw datasets using the links in `data/DATA_DOWNLOAD_INSTRUCTIONS.md`.
2. Place the folders in the same directory.
3. Run `python label_domains.py` to clean, align, and concatenate the three datasets into a single standard format.

*Note: The data processing script deliberately excludes the first 9 CSV files from the Industrial dataset (`exportloc1IQ` to `exportloc9IQ`), as they do not contain the necessary LOS/NLOS ground-truth labels required for supervised learning.*

### Required Directory Structure
Before running `label_domains.py`, ensure your local directory looks exactly like this:

```text
LOS_NLOS_Classifier/
│
├── label_domains.py
├── e-wine/
│   ├── uwb_dataset_part1.csv
│   ├── ... (up to part7.csv)
├── industrial/
│   ├── exportloc10IQ.csv
│   ├── ... (up to exportloc23IQ.csv)
└── pozyx/
    └── pozyx_uwb_dataset.csv
