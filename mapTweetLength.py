#!/usr/bin/python

import sys
import json

count_ln =0
Prez_twit_count = 0
input_dict = {}
user_dict ={}
#createdtime =[]
map_out ={}
PreZLength = 0
OtherLength = 0

tweet_det = False
PrezCount =0
OtherCount =0
Prez_Len_count = {}
Other_Len_count = {}

for line in sys.stdin:
  #count_ln is to count number of tweets it processed
  input_dict = json.loads(line)
  user_dict = input_dict['user']
  if user_dict['screen_name'] == "PrezOno":
    tweet =  input_dict['text']
    PreZLength = PreZLength + len(tweet)
    PrezCount = PrezCount + 1
    tweet_det = True
  else:
    tweet =  input_dict['text']
    OtherLength = OtherLength + len(tweet)
    OtherCount = OtherCount + 1
    
#print '%s\t%s' % ('PrezOno',len(tweet))
    
if tweet_det == True:
  Prez_Len_count={'PrezOno': [PreZLength, PrezCount]}
  print '%s\t%s' %('PrezOno', Prez_Len_count['PrezOno'])
  tweet_det = False

Other_Len_count={'Other': [OtherLength, OtherCount]}
print '%s\t%s' %('Other', Other_Len_count['Other'])
       
       
#Test to check no of twits analysed by each mapper 
#print count_ln

