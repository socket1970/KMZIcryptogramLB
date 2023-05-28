# Декодирование сообщений по таблице соответствия

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/funny_m4n)
## Дополнение к лабораторным работам:
* [Шифр Шамира(Трёхэтапный протокол Шамира)](https://github.com/socket1970/shamirCipherKMZIlab)
***
Переводит сообщение вида `[int]` в сообщение вида `string`.
Таблица кодировки приведена в файле alphabet.json

Пример:
```python
dec = [805464733912570221]
print("".join(encod.decoding(dec, encod="64_lw")))
```
Вывод:
```pycon
привет мир
```
***