# Завдання 1
import matplotlib.pyplot as plt

weeks = ['Тиждень 1', 'Тиждень 2', 'Тиждень 3', 'Тиждень 4']

traffic = [1500, 1600, 1700, 1800]

sales_product_a = [300, 350, 400, 450]
sales_product_b = [200, 250, 300, 350]
sales_product_c = [100, 150, 200, 250]

plt.plot(weeks, traffic, label='Активність трафіку', color='red', marker='o', ls=':')
plt.plot(weeks, sales_product_a, label='Продукт А', color='purple', marker='^', ls='-.')
plt.plot(weeks, sales_product_b, label='Продукт Б', color='blue', marker='s', ls='-')
plt.plot(weeks, sales_product_c, label='Продукт С', color='pink', marker='*', ls='--')
plt.title('Aктивність веб-трафіку i трьох продуктів')
plt.xlabel('Тижні')
plt.ylabel('Продажі')
plt.legend()
plt.show()

# Завдання 2
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x) * np.cos(x)

plt.figure(figsize=(12, 6))

plt.plot(x, y, label='sin(x) * cos(x)', color='green', ls='-', lw=2)
plt.title('Графік функції sin(x) * cos(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()

# Завдання 3
import matplotlib.pyplot as plt

sizes = [50, 25, 15, 10]
labels = ['Продажі', 'Інвестиції', 'Ліцензії', 'Інше']
colors = ['#FF9999', '#66B3FF', '#3ad67b', '#fcf644']
plt.pie(sizes, labels=labels, colors=colors)
plt.title("Кольори сегментів")
plt.show()
