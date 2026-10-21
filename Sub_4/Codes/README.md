# GIVES AN OVERVIEW ON WHAT CODES ARE PRESENT

# Peptide Classification Pipeline

> **Note:** All the commands below assume you are running on a Windows environment. They can also be run on Linux by changing the environment setup accordingly.
>
> It also assumes that you are running every file in the same directory. It is recommended to run in the same directory, as some outputs are stored in the working directory.

---

## 1) Protein Feature Extraction

**Files:** `extraction_of_features_for_train_set.py` and `extraction_of_features_for_test_set.py`

These two files are used to extract the one-hot encoding of each peptide using basic Python code.

1. Activate the conda environment:
```bash
   conda activate mlba_v1
```
2. Run the following command:
```bash
   python extraction_of_features_for_train_set.py
```
3. Follow the directions as given.
4. It will store the `.npy` tensor file for the train set in the working directory.
5. Do the similar command for the test set:
```bash
   python extraction_of_features_for_test_set.py
```

---

## 2) Model Finder

**File:** `best_model_finder.py`

This file is used to select the best ML model out of all the models that are present in the Scikit-learn package.

1. Activate the conda environment as shown earlier.
2. Run the following command:
```bash
   python best_model_finder.py
```
3. Follow the directions as given.
4. The printed matrix will show the best model at the top.
5. We will use the top model, which in our case is **`RandomForestClassifier`**.

---

## 3) Model Trainer

**File:** `model_trainer.py`

This file is used to train the `RandomForestClassifier` model.

1. Activate the `mlba_v1` conda environment as shown above.
2. Run the command:
```bash
   python model_trainer.py
```
3. Follow the directions as given.
4. The model will be trained and saved as a `.joblib` file.

---

## 4) Stratified K-Fold Validation

**File:** `skfold_validator.py`

This file contains the code for validating the trained `RandomForestClassifier` model. It is used to test the model while preserving the actual essence of the dataset.

1. Activate the `mlba_v1` environment.
2. Run the command:
```bash
   python skfold_validator.py
```
3. Follow the directions as given.
4. It will run a 10-fold validation.
5. Results will be printed.

---

## 5) Predicting Labels for the Test Set

**File:** `test_set_label_predictor.py`

This file contains the code to predict the labels of the peptides present in the test set.

1. Activate the `mlba_v1` environment.
2. Run the command:
```bash
   python test_set_label_predictor.py
```
3. Follow the directions as given.
4. It will save a CSV file containing the predicted labels for each peptide.
