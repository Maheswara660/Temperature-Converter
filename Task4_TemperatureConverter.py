"""
Temperature Converter Program
A clean, modular, console-based utility for converting temperatures
between Celsius and Fahrenheit.
"""

import sys
import os

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


# ANSI Escape Codes for colorized console output
COLOR_RESET = "\033[0m"
COLOR_HEADER = "\033[95m"  # Purple/Magenta
COLOR_INFO = "\033[96m"    # Cyan
COLOR_SUCCESS = "\033[92m" # Green
COLOR_WARNING = "\033[93m" # Yellow
COLOR_ERROR = "\033[91m"   # Red
COLOR_BOLD = "\033[1m"

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def print_styled(text: str, color_code: str, bold: bool = False) -> None:
    """Helper to print text with ANSI color codes."""
    bold_code = COLOR_BOLD if bold else ""
    print(f"{bold_code}{color_code}{text}{COLOR_RESET}")

def get_numeric_temperature() -> float:
    """Prompt the user for a numeric temperature, validate, and return it."""
    while True:
        try:
            user_input = input(f"{COLOR_INFO}Enter the temperature value: {COLOR_RESET}").strip()
            return float(user_input)
        except ValueError:
            print_styled("Error: Please enter a valid numeric temperature value (e.g., 25, 98.6, -10).", COLOR_ERROR)

def display_menu() -> None:
    """Display the main option menu."""
    print()
    print_styled("===================================", COLOR_HEADER)
    print_styled("    Temperature Converter Menu    ", COLOR_HEADER, bold=True)
    print_styled("===================================", COLOR_HEADER)
    print()
    print("1. Convert Celsius (°C) → Fahrenheit (°F)")
    print("2. Convert Fahrenheit (°F) → Celsius (°C)")
    print("3. Exit Program")
    print()
    print_styled("===================================", COLOR_HEADER)
    print()

def main() -> None:
    """Main loop for the Temperature Converter program."""
    clear_screen()
    print_styled("Welcome to the Temperature Converter!", COLOR_SUCCESS, bold=True)
    
    while True:
        display_menu()
        choice = input(f"{COLOR_INFO}Choose an option (1-3): {COLOR_RESET}").strip()
        
        if choice == '1':
            print_styled("\n--- Celsius to Fahrenheit ---", COLOR_INFO, bold=True)
            c = get_numeric_temperature()
            f = celsius_to_fahrenheit(c)
            print_styled(f"\nSuccess: {c:.2f}°C is equal to {f:.2f}°F\n", COLOR_SUCCESS, bold=True)
            input(f"{COLOR_INFO}Press Enter to return to the main menu... {COLOR_RESET}")
            clear_screen()
        
        elif choice == '2':
            print_styled("\n--- Fahrenheit to Celsius ---", COLOR_INFO, bold=True)
            f = get_numeric_temperature()
            c = fahrenheit_to_celsius(f)
            print_styled(f"\nSuccess: {f:.2f}°F is equal to {c:.2f}°C\n", COLOR_SUCCESS, bold=True)
            input(f"{COLOR_INFO}Press Enter to return to the main menu... {COLOR_RESET}")
            clear_screen()
            
        elif choice == '3':
            print_styled("\nThank you for using the Temperature Converter! Goodbye.", COLOR_SUCCESS)
            break
            
        else:
            print_styled("Error: Invalid choice. Please enter 1, 2, or 3.", COLOR_ERROR)
            input(f"{COLOR_INFO}Press Enter to return to the main menu... {COLOR_RESET}")
            clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_styled("\n\nProgram interrupted by user. Goodbye!", COLOR_WARNING)
        sys.exit(0)
