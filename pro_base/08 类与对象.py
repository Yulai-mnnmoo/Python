#定义类
class Car(object):
    pass

#创建对象
car= Car()

# 实例变量
class Dog:
    def __init__(self,name,age):  # __int__  是构造方法，构造方法用来初始化实例变量
        self.name=name
        self.age=age

d=Dog('shan',2)

print('狗子名字是{0}，今年{1}岁了'.format(d.name,d.age)) #对实例变量通过"对象.实例变量"形式访问


# 构造方法
class Dogs:
    def __init__(self,name,age,sex='雌性'):  # __int__  是构造方法，构造方法用来初始化实例变量
        self.name=name
        self.age=age
        self.sex=sex

d1=Dogs('球球',3)
d2=Dogs('哈哈',1,'雌性')
d3=Dogs(name='拖布',sex='雄性',age=1)

print('{0}:{1}岁{2}'.format(d1.name,d1.age,d1.sex))
print('{0}:{1}岁{2}'.format(d2.name,d2.age,d2.sex))
print('{0}:{1}岁{2}'.format(d3.name,d3.age,d3.sex))


# 实例方法
class Dog1:
    def __init__(self,name,age,sex='雌性'):  # __int__  是构造方法，构造方法用来初始化实例变量
        self.name=name
        self.age=age
        self.sex=sex

    def run(self):
        print('{0}在跑。。。'.format(self.name))
    def speak(self,sound):      #定义实例方法 第一个参数是self 第二个参数是sound
        print('{0}在叫：{1}'.format(self.name,sound))

dog1=Dog1('球球',2)
dog1.run()
dog1.speak('旺旺')


#类变量
class Account:
    interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.amount=amount

account=Account('Tony',80000.0)

print('账户名：{0}'.format(account.owner))
print('余额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))   #对类变量通过‘类名.类变量’形式访问

#类方法
class Account1:
    interest_rate=0.0668  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.amount=amount
    @classmethod
    def interert_by(cls,amt): #cls 代表类自身
        return cls.interest_rate * amt

interest = Account1.interert_by(12000.0) #对类方法 用’类名.类方法‘形式访问

print('利息计算：{0:.4f}'.format(interest))

# 注意 ： 类方法可以访问类变量和其他类方法 但不可以访问其他实例变量和其他实例变量

#私有变量
class Account2:
    __interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount
    def desc(self):
        print('{0}金额：{1}利率：{2}'.format(self.owner,self.__amount,Account2.__interest_rate))

ac=Account2('zahngsan',800000.0)
ac.desc()

print(ac.owner)
# print(ac.__amount)    发生错误   在类的外部 不可以访问私有变量
# print(Account2.__interest_rate)  发生错误   在类的外部 不可以访问私有变量

#私有方法  类似私有变量
class Account3:
    __interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount
    def __get_info(self):  #定义私有方法
        print('{0}金额：{1}利率：{2}'.format(self.owner,self.__amount,Account3.__interest_rate))
    def desc(self):
        self.__get_info()     #在类的内部 可以访问私有方法

am=Account3('zahngsan1',800000.0)
am.desc()
#am.__get_info()   #在类得外部不能访问私有变量  发生错误


#使用属性  全设置为私有变量 实现封装  然后用set get方法 获取
class Account4:
    __interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount
    def get_amount(self):
        return self.__amount
    def set_amount(self,amount):
        self.__amount=amount

    def get_rate(self):
        return self.__interest_rate
    def set_rate(self,interest_rate):
        self.__interest_rate=interest_rate

acc=Account4('zhangsan222',80000.0)
print('{0}金额：{1}利率：{2}'.format(acc.owner,acc.get_amount(),acc.get_rate()))
acc.set_amount(60000.0)
acc.set_rate(0.0666)
print('修改后的 {0}金额：{1}利率：{2}'.format(acc.owner,acc.get_amount(),acc.get_rate()))

#替代set  get 方法
class Do:
    def __init__(self,name,age):
        self.name =name
        self._age = age
    @property      #定义属性age的get方法 使用 @property 修饰 方法名就是属性名
    def age(self):
        return self._age
    @age.setter     #定义属性age的set方法 使用  @age.setter 修饰 方法名就是属性名
    def age(self,age):
        self._age=age
do=Do('拖布',1)

print('狗子年龄：{0}'.format(do.age))  #这样可以 通过属性取值
do.age=3        #可以 通过属性修改值
print('修改后 狗子年龄：{0}'.format(do.age))



#继承   子类继承父类是 只有公有的成员变量和方法才能被继承
class Animal:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('动物的名字是：{0}'.format(self.name))
    def move(self):
        print('动了。。。')
class Cat(Animal):  #定义子类
    def __init__(self,name,age):
        super().__init__(name)  #调用父类构造方法  初始化成员变量
        # self.name=name
        self.age=age

cat =Cat('Tom',3)
cat.move()
cat.show_info()


#多继承    子类优先继承左边父类中的成员方法或成员变 量，从左到右继承级别从高到低
class Horse:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('马的名字：{0}'.format(self.name))
    def run(self):
        print('马跑...')

class Donkey:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('驴的名字：{}'.format(self.name))
    def run(self):
        print('驴跑...')
    def roll(self):
        print('驴打滚...')

class Mule(Horse,Donkey):
    def __init__(self,name,age):
        super().__init__(name)
        self.age =age
    def show_info(self):     #方法重写
        print('骡子的名字是：{}'.format(self.name))
m=Mule('lisi',2)
m.run()         #  两个父类都有run方法 调用前者 马的run方法
m.roll()        #只有父类驴友roll方法 所以调用 驴的roll方法
m.show_info()   #  两个父类都有show_info方法 调用前者 马的show_info方法



#多态性
class Animal1:
    def speak(self):
        print('动物叫了，但不知道是那种动物')

class Cat1(Animal1):
    def speak(self):
        print('小猫喵喵叫。。。')

class Dogd(Animal1):
    def speak(self):
        print("小狗旺旺叫。。。")

an1 =Dogd()
an2=Cat1()
an1.speak()
an2.speak()

#鸭子类型测试与多态  鸭子类型测试:若看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟可以被称为鸭子

def start(obj):
    obj.speak()
class Animal2:
    def speak(self):
        print('动物叫了，但不知道是那种动物')

class Cat2(Animal2):
    def speak(self):
        print('小猫喵喵叫。。。')

class Dogd1(Animal2):
    def speak(self):
        print("小狗旺旺叫。。。")
class Car3:
    def speak(self):
        print('小汽车滴滴叫。。。')

start(Dogd1())
start(Cat2())
start(Car3())