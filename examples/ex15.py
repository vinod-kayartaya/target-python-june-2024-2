class Camera:
    def __init__(self) -> None:
        super().__init__()
        print('Camera.__init__() called')


class MusicPlayer:
    def __init__(self) -> None:
        super().__init__()
        print('MusicPlayer.__init__() called')

    def f1(self):
        print('MusicPlayer.f1() called')


class Phone():
    def __init__(self) -> None:
        super().__init__()
        print('Phone.__init__() called')

    def f1(self):
        print('Phone.f1() called')

class MobilePhone(Phone):
    def __init__(self) -> None:
        super().__init__()
        print('MobilePhone.__init__() called')


class SmartPhone(MusicPlayer, MobilePhone, Camera):
    def __init__(self) -> None:
        super().__init__()
        print('SmartPhone.__init__() called')


def main():
    sp = SmartPhone()
    
    for mro in SmartPhone.mro():
        print(mro)
    
    sp.f1()
    # Phone.f1(sp)

if __name__ == '__main__':
    main()

