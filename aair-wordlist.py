import os
if __name__ == "__main__":
    while(True):
        print("==================================")
        print('''
输入数字编号
1.添加密码字典
2.显示所有字典
3.设置默认密码字典
4.安装wpa-dictionary字典
5.安装kali的rockyou字典
6.清空字典
7.返回
            ''')
        
        try:
            ret1=int(input("配置密码字典>"))
        except ValueError:
            continue
        else:
            if(ret1==1):
                print("请将字典复制到AutoAir根目录下的wordlists文件夹中")
            elif(ret1==2):
                os.system("ls wordlists/")
            elif(ret1==3):
                os.system("ls wordlists/")
                print("开发中")
            elif(ret1==4):
                print("wpa-dictionary由conwnet制作")
                ret=os.system("git --version")
                if(ret!=0):
                    print("Git Error\nGit未安装")
                else:
                    ret=os.system("git clone https://github.com.cnpmjs.org/conwnet/wpa-dictionary.git")
                    if(ret!=0):
                        print("Git获取wpa-dictionary失败")
                    else:
                        os.system("rm wpa-dictionary/normalize.py")
                        os.system("rm wpa-dictionary/README.md")
                        os.system("mv wpa-dictionary/* wordlists/")
                        os.system("rm -r wpa-dictionary/")
                        print("wpa-dictionary安装完成")
            elif(ret1==5):
                os.system("sh aair-down-rockyou.sh")
                os.system("gzip -d rockyou.txt.gz")
                os.system("mv rockyou.txt wordlists/")
            elif(ret1==6):
                ret1=input("注意，将删除所有的密码字典，是否继续?[y/n]")
                if(ret1=="y"):
                    os.system("rm -r wordlists/*")
            elif(ret1==7):
                exit()

    