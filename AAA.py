# Заданий рядок
word = "pynative"
# Використовуємо зріз із кроком 2
result = word[::2]
print(result)  # Виведе: pntv

def remove_chars(word, n):
    # Повертаємо частину рядка, починаючи з індексу n до кінця
    return word[n:]
# Перевірка згідно з прикладами із завдання:
print(remove_chars("pynative", 4))  # Виведе: tive
print(remove_chars("pynative", 2))  # Виведе: native

def calculate_product_or_sum(a, b):
     product = a * b
     if product <= 1000:
          return product
     else:
          return a + b
a, b = 20, 50
result = calculate_product_or_sum(a, b)
print(result)
a, b = 20, 30
result = calculate_product_or_sum(a, b)
print(result)


print("Printing current and previous number sum in a range(10)")
# Зберігаємо попереднє число, починаючи з 0
previous_num = 0
# Проходимо в циклі від 0 до 9
for current_num in range(10):
    # Обчислюємо суму поточного та попереднього числа
    current_sum = current_num + previous_num
    # Виводимо результати згідно з очікуваним форматом
    print(f"Current Number {current_num} Previous Number {previous_num} Sum: {current_sum}")
    # Оновлюємо попереднє число: тепер поточне стає попереднім для наступного кроку
    previous_num = current_num
git add 
git commit -m "add new file"
git push

