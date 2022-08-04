def dexRomEng(cuvinte_romana, cuvinte_engleza):
    word = input('cuvant in romana: ').strip().lower()
    if word in cuvinte_romana:
        return cuvinte_engleza[cuvinte_romana.index(word)]
    else:
        known = input("cunoastem traducerea cuvantului?: 1-->da, 2-->nu ").strip()
        while int(known) != 1 and int(known) != 2:
            known = input("cunoastem traducerea cuvantului?: 1-->da, 2-->nu ").strip()

        if int(known) == 1:
            translation = input('traducerea cuvantului: ').strip().lower()
            cuvinte_romana.append(word)
            cuvinte_engleza.append(translation)
            return "cuvant adaugat cu succes"
        else:
            return "nu exista traducere"


def dexEngRom(cuvinte_romana, cuvinte_engleza):
    word = input('cuvant in engleza: ').strip().lower()
    if word in cuvinte_engleza:
        return cuvinte_romana[cuvinte_engleza.index(word)]
    else:
        known = input("cunoastem traducerea cuvantului?: 1-->da, 2-->nu ").strip()
        while int(known) != 1 and int(known) != 2:
            known = input("cunoastem traducerea cuvantului?: 1-->da, 2-->nu ").strip()
        
        if int(known) == 1:
            translation = input('traducerea cuvantului: ').strip().lower()
            cuvinte_romana.append(translation)
            cuvinte_engleza.append(word)      
            return "cuvant adaugat cu succes"
      
        else:
            return "nu exista traducere"

def checkLang(rom_eng, cuvinte_romana, cuvinte_engleza):
    if int(rom_eng) == 1:
        return dexRomEng(cuvinte_romana, cuvinte_engleza)
    else:
        return dexEngRom(cuvinte_romana, cuvinte_engleza)
    

def typeLang():
    rom_eng = input("press 1 for ro-en and 2 for en-ro: ").strip()
    while rom_eng != str(1) and rom_eng != str(2):
        rom_eng = input("press 1 for ro-en and 2 for en-ro: ").strip()
    return rom_eng

def main():
    cuvinte_romana = ['mama', 'tata']
    cuvinte_engleza = ['mother', 'father']
    rom_eng = typeLang()
    print(checkLang(rom_eng, cuvinte_romana, cuvinte_engleza))


if __name__ == '__main__':
    main()