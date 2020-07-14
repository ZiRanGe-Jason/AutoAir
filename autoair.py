import os

def start():
    print(r'''
   _____          __            _____  .__        
  /  _  \  __ ___/  |_  ____   /  _  \ |__|______ 
 /  /_\  \|  |  \   __\/  _ \ /  /_\  \|  \_  __ \
/    |    \  |  /|  | (  <_> )    |    \  ||  | \/
\____|__  /____/ |__|  \____/\____|__  /__||__|   
        \/                           \/       
    ''')
    #print("==================================")
    print("AutoAir 0.01")
    print("By ZiRanGe_Jason")
    



if __name__ == "__main__":
    pass
    start()
    while(True):
        print("==================================")
        print('''
输入数字编号
1.使用Aircrack-ng破解WIFI
2.配置密码字典
3.介绍
        ''')
        try:
            ret1=int(input(">"))
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("\nGoodbye!See you next time!")
            exit()
        else:
            if(ret1==3):
                print("==================================")
                start()
                print("这是一个半自动化的WIFI破解程序")
            elif(ret1==1):
                os.system("python3 aair-aircrack.py")
            elif(ret1==2):
                os.system("python3 aair-wordlist.py")
                
        
