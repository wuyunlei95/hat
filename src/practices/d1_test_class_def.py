# 类，方法，调用类里的方法
# 类中没有 __init__
class Test1:

    def bird(self,bird_type):
        if bird_type == '鹦鹉':
            print("鹦鹉")
        else:
            print("不是鹦鹉")

    def fish(self,fish_type):
        if fish_type == "鲤鱼":
            print("鲤鱼")
        else:
            print("不是鲤鱼")


# 类，方法，调用类里的方法
# 类中有 __init__
class Test2:
    BIRD_TYPE = 'YingWu'
    FISH_TYPE = 'LiYu'

    def __init__(self,bird_type,fish_type):
        self.bird_type = bird_type
        self.fish_type = fish_type

    def bird(self):
        if self.bird_type == self.BIRD_TYPE:
            print("鹦鹉")
        else:
            print("不是鹦鹉")

    def fish(self):
        if self.fish_type == self.FISH_TYPE:
            print("鲤鱼")
        else:
            print("不是鲤鱼")

if __name__ == '__main__':
    # 类中无 __init__
    test1 = Test1()
    test1.bird('鹦鹉')
    test1.fish('鲤鱼')

    # 类中有 __init__
    test2 = Test2('YingWu','LiYu')
    test2.bird()
    test2.fish()