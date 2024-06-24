import pyautogui


i = 120  # 第一個檔案的y位置
while i <= 550:  # 最後一個檔案的y位置
    # 換檔
    pyautogui.click(23, 805, duration=1)  # 選取檔案的位置
    pyautogui.click(296, i, duration=0.5)  # 依序排下去選取檔案
    print(i)
    pyautogui.click(2485, 1498, duration=0.2)  # 按下確定鈕,完成換檔

    #
    pyautogui.click(2529, 417, duration=0.5)
    pyautogui.click(2442, 1251, duration=0.5)
    pyautogui.click(589, 730)
    pyautogui.click(515, 809, duration=0.5)
    pyautogui.click(2310, 736)
    pyautogui.click(2309, 814, duration=0.5)
    pyautogui.click(2274, 872)
    pyautogui.click(2267, 907, duration=0.5)  # 改成0db
    pyautogui.click(2477, 1504)  # 存成webm

    pyautogui.click(589, 730, duration=60)
    pyautogui.click(521, 752, duration=0.5)  # 換成wav
    pyautogui.click(2310, 736)
    pyautogui.click(2265, 757, duration=0.5)

    pyautogui.click(1950, 540)  # 改黨名
    pyautogui.click(1064, 593)  #! 點選黨名位置
    pyautogui.typewrite("db")
    pyautogui.press("enter")
    pyautogui.click(2477, 1504, duration=0.5)

    pyautogui.click(1950, 540, duration=1)  # 改黨名
    pyautogui.click(1092, 593, duration=0.5)  #! 點選黨名位置
    pyautogui.typewrite("6")
    pyautogui.press("enter")
    pyautogui.click(2274, 872)
    pyautogui.click(2267, 935, duration=0.5)
    pyautogui.click(2477, 1504)

    pyautogui.click(1950, 540, duration=1)  # 改黨名
    pyautogui.click(1104, 593, duration=0.5)  #! 點選黨名位置
    pyautogui.press("backspace", interval=0.5)
    pyautogui.typewrite("12")
    pyautogui.press("enter")
    pyautogui.click(2274, 872)
    pyautogui.click(2267, 957, duration=0.5)
    pyautogui.click(2477, 1504)

    pyautogui.click(2525, 69, duration=1)

    i = i + 30

print(i)
