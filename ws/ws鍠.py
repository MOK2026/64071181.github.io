


'''

    :::       :::       ::::::::                           :::       :::    :::   :::::::::::       ::::::::                       :::::::::       ::::::::::
   :+:       :+:      :+:    :+:                        :+: :+:     :+:    :+:       :+:          :+:    :+:                      :+:    :+:      :+:
  +:+       +:+      +:+                              +:+   +:+    +:+    +:+       +:+          +:+    +:+                      +:+    +:+      +:+
 +#+  +:+  +#+      +#++:++#++                      +#++:++#++:   +#+    +:+       +#+          +#+    +:+                      +#++:++#:       +#++:++#
+#+ +#+#+ +#+             +#+                      +#+     +#+   +#+    +#+       +#+          +#+    +#+                      +#+    +#+      +#+
#+#+# #+#+#       #+#    #+#                      #+#     #+#   #+#    #+#       #+#          #+#    #+#                      #+#    #+#      #+#
###   ###         ########       ##########      ###     ###    ########        ###           ########       ##########      ###    ###      ##########

All rights reserved by 64071181.github.io

'''






import os
import time
import sys
import requests
import subprocess
import random

# Windows API 阻止系统休眠
import ctypes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains


# 剪贴板
import pyperclip

from bs4 import BeautifulSoup












































'''
      ::::::::       :::    :::       :::::::::       ::::::::         :::   :::       ::::::::::
    :+:    :+:      :+:    :+:       :+:    :+:     :+:    :+:       :+:+: :+:+:      :+:
   +:+             +:+    +:+       +:+    +:+     +:+    +:+      +:+ +:+:+ +:+     +:+
  +#+             +#++:++#++       +#++:++#:      +#+    +:+      +#+  +:+  +#+     +#++:++#
 +#+             +#+    +#+       +#+    +#+     +#+    +#+      +#+       +#+     +#+
#+#    #+#      #+#    #+#       #+#    #+#     #+#    #+#      #+#       #+#     #+#
########       ###    ###       ###    ###      ########       ###       ###     ##########
'''
import shutil
def _下載賺錢王Chrome():
    # 確定 EXE 同層目錄，若在打包環境下，使用 sys.executable 取得 EXE 目錄
    exe_dir = os.path.dirname(sys.executable) if hasattr(sys, 'frozen') else os.path.dirname(os.path.abspath(__file__))

    # 設置 MoneyKingChrome 資料夾路徑
    chrome_dir = os.path.join(exe_dir, 賺錢王瀏覽器位)
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = chrome_dir

    # Playwright 預設下載的臨時位置
    temp_chrome_dir = os.path.join(os.getenv("LOCALAPPDATA"), "ms-playwright")

    chromium_path = os.path.join(chrome_dir, "chromium-1140", "chrome-win", "chrome.exe")
    #print('chromium_path =', chromium_path)

    # 檢查 EXE 同層 MoneyKingChrome 資料夾是否已存在 Chrome
    if not os.path.isfile(chromium_path):
        try:
            # 執行 playwright install
            subprocess.run(["playwright", "install"], check=True)
            
            # 在臨時資料夾中找到下載的 Chrome 目錄並複製到 EXE 同層目錄
            downloaded_chrome = os.path.join(temp_chrome_dir, "chromium-1140", "chrome-win")
            if os.path.exists(downloaded_chrome):
                # 若 EXE 同層 MoneyKingChrome 資料夾已存在，先刪除再複製
                if os.path.exists(chrome_dir):
                    shutil.rmtree(chrome_dir)
                shutil.copytree(downloaded_chrome, os.path.join(chrome_dir, "chromium-1140", "chrome-win"))
                print(f"已將 Chrome 瀏覽器複製到 EXE 同層的 {賺錢王瀏覽器位} 資料夾中。")
            else:
                print("瀏覽器下載失敗，無法找到下載的目錄。")
        except subprocess.CalledProcessError as e:
            print(f"安裝 Playwright 瀏覽器失敗: {e}")
    #else:
        #print("Chrome 瀏覽器已安裝在指定路徑中。")














