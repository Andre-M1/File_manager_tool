# File Manager - Menedżer Plików i Folderów

**Projekt edukacyjny** - skrypt został napisany w celach naukowych do nauki programowania w Pythonie.


Prosty menedżer plików i folderów z interfejsem konsolowym umożliwiający tworzenie, przemianowywanie i organizację plików w sposób interaktywny.

## O projekcie

Ten projekt powstał jako **ćwiczenie programistyczne** mające na celu:
- Naukę obsługi systemu plików w Pythonie
- Praktyczne zastosowanie bibliotek `pathlib` i `logging`
- Implementację wzorca projektowego z podglądem zmian
- Tworzenie intuicyjnego interfejsu konsolowego


## Funkcje

- **Nawigacja po katalogach** - przeglądanie struktury folderów
- **Tworzenie plików** - pojedynczo lub masowo z automatyczną numeracją
- **Tworzenie folderów** - pojedynczo lub masowo z automatyczną numeracją  
- **Sekwencyjne przemianowywanie** - automatyczne nadawanie nazw z numeracją
- **Podgląd zmian** - możliwość sprawdzenia operacji przed wykonaniem
- **Rozwiązywanie konfliktów** - automatyczne generowanie unikalnych nazw
- **Logowanie operacji** - wszystkie akcje zapisywane w pliku `logs`

## Wymagania

- Python min. 3.6 lub nowszy (Działa również na Python 3.13)
- System operacyjny: Windows, macOS, Linux

## Instalacja

1. Pobierz plik `file_manager.py`
2. Upewnij się, że masz zainstalowany Python 3.6+
3. Uruchom skrypt w terminalu/wierszu poleceń

## Użycie

### Uruchomienie programu
python file_manager.py


**Wskazówki:**
- Użyj pełnej ścieżki do folderu (np. `C:\Users\Nazwa\Documents\MojProjekt`)
- Na Linuksie/macOS: `/home/user/mojfolder` lub `~/mojfolder`
- Folder musi istnieć - program go nie utworzy automatycznie

### Menu główne

Po wybraniu folderu zobaczysz menu z opcjami:

=== MENEDŻER PLIKÓW I FOLDERÓW ===
Aktualny folder: C:\MojFolder

Zawartość folderu:
Foldery: folder1, folder2
Pliki: plik1.txt, plik2.doc

Przejdź do folderu

Wróć do folderu nadrzędnego

Utwórz foldery

Utwórz pliki

Utwórz foldery masowo

Utwórz pliki masowo

Zmień nazwy plików sekwencyjnie

Zmień nazwy folderów sekwencyjnie

Wyjście



### Szczegółowy opis opcji

#### **1. Przejdź do folderu**
- Wyświetla listę dostępnych folderów
- Wpisz numer folderu, do którego chcesz przejść
- Przykład: `Wybierz folder (1-3): 2`

#### **2. Wróć do folderu nadrzędnego**
- Przenosi do folderu wyżej w hierarchii
- Jeśli jesteś w folderze głównym, opcja nie będzie dostępna

#### **3. Utwórz foldery**
- Pozwala utworzyć jeden lub więcej folderów jednocześnie
- Wpisz nazwy folderów oddzielone przecinkami
- Przykład: `Nazwy folderów: Projekty, Dokumenty, Zdjęcia`

#### **4. Utwórz pliki**
- Pozwala utworzyć jeden lub więcej plików jednocześnie
- Wpisz nazwy plików z rozszerzeniami, oddzielone przecinkami
- Przykład: `Nazwy plików: notatki.txt, lista.doc, dane.xlsx`

#### **5. Utwórz foldery masowo**
- Tworzy określoną liczbę folderów z automatyczną numeracją
- Przykład: `Ile folderów: 5` → utworzy folder_001, folder_002, folder_003, folder_004, folder_005

#### **6. Utwórz pliki masowo**
- Tworzy określoną liczbę plików z automatyczną numeracją
- Przykład: `Ile plików: 3` → utworzy plik_001.txt, plik_002.txt, plik_003.txt

#### **7. Zmień nazwy plików sekwencyjnie**
- Przemianowuje wszystkie pliki w folderze na sekwencyjne nazwy
- Przykład: dokument1.txt, dokument2.txt → plik_001.txt, plik_002.txt

#### **8. Zmień nazwy folderów sekwencyjnie**
- Przemianowuje wszystkie foldery w folderze na sekwencyjne nazwy
- Przykład: MojFolder, InnyFolder → folder_001, folder_002

### Podgląd i potwierdzanie zmian

Przed wykonaniem każdej operacji program pokaże podgląd:

Podgląd zmian:
Utwórz folder: Projekty -> Projekty
Utwórz folder: Dokumenty -> Dokumenty_001

Zastosować zmiany? (tak/nie): tak


**Ważne:** Wpisz `tak` aby potwierdzić lub `nie` aby anulować operację.

### Rozwiązywanie konfliktów nazw

Program automatycznie rozwiązuje konflikty nazw:
- Jeśli folder `Projekty` już istnieje, nowy będzie nazywał się `Projekty_001`
- Jeśli `Projekty_001` też istnieje, następny będzie `Projekty_002` itd.

### Logowanie

Wszystkie operacje są zapisywane w pliku `logs` w tym samym folderze co skrypt:

2025-06-06 15:40:23,123 - INFO - Utworzono folder Projekty
2025-06-06 15:40:25,456 - INFO - Zmieniono nazwę stary_plik.txt na plik_001.txt


## Przykłady użycia

### Scenariusz 1: Organizacja zdjęć
1. Przejdź do folderu ze zdjęciami
2. Wybierz opcję 7 (zmień nazwy plików sekwencyjnie)
3. Wszystkie zdjęcia dostaną nazwy: zdjecie_001.jpg, zdjecie_002.jpg, etc.

### Scenariusz 2: Tworzenie struktury projektu
1. Wybierz opcję 3 (utwórz foldery)
2. Wpisz: `src, docs, tests, config`
3. Potwierdź utworzenie folderów

### Scenariusz 3: Generowanie plików testowych
1. Wybierz opcję 6 (utwórz pliki masowo)
2. Wpisz liczbę plików: `10`
3. Zostanie utworzonych 10 plików: plik_001.txt do plik_010.txt

## Rozwiązywanie problemów

### Program nie uruchamia się
- Sprawdź czy masz zainstalowany Python 3.6+
- Uruchom: `python --version` lub `python3 --version`

### Błąd "Folder nie istnieje"
- Upewnij się, że ścieżka do folderu jest poprawna
- Sprawdź czy folder rzeczywiście istnieje
- Na Windows używaj `\` lub `\\` w ścieżkach

### Błąd uprawnień
- Upewnij się, że masz uprawnienia do zapisu w wybranym folderze
- Na Linux/macOS może być potrzebne `sudo`

### Program się zawiesza
- Naciśnij `Ctrl+C` aby przerwać
- Sprawdź plik `logs` aby zobaczyć gdzie wystąpił problem

## Kontakt
Autor: [Andrzej]
Email: andre.analyze@gmail.com
GitHub: Andre-M1

## Licencja

MIT License - zobacz plik LICENSE
