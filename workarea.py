# settings= {
#     'initial_file':'path/to/inital/file.txt',
#     'encrypted_file':'path/to/encrypted/file.txt',
#     'decrypted_file':'path/to/decrypted/file.txt',
#     'symmetric_key':'path/to/symmetric/key.txt',
#     'public_key':'path/to/public/key.pem',
#     'secret_key':'path/to/secret/key.pem',
# }

# import json
# # пишем в файл
# with open('settings.json', 'w') as fp:
#     json.dump(settings, fp)
# # читаем из файла
# with open('settings.json') as json_file:
#     json_data = json.load(json_file)

# print(json_data)

# import argparse
# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group(required = True)
# group.add_argument('-gen','--generation',help='Запускает режим генерации ключей')
# group.add_argument('-enc','--encryption',help='Запускает режим шифрования')
# group.add_argument('-dec','--decryption',help='Запускает режим дешифрования')

# args = parser.parse_args()
# if args.generation is not None:
#   # генерируем ключи
#     else if args.encryption is not None:
#   # шифруем
#     else:
#   # дешифруем

#   # генерация ключа симметричного алгоритма шифрования
# import os #можно обойтись стандартным модулем

# key = os.urandom(32) # это байты

# print(type(key))
# print(key)

# # генерация ключа симметричного алгоритма шифрования
# import os #можно обойтись стандартным модулем

# key = os.urandom(32) # это байты

# print(type(key))
# print(key)

# # паддинг данных для работы блочного шифра - делаем длину сообщения кратной длине шифркуемого блока
# from cryptography.hazmat.primitives import padding

# padder = padding.ANSIX923(32).padder()
# text = bytes('кто прочитал тот здохнет', 'UTF-8')
# padded_text = padder.update(text)+padder.finalize()

# print(text)
# print(padded_text)


# # шифрование текста симметричным алгоритмом
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# iv = os.urandom(16) #случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
# cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
# encryptor = cipher.encryptor()
# c_text = encryptor.update(padded_text) + encryptor.finalize()

# print(c_text)

# # дешифрование и депаддинг текста симметричным алгоритмом

# decryptor = cipher.decryptor()
# dc_text = decryptor.update(c_text) + decryptor.finalize()

# unpadder = padding.ANSIX923(32).unpadder()
# unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

# print(dc_text.decode('UTF-8'))
# print(unpadded_dc_text.decode('UTF-8'))


# # генерация пары ключей для асимметричного алгоритма шифрования
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.primitives import serialization

# keys = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048
# )
# private_key = keys
# public_key = keys.public_key()

# print(type(private_key))
# print(private_key)
# print(type(public_key))
# print(public_key)