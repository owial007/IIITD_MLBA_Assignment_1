##Best Model Finder
#importng libraries
import time
from datetime import datetime
from lazypredict import LazyClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

##input the file to the one hot tensor File
print("\n\nBEST MODEL FINDER\n\n")
tensor_file = input("\nEnter the train.npy file path if you have, \nElse press 'Enter' to run on defaut file:")
#if file provided
if tensor_file:
    x = np.load(tensor_file)
#using the defualt file    
else:
    print("Using the default Tensor file")
    x=np.load(f"train_onehot_flat_340.npy")

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
log_file.write(f"Update: Selected the best model\n\n\n")
log_file.close()