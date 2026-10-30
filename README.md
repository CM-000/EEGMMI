# EEGMMI

A modular EEG motor imagery classification project built with **MNE-Python** and **Docker**, using the [PhysioNet EEG Motor Movement/Imagery Dataset](https://physionet.org/content/eegmmidb/1.0.0/) (EEGMMIDB).

---

## Project Goal

The long-term goal of this project is to investigate whether intended motor actions can be inferred from EEG recordings during motor imagery.

```text
Imagined Movement
       ↓
     EEG
       ↓
Machine Learning Model
       ↓
Predicted Intended Action
```

---

## Architecture

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

---

## Pipeline

```text
EEG Recording
    ↓
Bandpass Filter (8–30 Hz)
    ↓
Epoch Extraction
    ↓
Common Spatial Patterns (CSP)
    ↓
Linear SVM
    ↓
Classification
```

---

## Results

### Experiment 1: Imagined Left vs. Imagined Right

| Setting | Value |
|---|---|
| Subjects | S001–S005 |
| Runs | R04, R08, R12 |
| Channels | C3, Cz, C4 |
| Features | CSP |
| Classifier | Linear SVM |

| Metric | Value |
|---|---|
| Epochs | 225 |
| Cross-validation accuracy | ~64% |
| Class balance | 113 vs. 112 samples |

This demonstrates that motor imagery EEG contains enough information to classify intended left- and right-hand actions above chance level.

---

## Implemented

- **Data Loading**
  - Load EEGMMIDB EDF recordings
  - Multi-run and multi-subject support
  - EEG montage application
  - Channel selection
- **Preprocessing**
  - Bandpass filtering
  - Event extraction
  - Epoch generation
  - Bad epoch removal
- **Feature Extraction**
  - Common Spatial Patterns (CSP)
- **Model Training**
  - Linear SVM
- **Evaluation**
  - Train/test evaluation
  - Cross-validation
  - Class distribution reporting
- **Environment**
  - Dockerized workflow
  - GitHub version control

---

## Future Work

- **Classification**
  - Additional classifiers
  - Hyperparameter tuning
  - Frequency band optimization
- **Research Directions**
  - Actual vs. imagined movement comparisons
  - Train-on-actual, test-on-imagined experiments
  - Subject-specific optimization
  - Cross-subject generalization
- **Tooling**
  - Experiment runner
  - Visualization and reporting
  - Configuration-based experiments

---

## Dataset

This project uses the PhysioNet EEG Motor Movement/Imagery Dataset (EEGMMIDB). The dataset is **not included** in this repository.

---

## Running

**Build**

```bash
docker build -t eegmmi .
```

**Run**

```bash
docker run --rm \
  -v "<dataset_path>:/app/physionet.org" \
  eegmmi
```

---

## Status

Active learning and research project.