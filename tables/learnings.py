if __name__ == '__main__':

    #Beispiel für Seiteneffekte bei iterables
    # Die Frage ist, ob folgender Code die Tabelle nach Zeile ['b',5,6] filtert:
    # for row in lis
    # if row[0]!='b':
    #   lis.remove[row]

    #Antwort: Nein. Der iterator erhält hier einen Seiteneffekt.

        lis = [
            ['a', 1, 2],
            ['a', 3, 4],
            ['b', 5, 6]
        ]
        for row in lis:
            print("Betrachte row:", row)
            if row[0] != 'b':
                lis.remove(row)
                print(row)
                print(lis)
        print(lis)