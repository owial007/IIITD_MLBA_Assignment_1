#Straitified K fold Validator!!

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import make_scorer, matthews_corrcoef
import time
from datetime import datetime
##input the file to the train_DPC File
print("\n\nVALIDATING THE TRAINED MODEL\n\n")
start_time_ini=time.time()

tensor_file = input("\nEnter the train.npy file path if you have, \nElse press 'Enter' to run on defaut file:")
#if file provided
if tensor_file:
    x = np.load(tensor_file)
#using the defualt file    
else:
    print("Using the default Tensor file")
    x=np.load(f"train_onehot_flat_340.npy")

#input the peptide train.csv file
train = input("\nEnter the Train Sequence file path if you have, \nElse press 'Enter' to run on defaut file:")
if train:
    train=pd.read_csv(train)
else:
    print("\nUsing the deafult train sequence set\n")
    train=pd.read_csv("train.csv")

#defining the y variable
y=train['label']


# Loading the model
print("\n\nLOADING THE TRAINED MODEL!!\n\n")
start_time = time.time()

clf = joblib.load("random_forest_model.joblib")
end_time = time.time()

print("\n\nMODEL LOADED\n\n")

#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to load the model: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Random Forest Model Loaded\n\n\n")
log_file.close()


#Initialising the Kfold validator
print("\n\nINITIALISING THE STRATIFIED K-FOLD CROSS VALIDATOR\n\n")
start_time=time.time()
kfold = StratifiedKFold(
    n_splits=10,
    shuffle=True,
    random_state=42
)

scoring = {
    'accuracy': 'accuracy',
    'precision': 'precision',
    'recall': 'recall',
    'f1': 'f1',
    'roc_auc': 'roc_auc',
    'mcc': make_scorer(matthews_corrcoef)
}
end_time=time.time()
#mapping the log values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to load the SKFOLD Validator: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: SKFOLD Validator Loaded\n\n\n")
log_file.close()


print("\n\nRUNNING THE STRATIFIED K-FOLD CROSS VALIDATOR\n\n")
start_time=time.time()
results = cross_validate(
    clf,
    x,
    y,
    cv=kfold,
    scoring=scoring,
    n_jobs=1,
    verbose=2,
    error_score='raise'
)
end_time=time.time()
#logggin the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to run the SKFOLD Validator: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: SKFOLD Validator finished running\n\n\n")
log_file.close()


#Getting the results
print("\n\n10-SK-FOLD VALITOR RESULTS\n\n")
start_time=time.time()
for metric in scoring:
    scores = results['test_' + metric]

    print(f"\n{metric.upper()}")
    print("Individual fold scores:", np.round(scores, 4))
    print("Mean score:", round(scores.mean(), 4))
    print("Standard deviation:", round(scores.std(), 4))
end_time=time.time()
#logggin the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to print the SKFOLD Validator results: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: SKFOLD Validator printed results\n\n\n")
log_file.close()

print("\nCross-validation completed.")
end_time_ini = time.time()
#logggin the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to run the SKFOLD Validator: {(end_time_ini - start_time_ini):.4f}\n")
log_file.write(f"Update: Completed SKFOLD Validator\n\n\n")
log_file.close()