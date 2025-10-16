#teste de ambiente virtual

from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.google.com")
        
        print(f"Título da página: {page.title()}")
        
        print("O navegador permanecerá aberto por 10 segundos.")
        time.sleep(10)
        
        browser.close()
        print("Navegador fechado.")

if __name__ == "__main__":
    main()