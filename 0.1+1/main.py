import requests
import json
import time
import urllib.request
import sys
import getpass
import tkinter as tk
from tkinter import filedialog

from colorama import init, Fore, Style
init()

app_version_type=0
print("""
                                                                               
                                     ,----..                                   
    ,---,                           /   /   \                                  
  .'  .' `\                        /   .     : ,-.----.                        
,---.'     \                      .   /   ;.  \\    /  \                ,---,  
|   |  .`\  |               .---..   ;   /  ` ;|   :    |           ,-+-. /  | 
:   : |  '  |   ,---.     /.  ./|;   |  ; \ ; ||   | .\ :   ,---.  ,--.'|'   | 
|   ' '  ;  :  /     \  .-' . ' ||   :  | ; | '.   : |: |  /     \|   |  ,"' | 
'   | ;  .  | /    /  |/___/ \: |.   |  ' ' ' :|   |  \ : /    /  |   | /  | | 
|   | :  |  '.    ' / |.   \  ' .'   ;  \; /  ||   : .  |.    ' / |   | |  | | 
'   : | /  ; '   ;   /| \   \   ' \   \  ',  / :     |`-''   ;   /|   | |  |/  
|   | '` ,/  '   |  / |  \   \     ;   :    /  :   : :   '   |  / |   | |--'   
;   :  .'    |   :    |   \   \ |   \   \ .'   |   | :   |   :    |   |/       
|   ,.'       \   \  /     '---"     `---`     `---'.|    \   \  /'---'        
'---'          `----'                            `---`     `----'              
欢迎使用铁榔头原生API快捷操作应用！
Released under GPL-3 , Tlt-Oj-App Copyright © 2023 DevOpen
version.0.1+1
----------
""")
time.sleep(2)
if app_version_type==0:
    print(f'{Fore.YELLOW}[WARN]{Style.RESET_ALL}本应用为开发测试版本')
else:
    print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}正式发行版')
print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}准备初始化，请稍后...')

try:
    urllib.request.urlopen('https://www.baidu.com', timeout=3)
    print(f'{Fore.BLUE}[notice]{Style.RESET_ALL}网络已连接')
except urllib.error.URLError:
    print(f'{Fore.RED}[ERR]{Style.RESET_ALL}未检查到网络连接，3秒后退出...')
    time.sleep(3)
    sys.exit()
print("----------")
tlt_username=input(f'{Fore.BLUE}[INPUT]{Style.RESET_ALL}登录用户名：')
tlt_pwd = getpass.getpass(f'{Fore.BLUE}[INPUT]{Style.RESET_ALL}登录密钥：')
print(f'{Fore.BLUE}[notice]{Style.RESET_ALL}正在尝试登录'+tlt_username+' ，密钥：'+tlt_pwd+'')
url="https://lc.ihammertech.com/tielangtou_api/web/user/login"#注意令牌
headers = {'content-type':"application/json;charset=utf-8"}
jsonfile=json.dumps({
	"username": tlt_username,
	"password": tlt_pwd
})
postreturn=requests.post(url,data=jsonfile,headers=headers)
postreturn=json.loads(postreturn.text)
if postreturn["code"]==200:
    print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}登录成功')
    print(f'{Fore.BLUE}[notice]{Style.RESET_ALL}正在尝试创建会话')
    cookie=postreturn["data"]
    time.sleep(2)
    print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}'+cookie+'')
    print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}会话创建完成')
else:
    print(f'{Fore.RED}[ERR]{Style.RESET_ALL}登录失败，请重试...（3秒后关闭）')
    time.sleep(3)
    sys.exit()

print("----------")
print("Hi，"+tlt_username+"！欢迎来到铁榔头原生API学习中心~ - Powered by DevOpen")
while True:
    print("-----功能面板-----")
    print("""
    1 提交测评
    敬请期待...
    """)
    menu=input(f'{Fore.BLUE}[INPUT]{Style.RESET_ALL}请输入功能编号：')
    if menu=="1":
        print("----------")
        tlt_question_num=input(f'{Fore.BLUE}[INPUT]{Style.RESET_ALL}请输入题目编号：')
        url="https://lc.ihammertech.com/tielangtou_api/web/problem/evaluationList"#注意令牌
        headers = {'content-type':"application/json;charset=utf-8",'Cookie':'eva-auth-token='+cookie+''}
        jsonfile=json.dumps({
            "difficulty": "",
            "keyword": tlt_question_num,
            "limit": 10,
            "problemType": 1,
            "type": 0,
            "offset": "1",
            "source": "",
            "tags": "",
            "year": ""
        })
        postreturn=requests.post(url,data=jsonfile,headers=headers)
        # print(postreturn.text)
        postreturn=json.loads(postreturn.text)
        if postreturn["code"]==200 and postreturn["data"]["results"]!=None:
            question_data=postreturn["data"]['results'][0]
            print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}题号搜索完成，题目信息见下：')
            question_id=question_data["id"]
            question_name=question_data["title"]
            print("题目名称："+question_name+"")
            print("题目标识："+question_id+"")
            print("题目编号："+tlt_question_num+"")
            print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}请选择评测文件：')
            time.sleep(2)
            # 创建一个 Tkinter 根窗口
            root = tk.Tk()
            root.withdraw()  # 隐藏根窗口

            # 打开文件选择对话框
            file_path = filedialog.askopenfilename(filetypes=[("C++ Files", "*.cpp")])

            # 读取文件内容并保存到变量中
            with open(file_path, 'r') as file:
                file_content = file.read()

            # 输出文件内容
            print(file_content)
            url="https://lc.ihammertech.com/tielangtou_api/web/problem/evaluationScore"#注意令牌
            headers = {'content-type':"application/json;charset=utf-8",'Cookie':'eva-auth-token='+cookie+''}
            jsonfile=json.dumps({
                "problem": question_id,
                "language": "C++",
                "isContest": False,
                "code": file_content
            })
            postreturn=requests.post(url,data=jsonfile,headers=headers)
            # print(postreturn.text)
            postreturn=json.loads(postreturn.text)
            if postreturn["code"]==200:
                print(f'{Fore.GREEN}[INFO]{Style.RESET_ALL}测评提交成功，请稍后...')
                
                submission_id=postreturn["data"]["submission_id"]
                url="https://lc.ihammertech.com/tielangtou_api/web/problem/getSubmission?id="+submission_id+""#注意令牌
                headers = {'content-type':"application/json;charset=utf-8",'Cookie':'eva-auth-token='+cookie+''}
                
                postreturn=requests.get(url,headers=headers)
                # print(postreturn.text)
                postreturn=json.loads(postreturn.text)
                if postreturn["code"]==200:
                    submit_time=postreturn["data"]["problem"]["lastUpdateTime"]
                    score=postreturn["data"]["statistic_info"]
                    score=json.loads(score)
                    score=score["score"]
                    
                    if score==100:
                        print(f'{Fore.GREEN}[SUCCESS]{Style.RESET_ALL}测评通过，得分：'+str(score)+'')
                    else:
                        print(f'{Fore.RED}[LOSS]{Style.RESET_ALL}测评未通过，得分：'+str(score)+'')
                    print("----------")
                else:
                    print(f'{Fore.RED}[ERR]{Style.RESET_ALL}测评失败，请重试')
            else:
                print(f'{Fore.RED}[ERR]{Style.RESET_ALL}测评提交失败，请重试')
        else:
            print(f'{Fore.YELLOW}[WARN]{Style.RESET_ALL}题目不存在，请检查')
    else:
        print(f'{Fore.YELLOW}[WARN]{Style.RESET_ALL}功能不存在，请重试')
        time.sleep(2)
