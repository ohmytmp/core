from ohmytmp import Ohmytmp, Info, PluginAfter, FUNC, VERSION

print(VERSION)

a = Ohmytmp()


def prt(i: Info) -> None:
    print(i.to_dict())


class CC:
    def __init__(self) -> None:
        pass
    @a.reg_handle(FUNC.ADDTAGS, -1)
    def f(info):
        print(FUNC.ADDTAGS, '_handle_f')
    def g(self, info: Info):
        print(FUNC.DESTINATION, '_f_g')


a.register(PluginAfter(prt))
a.reg_f(CC().g, FUNC.DESTINATION)

a.walk('./')
