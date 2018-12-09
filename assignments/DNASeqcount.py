#!/usr/bin/env python
#This scripts counts specific bases in a DNA sequence provided from the commandline
#Prompt to type in the DNA sequence
DNASeq=input('Enter your DNA sequence here')
#Convert any lower case letters into uppercase
DNASeq=DNASeq.upper()
#Count each of the bases.
NumA=DNASeq.count('A')
NumC=DNASeq.count('C')
NumG=DNASeq.count('G')
NumT=DNASeq.count('T')
#Output the numbers
print ('Number of As:', NumA)
print ('Number of Cs:', NumC)
print ('Number of Gs:' , NumG)
print ('Number of Ts:', NumT)

# DB: Good! The only thing is that you're missing the '#' in the shebang line.