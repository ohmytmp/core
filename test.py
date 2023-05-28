import os
from ohmytmp import Initializer

src = '../'
dst = '../example'


def walk(src: str, dst: str):
    a = Initializer(dst)
    for p, _, f in os.walk(src):
        for i in f:
            print(a.init_file(os.path.join(p, i)).to_dict())

walk(src, dst)
