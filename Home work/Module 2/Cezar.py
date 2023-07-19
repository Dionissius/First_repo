# Код Цезаря
# Шифрование текста
message = 'Hello world!'

offset = 1               #Количество букв для смещения
encoded_message = ""

for ch in message:

    if ord(ch) in range(ord('A'), ord('Z')):             #Сначала проверяем заглавная ли это буква

        pos = ord(ch) - ord('A')
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
        encoded_message += new_char
   
    elif ord(ch) in range(ord('a'), ord('z')):           #Потом проверяем маленькая ли это буква

        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
        
        encoded_message += new_char
    
    elif ch in (' ', ',', '.', '!', '?') :               #На последок проверяем пробелы и символы
        new_char = ch
        encoded_message += new_char

print(encoded_message)