def _Chrome設定():
    global driver

    ''''''
    exe_dir = os.path.dirname(sys.executable) if hasattr(sys, 'frozen') else os.path.dirname(os.path.abspath(__file__))
    chromium_path = os.path.join(exe_dir, 賺錢王瀏覽器位, "chromium-1140", "chrome-win", "chrome.exe")
    

    # 配置 Chrome 选项
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chromium_path  # 指定 Chrome 可执行路径

    # Chrome配置选项
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=3')  # 只显示严重错误
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--remote-debugging-port=9222')

    # 每次執行程式都會重用此資料夾，LocalStorage、Cookies 等記錄不會消失
    USER_DATA_DIR = os.path.join(os.getcwd(), 'chrome_user_data')
    chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    chrome_options.add_argument("--profile-directory=Default")       # 使用預設設定檔
    chrome_options.add_argument("--disable-restore-session-state")  # 禁用会话恢复
    
    # 初始化浏览器
    driver = webdriver.Chrome(options=chrome_options)
    #driver.set_window_size(768, 1366)  # 设置浏览器窗口大小









































'''
      ::::::::   :::::::::::       :::    :::       ::::::::::       :::::::::
    :+:    :+:      :+:           :+:    :+:       :+:              :+:    :+:
   +:+    +:+      +:+           +:+    +:+       +:+              +:+    +:+
  +#+    +:+      +#+           +#++:++#++       +#++:++#         +#++:++#:
 +#+    +#+      +#+           +#+    +#+       +#+              +#+    +#+
#+#    #+#      #+#           #+#    #+#       #+#              #+#    #+#
########       ###           ###    ###       ##########       ###    ###
'''

class ReloadPageException(Exception):
    """自定义异常用于触发页面重载"""
    pass



def _檢查元素存在(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
        return True
    except NoSuchElementException:
        return False



查點 = 0
def _檢查點擊(位置,xpath, timeout=10):
    global 查點
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        return True
    except Exception as e:
        查點 += 1
        if 查點 > 3:
            查點 = 0
            _請告知作者更新(位置, xpath)
        return False



檢字 = 0
def _檢查文字輸入(位置,xpath, text, timeout=10):
    global 檢字
    if _檢查元素存在(xpath):
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        element.send_keys(text)
        return True
    else:
        檢字 += 1
        if 檢字 > 3:
            檢字 = 0
            _請告知作者更新(位置, xpath)
        return False



檢列 = 0
def _登入ws_等待對話列表出現():
    global 檢列
    try:
        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((
            By.XPATH, 
            其他_xpaths['對話列表']  # 同时验证属性
        ))
        )
        return True
    except TimeoutException:
        檢列 += 1
        if 檢列 > 3:
            檢列 = 0
            _請告知作者更新('對話列表', 其他_xpaths['對話列表'])
        return False



def _請告知作者更新(位置名, xpath):
    print(f'''請告知作者更新:
        https://api.whatsapp.com/send/?phone={官Ws}&text=找不到{位置名}元素[{xpath}]
        ''')




def _WindowsAPI阻止系统休眠():
    # 定义常量
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    # 阻止系统休眠和关闭显示器
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )
    

















































'''
    :::       :::       :::    :::           :::    :::::::::::       ::::::::           :::        :::::::::       :::::::::
   :+:       :+:       :+:    :+:         :+: :+:      :+:          :+:    :+:        :+: :+:      :+:    :+:      :+:    :+:
  +:+       +:+       +:+    +:+        +:+   +:+     +:+          +:+              +:+   +:+     +:+    +:+      +:+    +:+
 +#+  +:+  +#+       +#++:++#++       +#++:++#++:    +#+          +#++:++#++      +#++:++#++:    +#++:++#+       +#++:++#+
+#+ +#+#+ +#+       +#+    +#+       +#+     +#+    +#+                 +#+      +#+     +#+    +#+             +#+
#+#+# #+#+#        #+#    #+#       #+#     #+#    #+#          #+#    #+#      #+#     #+#    #+#             #+#
###   ###         ###    ###       ###     ###    ###           ########       ###     ###    ###             ###
'''


