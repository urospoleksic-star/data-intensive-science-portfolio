# Data Intensive Science Portfolio

This repository contains two independent research projects demonstrating my capabilities in machine learning, domain adaptation, numerical linear algebra, and data engineering. 

## 📂 Project 1: Cross-Domain LOS/NLOS Classification
**Directory:** `LOS_NLOS_Classifier/`

A deep learning pipeline designed to classify Line-of-Sight (LOS) vs Non-Line-of-Sight (NLOS) in wireless signals. 
*   **Challenge:** Severe domain shift and missing tabular features across three distinct datasets.
*   **Solution:** Implemented a custom Deep CORAL (Correlation Alignment) network using TensorFlow/Keras, combined with semi-supervised fine-tuning and ensemble Test-Time Augmentation (TTA).
*   **Result:** Achieved ~74.3% accuracy on an unseen target domain (up from ~50% chance), using only a small fraction of labeled target data.
*   **Key Skills:** Data Engineering, Deep Learning, Domain Adaptation, Keras/TensorFlow.

## 📂 Project 2: Filtering & Subsystem Relational Analysis
**Directory:** `Filtering_Analysis/`

A mathematical framework to discover and classify hidden structural relationships in multi-dataset linear systems.
*   **Challenge:** Extracting localized subsystem dynamics from global noisy matrices.
*   **Solution:** Developed an SVD-based null-space extraction engine with a spatial soft-filtering mask. Automatically identifies 2-variable and 3-variable planar constraints.
*   **Result:** Successfully identified structurally invariant relationships and state-dependent relationships, using prediction error spikes as diagnostic indicators for global subsystem coupling.
*   **Key Skills:** Linear Algebra (SVD), Numerical Optimization, Algorithm Design, Scientific Computing.

---
*Note: The raw datasets for Project 1 are not included in this repository due to size constraints. Please see the `data/` folder in that directory for instructions on how to download and reproduce the pipeline.*
