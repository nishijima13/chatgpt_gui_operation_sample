"""Demo code of screen operation by ChatGPT.
"""
import argparse
import time
import os
import re
import openai
import modules.control_gui.control_gui as cgui

system_prompt = """
You give commands to the PC in sentences.
you can give commands to notepad.
Instructions to Notepad should be of the form:
'Notepad: "What to put in notepad" EndNotepad'\n\n
"""

def demo(
    app_position: tuple,
):
    control_gui = cgui.ControlGUI()

    query = input("What do you want your PC to do? : ")

    print("Thinking...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )
    print("Done!")
    response_msg = response["choices"][0]["message"]["content"]
    notepad_msg_list = re.findall(r'Notepad: (.+)EndNotepad', response_msg)
    
    if len(notepad_msg_list) == 0:
        print("I didn't find any instructions to the notepad app from ChatGPT's answer. : {0}".format(response_msg))

    else:
        print("Start automatic control.")
        for nidx, nmsg in enumerate(notepad_msg_list):
            if nidx == 0:
                control_gui.click_app(
                    app_position=app_position,
                    duration=1.0,
                )
            time.sleep(2.0)
            control_gui.write_message(
                message=nmsg,
                interval=0.1,
            )
        print("Finish automatic control.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Demo code of screen operation by ChatGPT.',
    )
    parser.add_argument('-apx', '--app_position_x', help="Position of the app on the screen (x).", type=int, required=True)
    parser.add_argument('-apy', '--app_position_y', help="Position of the app on the screen (y).", type=int, required=True)


    args = parser.parse_args()

    openai.api_key = os.getenv("OPENAI_API_KEY")
    app_position = (args.app_position_x, args.app_position_y)

    demo(
        app_position=app_position,
    )