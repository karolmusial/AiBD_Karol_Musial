Celem projektu było uporządkowanie zbioru danych na temat liczby zarażeń gruźlicą w różnych krajach i przedziałach wiekowych zgodnie z protokołem TIER i zasadamy "Tidy Data".
Analizę rozpoczęto od wczytania i wyświetlenia bazy zapisanej w pliku .csv. Surowe dane były calkowicie nieczytelne oraz niezdatne do analizy, dlatego niezbędne było przeprowadzenie kilku operacji.
Korzystając z modułu Pandas oraz udostępnianych przez niego funkcji, w pierwszym kroku dokonano "meltowania" danych czyli zamiany kolumn na wiersze oraz wyszczególnienie kolumny "Cases" (zawierającą informację o liczbie zarażeń) i "Mixed" (wciąż nieczytelny zlepek wielu danych"
W drugim kroku rozdzielono kolumnę "Mixed" składającą się z: niepotrzebnego prefiksu "new_sp", informacji i płci oraz grupie wiekowej.
W ten sposób otrzymano kilka niepotrzebnych kolumn które usunąć ze struktury.
Następnie zamieniono miejscami kolumny z liczbą przypadków oraz z przedziałem wiekowym. Zmieniono nazwy na bardziej odpowiadające zawieranym informacjom oraz posortowano wiersze w pierwszej kolejności według państwa, a w drugiej według roku.
By poprawić wizualizację danych, zmodyfikowano wszystkie komórki kolumny "Age" i przy pomocy funkcji apply() oraz dość złożonego wyrażenia lambda odseparowano poszczególne fragmenty ciągu cyft, zwiększając tym samym czytelność
Ostatnim etapem przetwarzania było pozbycie się zepsutych oraz pustych rekordów, w tym celu zastosowano funkcję drop().

Po tych kilku operacjach rozmiar bazy danych został zredukowany z ponad 110 tysięcy wpisów do niewele ponad 30 tysięcy.
W części podsumuwującej i wizualizującej strukturę, przedstawiono informację o danych oraz ich opis.

Do analizy wyników wykorzystano pakiet pyplot z biblioteki matplotlib, w ten sposób stworzono dwa wykresy.
Pierwszy z nich, prezentujący liczbę zarażen przypadającą na dany rok jasno pokazuje, że przez pierwsze 15 lat badań, gruźlica rozprzestrzeniała się dosyć wolno, ogromny skok nastąpił w roku 1995 i stopniowo zwiększał się przez następne lata aż do roku 2008 gdzie zakończono gromadzenie danych.
Drugi wykres opisuje liczbę zarażeń ze względu na przedział wiekowy. Najbardziej narażone na ryzyko zakażenia są osoby między 20 a 40 rokiem życia, czyli najczęściej pracujące i posiadające kontakt z wieloma ludźmi. Osoby starsze również wykazują skłonność do zarażenia, jednak dziwić może fakt że dzieci wśród dzieci do 14 roku życia odnotowuje się mała ilość zarażeń.
