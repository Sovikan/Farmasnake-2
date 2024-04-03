import 3_dec2bin_function as dec2bin_func
import 4_bin2dec_function as bin2dec_func

def main():
    choix = input("Choisissez le type de conversion (dec2bin ou bin2dec) : ")
    if choix == "dec2bin":
        decimal = int(input("Entrez un nombre décimal entre 0 et 255 : "))
        if 0 <= decimal <= 255:
            binary = dec2bin_func.dec2bin(decimal)
            print(f"Le nombre {decimal} en binaire est : {binary}")
        else:
            print("Le nombre entré n'est pas entre 0 et 255.")
    elif choix == "bin2dec":
        binary = input("Entrez un nombre binaire (8 bits) : ")
        if len(binary) == 8 and all(bit in '01' for bit in binary):
            decimal = bin2dec_func.bin2dec(binary)
            print(f"Le nombre binaire {binary} en décimal est : {decimal}")
        else:
            print("Le nombre binaire entré n'est pas valide.")
    else:
        print("Choix invalide. Veuillez choisir dec2bin ou bin2dec.")

if __name__ == "__main__":
    main()
