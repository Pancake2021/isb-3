import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import padding as padding2
import yaml





def decrypting_data(encrypted_file_path: str, secret_key_path: str, symmetric_key_path: str,
                    decrypted_file_path: str) -> None:
    
    # :param encrypted_file_path: путь к зашифрованному текстовому файлу
    # :param secret_key_path: путь к закрытому ключу ассиметричного алгоритма
    # :param symmetric_key_path: путь к зашифрованному ключу симметричного алгоритма
    # :param decrypted_file_path: путь, по которому сохранить расшифрованный текстовый файл
    # :return: ничего не возвращает


    # десериализация ключа симметричного алгоритма
    symmetric_file = symmetric_key_path + '\\key.txt'
    with open(symmetric_file, mode='rb') as key_file:
        encrypted_symmetric_key = key_file.read()