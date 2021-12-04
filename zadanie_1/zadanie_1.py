def podzielniki_wlasciwe(liczba):
    lista = []
    for podzielnik in range(1, liczba):
        if liczba % podzielnik == 0:
            lista.append(podzielnik)
    return lista


if __name__ == "__main__":
    liczba_uzytkownika = int(input("Podaj liczbę całkowitą os 1 do n...: "))
    for liczba in range(1, liczba_uzytkownika + 1):
        podzielniki = podzielniki_wlasciwe(liczba)
        if liczba == sum(podzielniki):
            print(f"Liczba {liczba} jest doskonała dla podzielników {podzielniki}")