def _登入ws(国家代码,电话号码):

    while True:
        try:
            # 打开WhatsApp网页版
            driver.get("https://web.whatsapp.com/")
            time.sleep(random.uniform(3, 6))

            if _登入ws_等待對話列表出現():
                print(f"已登入WhatsApp,如需登入其他帳號，請登出再重新執行程式。")
                break

            # 段2 = 填寫手機號碼
            try:
                for 鍵, 值 in 登入流程_xpaths.items():
                    if 鍵 in ("国家代码", "电话号码"):
                        # 使用字典映射對應參數
                        參數映射 = {"国家代码": 国家代码, "电话号码": 电话号码}
                        if not _檢查文字輸入(鍵, 值, 參數映射[鍵]):
                            raise ReloadPageException()
                    else:
                        if not _檢查點擊(鍵,值):
                            raise ReloadPageException()
                    time.sleep(random.uniform(0.8, 4.8))
            except ReloadPageException:
                continue

            # 段3 = 等待验证码加载
            time.sleep(5)
            verification_code = []
            for i in range(1, 9):
                验证码字符XPATH = 其他_xpaths['验证字符頭'] + str(i) + 其他_xpaths['验证字符尾']
                try:
                    code_element = WebDriverWait(driver, 30).until(
                        EC.visibility_of_element_located((
                            By.XPATH, 
                            验证码字符XPATH))
                    )
                    verification_code.append(code_element.text)
                except ReloadPageException:
                    print(f"无法获取验证码字符:")
                    continue
            print("\n验证码为:", ''.join(verification_code))

            # 段4 = 等待验证成功後 使用QR碼登入 消失
            print("等待手機端填寫验证碼...")
            WebDriverWait(driver, 180).until_not(
                EC.presence_of_element_located((
                    By.XPATH, 
                    其他_xpaths['验证成功使用QR碼登入消失']
                ))
            )
            
            # 段5 = 验证成功 等待對話列表出現
            time.sleep(random.uniform(3.8, 5.8))
            _登入ws_等待對話列表出現()

        except Exception as e:
            #print(f"主程序出错: {str(e)}")
            print(f"登入WhatsApp超时，刷新页面...")
            continue

    # 段6 = send登入信息比admin
    _send登入信息比admin()







def _send登入信息比admin():
    driver.get(f"https://api.whatsapp.com/send/?phone={官Ws}&text={月費用戶}%0D%0A{本程式名}%0D%0A{帳號1181}")

    while True:
        try:
            _檢查點擊('繼續前往對話','//*[@id="action-button"]')
            _檢查點擊('使用 WhatsApp 網頁版','//*[@id="fallback_block"]/div/div/h4[2]/a')

            # 等待輸入框出現並輸入回覆
            對話輸入框 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, 其他_xpaths['對話輸入框']))
            )

            對話輸入框.send_keys(Keys.RETURN)
            print("成功登入WhatsApp")
            break
        except:
            continue






計等錢 = 0
def _ws自動客服():
    global 計等錢

    while True:
        try:
            _登入ws_等待對話列表出現()
            break
        except:
            continue
    
    while True:
        計等錢 +=1
        print(f"你已收到{計等錢}萬元")

        try:
            # 每次迭代時重新獲取 chat_list
            chat_list = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, 其他_xpaths['對話列表']))
            )

            for chat in chat_list:
                try:
                    # 每次點擊前重新獲取 chat 元素
                    chat = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,其他_xpaths['客戶信息位']))
                    )
                    客來詢 = chat.text

                    # 判斷是否需回覆
                    if 客來詢 in 回覆內容:
                        chat.click()  # 點擊進入對話
                        _ws自動回覆(客來詢)
                except StaleElementReferenceException:
                    print("元素已過期，重新取得 chat 元素...")
                    continue
                except TimeoutException:
                    print("等待訊息載入超時，跳過此聊天...")
                    continue
        except TimeoutException:
            continue
        time.sleep(3)
        continue













def _ws自動回覆(來):
    global 計等錢

    if not 月費用戶:
        _檢查使用次數()

    try:
        # 等待輸入框出現並輸入回覆
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, 其他_xpaths['對話輸入框']))
        )

        # 使用 ActionChains 替换所有 \n 为 Shift+Enter
        actions = ActionChains(driver)
        處理後內容 = 回覆內容[來].split('\n')
        for i, 處理後內容 in enumerate(處理後內容):
            if i > 0:  # 从第二行开始换行
                actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
            actions.send_keys(處理後內容)

        actions.send_keys(Keys.RETURN)  # 最后提交
        actions.perform()

        print(f"客戶: {來}, 已自動回覆\n{回覆內容[來]}\n")
        計等錢 = 0  # 回覆成功，重置計等錢

    except TimeoutException as e:
        print(f"操作超时: {str(e)}")
    except Exception as e:
        print(f"发生错误: {str(e)}")










































