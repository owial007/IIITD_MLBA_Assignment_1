###Creating the fasta file for Train set
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import time
from datetime import datetime

#import the train set, if not defautl will be used
print("\n\nFASTA FILE FORMATION FOR TRAIN SET\n\n")
start_time = time.time()
#entering the file
file = input("\nEnter the file path if you have, \nElse press 'Enter' to run on defaut file:")
if file:
    train = pd.read_csv(file)
else:
    print("\n\nUsing the default file\n\n")
    train=pd.read_csv("train.csv")

#prinitng the inputted file
print(train.head())

#Extracting the peptide sequence
seqs=[]
for i in range(train.shape[0]):
    val = train.iloc[i,0]
    #print(val)
    #print(len(val))
    if len(val)!=17:
        print(len(val))
    seqs.append(val)


#creating ids list for each seq
ids=[]
for i in range(train.shape[0]):
    val = f"pid_"+f"{i+1}"
    ids.append(val)

#Creating the fasta file
records=[]
for i in range(len(seqs)):
    rec = SeqRecord(seq=Seq(seqs[i]),id=ids[i],description=f"{len(seqs[i])}")
    records.append(rec)

print("\n\nSAVING IN RUNNING DIRECTORY AS: train.fasta\n\n")
SeqIO.write(records,"train.fasta","fasta")

#mapping the end of job
end_time = time.time()

#logging the values
log_file = open("log_file.txt","a")
log_file.write(f"Log Status on: {datetime.now().date()} at {datetime.now().time()}\n")
log_file.write(f"Fasta file creation Start Time: {start_time:.4f}\n")
log_file.write(f"Fasta file creation End Time: {end_time:.4f}\n")
log_file.write(f"Total Time Taken to create fasta file: {(end_time - start_time):.4f}\n")
log_file.write(f"Update: Created fasta file for train set.\n\n\n")
log_file.close()