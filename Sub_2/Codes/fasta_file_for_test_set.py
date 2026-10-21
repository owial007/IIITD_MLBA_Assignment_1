###Creating the fasta file for test set
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import time
from datetime import datetime

#import the test set, if not defautl will be used
print("\n\nFASTA FILE FORMATION FOR TEST SET\n\n")
start_time = time.time()
#entering the file
file = input("\nEnter the file path if you have, \nElse press 'Enter' to run on defaut file:")
if file:
    test = pd.read_csv(file)
else:
    print("\n\nUsing the default file\n\n")
    test=pd.read_csv("test_new.csv")

#prinitng the inputted file
print(test.head())

#Extracting the peptide sequence
seqs=[]
for i in range(test.shape[0]):
    val = test.iloc[i,1]
    #print(val)
    #print(len(val))
    if len(val)!=17:
        print(len(val))
    seqs.append(val)


#creating ids list for each seq
ids=[]
for i in range(test.shape[0]):
    val = f"pid_"+f"{i+1}"
    ids.append(val)

#Creating the fasta file
records=[]
for i in range(len(seqs)):
    rec = SeqRecord(seq=Seq(seqs[i]),id=ids[i],description=f"{len(seqs[i])}")
    records.append(rec)


print("\n\nSAVING IN RUNNING DIRECTORY AS: test_new.fasta\n\n")
SeqIO.write(records,"test_new.fasta","fasta")

#mapping the end of job
end_time = time.time()

#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Fasta file creation Start Time: {start_time:.4f}\n")
log_file.write(f"Fasta file creation End Time: {end_time:.4f}\n")
log_file.write(f"Total Time Taken to create fasta file: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Created fasta file for test set.\n\n\n")
log_file.close()