def convert_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

if __name__ == "__main__":
    binary = input("Entrez un nombre binaire (8 bits) : ")
    if len(binary) == 8 and all(bit in '01' for bit in binary):
        decimal = convert_to_decimal(binary)
        print(f"Le nombre binaire {binary} en décimal est : {decimal}")
    else:
        print("Le nombre binaire entré n'est pas valide.")
