# EEGMMI

A modular EEG motor imagery classification project built with MNE-Python and Docker using the PhysioNet EEG Motor Movement/Imagery Dataset (EEGMMIDB).

## Project Goals

This project serves as a learning and research platform for exploring:

- EEG signal processing
- Motor imagery classification
- Feature extraction techniques (CSP)
- Traditional machine learning methods
- Subject-specific EEG optimization
- Reproducible machine learning workflows with Docker

## Current Architecture
```text
EDF Files
    ↓
data_loader.py
    ↓
preprocessing.py
    ↓
feature_extraction.py
    ↓
model_training.py
    ↓
evaluation.py
```

# Implemented
```text
Data Loading
Load EDF recordings from EEGMMIDB
Concatenate multiple runs
Apply EEG montages
Channel selection
Preprocessing
Bandpass filtering
Event extraction
Epoch generation
Bad epoch removal
Feature Extraction
Common Spatial Patterns (CSP)
Model Training
Initial linear SVM implementation
```
# Environment
```text
Dockerized development environment
GitHub version control
```

# Future Work
```text
Cross-validation evaluation pipeline
Additional classifiers
Subject-specific frequency band optimization
Actual vs imagined movement classification
Automated experiment runner
Improved visualization and reporting
```

# Dataset
```text
This project uses the PhysioNet EEG Motor Movement/Imagery Dataset (EEGMMIDB).
The dataset is not included in this repository.
```

# Running:
```text
Build the Docker image:
       docker build -t eegmmi .
```

# Run the project:
```text
docker run --rm eegmmi
```

# Status:
```text
Early-stage research and learning project.
```
