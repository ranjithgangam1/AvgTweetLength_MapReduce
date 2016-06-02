# AvgTweetLength_MapReduce
Average TweetLength Calculation Using Map Reduce.

###This data is twitter data for last one year of Cincinnati city. It is in JSON format. It is distributed in 50 node cluster.
####How does @PrezOno’s tweet length compare to the average of all others?  What is his average length?  All others?

Approach:
I chose streaming-mode. I wrote Map and Reduce jobs in python. mapTweetLength.py and reduceTweetLength.py are the map and reduce python files.

Mapper explanation: 
Mapper reads each tweet from HDFS file system and checks whether it has tweet from PrezOno, counts its length and number of tweets from president. If it is a tweet from other user it emits ‘Others’ as key, [length of tweets and count of tweets] from them as value.

Mapper output <PrezOno/Other, [tweet_length, tweet_count]>
Example mapper output:  
PrezOno, [120, 2]
Others, [10000, 26]
Others, [12000, 30]

Reducer explanation:
Reducer get tweet length and count from each mapper. Reducer adds them and calculates average length by dividing with tweet count. It separates PrezOno tweet average and others average and writes them to output file.

Reducer output <PrezOno average/other, average tweet length>

Reducer Output from HDFS.

PrezOno average	[104.33431085043988]
Others average	[81.697261873883733]


