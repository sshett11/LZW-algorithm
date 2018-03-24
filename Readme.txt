Program Overview : Encoder takes the input file and compresses the file into bits as given by LZW algorithm. The decoder takes the compressed file and turns into an uncompressed readable file. 

Data structure design: My program uses lists. Its a dynamic data structure in python and most used one. Lists can be concatenated, appended etc & list has better memory utilization over hash maps so when encoding/decoding
large files using LZW Algorithm, Lists will perform better than hash maps.

Files: Two files – LZWD.py and LZWE.py

Programming Language: Python

Python Environment Version : Python 3.6

IDE Used - Microsoft Visual Studio Community for Python  

How to run? 
(python filename  inputfilename	bitlength)
 
To encode - python LZWE.py input1.txt 12
To decode - python LZWD.py input1.lzw 12


I have even done in java, in java I used hashmaps and outputting binary 16 bit values, but my python code perfroms well and more accurate to the given conditions, so i am uploading this.