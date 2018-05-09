import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 called!!")
        print("__________________________")

    def function2(self):
        print(id(self))
        print("function2 called!!")


f = SelfTest()  # 인스턴스화
print(dir(f))   # 파이썬 내장변수
print(id(f))
f.function2()
print(SelfTest.__dict__)
print(SelfTest.function1())
