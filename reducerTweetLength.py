#!/usr/bin/python
import sys
import string
import json

input_dict = {}
count_dict ={}
tweet_count =0
count =[]
Oldtime = None
PreZLength = 0
Prezcount = 0
OtherLength = 0
othercount =0
tweet_det = False
for line in sys.stdin:
    line = line.strip()
    (name,tweet_stats) =line.split('\t',1)
    twt1 = tweet_stats.strip('[],')
    twt= twt1.strip('').split(',')
    #print type(a)
    if name == 'PrezOno':
      #a= list(tweet_stats)
      a= twt[0]
      PreZLength = PreZLength + int(a)
      Prezcount = Prezcount + int(twt[1])
      tweet_det = True
      
    else:
      OtherLength = OtherLength + int(twt[0])
      othercount = othercount + int(twt[1])
      

if tweet_det == True:
  print '%s\t%s' %('PrezOno average', [float(PreZLength)/Prezcount])
  tweet_det = False
  
print '%s\t%s' %('Others average', [float(OtherLength)/othercount]  )



