""" SURAJ MAHESH SHETTY - This script prompts ord user to enter encoded file name & bit length(encoding bits) at command line to Decode/De-Compress the file using LZW algorithm"""

import sys  # To access System-specific parameters and functions
import io   # To access I/O Streams

print("Welcome to Lempel-Ziv-Welch De-compression Algorithm")
TABLE = []
FINAL = []


INPUTFILE = sys.argv[1]     # To take input
FILE = io.open(INPUTFILE, 'r', encoding = 'UTF-16BE')       # Read the input
INPUTSTR = FILE.read()

BIT_LENGTH = sys.argv[2]     # Get the bit length from the user

if (int(BIT_LENGTH) < 9) or (int(BIT_LENGTH) > 16):
    print("Please enter bitlength between 9-16 as processor interpretor is set 8 to 16bits")
else:Encdoing_Bits = int (BIT_LENGTH)
	
MAX_TABLE_SIZE = 2 ** Encdoing_Bits # 2 to the power of bit length

for i in range(0,255):      # Table range with max and min values as in pseudo code
    TABLE.append(chr(i))

STRING = TABLE[ord(INPUTSTR[0])]						    # First code to be appended to string
FINAL.append(TABLE[ord(STRING)])

for j in range(1,len(INPUTSTR)):						# Check any codes yet to be recieved
    if ord(INPUTSTR[j]) >= len(TABLE):					# Decoder may not yet have code. So, checking it!
        NEW_STRING = STRING + STRING[0]
    else:
        NEW_STRING = TABLE[ord(INPUTSTR[j])]
    FINAL.append(NEW_STRING)								
    if len(TABLE) < MAX_TABLE_SIZE:						# If table is not full
        TABLE.append(STRING + NEW_STRING[0])
    STRING = NEW_STRING	
j=j+1
print('\nDecoded Output is:\n'+''.join(FINAL))  	

OUTPUTFILE = INPUTFILE.split(".")[0]+"_Decompressed"+".txt"  # to append file extension after(0th position) after name ends(.)
LZWD = open(OUTPUTFILE,'w')                       	    # Open file to write
LZWD.write(''.join(FINAL))
LZWD.close()                            				# closes the output file
FILE.close()											# closes the input file
print("\nDecoded/Decompressed FILE SAVED AS - " +OUTPUTFILE)
print("\n")