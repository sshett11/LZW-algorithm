""" SURAJ MAHESH SHETTY - This script prompts a user to enter file name & bit length(encoding bits) at command line to Encode/Compress the file using LZW algorithm"""

import sys       # To access System-specific parameters and functions
import io        # To access I/O Streams

print("Welcome to Lempel-Ziv-Welch Compression Algorithm")
STRING = ""
FINAL = []
TABLE = []
CONVERT = ""    

INPUTFILE = sys.argv[1]         # To take input
FILE = open(INPUTFILE, 'r')     # Read the input
INPUTSTR = FILE.read()         
print("\nFile entered for read is:\n\n"+ INPUTSTR)
 
BIT_LENGTH = sys.argv[2]        # Get the bit length from the user

if (int(BIT_LENGTH) < 9) or (int(BIT_LENGTH) > 16):
    print("Please enter bitlength between 9-16 as processor interpretor is taking 8 to 16bits")
else:Encdoing_Bits = int(BIT_LENGTH)

MAX_TABLE_SIZE = 2 ** Encdoing_Bits  # 2 to the power of bit length


for i in range(0, 255):     # Table range with max and min values as in pseudo code
    TABLE.append(chr(i))

for SYMBOL in INPUTSTR:
    TOTAL = STRING + SYMBOL    
    if TOTAL in TABLE:    		
        STRING = TOTAL
    else:
        FINAL.append(TABLE.index(STRING))     
        if len(TABLE) < MAX_TABLE_SIZE:        # If table is not full
            TABLE.append(STRING + SYMBOL)      # STRING + SYMBOL has a code now
            STRING = SYMBOL
FINAL.append(TABLE.index(STRING))             # Output the code for STRING


for CODE in FINAL:
    CONVERT = CONVERT + chr(CODE)

print("\nEncoded Output is:\n"+str(FINAL))

OUTPUTFILE = INPUTFILE.split(".")[0]+".lzw"      # to append file extension after(0th position) after name ends(.)
LZWC = open(OUTPUTFILE, 'wb')            	     # Open file to write
LZWC.write(CONVERT.encode("UTF-16BE"))           # Encode to 16 Bit format 
LZWC.close()                                     # closes the output file
FILE.close()							         # closes the input file
print("\nEncoded/Compressed FILE SAVED AS - " +OUTPUTFILE)
print("\n")