import pyshorteners
import colorama
from colorama import Fore, Style
import validators

colorama.init(autoreset=True)

def clear_screen():
    print("\033c", end="")

def print_intro(name):
    intro = f"🚀 Welcome to the URL Shortener by {name}! 🚀"
    line = "=" * len(intro)
    print(line)
    print(intro)
    print(line)

def main():
    name = "SAHIL" 
    print_intro(name)

    try:
        while True:
            # Get the URL from the user
            original_url = input("\nEnter the URL to shorten: ")

            if original_url.lower() == 'exit':
                print("\nThank you for using the URL Shortener!")
                print(f"Check out my GitHub repository: https://github.com/yourusername")
                break

            if not validators.url(original_url):
                print("Invalid URL. Please enter a valid URL.")
                continue

            # Create a Shortener object
            s = pyshorteners.Shortener()

            try:
                # Shorten the URL
                shortened_url = s.tinyurl.short(original_url)
                print("\nShortened URL:", Fore.BLUE + Style.BRIGHT + shortened_url)
                print("\nThank you for using the URL Shortener!")
                print(f"Check out my GitHub repository: https://github.com/yourusername")
                break  # Exit the loop after displaying the URL
            except pyshorteners.exceptions.UnknownShortenerException:
                print("Unknown shortener error occurred.")
            except pyshorteners.exceptions.ShorteningErrorException:
                print("An error occurred while shortening the URL.")
            except Exception as e:
                print("An unexpected error occurred:", e)
    
    except KeyboardInterrupt:
        print("\n\nCtrl+C detected. Exiting gracefully.")
        print("\nThank you for using the URL Shortener!")
        print(f"Check out my GitHub repository: https://github.com/yourusername")

if __name__ == "__main__":
    main()
