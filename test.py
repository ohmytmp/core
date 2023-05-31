from ohmytmp import Ohmytmp, Info, PluginAfter, FUNC, VERSION
from ohmytmp.__constant import Info

print(VERSION)

a = Ohmytmp()

class CC(PluginAfter):
    def __init__(self) -> None:
        pass
    @a.reg_handle(FUNC.ADDTAGS, -1)
    def f(info):
        print(FUNC.ADDTAGS, '_handle_f')
    def g(self, info: Info):
        print(FUNC.DESTINATION, '_f_g')
    def func(self, _info: Info) -> None:
        print(_info.to_dict())


cc = CC()
a.register(cc)
a.reg_f(cc.g, FUNC.DESTINATION)

a.walk('./')
