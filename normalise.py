# What this program does: Normalises a range of values, meaning one range of values is changed into another range of values

# Read more here: https://stackoverflow.com/a/28121940  and  https://en.wikipedia.org/wiki/Normalization_(image_processing)

# TO DO: add a way to normalise a range of bits rather than singular values (see bitValueTest)

# CONCERNS: what if the pixels colours are encoded in floats?


import math

def main():
    lsb = getMinBits() # least significant bits
    maxBits = getMaxBits() # total bits encoded in image (i.e. 8-bits for 256 colours)
    baseRange = getRangeOfBits(lsb) # range of colours for the LSB entered.
    goalRange = getRangeOfBits(maxBits) # range of colours to normalise to
    convertedRange = normalise(baseRange, goalRange) # normalise the LSB range
    
    bitValueTest(convertedRange) #DEBUG normalises any binary values to the original colour range.

# get the number of least signifcant bits to use.
def getMinBits():
    while True:
        try:
            leastSigBits = int(input("What is the number of least significant bits?"))
            if leastSigBits > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")
    return leastSigBits

 
# get the total number of bits. i.e. if original image uses 256 colours, use 8-bits.
def getMaxBits():
    while True:
        try:
            colourBits= int(input("What is the number of bits of colour? (8-bits default)"))
            if colourBits > 7:
                break
            else: # add a way to default to 8-bits (256 colours)
                colourBits = 8
                break
        except ValueError:
            print("Please enter a positive integer of 8 or more.")
    return colourBits
   
# range of bits to use, to compare LSB range to original range.
def getRangeOfBits(sigBits):
    maxBitValue = 2**sigBits # power of 2
    print("maxBitValue = ", maxBitValue) #debug
    rangeOfBits = list(range(0,maxBitValue))
    #print("rangeOfBits = ", rangeOfBits) #debug
    return rangeOfBits
    
    
def normalise(baseBits, goalBits):
    baseMinValue = baseBits[0]
    print("baseMinValue = ", baseMinValue) # the first value in the range of bits (should be 0)
    
    
    baseMaxValue = baseBits[-1]
    print("baseMaxValue = ", baseMaxValue) # the number of values in the bit array (should be log2 of the colourBits, i.e. log2 of 8 colour bits = 3)
    
    goalMaxValue = goalBits[-1] # the final value in the range of bits (i.e. 8-bits = 255)
    print("goalMaxValue = ", goalMaxValue)
    
    convertBy = math.ceil(goalMaxValue / baseMaxValue) # the amount to step the range of colour values by to fit the original colour encoding
    print("convertBy = ", convertBy)
    
    finalColourRange = [i*convertBy for i in baseBits] # stretches/normalises the LSB colour range to fit the range of the original colour encoding using the step value above (i.e. 2 bits to 8 bits = [0, 85, 170, 255])
    print("Final range: ", finalColourRange)
    return finalColourRange
    
# test for converting binary numbers to the colour values from normalised colour range.
def bitValueTest(bitRange):
    colourBitValue = 0b10 # 2 in binary
    print("colourBitValue = ", colourBitValue)
    
    convertedBit = bitRange[colourBitValue] # convert binary value to decimal colour value from normalised range (i.e. 2 becomes 170 in 2-bit LSB normalised to 8-bits)
    print("convertedBit = ", convertedBit)
    
    toBinary = bin(convertedBit) # convert new decimal back to binary for colour encoding
    print("toBin = ", toBinary)
    
    toRawBinary = toBinary[2:]
    print("toRawBinary = ", toRawBinary) # convert to raw binary (i.e. remove "0b" from "0b101010")
    
    
if __name__ == "__main__":
    main()