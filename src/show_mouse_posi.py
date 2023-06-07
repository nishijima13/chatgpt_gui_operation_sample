import time
import pyautogui as pag

while True:
    m_posi_x, m_posi_y = pag.position()
    print("Current mouse position : x = " + str(m_posi_x) + ", y = " + str(m_posi_y))
    time.sleep(0.5)