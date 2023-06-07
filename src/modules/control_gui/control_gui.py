"""GUI control code.
"""

import pyautogui as pag

class ControlGUI:
    
    def write_message(
            self,
            message: str,
            interval: float = None,
        ):
        """Write message on the screen.
        
        Args:
            message (str): Message to write.
            interval (float, optional): Interval between each character. Defaults to None.
        """
        for msg in message.split('\n'):
            if interval is not None:
                pag.write(msg, interval=interval)
            else:
                pag.write(msg)

            pag.press('enter')
    
    def click_app(
        self,
        app_position: tuple,
        duration: float = 1.0,
    ):
        """Click the app on the screen.
        
        Args:
            app_position (tuple): Position of the app.
            duration (float, optional): Duration of the click. Defaults to 1.0.

        """
        pag.moveTo(app_position[0], app_position[1], duration=duration)
        pag.click()