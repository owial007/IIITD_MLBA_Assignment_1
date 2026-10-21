
#one hot encoding for test set
import numpy as np
import pandas as pd
import time
from datetime import datetime

#Adding the time slot to check for time taken to run the job
print("\n\nONE-HOT FEATURE EXRACTION FROM TEST.CSV FILE\n\n")
start_time = time.time()
#running the job
file = input("\nEnter the file path if you have, \nElse press 'Enter' to run on defaut file:")

#running on the file
if file:
    df = pd.read_csv(file) 
else:
    #use the provided train.csv file
    print("\n\nUSING THE EXISTING TEST_NEW.CSV FILE\n\n")
    df = pd.read_csv("test_new.csv")


#Defining the Amino Acids
AA = "ACDEFGHIKLMNPQRSTVWY"
AA_INDEX = {aa: i for i, aa in enumerate(AA)}
L = 17

#Checking if the uploaded files ave equal length peptides
assert (df["sequence"].str.len() == L).all(), "Some sequences are not 17 residues"

# One-Hot Encoding for eahc peptide with shape (N, 17, 20): rows = positions, columns = amino acids
X_oh = np.zeros((len(df), L, len(AA)), dtype=np.uint8)
for i, seq in enumerate(df["sequence"]):
    for pos, aa in enumerate(seq):
        if aa in AA_INDEX:
            X_oh[i, pos, AA_INDEX[aa]] = 1

#Saving the flattened 340 features
print("\n\nSAVING THE FLATTENED TEST TENSOR IN WORKING DIRECTORY\n\n")
np.save("test_onehot_flat_340.npy", X_oh.reshape(len(df), -1))

    
print("\n\nFLATTENED TENSOR FILE SAVED IN THE RUNNING DIRECTORY AS: test_onehot_flat_340.npy\n\n")

#mapping the end of job
end_time = time.time()
#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Total Time Taken to Extract One-Hot Encodes: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Extracted One-Hot Encodes for test set\n\n\n")
log_file.close()
