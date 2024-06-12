# Projekt Śledzenia Przechodniów

## Opis Projektu

Projekt polega na stworzeniu systemu śledzącego przechodniów z wykorzystaniem probabilistycznych modeli grafowych. System ma za zadanie określić położenie przechodniów na kolejnych klatkach obrazu z kamery, przypisując odpowiednie prostokąty ograniczające (Bounding Boxes, BBoxes) do poszczególnych osób.

### Założenia Projektu

1. Dla każdej klatki obrazu dostępne są współrzędne BBoxes, ale nie jest określone, który BBox należy do którego przechodnia.
2. Zadaniem jest określenie, którym BBoxes z poprzedniej klatki odpowiadają BBoxes z aktualnej klatki. Można do tego wykorzystać dane z więcej niż dwóch klatek naraz.
3. Dla każdej klatki należy wypisać na standardowe wyjście liczby oddzielone spacją i zakończone znakiem nowej linii, gdzie liczba oznacza indeks BBox z poprzedniej klatki lub -1 w przypadku, gdy przechodzień dopiero pojawia się na ekranie.

### Przykładowe Wyjście

Dla dwóch klatek z dwoma i trzema BBoxes:

```
1 2
0 -1 1
```

### Struktura Danych

Ścieżka do katalogu ze zbiorem danych będzie podana jako pierwszy argument programu. Struktura katalogu:

```
.
├── frames
│   ├── c6s1_000451.jpg
│   ├── c6s1_000476.jpg
│   └── ...
└── bboxes.txt
```

Plik `bboxes.txt` zawiera dane o BBoxes:

```
nazwa_zdjęcia_0
N0
x_0 y_0 w_0 h_0
...
x_N0 y_N0 w_N0 h_N0
nazwa_zdjęcia_1
N1
x_0 y_0 w_0 h_0
...
x_N1 y_N1 w_N1 h_N1
```

Przykładowy plik `bboxes.txt`:

```
c6s1_000451.jpg
1
420.836933 144.188985 88.328294 216.466523
c6s1_000476.jpg
3
325.044276 151.653348 126.894168 204.025918
177.001080 160.361771 90.816415 153.019438
129.726782 129.260259 83.352052 195.317495
```

## Dodatkowe Informacje

### Wymagania Projektu
- Wykonany samodzielnie.
- Preferowaną formą oddania pracy jest prywatne repozytorium na GitHubie.
- Raport z opisem algorytmów umieszczony w pliku README.md. W raporcie opis koncepcji i zasady działania projektu.

### Przykładowe Dane
Przykładowe dane niezbędne do wykonania projektu można pobrać [tutaj](https://drive.google.com/file/d/1saVmRWqBBfeJTLH3Lo91bXtbI2h4T3vi/view?usp=sharing).

### Struktura Katalogu z Danymi
```
.
├── frames
│   ├── c6s1_000451.jpg
│   ├── c6s1_000476.jpg
│   └── ...
└── bboxes.txt
```

### Format Pliku `bboxes.txt`
```
nazwa_zdjęcia_0
N0
x_0 y_0 w_0 h_0
...
x_N0 y_N0 w_N0 h_N0
nazwa_zdjęcia_1
N1
x_0 y_0 w_0 h_0
...
x_N1 y_N1 w_N1 h_N1
```
gdzie:
- N0, N1: liczba BBoxes na zdjęciu 0 i 1.
- x, y, w, h: współrzędne prawego górnego wierzchołka oraz szerokość i wysokość.

Przykładowy plik `bboxes.txt`:
```
c6s1_000451.jpg
1
420.836933 144.188985 88.328294 216.466523
c6s1_000476.jpg
3
325.044276 151.653348 126.894168 204.025918
177.001080 160.361771 90.816415 153.019438
129.726782 129.260259 83.352052 195.317495
```

## TODO
- Implementacja funkcji sprawdzającej zgodność BBoxes na kolejnych klatkach.
- Testowanie i walidacja algorytmu na przykładowym zbiorze danych.
- Przeprowadzenie testów efektywności i wydajności algorytmu.
- Optymalizacja algorytmu pod kątem szybkości działania.