'''
          :::        ::::::::         :::         :::       ::::::::         :::
       :+: :+:     :+:    :+:      :+:+:       :+:+:      :+:    :+:      :+:+:
     +:+   +:+    +:+               +:+         +:+      +:+    +:+        +:+
   +#++:++#++:   +#+               +#+         +#+       +#++:++#         +#+
  +#+     +#+   +#+               +#+         +#+      +#+    +#+        +#+
 #+#     #+#   #+#    #+#        #+#         #+#      #+#    #+#        #+#
###     ###    ########       #######     #######     ########       #######
'''


def 獲取用戶輸入(執行碼):
    global 月費用戶

    輸入行 = 執行碼.split('\n') #[]
    輸入文本 = "\n".join(輸入行)

    # 解析並替換參數
    _解析輸入內容(輸入文本)

    if 獲取帳號資料(帳號1181):
        月費用戶 = True










# 請使用者在執行時輸入 Python 格式的資料
def _解析輸入內容(輸入文本):
    #print("""將用戶輸入的文本解析為Python變量""")
    
    try:
        # 創建一個臨時命名空間來執行輸入的程式碼
        臨時命名空間 = {}
        exec(輸入文本, globals(), 臨時命名空間)
        
        # 更新全局變量
        globals().update({k: v for k, v in 臨時命名空間.items() 
                        if k in ['帳號1181', '国家代码', '电话号码', 
                                '回覆內容', '登入流程_xpaths', '其他_xpaths']})
    except Exception as e:
        print(f"解析錯誤: {e}")











def 獲取帳號資料(帳號):
    try:
        # 獲取網頁內容
        response = requests.get(VipDurl)
        response.raise_for_status()  # 檢查請求是否成功
        
        # 搜索 帳號1181
        if 帳號 in response.text:
            return True
            
    except requests.exceptions.RequestException as e:
        print(f"請求帳號資料失敗:{e}")







def _檢查使用次數():
    global 用次數

    用次數 += 1
    if 用次數 > 試用次數:
        print(f"已超過試用次數 {試用次數} 次，退出程式...")
        driver.quit()
        sys.exit()

















































'''
     :::    :::       :::::::::       :::::::::           :::    :::::::::::           :::                        ::::::::::       :::    :::       ::::::::::
    :+:    :+:       :+:    :+:      :+:    :+:        :+: :+:      :+:             :+: :+:                      :+:              :+:    :+:       :+:
   +:+    +:+       +:+    +:+      +:+    +:+       +:+   +:+     +:+            +:+   +:+                     +:+               +:+  +:+        +:+
  +#+    +:+       +#++:++#+       +#+    +:+      +#++:++#++:    +#+           +#++:++#++:                    +#++:++#           +#++:+         +#++:++#
 +#+    +#+       +#+             +#+    +#+      +#+     +#+    +#+           +#+     +#+                    +#+               +#+  +#+        +#+
#+#    #+#       #+#             #+#    #+#      #+#     #+#    #+#           #+#     #+#                    #+#              #+#    #+#       #+#
########        ###             #########       ###     ###    ###           ###     ###    ##########      ##########       ###    ###       ##########
'''
def _UpData本程式():
    try:
        # 取得網頁內容
        response = requests.get(f'{Ws客服官網}ws/index.html')
        response.raise_for_status()  # 檢查請求是否成功
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        p_element = soup.find('p', id='更新日期')
        
        if not p_element:
            raise Exception("找不到更新日期元素")
        
        web_time = p_element.text.strip()
        
        # 比較時間
        if web_time > 更新時間:
            # 下載檔案
            download_url = f'https://github.com/64071181/64071181.github.io/raw/main/ws/{本程式名}.exe'
            exe_response = requests.get(download_url)
            exe_response.raise_for_status()
            
            # 產生新檔名
            new_filename = f'{本程式名}{web_time}.exe'
            
            # 儲存檔案
            with open(new_filename, 'wb') as f:
                f.write(exe_response.content)
            
            print(f'[{new_filename}]已更新,請重新執行')
            sys.exit()
            
        else:
            print("\n🥳目前版本已是最新版本🥳\n")
            檢查並刪除舊版本()

    except requests.exceptions.RequestException as e:
        print(f"網路錯誤: {str(e)}")
    except Exception as e:
        print(f"發生錯誤: {str(e)}")















