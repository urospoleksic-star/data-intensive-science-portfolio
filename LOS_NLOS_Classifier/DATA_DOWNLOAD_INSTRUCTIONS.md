# Raw Data Sources & Descriptions

The pipeline uses three independent UWB (Ultra-Wideband) datasets to simulate domain shift.

## 1. e-wine Dataset (Domain 1)
*   **Source:** https://github.com/ewine-project/UWB-LOS-NLOS-Data-Set
*   **Description:** 7 CSV files. Contains full CIRs (1016 elements), LOS/NLOS labels, and measured distances. No ground truth distances.

## 2. Industrial Dataset (Domain 2)
*   **Source:** https://github.com/JaronFontaine/Industrial-UWB-localization-CIR-dataset
*   **Description:** 23 CSV files. Contains full CIRs, measured distances, LOS/NLOS labels, ground truth distances, and NLOS errors. Note: CIR is in complex format (A + jB), magnitude must be computed.

## 3. Pozyx Dataset (Domain 3)
*   **Source:** https://ieee-dataport.org/open-access/pozyx-cir-and-range-los-and-nlos
*   **Description:** 1 CSV file. Contains full CIRs, measured distances, LOS/NLOS labels, and ground truth distances. Note: 12 of the 14 tabular features are constant (-1) in this dataset.
