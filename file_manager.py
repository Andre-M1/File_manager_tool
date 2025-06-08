import os
from pathlib import Path
import logging

# Konfiguracja logowania
logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FileFolderManager:
    def __init__(self, source_dir):
        """Inicjalizacja menedżera plików i folderów."""
        self.source_dir = Path(source_dir)
        if not self.source_dir.exists():
            logging.error(f"Folder {source_dir} nie istnieje.")
            raise FileNotFoundError(f"Folder {source_dir} nie istnieje.")
        if not self.source_dir.is_dir():
            logging.error(f"{source_dir} nie jest folderem.")
            raise NotADirectoryError(f"{source_dir} nie jest folderem.")

    def get_unique_name(self, new_name):
        """Generuje unikalną nazwę pliku lub folderu w przypadku konfliktu."""
        base, ext = os.path.splitext(new_name)
        counter = 1
        unique_name = new_name
        while (self.source_dir / unique_name).exists():
            unique_name = f"{base}_{counter:03d}{ext}"
            counter += 1
        return unique_name

    def list_contents(self):
        """Zwraca listę folderów i plików w bieżącym katalogu."""
        folders = [item.name for item in self.source_dir.iterdir() if item.is_dir()]
        files = [item.name for item in self.source_dir.iterdir() if item.is_file()]
        return folders, files

    def navigate_to_folder(self, folder_name):
        """Przechodzi do wybranego folderu."""
        new_path = self.source_dir / folder_name
        if new_path.is_dir():
            self.source_dir = new_path
            logging.info(f"Przejście do folderu: {self.source_dir}")
            return True
        else:
            logging.error(f"Folder {folder_name} nie istnieje w {self.source_dir}.")
            return False

    def navigate_to_parent(self):
        """Przechodzi do folderu nadrzędnego."""
        parent = self.source_dir.parent
        if parent != self.source_dir:  # Zapobiega wyjściu poza root
            self.source_dir = parent
            logging.info(f"Przejście do folderu nadrzędnego: {self.source_dir}")
            return True
        else:
            logging.warning("Nie można przejść выше, już w katalogu głównym.")
            return False

    def create_folders(self, folder_names):
        """Tworzenie nowych folderów."""
        changes = []
        for name in folder_names:
            unique_name = self.get_unique_name(name)
            changes.append(('Utwórz folder', name, unique_name))
        return changes

    def create_folders_count(self, count, prefix="folder"):
        """Tworzenie określonej liczby folderów z sekwencyjnymi nazwami."""
        changes = []
        for i in range(1, count + 1):
            name = f"{prefix}_{i:03d}"
            unique_name = self.get_unique_name(name)
            changes.append(('Utwórz folder', name, unique_name))
        return changes

    def create_files(self, file_names):
        """Tworzenie nowych plików z podanymi nazwami."""
        changes = []
        for name in file_names:
            unique_name = self.get_unique_name(name)
            changes.append(('Utwórz plik', name, unique_name))
        return changes

    def create_files_count(self, count, prefix="file"):
        """Tworzenie określonej liczby plików z sekwencyjnymi nazwami."""
        changes = []
        for i in range(1, count + 1):
            name = f"{prefix}_{i:03d}.txt"
            unique_name = self.get_unique_name(name)
            changes.append(('Utwórz plik', name, unique_name))
        return changes

    def rename_files_sequential(self, prefix="file"):
        """Zmiana nazw wszystkich plików na sekwencyjne."""
        changes = []
        counter = 1
        for item in self.source_dir.iterdir():
            if item.is_file():
                ext = item.suffix
                new_name = f"{prefix}_{counter:03d}{ext}"
                unique_name = self.get_unique_name(new_name)
                changes.append(('Zmień nazwę pliku', item.name, unique_name))
                counter += 1
        return changes

    def rename_folders_sequential(self, prefix="folder"):
        """Zmiana nazw wszystkich folderów na sekwencyjne."""
        changes = []
        counter = 1
        for item in self.source_dir.iterdir():
            if item.is_dir():
                new_name = f"{prefix}_{counter:03d}"
                unique_name = self.get_unique_name(new_name)
                changes.append(('Zmień nazwę folderu', item.name, unique_name))
                counter += 1
        return changes

    def apply_changes(self, changes, preview=False):
        """Wykonanie zmian (tworzenie, zmiana nazw)."""
        if not changes:
            print("Brak zmian do zastosowania.")
            return

        print("Podgląd zmian:")
        for op_type, old_name, new_name in changes:
            print(f"{op_type}: {old_name} -> {new_name}")

        if preview:
            apply_changes = input("Zastosować zmiany? (tak/nie): ").lower() == 'tak'
            if not apply_changes:
                print("Zmiany nie zostały zastosowane.")
                return

        for op_type, old_name, new_name in changes:
            try:
                if op_type.startswith('Utwórz folder'):
                    (self.source_dir / new_name).mkdir()
                    logging.info(f"Utworzono folder {new_name}")
                elif op_type.startswith('Utwórz plik'):
                    (self.source_dir / new_name).touch()
                    logging.info(f"Utworzono plik {new_name}")
                elif op_type.startswith('Zmień nazwę'):
                    os.rename(self.source_dir / old_name, self.source_dir / new_name)
                    logging.info(f"Zmieniono nazwę {old_name} na {new_name}")
            except Exception as e:
                logging.error(f"Błąd podczas operacji '{op_type}' dla {old_name}: {e}")
                print(f"Błąd: {op_type} dla {old_name} nie powiodło się: {e}")

        print("Operacje zakończone. Sprawdź log w pliku file_manager.log.")

