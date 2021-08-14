#!/usr/bin/python

import vcf
import regex
import math
import sys, getopt

#using pandas for ease of merging columns to tsv files
import pandas as pd


#using this because I can't easily sort an excel sheet using the apache poi but I can sort using pandas library


def main(argv):
    global inputfiles
    
    inputfiles=[]
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'merge_annovar.py -i <inputannovar, can be multiple, specify each by -i>  -o <outputannovar>'
        sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
        print 'merge_annovar.py -i <inputannovar, can be multiple, specify each by -i>  -o <outputannovar>'
        print 'The purpose of the simple python script is to sort and merge multiple annovar files generated by different pipelines'
        print 'variants will be sorted by chr location then position'
        sys.exit()
      elif opt in ("-i", "--ifile"):
        inputfiles.append(arg)
      elif opt in ("-o", "--ofile"):
        outputfile = arg
    for i in range(0,len(inputfiles)):
        if i == 0:
            result=pd.read_csv(inputfiles[i],delimiter="\t")
        else:
            inputfile=pd.read_csv(inputfiles[i],delimiter="\t")
            result=pd.concat([result,inputfile])
            
    result=result.sort(['Chr','Start'], ascending=[True,True])    
    result.to_csv(outputfile,sep="\t",index=False)    
    
    
    
#############end def main  




if __name__ == "__main__":
   main(sys.argv[1:])     