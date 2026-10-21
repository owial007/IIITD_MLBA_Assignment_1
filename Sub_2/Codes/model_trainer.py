##Training the best model
from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, roc_auc_score,accuracy_score
import warnings
warnings.filterwarnings('ignore')
import time
from datetime import datetime
import joblib 

##input the file to the train_DPC File
print("\n\nTRAINING THE BEST MODEL\n\n")
dpc_file = input("\nEnter the Train DPC.csv file path if you have, \nElse press 'Enter' to run on defaut file:")
#if file provided
if dpc_file:
    x = pd.read_csv(dpc_file)
#using the defualt file    
else:
    print("Using the default Train DPC file")
    x=pd.read_csv(f"train_DPC.csv")

#input the peptide train.csv file
train = input("\nEnter the Train Sequence file path if you have, \nElse press 'Enter' to run on defaut file:")
if train:
    train=pd.read_csv(train)
else:
    print("\nUsing the deafult train sequence set\n")
    train=pd.read_csv("train.csv")

#defining the y variable
y=train['label']
#splitting the daastet
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=42)

#Training the best model
print("\n\nTRAINING STARTED\n\n")
start_time = time.time()
clf = ExtraTreesClassifier(random_state=4,n_jobs=-1)
clf.fit(x_train,y_train)
end_time = time.time()
#predicting the labels and probabilities on x_test set 
print("\n\nPREDICITNG THE VALUES\n\n")
pred=clf.predict(x_test)
prob=clf.predict_proba(x_test)[:, 1]
#calculating the predicited scores
print("Accuracy:",accuracy_score(y_test,pred))
print("F1 Score:",f1_score(y_test,pred))
print("AUCROC:",roc_auc_score(y_test,prob))
#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to train the model: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: ExtraTrees Model Trained\n\n\n")
log_file.close()


#Saving the model
start_time = time.time()
print("\n\nSAVING THE TRAINED MODEL IN THE RUNNING DIRECTORY AS: extra_trees_model.joblib\n\n")
joblib.dump(clf, "extra_trees_model.joblib")
end_time = time.time()
#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to save the model: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: ExtraTrees Model saved\n\n\n")
log_file.close()
