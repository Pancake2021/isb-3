import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def symmetric_generation_key(key_length: int) -> bytes:
    """
    Генерация ключа симметричного алгоритма шифрования.
    :param key_length: Длина ключа.
    """
    key = os.urandom(key_length)
    return key


def write_symmetric_key(file: str, symmetric_key: bytes) -> None:
    """
    Запись симметричного ключа в файл.
    :param file: Путь к файлу.
    :param symmetric_key: Симметричный ключ.
    """
    try:
        with open(file, 'wb') as key_file:
            key_file.write(symmetric_key)
        logging.info(f'Симметричный ключ записан в {file}!')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи симметричного ключа в {file}!')


def asymmetric_generation_keys(private_pem: str, public_pem: str) -> bytes:
    """
    Генерация и запись в файлы ассиметричных ключей.
    :param private_pem: Путь к приватному ключу.
    :param public_pem: Путь к открытому ключу.
    """
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
        logging.info(f' Открытый ключ записан в {public_pem}!')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи ключа в {public_pem}!')
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
        logging.info(f'Приватный ключ записан в {private_pem}!')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи ключа в {private_pem}!')
    return public_key
