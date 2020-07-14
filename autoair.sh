sudo chmod +x ./*

python3 -h
if [ $? -ne 0 ]
then 
    echo "AutoAir[ERROR]:Python3未安装"
    exit
fi


aircrack-ng
ai=$?

git --version
gi=$?


clear

if [ $ai -ne 0 ]
then 
    echo "AutoAir[WARNING]:Aircrack-ng未安装"
fi

if [ $gi -ne 0 ]
then 
    echo "AutoAir[WARNING]:Git未安装"
fi

sudo python3 autoair.py
if [ $? -ne 0 ]
then 
    echo "AutoAir[ERROR]:AutoAir未启动成功"
    exit
fi
exit