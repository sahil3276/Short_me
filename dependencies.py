import subprocess

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call(["pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Error installing {package}")

def main():
    required_packages = ["pyshorteners", "colorama", "validators"]
    install_packages(required_packages)

if __name__ == "__main__":
    main()
