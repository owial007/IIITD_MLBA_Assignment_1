# GIVES AN OVERVIEW ON WHAT CODES ARE PRESENT

# Peptide Classification Pipeline

> **Note:** All the commands below assume you are running on a Windows environment. They can also be run on Linux by changing the environment setup accordingly.
>
> It also assumes that you are running every file in the same directory. It is recommended to run in the same directory, as some outputs are stored in the working directory.

---

## 1) FASTA File Formation

**Files:** `fasta_file_for_train_set.py` and `fast_file_for_test_set.py`

Both files are used to convert the provided sequences into FASTA format. This is because we are making use of a package called [`pfeature`](https://pypi.org/project/pfeature/), which is used to extract the features for each peptide sequence.

Follow these steps to run both files:

1. Open the command prompt, go to the directory in which the Python files are present, then activate the conda environment:
```bash
   conda activate mlba_v1
```
2. Run the training set file:
```bash
   python fasta_file_for_train_set.py
```
3. Follow all the instructions as directed by the file.
4. Do the same with the test set file:
```bash
   python fasta_file_for_test_set.py
```
5. FASTA files for both the train and test sets will be saved in the working directory itself.

---

## 2) Protein Feature Extraction

**Files:** `extraction_of_features_for_train_set.py` and `extraction_of_features_for_test_set.py`

These two files are used to extract the **Dipeptide Composition (DPC)** for each peptide, using the FASTA files for both the train and test sets. We have used only DPCs, as the models trained on these features performed the best out of all the features we extracted.

### a) Linux Environment

The package will run only in a Linux environment. If you have Linux, follow the steps below:

1. Open the terminal and run:
```bash
   conda activate mlba_v1_linux
```
2. After activating the environment, install the package:
```bash
   pip install pfeature
```
3. Go to the directory in which you have saved the above files and run the training set file:
```bash
   python extraction_of_features_for_train_set.py
```
4. Follow the steps as directed after running the Python file. Do the same with the test set file. You will now have the DPC features for the training and testing sets.

### b) Google Colab (Alternative)

If you do not have a Linux environment or are facing errors, it is recommended to run the code in Google Colab. Both Python files contain a link to Google Colab. Click on it to open the notebook, which you can use as a reference to extract the features.

---

## 3) Model Finder

**File:** `best_model_finder.py`

This file is used to select the best ML model out of all the models present in the Scikit-learn package.

1. Activate the conda environment as shown earlier.
2. Run the following command:
```bash
   python best_model_finder.py
```
3. Follow the directions as given.
4. The printed matrix will show the best model at the top.
5. We will use the top model, which in our case is **`ExtraTreesClassifier`**.

---

## 4) Model Trainer

**File:** `model_trainer.py`

This file is used to train the `ExtraTreesClassifier` model.

1. Activate the `mlba_v1` conda environment as shown above.
2. Run the command:
```bash
   python model_trainer.py
```
3. Follow the directions as given.
4. The model will be trained and saved as a `.joblib` file.

---

## 5) Stratified K-Fold Validation

**File:** `skfold_validator.py`

This file contains the code for validating the trained `ExtraTreesClassifier` model. It is used to test the model while preserving the actual essence of the dataset.

1. Activate the `mlba_v1` environment.
2. Run the command:
```bash
   python skfold_validator.py
```
3. Follow the directions as given.
4. It will run a 10-fold validation.
5. Results will be printed.

---

## 6) Predicting Labels for the Test Set

**File:** `test_set_label_predictor.py`

This file contains the code to predict the labels of the peptides present in the test set.

1. Activate the `mlba_v1` environment.
2. Run the command:
```bash
   python test_set_label_predictor.py
```
3. Follow the directions as given.
4. It will save a CSV file containing the predicted labels for each peptide.
