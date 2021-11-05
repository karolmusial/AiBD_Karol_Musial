Plik 'original_data' zawiera statystyki zakupów odkurzaczy w województwie Małopolskim.Dane są wstępnie obrobione, zachowane są zasady Tidy Data, jednak nie wszystko jest przyjazne do analizy. Plik zawiera 6 kolumn:
 - <b>Unnamed:0</b> - kolumna odpowiadająca indexom rekordów (od 0 do 505)
 - <b>Dni od zakupu</b> - ile dni upłynęło od dokonania zakupu (od 1 do 15)
 - <b>Marka</b> - marka zakupionego odkurzacza (Beko, Dyson, Tefal, Samsung, Electrolux)
 - <b>Wiek kupującego</b> - wiek kupującego sprzęt (od 18 do 70 lat)
 - <b>Płeć kupującego</b> - kobieta lub mężczyzna
 - <b>Ocena</b> - punkty opisujące zadowolenie klienta (od 0 do 5)

Dane poddano drobnej zmianie (zmianie nazw i pozbyciu się niechcianych wartości) przed przystąpieniem do właściwej analizy.

Pozbyto się pierwszej redundantnej kolumny odpowiadającej indexowi, pozbyto się polskich znaków z pozostałych i zmieniono ich nazwy na angielskie. Oprócz tego zamieniono oznaczenie 'bd.' - brak danych w kolumnie płci na uniwersalną w analizie wartość None.
