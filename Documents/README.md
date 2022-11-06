# Dane o gruźlicy w różnych grupach pacjentów.

## 1. Zawartość pliku źródłowego.

Plikiem źródłowym jest tabela w formacie csv zawierająca dane o przypadkach gruźlicy. Plik ten znajduje się w folderze 
'Analysis Data'.

Kolumny tabeli w pliku źródłowym opisują kolejno: 
1. Indeks wiersza, 
2. iso2 - kod kraju w formacie [iso-2](https://pl.wikipedia.org/wiki/ISO_3166-1_alfa-2).
3. year - rok, w którym wystąpiła dana liczba nowych przypadków.
4. new_sp - całkowita liczba przypadków w danym roku w danym kraju.
5. Kolumny 5-13 - liczba przypadków wśród mężczyzn w danej grupie wiekowej, np. new_sp_m1524 oznacza liczbę nowych
przypadków wśród mężczyzn w wieku między 15 a 24 rokiem życia. Warto zwrócić uwagę na obecność trzech kolumn: new_sp_m04,
new_sp_m0514 oraz new_sp_m014. Może ona spowodować wygenerowanie błędnych wyników, ponieważ w niektórych krajach i latach
grupa wiekowa 0-14 lat była traktowana jako jedna grupa, a w innych jako dwie grupy. W drugim przypadku kolumna
new_sp_m014 zawiera sumę kolumn new_sp_m04 oraz new_sp_m514.
6. new_sp_mu - liczba przypadków wśród mężczyzn w nieznanym wieku.
7. Kolumny 15-23 0 liczba przypadków wśród kobiet w danej grupie wiekowej. Sposób kodowania taki sam jak w przypadku
kolumn 5-13, zawierających informację o mężczyznach. Mamy do czynienia z tym samym problemem jak wyżej z kolumnami
new_sp_f04, new_sp_f0514 oraz new_sp_f014.
8. new_sp_fu - liczba przypadków wśród kobiet w nieznanym wieku.

## 2. Modyfikacje danych źródłowych.

Dane źródłowe zawierają komórki, o wartości NaN, co oznacza brak pomiaru w danej kategorii/roku. W celu wygodniejszego 
korzystania z danych, komórki te zostały zamienione na zera. Dodatkowo część wierszy zawierała pomiary, które wskazywały
na 0 przypadków w danym pomiarze. Wiersze te zostały odrzucone, a przy tworzeniu wykresów przyjęto, że brak danej kolumny
oznacza zero przypadków w danym roku i kraju. 

Modyfikacji pliku źródłowego dokonuje skrypt 'process_data.py' z folderu 'Command Files'

Wynikowa tabela została zapisana w pliku tb_processed.csv w folderze Analysis Data.

## 3. Wyniki analizy.

Na podstawie przetworzoncyh danych stworzono trzy wykresy. Wszytkie one są dostępne w skrypcie 
"generate_result.ipynb" w folderze "Command Files". Opis wykresów:

### a) Wykres przypadków gruźlicy w różnych grupach wiekowych i płciowych.

Wykres ten przedstawia całkowitą liczbę przypadków we wszystkich latach i krajach dla konkretnych grup wiekowych oraz płci.
Jego analiza pozwala nam stwierdzić, że w każdej grupie wiekowej mężczyźni są grupą z większą liczbą przypadków od kobiet,
a najwięcej przypadków, niezależnie od płci, jest w grupie wiekowej 25-34 lat. Natomiast najmniej przypadków odnotowano
w grupach wiekowych 0-14 lat.

Dane te niekoniecznie oznaczają, że osoby w wieku 25-34 lat, a szczególnie mężczyźni, są najbardziej podatne na gruźlicę.
Podwyższona liczba przypadków może oznaczać większą wykrywalność gruźlicy w tych grupach (np. ze względu na częstsze 
objawy ciężkie) lub może wynikać z większej liczby ludności w tych grupach wiekowych i płciowych w danych krajach i 
latach. Dlatego w dalszej analizie tych badań należałoby porównać ilość przypadków do ogólnej liczby ludności w danej 
grupie. Dodatkowo należałoby ustalić, w jaki sposób przebiega choroba wśród różnych grup oraz dowiedzieć się, co tak 
naprawdę oznacza.

### b) Wykres ilości przypadków w poszczególnych latach.

Drugi wykres przedstawia liczbę przypadków gruźlicy na świecie w latach 1980-2008. Na osi y zastosowano skalę 
logarytmiczną, ponieważ pozwala ona w łatwiejszy sposób spojrzeć na wszystkie dane oraz ocenić relatywny wzrost 
liczby przypadków, a nie bezwzględny. Analizując ten wykres można dojśc do wniosku, że jedynie w początkowych latach
obserwowano spadek liczby przypadków gruźlicy, natomiast poźniej następował nieustanny wzrost, z największym skokiem w 
latach 1992-1993.

Większa liczba przypadków w poszczególnych latach nie musi też oznaczać wzrostu rzeczywistej liczby przypadków, ale może
wynikać z większego stopnia wykrywalności przypadków. Dlatego w dalszej analizie należałoby porównać te wyniki z liczbą
wykonywanych testów oraz powszechnością badań w kierunku gruźlicy w danych latach. Dodatkowo można by było dowiedzieć się,
jakie metody wykrywania przypadków były stosowane oraz jak dokładne one były. 

### c) Wykres całkowitej liczby przypadków w dwóch krajach o największej sumarycznej liczbie przypadków.
Ostatni wykres prezentuje liczbę przypadków w dwóch krajach z podziałem na płeć. Mówi nam on o rozwoju i przebiegu 
choroby w krajach najbardziej nimi dotkniętymi. Lepszym wyborem byłoby pokazanie dwóch krajów z największym procentowym
udziałem osób chorych w społeczeństwie, lecz do tego potrzebna by była informacja o całkowitej liczbie ludności w danych
krajach i latach. Brak tej informacji skłonił do rozwiązania obecnego w końcowej formie skryptu.

Wykres mówi nam, że najwięcej przypadków było w Indiach oraz Chinach, co nie jest zaskakujące, ponieważ to są jednocześnie
kraje z największą liczbą ludności. W obu jednak przypadkach można potwierdzić wniosek z pierwszego wykresu, że więcej 
zachorowań miało miejsce wśród mężczyzn. Na wykresie można zaobserwować wzrost liczby przypadków w każdej grupie w niemal
każdym kolejnym roku. Kształt wykresu dla kobiet i mężczyzn w danym kraju jest bardzo podobny, co w połączeniu z pierwszym
wykresem mogłoby być powodem do wysunięcia hipotezy o większej podatności na gruźlicę wśród mężczyzn, lecz do potwierdzenia
jej należałoby przeanalizować inne badania oraz dane.


