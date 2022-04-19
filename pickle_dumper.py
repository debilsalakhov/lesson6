import os
import argparse
import pickle


class MyClass:
    def __init__(self, par1, par2):
        self.par1 = par1
        self.par2 = par2


parser = argparse.ArgumentParser(description='Сериализуем объекты в файл пикл')
parser.add_argument('-p', '--path', help='Путь файла')
args = parser.parse_args()

obj1 = MyClass(1, 2)
obj2 = MyClass(3, 4)
obj_list = [obj1, obj2]
with open(args.path, 'wb') as f:
    pickle.dump(obj_list, f)
