import pickle
import pickle_dumper
import os
import argparse


if os.path.exists('settings/obj.pickle'):
    with open('settings/obj.pickle', 'rb') as f:
        obj_list = pickle.load(f)
else:
    print("File doesn't exists")

obj1 = obj_list[0]
obj2 = obj_list[1]
print(obj2.par2)
