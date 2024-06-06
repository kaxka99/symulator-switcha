# Imię i nazwisko oraz nr studenta

Kamil Kielak s21383


# Symulacja Sieci Komputerowej

Projekt symulacji sieci komputerowej z użyciem przełącznika (switch) i komputerów (PC) komunikujących się za pomocą protokołu UDP. Kod został napisany w języku Python i symuluje podstawowe działanie sieci komputerowej z wykorzystaniem przełącznika.

## Pliki w Projekcie

- `NetworkManager.py`: Główny skrypt uruchamiający interfejs tekstowy do zarządzania przełącznikiem i komputerami.
- `Sw.py`: Skrypt przełącznika, który obsługuje komunikację między komputerami.
- `Pc.py`: Skrypt komputera, który umożliwia wysyłanie i odbieranie wiadomości przez sieć.

## Instrukcja Obsługi

### Uruchomienie Interfejsu Zarządzania

1. Uruchom `NetworkManager.py`

2. Po uruchomieniu, zobaczysz menu:

    ```
    Menu:
    1. Deploy Switch
    2. Deploy PC
    3. Shutdown System
    q. Quit
    Select an option:
    ```

### Opcje Menu

- **Deploy Switch**: Uruchamia przełącznik w nowym oknie konsoli.
- **Deploy PC**: Uruchamia komputer w nowym oknie konsoli. Po wybraniu tej opcji, zostaniesz poproszony o podanie portu komputera.
- **Shutdown System**: Zamyka przełącznik i wszystkie uruchomione komputery.
- **Quit**: Zamyka program i wyłącza wszystkie uruchomione procesy.

## Przykładowe Uruchomienie

1. Uruchom przełącznik wybierając opcję `1` w menu.
2. Uruchom komputer wybierając opcję `2` w menu i podając port komputera (np. `10001`).
3. W nowo otwartym oknie konsoli komputera, możesz wysyłać wiadomości do innych komputerów podając numer portu i treść wiadomości w formacie `dst_port,msg_data`.

## Wymagania

- Python 3.x

## Struktura Kodu

### `NetworkManager.py`

- **NetworkManager**: Klasa zarządzająca uruchamianiem i zamykaniem przełącznika oraz komputerów.
  - `deploy_switch()`: Uruchamia przełącznik.
  - `deploy_pc(pc_port, switch_port)`: Uruchamia komputer na zadanym porcie.
  - `shutdown_system()`: Zamyka przełącznik i wszystkie uruchomione komputery.
  - `run()`: Uruchamia interfejs tekstowy do zarządzania siecią.

### `Sw.py`

- **Switch**: Klasa reprezentująca przełącznik sieciowy.
  - `__init__(listen_port, connected_ports)`: Inicjalizuje przełącznik na zadanym porcie.
  - `print_mac_table()`: Wyświetla aktualną tablicę MAC.
  - `listen()`: Nasłuchuje na wiadomości i przetwarza je.
  - `run()`: Uruchamia wątek nasłuchujący.

### `Pc.py`

- **PC**: Klasa reprezentująca komputer w sieci.
  - `__init__(src_port, switch_port)`: Inicjalizuje komputer na zadanym porcie.
  - `listen()`: Nasłuchuje wiadomości i je przetwarza.
  - `send_message(dst_port, message)`: Wysyła wiadomość do zadanego portu.
  - `run()`: Uruchamia wątek nasłuchujący i obsługuje wysyłanie wiadomości.
 
    
Projekt ten jest przykładem symulacji sieci komputerowej i został stworzony w celach edukacyjnych.