# not work qqqqqqqqqqqqqq
def 檢查並刪除舊版本():
    try:
        當前目錄 = os.getcwd()
        所有檔案 = os.listdir(當前目錄)
        刪除計數 = 0

        for 檔名 in 所有檔案:
            # 檢查是否符合命名模式
            if 檔名.startswith(本程式名) and 檔名.endswith('.exe'):
                # 提取時間戳部分
                時間部分 = 檔名[6:-4]  # 移除前6字元和後4字元(.exe)
                
                # 驗證時間格式
                if len(時間部分) != 12 or not 時間部分.isdigit():
                    continue  # 跳過不符合格式的檔案
                
                # 比較時間
                if 時間部分 < 更新時間:
                    os.remove(檔名)
                    print(f'🥳已刪除舊版本檔案: {檔名}')
                    刪除計數 += 1

    except Exception as e:
        print(f'清理過程中發生錯誤: {str(e)}')




































'''
          :::        :::::::::         :::   :::       :::::::::::       ::::    :::
       :+: :+:      :+:    :+:       :+:+: :+:+:          :+:           :+:+:   :+:
     +:+   +:+     +:+    +:+      +:+ +:+:+ +:+         +:+           :+:+:+  +:+
   +#++:++#++:    +#+    +:+      +#+  +:+  +#+         +#+           +#+ +:+ +#+
  +#+     +#+    +#+    +#+      +#+       +#+         +#+           +#+  +#+#+#
 #+#     #+#    #+#    #+#      #+#       #+#         #+#           #+#   #+#+#
###     ###    #########       ###       ###     ###########       ###    ####
'''

def _Admin模式(txt):
    input(f'*** {txt} _Admin模式***\n按任何鍵執行下步...')


































'''
      ::::::::   :::::::::::           :::        :::::::::   :::::::::::
    :+:    :+:      :+:             :+: :+:      :+:    :+:      :+:
   +:+             +:+            +:+   +:+     +:+    +:+      +:+
  +#++:++#++      +#+           +#++:++#++:    +#++:++#:       +#+
        +#+      +#+           +#+     +#+    +#+    +#+      +#+
#+#    #+#      #+#           #+#     #+#    #+#    #+#      #+#
########       ###           ###     ###    ###    ###      ###
'''









def _執行Ws自動客服():


    driver.get(f'{Ws客服官網}ws/set.html')

    # 写入空内容覆盖剪贴板
    pyperclip.copy('')
    # 点击前的剪贴板内容（用于检测变化）
    original_clipboard = pyperclip.paste()

    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != original_clipboard and '帳號1181 = "' in current_clipboard:
            break
        print(f"設置完成後，請按 執行{本程式名}...")
        time.sleep(1)  # 避免过高频率检查

    # 写入内容覆盖剪贴板
    #pyperclip.copy('MOKAGI金流商匯 ws鍠')

    獲取用戶輸入(current_clipboard)


















if __name__ == "__main__":

    
    更新時間 = '202504160205'
    本程式名 = 'ws鍠'
    賺錢王瀏覽器位 = 'MoneyKingChrome'


    官Ws = '85264071181'
    Ws客服官網 = 'https://64071181.github.io/'
    VipDurl = "https://github.com/64071181/64071181.github.io/blob/main/ws/d"

    月費用戶 = False 
    試用次數 = 10
    用次數 = 0

    driver = None
    帳號1181 = None
    电话号码 = None
    国家代码 = None
    回覆內容 = None
    登入流程_xpaths = None
    其他_xpaths = None

    _UpData本程式()
    _下載賺錢王Chrome()
    _Chrome設定()

    _執行Ws自動客服()

    print(f'''
            _\|/_
            (o o)
    +----oOO--U--OOo-------------------------{更新時間}-+
    |                                                     |
      {本程式名} 歡迎您 !                                      
    |                                                     |
           {帳號1181}    
           月費用戶 = {月費用戶}                      
           国家代码 = {国家代码}      
           电话号码 = {电话号码}                  
    |                                                     | 
           官網 = {Ws客服官網}                 
           聯絡我們 = {Ws客服官網}ContactAKI.html                 
    |                                                     | 
           *****************************************          
    |                                                     |
    +-----------------------------------------------------+
    ''')

    _WindowsAPI阻止系统休眠()
    _登入ws(国家代码,电话号码)
    _ws自動客服()


# 執行本程式系列 \


