from ohmytmp import Ohmytmp, Info, PluginAfter

def prt(i: Info)->None:
    print(i.to_dict())

a = Ohmytmp()
a.register(PluginAfter(prt))
a.walk('./')
