import re
VALID_NUMS_ZEROS = {}


def validNumbersAndZeros():
    global VALID_NUMS_ZEROS
    baseNum = 255
    VALID_NUMS_ZEROS = {255: 0}
    power = -1
    while baseNum:
        power += 1
        baseNum = baseNum - (2**power)
        VALID_NUMS_ZEROS[baseNum] = power+1
    print("valid nums and zeros", VALID_NUMS_ZEROS)

# input 255.255.255.162 -> 8+8+8+0
# 255 -> 1 1 1 1 1 1 1 0

def countOnes(number):
    zeros = 0

    # # base conditions
    # if number == 255:
    #     return 8
    # if number == 0:
    #     return 0

    # # approach1 - find ones from left to right
    # for bit in range(8, -1, -1):
    #     if not (number & (1 << bit)):
    #         zeros += 1

    # # approach2 - find zeros from right to left
    # for bit in range(0, 8):
    #     if not (number & (1 << bit)):
    #         zeros += 1
    #     else:
    #         break

    # # approach3 - find zeros by calculating ones in diff
    # diff = 255-number
    # while diff:
    #     diff = diff & (diff-1)
    #     zeros += 1

    # approach4 - use precomputed dict holding valid numbers and zeros
    zeros = VALID_NUMS_ZEROS[number]

    return 8-zeros

def isValidPart(partInt):
    if partInt not in VALID_NUMS_ZEROS:
        return False
    return True
    # foundOne = False
    # for i in range(8):
    #     result = (partInt & 1<<i)
    #     if not foundOne and result == 1:
    #         foundOne = True
    #     elif foundOne and result == 0:
    #         return False
    # return True

def findOnesInMask(mask):
    pat = re.compile('([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})')
    res = pat.match(mask)
    ones = 0
    if res:
        groups = res.groups()
        if len(groups) != 4:
            return -1

        if not isValidPart(int(groups[0])): #invalid
            return -1

        ones += countOnes(int(groups[0]))

        taper = True if int(groups[0]) < 255 else False

        for grpIndex in range(1, len(groups)):
            if taper:
                if groups[grpIndex] != '0':
                    return -1
                elif groups[grpIndex] == '0':
                    ones += countOnes(int(groups[grpIndex]))
            else:
                if not isValidPart(int(groups[grpIndex])): #invalid
                    return -1
                if groups[grpIndex] != '255' and groups[grpIndex-1] != '255':
                    return -1
                if groups[grpIndex] == '255' and groups[grpIndex-1] != '255':
                    return -1

                if groups[grpIndex] != '255' and groups[grpIndex - 1] == '255':
                    taper = 1
                ones += countOnes(int(groups[grpIndex]))
        return ones
    return -1

validNumbersAndZeros()

mask = "255.255.255.0"
count = findOnesInMask(mask)
print("mask", mask, "ones", count)
