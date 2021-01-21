from appium import webdriver
import time
# server 启动参数
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0.0'
desired_caps['deviceName'] = 'UYT0217A16001091'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.HWSettings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def test():
    print(driver.device_time)

# 打印手机分辨率 {'width': 1440, 'height': 2560}
# phone_size = driver.get_window_size()
# x = phone_size.get("width")/2
# y_0 = phone_size.get("height")*0.8
# y_1 = phone_size.get("height")*0.2
# driver.swipe(x,y_0,x,y_1,3000)

# 音量减
# for i in range(3):
#     driver.keyevent(25)

# 打开通知栏
# driver.open_notifications()
# # 点击操作横幅
# driver.find_element_by_id("com.android.systemui:id/header").click()
# # 点击飞行模式
# driver.find_element_by_xpath("//*[contains(@text,'飞')]").click()
#
# # 点击home键
# driver.keyevent(3)

# 点击开发者头条通知

# driver.open_notifications()
# text_desc = driver.find_element_by_xpath("//*[contains(@text,'拜拜')]")
# # 打印标题
# print(text_desc.text)
# # 通过通知栏进入app
# text_desc.click()

# 获取手机当前网络

# 获取手机当前网络
# print(driver.network_connection)
# # 设置手机网络，可能需要超级权限
# driver.set_network_connection(2)
#
# driver.get_screenshot_as_file("./screenshot_page/air.png")
if __name__ == '__main__':
    test()
    time.sleep(5)

    driver.quit()