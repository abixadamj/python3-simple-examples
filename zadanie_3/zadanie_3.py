def czas_txt(dni_max):
    lat = dni_max // 365
    miesiecy = (dni_max - (lat * 365)) // 30
    dni = (dni_max - (lat * 365) - (miesiecy * 30))
    return f"{lat} lat, {miesiecy} miesiecy i {dni} dni"


def licz_wiek(data_urodzenia):
    from datetime import datetime
    data_urodzenia = datetime.fromisoformat(data_urodzenia)
    dokladny_wiek = datetime.now() - data_urodzenia
    brakuje = "nic"
    lata = dokladny_wiek.days // 365
    if lata < 18:
        brakuje = czas_txt(6570 - dokladny_wiek.days)
    return lata, brakuje


if __name__ == "__main__":
    data_urodzenia = input("Podaj datę urodzenia (YYYY-MM-DD): ")
    wiek, brakuje = licz_wiek(data_urodzenia)
    if wiek < 18:
        print(f"Brakuje ci {brakuje} dni do 18 lat....")
    else:
        print(f"Masz już ponad 18 lat... {wiek} lat.")
