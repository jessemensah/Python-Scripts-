class Screen:
    def displayscreenmessage(self, screenmessage):
        print(screenmessage, end='')

    def displayscreenmessageline(self, screenmessage):
        print(screenmessage)

    def displaypoundamount(self, amounttobedisplayed):
        print(f'${amounttobedisplayed:.2f}',  end='')
