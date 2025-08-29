FAYL_NOMI = "malumotlar.txt"

def vazifalarni_yuklash():
    try:
        with open(FAYL_NOMI, "r") as f:
            return [qator.strip() for qator in f if qator.strip()]
    except FileNotFoundError:
        return []


def vazifalarni_saqlash(vazifalar):
    with open(FAYL_NOMI, "w") as f:
        for v in vazifalar:
            f.write(v + "\n")
