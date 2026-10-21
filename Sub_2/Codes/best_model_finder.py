##Best Model Finder
#importng libraries
import time
from datetime import datetime
from lazypredict import LazyClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

##input the file to the train_DPC File
print("\n\nBEST MODEL FINDER\n\n")
dpc_file = input("\nEnter the DPC.csv file path if you have, \nElse press 'Enter' to run on defaut file:")
#if file provided
if dpc_file:
    x = pd.read_csv(dpc_file)
#using the defualt file    
else:
    print("Using the default DPC file")
    x=pd.read_csv(f"train_DPC.csv")

#input the peptide train.csv file
train = input("\nEnter the Sequence file path if you have, \nElse press 'Enter' to run on defaut file:")
if train:
    train=pd.read_csv(train)
else:
    print("\nUsing the deafult train sequence set\n")
    train=pd.read_csv("train.csv")

#defining the y variable
y=train['label']
#splitting the daastet
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=42)
#Model selections
start_time = time.time()
print("RUNNING THE MODEL FINDER")
clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
models,predictions = clf.fit(x_train, x_test, y_train, y_test)
#mapping the end of training
end_time = time.time()
print("FINISHED RUNNING THE MODEL FINDER")
print(models)

#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to train the model selector: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Selected the First model\n\n\n")
log_file.close()