from vazifa import vazifa_qoshish, vazifalarni_korish, vazifa_ochirish
from file import vazifalarni_yuklash, vazifalarni_saqlash

def menyu():
    print("Vazifa royxati")
    print("1 - Vazifa qoshish")
    print("2 - Ro'yxatni korish")
    print("3 - Vazifani ochirish")
    print("0 - Chiqish")

def main():
    vazifalar = vazifalarni_yuklash()

    while True:
        menyu()
        tanlov = input("Tanlovni kiriting: ").strip()

        if tanlov == "1":
            vazifa_qoshish(vazifalar)
        elif tanlov == "2":
            vazifalarni_korish(vazifalar)
        elif tanlov == "3":
            vazifa_ochirish(vazifalar)
        elif tanlov == "0":
            vazifalarni_saqlash(vazifalar)
            print("Dasturdan chiqildi. Vazifalar saqlandi.")
            break
        else:
            print("Notogri tanlov, qaytadan urinib koring.")

if __name__ == "__main__":
    main()