def main():
    """Główna funkcja."""
    try:
        source_directory = input("Podaj początkową ścieżkę do folderu: ")
        manager = FileFolderManager(source_directory)

        while True:
            print(f"\nBieżący katalog: {manager.source_dir}")
            folders, files = manager.list_contents()
            if folders:
                print("Foldery:")
                for i, folder in enumerate(folders, 1):
                    print(f"{i}. {folder}")
            if files:
                print("Pliki:", files)
            else:
                print("Brak Plików")
            print("\nMenu:")
            print("1. Utwórz foldery (podaj nazwy)")
            print("2. Utwórz foldery (podaj liczbę)")
            print("3. Utwórz pliki (podaj nazwy)")
            print("4. Utwórz pliki (podaj liczbę)")
            print("5. Zmień nazwy plików (sekwencyjne)")
            print("6. Zmień nazwy folderów (sekwencyjne)")
            print("7. Przejdź do folderu")
            print("8. Wróć do folderu nadrzędnego")
            print("9. Wyjdź")

            choice = input("Wybierz opcję (1-9): ")
            preview = input("Pokazać podgląd zmian? (tak/nie): ").lower() == 'tak'

            changes = []
            if choice == '1':
                folder_names = input("Podaj nazwy folderów (oddzielone przecinkami): ").split(',')
                folder_names = [name.strip() for name in folder_names]
                changes = manager.create_folders(folder_names)
            elif choice == '2':
                count = int(input("Podaj liczbę folderów do utworzenia: "))
                prefix = input("Podaj prefiks dla folderów (domyślny 'folder'): ") or "folder"
                changes = manager.create_folders_count(count, prefix)
            elif choice == '3':
                file_names = input("Podaj nazwy plików (oddzielone przecinkami): ").split(',')
                file_names = [name.strip() for name in file_names]
                changes = manager.create_files(file_names)
            elif choice == '4':
                count = int(input("Podaj liczbę plików do utworzenia: "))
                prefix = input("Podaj prefiks dla plików (domyślny 'file'): ") or "file"
                changes = manager.create_files_count(count, prefix)
            elif choice == '5':
                prefix = input("Podaj prefiks dla nowych nazw plików (domyślny 'file'): ") or "file"
                changes = manager.rename_files_sequential(prefix)
            elif choice == '6':
                prefix = input("Podaj prefiks dla nowych nazw folderów (domyślny 'folder'): ") or "folder"
                changes = manager.rename_folders_sequential(prefix)
            elif choice == '7':
                folders, _ = manager.list_contents()
                if not folders:
                    print("Brak folderów do przejścia.")
                    continue
                print("Wybierz folder:")
                for i, folder in enumerate(folders, 1):
                    print(f"{i}. {folder}")
                folder_choice = int(input("Podaj numer folderu: ")) - 1
                if 0 <= folder_choice < len(folders):
                    if manager.navigate_to_folder(folders[folder_choice]):
                        print(f"Przejście do: {manager.source_dir}")
                    else:
                        print(f"Nie można przejść do folderu {folders[folder_choice]}.")
                else:
                    print("Nieprawidłowy wybór folderu.")
                continue
            elif choice == '8':
                if manager.navigate_to_parent():
                    print(f"Przejście do: {manager.source_dir}")
                else:
                    print("Nie można przejść do folderu nadrzędnego.")
                continue
            elif choice == '9':
                print("Zakończono program.")
                break
            else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")
                continue

            manager.apply_changes(changes, preview)

    except FileNotFoundError as e:
        print(f"Błąd: {e}")
    except NotADirectoryError as e:
        print(f"Błąd: {e}")
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość (np. liczba folderów/plików musi być liczbą).")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()