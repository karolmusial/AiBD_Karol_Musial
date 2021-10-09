### Celem projektu było uporządkowanie zbioru danych na temat liczby zarażeń gruźlicą w różnych krajach i przedziałach wiekowych zgodnie z protokołem <b>TIER</b> i zasadami <b>"Tidy Data"</b>.
 1. Analizę rozpoczęto od wczytania i wyświetlenia bazy zapisanej w pliku .csv. Surowe dane były calkowicie nieczytelne oraz niezdatne do analizy, dlatego niezbędne było przeprowadzenie kilku operacji.
 2. Korzystając z modułu <b>Pandas</b> oraz udostępnianych przez niego funkcji, w pierwszym kroku dokonano "meltowania" danych (funkcja <b>melt()</b>) czyli zamiany kolumn na wiersze oraz wyszczególnienie kolumny <b>"Cases"</b> (zawierającej informację o liczbie zarażeń) i <b>"Mixed"</b> (wciąż nieczytelny zlepek wielu danych).
 3. W drugim kroku rozdzielono kolumnę <b>"Mixed"</b> składającą się z: niepotrzebnego prefiksu "new_sp", informacji i płci oraz grupie wiekowej. - funkcja <b>str.split()</b>
 4. W ten sposób otrzymano kilka niepotrzebnych kolumn które należało usunąć ze struktury, korzystając z <b>drop()</b>.
 5. Następnie zamieniono miejscami kolumny z liczbą przypadków oraz z przedziałem wiekowym. Zmieniono nazwy na bardziej odpowiadające zawieranym informacjom (<b>rename()</b>) oraz posortowano wiersze w pierwszej kolejności według państwa, a w drugiej według roku - <b>sort_values()</b>.
 6. By poprawić wizualizację danych, zmodyfikowano wszystkie komórki kolumny <b>"Age"</b> i przy pomocy funkcji <b>apply()</b> oraz dość złożonego wyrażenia lambda odseparowano poszczególne fragmenty ciągu cyfr, zwiększając tym samym czytelność.
 7. Ostatnim etapem przetwarzania było pozbycie się zepsutych oraz pustych rekordów, w tym celu zastosowano ponownie funkcję <b>drop()</b>.

Po tych kilku operacjach rozmiar bazy danych został zredukowany z ponad <b>110 tysięcy</b> wpisów do niewele ponad <b>30 tysięcy</b>.

### W części podsumuwującej i wizualizującej strukturę, przedstawiono informację o danych oraz ich opis.

Do analizy wyników wykorzystano pakiet <b>pyplot</b> z biblioteki <b>matplotlib</b>, w ten sposób stworzono dwa wykresy:
 - Pierwszy z nich, prezentujący liczbę zarażeń przypadającą na dany rok jasno pokazuje, że przez pierwsze 15 lat badań, gruźlica rozprzestrzeniała się dość wolno, ogromny skok nastąpił w roku 1995 i stopniowo zwiększał się przez następne lata aż do roku 2008 gdzie zakończono gromadzenie danych.
 - Drugi wykres opisuje liczbę zarażeń ze względu na przedział wiekowy. Najbardziej narażone na ryzyko zakażenia są osoby między 20 a 40 rokiem życia, czyli najczęściej pracujące i posiadające kontakt z wieloma ludźmi. Osoby starsze również wykazują skłonność do zarażenia, jednak dziwić może fakt, że wśród dzieci do 14 roku życia odnotowuje się małą ilość zarażeń.

<b>Po zakończonej odbróbce i analizie, nowe, przetworzone dane zapisano do pliksu .csv</b>
