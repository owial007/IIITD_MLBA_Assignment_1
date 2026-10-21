##Getting result on test set
from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, roc_auc_score,accuracy_score
import warnings
warnings.filterwarnings('ignore')
import time
from datetime import datetime
import joblib 

#loading the trained model

print("\n\nLOADING THE TRAINED MODEL!!\n\n")
start_time = time.time()

model = joblib.load("random_forest_model.joblib")
end_time = time.time()

print("\n\nMODEL LOADED\n\n")

#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to load the model: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Random Forest Model Loaded\n\n\n")
log_file.close()

dpc_file = input("\nEnter the Test DPC.csv file path if you have, \nElse press 'Enter' to run on defaut file:")
#if file provided
if dpc_file:
    x = pd.read_csv(dpc_file)
#using the defualt file    
else:
    print("Using the default Test DPC file")
    x=pd.read_csv(f"test_new_DPC.csv")

#input the peptide train.csv file
test = input("\nEnter the Test Sequence file path if you have, \nElse press 'Enter' to run on defaut file:")
if test:
    test=pd.read_csv(test)
else:
    print("\nUsing the deafult test sequence set\n")
    test=pd.read_csv("test_new.csv")

#geting the predicitons
print("\n\nGetting Prediciton for Test Set\n\n")
start_time = time.time()
pred = model.predict(x)
end_time = time.time()
print("\n\nGot the Predicitons for Test Set\n\n")
#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to get predicitons on test set: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Got predictions on test set\n\n\n")
log_file.close()


#saving the predicitons as directed
print("\n\nSAVING THE PREDICITIONS IN RUNNING DIRECTORY\n\n")
start_time = time.time()
test_pred_df = pd.DataFrame({'id':test[test.columns[0]],
                             'label':pred})
test_pred_df.to_csv("test_pred.csv",index=False)
end_time = time.time()
print("\n\nSAVED THE PREDICTIED VALUES IN: test_pred.csv")

#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to save the predictions on test set: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Saved predictions on test set\n\n\n")
log_file.close()
