from selenium import webdriver

url = "https://web.telegram.org"
user_agent = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(options=options)
driver.get(url)

# Здесь страница будет открыта в браузере с указанным User-Agent

# Вы можете добавить дополнительный код для взаимодействия с открытой страницей, если это необходимо

# Закрыть браузер после использования
driver.quit()