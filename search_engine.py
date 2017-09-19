#!/usr/bin/python
#coding: utf-8

# Purpose: skeleton for the TextIR project
#
# Comment: parts to be completed or modified are denoted with '???'
#

# Code:

##########################################################################
#                            INITIALIZATION                              #
##########################################################################

from __future__ import division
from __future__ import unicode_literals
import os, codecs, sys, glob, re, getopt, random, operator, pickle
from math import *
from collections import defaultdict

reload(sys)
sys.setdefaultencoding('utf-8')


prg = sys.argv[0]
def P(output=''): raw_input(output+"\nDebug point; Press ENTER to continue")
def Info(output=''): print >> sys.stderr, output

#######################################
# special imports


#######################################
# files


#######################################
# variables



#########################################



#########################################
# USAGE - this part reads the command line

# typical call: search_engine.py -c cisi.all -q cisi.qry -o run1

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-c", "--collection", dest="file_coll",
                  help="file containing the docs", metavar="FILE")
parser.add_argument("-q", "--query", dest="file_query",
                  help="FILE contains queries", metavar="FILE")

# ??? update the path to the stop-word list here if needed

parser.add_argument("-s", "--stop", dest="file_stop", 
                  default='./common_words.total_en.u8.txt',  
                  help="FILE contains stop words", metavar="FILE")

parser.add_argument("-o", "--out", dest="prefix",
                  help="PREFIX for output files", metavar="STR")

parser.add_argument("-v", "--verbose",
                  action="store_false", dest="verbose", default=True,
                  help="print status messages to stdout")



args = parser.parse_args()

# command line arguments are named as  args.file_coll   args.file_query ...


################################################################################
################################################################################
##                                                                            ##
##                                 FUNCTIONS                                  ##
##                                                                            ##
################################################################################
################################################################################

def Tokenizer(sequence):
    # ??? transform a sequence as a list of words (or stems)
    # useful: line.split('...')  or better: re.split('...',line)
    # useful: line.lower()

    t_words = re.split('[ ,:!;,.,\',",\n,\r,:?]+', str(sequence).lower())

    return t_words


################################################################################
################################################################################
##                                                                            ##
##                                     CODE                                   ##
##                                                                            ##
################################################################################
################################################################################


Info('Reading stop words')

# useful: line = line.rstrip('\r\n') # remove the carriage return 

t_stop  = [ l.rstrip('\r\n') for l in codecs.open(args.file_stop) ]



#####################################################################

Info('Reading/indexing the collection file')


# ??? read and process the collection file to build the inverted file
# and collect any useful information (for TF-IDF/cosine or Okapi BM-25 or other models)

fileName=open(args.file_coll) # open file on read mode

dict_word  = defaultdict(lambda : defaultdict(lambda :0))

for line in fileName:
    m = re.match('^\.+I +([0-9]+)', line)
    if m is not None:
        did = m.group(1)
    else:
        for word in Tokenizer(line):
            dict_word[word][did]+=1

fileName.close()  # close file

#####################################################################

Info('Post-processing the inverted file')

# ??? filter out unwanted tokens in the inverted file
# compute IDF of terms (if TF-IDF is used)...
# useful: log(x)

# compute norms of documents (if cosine similarity is used)...
#useful: sum([(x*y)**2  for x in t_toto ])


#Filter of stop_words
for word in t_stop:
    if word in dict_word: del dict_word[word]

#Calculation of IDF

h_idf = {}
for word in dict_word:
    df = len(dict_word[word])
    h_idf[word] = log10( (len(dict_word)) / df )

#Calculation of vector length

h_norm = defaultdict(lambda :0)
for word in dict_word:
    for d in dict_word[word]:
        tf_idf = dict_word[word][d]*h_idf[word]
        h_norm[d] = tf_idf**2


#Square of h_norm
for v in h_norm:
    h_norm[v] = sqrt(h_norm[v])



#####################################################################


Info('Reading query file')


# dictionary query -> document -> score of document for this query
h_qid2did2score = defaultdict(lambda : defaultdict(lambda : 0))

# ??? read and process the queries and keep the results in a dictionary h_qid2did2score

fileName=open(args.file_query) # open file on read mode

for line in fileName:
    m = re.match('^\.+I +([0-9]+)', line)
    if m is not None:
        qid = m.group(1)
    else:
        for word in Tokenizer(line):
            for doc in dict_word[word]: # renvoie les doc
                tf_idf = dict_word[word][doc]*h_idf[word]
                h_qid2did2score[qid][doc] += tf_idf*h_idf[word]/h_norm[doc]
fileName.close()  # close file




# output the results with the expected results in a file
resultFile = open(args.prefix+'.res','w')

for qid in sorted(h_qid2did2score, key=int): # tri par numero de requete
    for (rank,(did,s)) in enumerate(sorted(h_qid2did2score[qid].items(), key=lambda (d,s):(-s,d) ) ): # tri par score decroissant 
        resultFile.write(str(qid)+'\tQ0\t'+str(did)+'\t'+str(rank+1)+'\t'+str(s)+'\tExp\n')

resultFile.close()
