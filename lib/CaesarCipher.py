from prettytable import PrettyTable
from loguru import logger
from art import text2art


class Cipher:
    def __init__(self, welcome=True):
        if welcome:
            print(text2art("Caesar's Cipher!"))
        self.__ALPHABET_RUS_LOWER = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        self.__ALPHABET_RUS_UPPER = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.__ALPHABET_ENG_LOWER = "abcdefghijklmnopqrstuvwxyz"
        self.__ALPHABET_ENG_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__NUMBERS = "0123456789"

    def decrypting(self, world, key=None, write_to_file=True):
        """

        :param world:
        :param key:
        :param write_to_file:
        :return:
        """
        table = PrettyTable(("KEY", "ENCODE VALUE"))
        if key is None:
            for i in range(0, 33):
                dec = self.__decode(world, i)
                table.add_row((i, dec))
        elif 32 >= key >= 0:
            table.add_row((key, self.__decode(world, key)))
        else:
            logger.error("Введен не верный ключ!")
            raise Exception("Введен не верный ключ!")

        if write_to_file:
            with open("decode.txt", "w", encoding="utf-8") as file:
                file.write(str(table))

        return str(table)

    def encrypting(self, world, key=None):
        """

        :param world:
        :param key:
        :return:
        """
        table = PrettyTable(("KEY", "DECODE VALUE"))

        if key is None:
            for i in range(0, 34):
                enc = self.__encode(world, i)
                table.add_row((i, enc))
        elif 33 >= key >= 0:
            table.add_row((key, self.__encode(world, key)))
        else:
            logger.error("Введен не верный ключ!")
            raise Exception("Введен не верный ключ!")

        return str(table)

    def __encode(self, word, key):
        """

        :param word:
        :param key:
        :return:
        """
        # Алгоритм шифровки
        encrypting_word = ""
        for i in word:
            if i in self.__ALPHABET_RUS_LOWER:
                encrypting_word += self.__ALPHABET_RUS_LOWER[(self.__ALPHABET_RUS_LOWER.find(i) + key) % 32]
            elif i in self.__ALPHABET_RUS_UPPER:
                encrypting_word += self.__ALPHABET_RUS_UPPER[(self.__ALPHABET_RUS_UPPER.find(i) + key) % 32]
            else:
                encrypting_word += i
        return encrypting_word

    def __decode(self, encrypted_world, key):
        """

        :param encrypted_world:
        :param key:
        :return:
        """
        # Алгоритм дешифровки шифра Цезаря.
        decrypting_word = ""

        for i in encrypted_world:
            if i in self.__ALPHABET_RUS_LOWER:
                decrypting_word += self.__ALPHABET_RUS_LOWER[(self.__ALPHABET_RUS_LOWER.find(i) - key) % 32]
            elif i in self.__ALPHABET_RUS_UPPER:
                decrypting_word += self.__ALPHABET_RUS_UPPER[(self.__ALPHABET_RUS_UPPER.find(i) - key) % 32]
            else:
                decrypting_word += i

        return decrypting_word
