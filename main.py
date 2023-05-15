import argparse
import os
import argparse
import json
import logging
import os
from generation_key import symmetric_generation_key, asymmetric_generation_keys, write_symmetric_key
from encryption_data import asymmetric_encryption, symmetric_text_encryption
from decryption_data import asymmetric_decryption, symmetric_text_decryption

logger = logging.getLogger()
logger.setLevel('INFO')


def read_settings(file: str) -> dict:
    """
    Считывает настройки из файла.
    :param file: Путь к файлу.
    """
    try:
        with open(file) as json_file:
            json_data = json.load(json_file)
        logging.info('Настройки считаны!')
    except OSError as err:
        logging.warning(f'{err} ошибка при чтении файла {file}!')
    return json_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str, help='Использовать собственный файл с настройками (Введите '
                                                             'путь к файлу)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
    args = parser.parse_args()
    if args.settings:
        settings = read_settings(args.settings)
    else:
        settings = read_settings(os.path.join("data", "settings.json"))
    if args.generation_key:
        symmetric_key = symmetric_generation_key(16)
        logging.info('Симметричный ключ сгенерирован!')
        public_key = asymmetric_generation_keys(settings['secret_key'], settings['public_key'])
        cipher_symmetric_key = asymmetric_encryption(public_key, symmetric_key)
        logging.info('Симметричный ключ зашифрован!')
        write_symmetric_key(settings['symmetric_key'], cipher_symmetric_key)
    elif args.encryption_data:
        symmetric_key = asymmetric_decryption(settings['secret_key'], settings['symmetric_key'])
        logging.info('Симметричный ключ расшифрован!')
        symmetric_text_encryption(settings['initial_file'], symmetric_key, settings['encrypted_file'])
    else:
        symmetric_key = asymmetric_decryption(settings['secret_key'], settings['symmetric_key'])
        logging.info('Симметричный ключ расшифрован!')
        symmetric_text_decryption(settings['encrypted_file'], symmetric_key, settings['decrypted_file'])