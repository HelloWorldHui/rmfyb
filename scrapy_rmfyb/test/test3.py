
def run():
    print("欢迎登录学生信息管理系统V1.0版本")
    print('*'*20)
    print('1.新建学生信息')
    print('2.显示全部学生')
    print('3.查询学生信息')
    print('0.保存并退出系统')
    print('*' * 20)
    choice = input("输入选择(默认选择0):")
    if choice == '1':
        create()
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    else:
        print('保存并退出成功')

def create():
    print("新建学生信息:请依次输入学生信息")
    s_name = input("学生姓名:")
    s_phone = input("学生电话号码:")
    s_qq = input("学生QQ:")
    s_email = input("学生email:")
    with open("student.txt",'a',encoding='utf8') as f:
        f.write(s_name+","+s_phone+','+s_qq+','+s_email+"\n")
    choice = input("添加学生信息成功,继续添加?(Y/N):")
    if choice.upper() == "Y":
        create()
    else:
        run()



with open("student.txt",'a',encoding='utf8') as f :
    f.write("姓名,电话,QQ,Email"+"\n")
if __name__ == '__main__':
    pass