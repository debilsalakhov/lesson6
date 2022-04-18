import argparse


parser = argparse.ArgumentParser(description='Удаление файла')
parser.add_argument('-n', '--name', default='Anon', help='Имя пользователя')
parser.add_argument('-p', '--path', help='Путь файла')
parser.add_argument('-nQ', '--noQ', action='store_true', help='Давай без вопросов')
args = parser.parse_args()
print(f'Привет, {args.name}!')
