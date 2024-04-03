"""conversion binaire de 192.168.2.28 : 11000000.10101000.00000010.00011100"""

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary.zfill(8)

def dec2bin():
    decimal = int(input("Entrez un nombre décimal entre 0 et 255 : "))
    if 0 <= decimal <= 255:
        binary = decimal_to_binary(decimal)
        print(f"Le nombre {decimal} en binaire est : {binary}")
    else:
        print("Le nombre entré n'est pas entre 0 et 255.")

if __name__ == "__main__":
    dec2bin()
