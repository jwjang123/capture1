import pyautogui

# 스크린샷 찍어서 저장
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')
print("스크린샷이 저장되었습니다.")
