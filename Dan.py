# class Hello:
#     def __init__(self):
#         print('Hello!')
#     def get_hello(self):
#         print("I'm parent")
#
#
# class Hello_World:
#     def __init__(self):
#         print('Hello World')
#         super().__init__()
#     def get_hello(self):
#         print("I'm child")
#         super().get_hello()
#
#
# hello_world = Hello_World()
# hello_world.get_hello()

# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
# cl2 = Class2()
# while True:
#     try:
#         a = int(input('A '))
#         print(10 / a)
#         break
#     except ZeroDivisionError:
#         print('Деление на 0 заперщено, веди не 0')
#     # except ValueError:
#     #     print("Ты ввел строку, а не число")
#     else:
#         print("ElSE - потому что выполнился TRY")
#         break
#     finally:
#         print('Finaly - я выпалняюсь всегда')
#
# print("OK")

# def checker(var_1):
#     if type(var_1) ! = str:
#         raise TypeError(f"Мы не можем работать с типом данных {type(var_1)}")
#     else:
#         return var_1
#
# a = "10"
# print(checker(a))

# class BuildingError(Exception):
#     def __str__(self):
#         return f"Нам не хватит материала"
#
# def build_check(material, limit):
#     if material > limit:
#         return "Все ок нам этого хватит для постройки дома"
#     else:
#         raise BuildingError(material)
#
#
# material = 450
# print(build_check(material, 300))

# import sys
#
# print(sys.platform)
# print(sys.version)
# print(sys.executable)
#
# for _ in dir(__builtins__):
#     print(_)
#
# print(help(list))

# import sys
#
# my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sys.getsizeof(my_lst))
#
# iter_obj = iter(my_lst)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))


class Counter:
    def __init__(self, start, stop):
        self.a = start
        self.b = stop

    def __iter__(self):
        self.i = self.a
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.b:
            raise StopIteration
        return self.i

count = Counter(2,8)

for i in count:
    print(i)
print()
for i in range (2,8):
    print(i)


