import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def set_info(self, name, phone):            #__init__ 초기화 될때 무조건 처음 실행 ex) user1 = UserInfo("kim", '010-222-4444')
        self.name = name
        self.phone = phone

    def print_info(self):
        print("------------------------")
        print("Name : " + self.name)
        print("Phone : " + self.phone)
        print("------------------------")

    def __del__(self):                          # 메모리에서 사라질 경우
        print("메모리에서 사라짐")

user1 = UserInfo()
user2 = UserInfo()

print(id(user1))
print(id(user2))

user1.set_info("kim", '010-222-4444')
user2.set_info("park", '010-7890-1234')

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, " | " ,user1.name)
