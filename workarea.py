# ###1. Генерация ключей гибридной системы
# *Входные параметры:*  
# *1) путь, по которому сериализовать зашифрованный симметричный ключ;*  
# *2) путь, по которому сериализовать открытый ключ;*  
# *3) путь, по которому сериазизовать закрытый ключ.*

# 1.1. Сгеренировать ключ для симметричного алгоритма.  
# 1.2. Сгенерировать ключи для ассиметричного алгоритма.  
# 1.3. Сериализовать ассиметричные ключи.   
# 1.4. Зашифровать ключ симметричного шифрования открытым ключом и сохранить по указанному пути. 

# ###2. Шифрование данных гибридной системой
# *Входные параметры:*  
# *1) путь к шифруемому текстовому файлу (очевидно, что файл должен быть достаточно объемным);*  
# *2) путь к закрытому ключу ассиметричного алгоритма;*  
# *3) путь к зашированному ключу симметричного алгоритма;*  
# *4) путь, по которому сохранить зашифрованный текстовый файл;*  

# 2.1. Расшифровать симметричный ключ.  
# 2.2. Зашифровать текст симметричным алгоритмом и сохранить по указанному пути.   

# ###3. Дешифрование данных гибридной системой
# *Входные парметры:*  
# *1) путь к зашифрованному текстовому файлу;*  
# *2) путь к закрытому ключу ассиметричного алгоритма;*  
# *3) путь к зашированному ключу симметричного алгоритма;*  
# *4) путь, по которому сохранить расшифрованный текстовый файл.*  

# 3.1. Расшифровать симметричный ключ.  
# 3.2. Расшифровать текст симметричным алгоритмом и сохранить по указанному пути. 



#argpass или графисечкий интерфейс 
#декомпозиция кода 
#(аля введите D чтобы дешифровать не подхдит)
# unit test сделать // c гихаюа юнит тест пайт тест теск дискавери (впечатиолиьь работататделатся)
# CA CD github
#на след лабе 4 обьяснят (к концу апреля)
#колизия и хэш
#что за алгоритм шифрования по варианту??? (для чего, где нужен, какой ключ, блочный или поточный,скомпрометрирован или нет насколько он старый)
#все по разному попытаться
#


import argparse
from tqdm import tqdm
tqdm.pandas()
from Task1 import run1
from Task1 import key_generation_func
from Task2 import run2
from Task2 import encrypt_data
from Task3 import run3
from Task3 import decrypting_data

# from tqdm import tqdm
# from tqdm.notebook import tqdm_notebook
import yaml


if __name__ == "__workarea__":
    run1()
    run2()
    run3()


parser = argparse.ArgumentParser(description="main")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
parser.add_argument('-symkey',
                    type=str,
                    help='Это обязательный строковый позиционный аргумент,'
                         'который указывает, путь к папке, в которую сериализуется зашифрованный симметричный ключ',
                    dest='symmetric_key_path')
parser.add_argument('-pubkey',
                    type=str,
                    help='Это обязательный строковый позиционный аргумент,'
                         'который указывает, путь к папке, в которую сериализуется открытый ключ',
                    dest='public_key_path')
parser.add_argument('-seckey',
                    type=str,
                    help='Это обязательный строковый позиционный аргумент,'
                         'который указывает, путь к папке, в которую сериализуется закрытый ключ',
                    dest='secret_key_path')
parser.add_argument('-initial',
                    type=str,
                    help='Это обязательный строковый позиционный аргумент,'
                         'который указывает, путь к папке, в которой хранится начальный файл',
                    dest='initial_file_path')
parser.add_argument('-encrypted',
                    type=str,
                    help='Это обязательный строковый позиционный аргумент,'
                         'который указывает, путь к папке, в которую сохраняется шифрованный файл',
                    dest='encrypted_file_path')
parser.add_argument('-dencrypted',
                    type=str,
                    help='Это обязательный строковый позиционный аргумент,'
                         'который указывает, путь к папке, в которую сохраняется дешифрованный файл',
                    dest='decrypted_file_path')
args = parser.parse_args()

if args.generation:
    key_generation_func(args.symmetric_key_path, args.public_key_path, args.secret_key_path)
if args.encryption:
    with tqdm(100, desc='Encryption mode') as prograssbar:
        encrypt_data(args.initial_file_path, args.secret_key_path, args.symmetric_key_path, args.encrypted_file_path)
        prograssbar.update(100)
if args.decryption:
    with tqdm(100, desc='Decryption mode') as prograssbar:
        decrypting_data(args.encrypted_file_path, args.secret_key_path, args.symmetric_key_path,
                        args.decrypted_file_path)
        prograssbar.update(100)

