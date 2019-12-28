# print(3.2*2)
import pysnooper
# 变量
@pysnooper.snoop()
def xuexi():
    """
    笨办法学python
    :return:
    """
    # day 1
    cars = 100
    space_in_a_car = 4.0
    drivers = 30
    passengers = 90
    cars_not_drivers = cars - drivers
    cars_driven = drivers
    carpool_capacity = cars_driven * space_in_a_car
    average_passengers_per_car = passengers / cars_driven

    # print("there are", cars, "cars available.")
    # print("there are only", drivers, "drivers available.")
    # print("There will be", cars_not_drivers, "empty cars today.")
    # print("we can transport", carpool_capacity, "people today.")
    # print("we have", passengers, "to carpool today.")
    # print("we need to put about", average_passengers_per_car, "in each car.")

    # 格式化字符串，变量引用
    my_name = 'zed A.Shaw'
    my_age = 24  # not a lie
    my_height = 74  # inches
    my_weight = 180  # lbs
    my_eyes = 'blue'
    my_teeth = 'white'
    my_hair = 'Brown'

    print("Let's talk about %s. 渣渣辉" % my_name)
    print("He's %d inches tall." % my_height)
    print("He's %d pounds heavy." % my_weight)
    print("Actually that's not too heavy.")
    print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
    print("His teeth are usually %s depending on the coffee." % my_teeth)
    # this line is tricky, try to get it exactly right
    print("If I add %d , %d, and %d I get %d." % (my_age, my_height, my_weight, my_age+my_height+my_weight))

def day2():
    # 有10种类型的人
    x = "There are %d types of people." % 10
    #
    binary = "binary"
    do_not = "don't"
    # 知道二元的人和不知道二元的人
    y = "Those who know %s and those who %s." % (binary, do_not)
    print(x)
    print(y)

    # 我说：有十种人
    print("I said: %r." % x)
    # 我还说：知道二元的人和不知道二元的人
    print("I also said: '%s'." % y)
    hilarious = False
    joke_evaluation = "Isn't that joke so funny ?! % r"
    # 这个笑话真的好笑吗？！假
    print(joke_evaluation % hilarious)
    w = "This is the left side of..."
    e = "a string with a right side."
    # 这是......右侧的字符串的左侧。
    print(w + e)
    print ("'.'* 10  # what'd that do?")

    # Here's some new strange stuff ,remember type it exactly.
    days = "Mon Tue Wed Thu Fri Sat Sun."
    months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
    print("here are thr days:", days)
    print("here are the months:", months)
    print("""There's something going on here. With the three double-quotes.
    we'll be able to type as much as we like. Even 4 lines if we want, or5, or6""")

if __name__ == '__main__':
    #xuexi()
    day2()