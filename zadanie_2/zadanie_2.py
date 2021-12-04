liczba_uzytkownika = int(input("Podaj liczbę całkowitą os 1 do n...: "))

if liczba_uzytkownika <= 5:
    for _ in range(liczba_uzytkownika):
        print(liczba_uzytkownika * "*")
else:
    for line in range(liczba_uzytkownika):
        if line in (0, liczba_uzytkownika - 1):
            print(liczba_uzytkownika * "*")
        else:
            plot_line = "*" + (line - 1) * " " + "*" + (liczba_uzytkownika - (2 + line)) * " " + "*"
            print(plot_line)
