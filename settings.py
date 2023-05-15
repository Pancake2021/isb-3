import logging
import json
import os

logger = logging.getLogger()
logger.setLevel('INFO')

settings = {
    'initial_file': 'data/initial_file.txt',
    'encrypted_file': 'data/encrypted_file.txt',
    'decrypted_file': 'data/decrypted_file.txt',
    'symmetric_key': 'data/symmetric_key.txt',
    'public_key': 'data/public_key.pem',
    'secret_key': 'data/secret_key.pem',
}

if __name__ == "__main__":
    try:
        with open(os.path.join('data', 'settings.json'), 'w') as f:
            json.dump(settings, f)
        logging.info("Настройки записаны в файл!")
    except OSError as err:
        logging.warning(f'{err} ошибка при записи в файл {"settings.json"}!')