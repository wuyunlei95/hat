class TestClassAndDef(object):
    def bird(self, bird_type):
        if bird_type == 'mq':
            print('麻雀')
        elif bird_type == 'yw':
            print('鹦鹉')
        else:
            print('都不是什么好鸟！')

    def fish(self, fish_type):
        if fish_type == 'jy':
            print('金鱼')
        else:
            print('不是金鱼')


if __name__ == '__main__':
    test_class_and_def = TestClassAndDef()
    test_class_and_def.bird('yw')
    test_class_and_def.fish('aa')
