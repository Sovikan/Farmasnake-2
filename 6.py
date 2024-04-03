def dec2bin(decimal):
    binary = bin(decimal)[2:].zfill(8)
    return binary

def bin2dec(binary):
    decimal = int(binary, 2)
    return decimal
