# -*- coding: utf-8 -*-
import random
from DNA_STRUCTURES import *
from utilities import colours
from collections import Counter


def validate_seq (dna_seq):
    """Checks that a input sequence variable is a valid DNA sequence""" #this is a dox string and explains a function in a editor
    tmpseq= dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq 

#creates random dna sequence for testing 
rndDNAstr= ''.join([random.choice(nucleotides)
                    for nuc in range(20)]) 
DNAStr= validate_seq(rndDNAstr)

#counts number of nucleotides by assigning to a dict as 0 then for each count adds 1 to dict 
def count_nuc_frequency(seq):
    """Counts number of nucleotides in DNA"""
    tmpFreqDict= {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
       tmpFreqDict[nuc] += 1 
    return tmpFreqDict
    #return dict(collections.Counter(seq)) one line of code does the above

#creates random dna sequence for testing 
rndDNAstr= ''.join([random.choice(nucleotides)
                    for nuc in range(20)]) 
DNAStr= validate_seq(rndDNAstr)

def transcription(seq):
    """Transcribes a given DNA string to RNA"""
    return seq.replace("T", "U")

def reverse_complement_def(seq):   
    """Gives reverse complement of DNA seq using a maketrans mapping table"""
    reverse_complement_seq=seq[::-1] #reverses seq
    reverse_complement_seq=seq.translate(reverse_complement_dict) #needed for translate and maketrans dict mapping table
    return reverse_complement_seq 

def GC_content(seq):
    """Gives GC content of a DNA string as a percentage"""
    GCcount=round(((seq.count("G")+seq.count("C"))/len(seq))*100)
    return GCcount

def GC_content_subsection(seq, k=20):
    """Splits seq into subseq of length k and gives GC content of each subseq"""
    res=[]
    for i in range(0, len(seq) -k+1, k): #for each nuccleotide in seq, split by k
        subseq=seq[i:i +k] #splits seq into subseqs of slice [] splitting each k value and appends to res list
        res.append(GC_content(subseq)) #runs GC on each subseq
    return res

def translate_seq(seq, init_pos=0):
    """Translates a sequence from DNA to Protein"""
    AA_seq_list=[DNA_codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq)-2, 3)] #splits seq into 3 letters and checks each againts codin table
    AA_STR=""
    return AA_STR.join(AA_seq_list) #str.join(iteratable)

def codon_usage(seq, aminoacid): #broken need to exchange frqdict key  with value of DNA_codons dict
    """Gives count of each amino acid codon in a sequence"""
    tmplist=[]
    for i in range(0, len(seq)-2, 3):  #splits seq into codons and appends to list
        if DNA_codons[seq[i:i +3]] == aminoacid:
            tmplist.append(seq[i:i + 3])
    
    freqdict= dict(Counter(tmplist))
    totalWight= sum(freqdict.values()) #sum will sum values of an iterable e.g. a list
    for seq in freqdict:
        freqdict[seq] =round(freqdict[seq]/ totalWight, 2)
    return freqdict
   # frqdict= dict(Counter(tmplist))
   # for frqdict[value] in frqdict: #makes tmplist a dict and Counter counts hashable objects
   #     key= DNA_codons.get(key)
    #for values in frqdict:
    #    frqdict[value] = frqdict[DNA_codons[value]    
    #return frqdict
    #for codon in tmplist:
        #if codon in DNA_codons.keys():
            
    


#f strings have f at start and values to replace are in curly brackets {}
#\n is newline
print (f'\nSequence: {DNAStr}\n')
print (f'[1]  Sequence Length: {len(DNAStr)}\n')
print (f'[2]  Nucleotide frequency: {count_nuc_frequency(DNAStr)}\n')
print (f'[3]  Transcribed sequence: {transcription(rndDNAstr)}\n')
print (f"[4]  DNA Sequence and reverse complement: \n5' {DNAStr} 3'")
print (f"   {''.join(['|' for c in range (len(DNAStr))])}") #puts command function in {} adds pipes for each letter
print (f"3' {reverse_complement_def(DNAStr)} 5' \n")
print (f'[5]  Sequence GC content= {GC_content(DNAStr)}%\n')
print (f'[6]  Sequence subsection GC content= {GC_content_subsection(DNAStr, k=5)} \n') 
print (f'[7]  DNA->Amino acid translation: {translate_seq(DNAStr)}\n     M = START ATG, _ = STOP ')
print (f'     Codon frequency of V: {codon_usage(DNAStr, "V")} \n')

#my_list[start, end, step] e.g step 2 skips other values
#string slices my_list=[0,1,2,3,4,5]
#my_list[1]=1 etc 0 is first
#my_list[-1]is last etc
#my_list=[::-1] reverses list
#my_list[0:3] is my_list[start, end index not inclusive]
#my_list[0:] start to finish
       
