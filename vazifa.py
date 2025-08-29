def vazifa_qoshish(vazifalar):
    matn = input("Yangi vazifani kiriting: ").strip()
    if not matn:
        print("Bosh vazifa qoshib bolmaydi!")
    else:
        vazifalar.append(matn)
        print("✅ Vazifa qoshildi.")


def vazifalarni_korish(vazifalar):
    if not vazifalar:
        print("Vazifalar royxati bo‘sh.")
    else:
        print(" Vazifalar royxati")
        for i, v in enumerate(vazifalar, start=1):
            print(f"{i}. {v}")


def vazifa_ochirish(vazifalar):
    if not vazifalar:
        print("Ochirish uchun vazifa yoq.")
        return

    raqam = input("Ochirish uchun vazifa raqamini kiriting: ").strip()
    if not raqam.isdigit():
        print("Iltimos, faqat raqam kiriting.")
        return

    idx = int(raqam)
    if 1 <= idx <= len(vazifalar):
        ochgan = vazifalar.pop(idx - 1)
        print(f"Vazifa ochirildi: {ochgan}")
    else:
        print("Bunday raqamli vazifa mavjud emas.")
