from lib.InternetChecker import InternetChecker

def main():
    internetChecker = InternetChecker(
        testUrls = ["http://www.google.com", "https://1.1.1.1"],
        dnsAddress = "8.8.8.8",
        timeout = 5
    )
    
    if internetChecker.check():
        print("Internet connection successful.")
    else:
        print("Internet connection failed.")

if __name__ == "__main__":
    main()