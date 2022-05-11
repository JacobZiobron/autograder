import PySimpleGUI as sg
import subprocess
import sys

# Global theme for PySimpleGUI
sg.theme('DarkBlack')

def startPage():
    
    layout = [
        [sg.T("""
    Instructions:
        1. Make sure you have the latest version of pytest installed on your machine
            a. open your terminal
            b. type 'pip install pytest'
                1. if you are using anaconda use 'conda install pytest'
            c. if you have any questions you can read this documentation -> https://docs.pytest.org/en/7.1.x/getting-started.html#get-started
        2. Click the Grade Button
        3. Click the assignment you wish to grade
            a. this will open the test file in your default text editor
        4. Remove the function from the bottom that runs the program
            a. for example 'main()' would need to be removed for pytest to work properly
        5. Click autograde for the assignment
        6. Read the rubric and grade depending on what tests passed/failed""", font = ("Arial", 16))],
        [sg.Button('Autograder', button_color=('white', 'purple'), size = (20,1)), sg.Button('Do I have pyTest installed?', button_color=('white', 'purple'), size = (20,1)), sg.Button('Exit', button_color=('white', 'purple'), size = (20,1))]]

    # Generates the startpage GUI
    window = sg.Window("CSC201 Assignment Autograder", layout, element_justification='c')
    while True:
            event, values = window.read(close=True)
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            elif event == 'Do I have PyTest installed?':
                try:
                  import pytest
                  print("PyTest is Installed")
                except:
                  print("Please install the PyTest library | pip install pytest")
                  exit()
            elif event == 'Autograder':
                main()

def main():

    # Generates the main GUI
    layout = [
        [sg.Multiline(size=(50, 15), echo_stdout_stderr=True, reroute_stdout=True, autoscroll=True, background_color='black', text_color='white', key='-MLINE-', font='ariel, 14')],
        # [sg.T('Promt> '), sg.Input(key='-IN-', focus=True, do_not_clear=False)],
        [sg.VPush()],
        [sg.Button('Assignment 8', button_color=('white', 'purple'), size = (20,1)), sg.Button('Autograde A8', button_color=('white', 'blue'), size = (20,1))],
        [sg.Button('Assignment 9', button_color=('white', 'purple'), size = (20,1)), sg.Button('Autograde A9', button_color=('white', 'blue'), size = (20,1))],
        [sg.Button('Assignment 10', button_color=('white', 'purple'), size = (20,1)), sg.Button('Autograde A10', button_color=('white', 'blue'), size = (20,1))],
        [sg.Button('Assignment 11', button_color=('white', 'purple'), size = (20,1)), sg.Button('Autograde A11', button_color=('white', 'blue'), size = (20,1))],
        [sg.Button('Assignment 12', button_color=('white', 'purple'), size = (20,1)), sg.Button('Autograde A12', button_color=('white', 'blue'), size = (20,1))],
        [sg.Button('Final Project', button_color=('white', 'purple'), size = (20,1)), sg.Button('Autograde FP', button_color=('white', 'blue'), size = (20,1))],
        [sg.Button('Exit', button_color=('white', 'red'), size = (46,1))],
        [sg.VPush()]]

    window = sg.Window('Autograder', layout, element_justification='c')
    while True:  # Event Loop
        event, values = window.read()

        # Handles exiting the window
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        # Block of code to:
        #   1. Open Assignment 8 in default text editor
        #   2. Run pytests
        elif event == 'Assignment 8':
            opener = "xdg-open" if sys.platform.startswith('linux') else "notepad"
            subprocess.call([opener, "./assignment8pyTests.py"])

        elif event == 'Autograde A8':
            sp = sg.execute_command_subprocess('pytest', 'assignment8pyTests.py', "--capture=sys", "-s", "--disable-pytest-warnings", pipe_output=True, wait=False)
            results = sg.execute_get_results(sp, timeout=1)
            print(results[0])

        # Block of code to:
        #   1. Open Assignment 9 in default text editor
        #   2. Run pytests
        elif event == 'Assignment 9':
            opener = "xdg-open" if sys.platform.startswith('linux') else "notepad"
            subprocess.call([opener, "./assignment9pyTests.py"])

        elif event == 'Autograde A9': 
            sp = sg.execute_command_subprocess('pytest', 'assignment9pyTests.py', "--capture=sys", "-s", "--disable-pytest-warnings", pipe_output=True, wait=False)
            results = sg.execute_get_results(sp, timeout=1)
            print(results[0])

        # Block of code to:
        #   1. Open Assignment 10 in default text editor
        #   2. Run pytests
        elif event == 'Assignment 10':
            opener = "xdg-open" if sys.platform.startswith('linux') else "notepad"
            subprocess.call([opener, "./assignment10pyTests.py"])

        elif event == 'Autograde A10':
            sp = sg.execute_command_subprocess('pytest', 'assignment10pyTests.py', "--capture=sys", "-s", "--disable-pytest-warnings", pipe_output=True, wait=False)
            results = sg.execute_get_results(sp, timeout=1)
            print(results[0])

        # Block of code to:
        #   1. Open Assignment 11 in default text editor
        #   2. Run pytests
        elif event == 'Assignment 11':
            opener = "xdg-open" if sys.platform.startswith('linux') else "notepad"
            subprocess.call([opener, "./assignment11pyTests.py"])
 
        elif event == 'Autograde A11':
            sp = sg.execute_command_subprocess('pytest', 'assignment11pyTests.py', "--capture=sys", "-s", "--disable-pytest-warnings", pipe_output=True, wait=False)
            results = sg.execute_get_results(sp, timeout=1)
            print(results[0])

        # Block of code to:
        #   1. Open Assignment 12 in default text editor
        #   2. Run pytests
        elif event == 'Assignment 12':
            opener = "xdg-open" if sys.platform.startswith('linux') else "notepad"
            subprocess.call([opener, "./assignment12pyTests.py"])

        elif event == 'Autograde A12':
            sp = sg.execute_command_subprocess('pytest', 'assignment12pyTests.py', "--capture=sys", "-s", "--disable-pytest-warnings", pipe_output=True, wait=False)
            results = sg.execute_get_results(sp, timeout=1)
            print(results[0])
        
        # Block of code to:
        #   1. Open Final Project file in default text editor
        #   2. Run pytests
        elif event == 'Final Project':
            opener = "xdg-open" if sys.platform.startswith('linux') else "notepad"
            subprocess.call([opener, "./finalExamTests.py"])

        elif event == 'Autograde FP':
            sp = sg.execute_command_subprocess('pytest', 'finalExamTests.py', "--capture=sys", "-s", "--disable-pytest-warnings", pipe_output=True, wait=False)
            results = sg.execute_get_results(sp, timeout=1)
            print(results[0])

    window.close()


startPage()