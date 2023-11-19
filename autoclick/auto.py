# pip install pyautogui --> установка библиотеки

# cd C:\Users\Pluug\Desktop\autoclick --> через cmd прописываетк подобный путь

# python auto.py --> запускаете код 







import pyautogui
import time

# Задержка перед началом кликов (если нужно)
time.sleep(5)

# Координаты, где будет выполняться клик (можете изменить)
# x, y = 500, 500



screen_width, screen_height = pyautogui.size()

# Вычисление середины экрана
x = screen_width / 2
y = screen_height / 2

while True:
    pyautogui.click(x, y)
    # time.sleep(0.1)  # Задержка между кликами (если нужно)
