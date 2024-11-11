### Напишите программу,
#которая меняет местами первую и последнюю букву каждой строки, введенной пользователем.
text=str(input(r"Введите текст (несколько строк, разделённых \n): "))
# Разделение текста на строки
lines = text.split("\\n")
print(lines)
# Замена первой и последней буквы в каждой строке
swapped_lines = []
for line in lines:
    if len(line) > 1:
        swapped_line = line[-1] + line[1:-1] + line[0]
    else:
        swapped_line = line
    swapped_lines.append(swapped_line)

# Объединение строк обратно в текст
swapped_text = "\\n".join(swapped_lines)

print("Изменённый текст:")
print(swapped_text)
