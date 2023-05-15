import logging
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import padding as s_padding
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger()
logger.setLevel('INFO')


def asymmetric_encryption(public_key, symmetric_key: bytes) -> bytes:
    """
    Ассиметричное шифрование симметричного ключа.
    :param public_key: Открытый ключ.
    :param symmetric_key: Текст.
    """
    cipher_text = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                 algorithm=hashes.SHA256(), label=None))
    return cipher_text


def symmetric_text_encryption(read_file: str, symmetric_key: bytes, write_file: str) -> None:
    """
    Шифрование текста симметричным алгоритмом и сохранение по указанному пути.
    :param read_file: Путь к файлу с зашифрованным текстом.
    :param symmetric_key: Симметричный ключ.
    :param write_file: Путь к файлу сохранения.
    """
    try:
        with open(read_file, 'r', encoding='utf-8') as text_file:
            text = text_file.read()
        logging.info(f' Текст считан из {read_file}!')
    except OSError as err:
        logging.warning(f'{err} Ошибка при чтении {read_file}!')
    padder = s_padding.ANSIX923(64).padder()
    padded_text = padder.update(bytes(text, 'utf-8')) + padder.finalize()
    iv = os.urandom(8)
    cipher = Cipher(algorithms.IDEA(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
    c_text = iv + c_text
    logging.info('Текст зашифрован!')
    try:
        with open(write_file, 'wb') as f_text:
            f_text.write(c_text)
        logging.info(f'Текст записан в {write_file}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи текста в {write_file}')