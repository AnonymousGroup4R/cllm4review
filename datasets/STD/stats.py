import pathlib
import os
from collections import Counter

if __name__ == '__main__':
    parent = pathlib.Path(__file__).parent.resolve()
    category_counter = Counter()
    for name in os.listdir(parent / 'functions'):
        category_counter.update([name.split('_')[0]])
    for k, v in category_counter.items():
        print(k, v)
    print('total:', sum(category_counter.values()))