#!/usr/bin/env Python3      
'''import PySimpleGUI as sg
import time

sg.ChangeLookAndFeel('GreenTan') 

def theme_browser_window_1(new_theme_1):

    layout_1 = [[sg.Text('Theme Browser')],
               [sg.Text('Click a Theme color to see demo window')],
               [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
               [sg.Button('Exit')]]

    #layout_tb = ""
    #layout_tb = layout_1
    window_1 = sg.Window('Theme Browser', layout_1)

    while True:  # Event Loop
        event, values = window_1.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        sg.theme(values['-LIST-'][0])
        sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))
        new_theme_1 = str(values['-LIST-'][0])
        print(values)
        print(new_theme_1)
        sg.theme(new_theme_1)
        print(new_theme_1)

    window_1.close()
    return new_theme_1
    
def main_window(event, values):

    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Option', ['Theme', 'Settings',], ],
                ['Help', 'About...'], ]      

    # ------ Column Definition ------ #      
    column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

    layout = [      
       [sg.Menu(menu_def, tearoff=False)],      
        [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
        [sg.Text('Here is some text.... and a place to enter text')],      
        [sg.InputText('This is my text')],      
        [sg.Frame(layout=[      
        [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
        [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
       [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
            sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
            sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
        [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),          
            sg.Frame('Labelled Group',[[      
            sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
            sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
            sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
            sg.Column(column1, background_color='#F7F3EC')]])],      
        [sg.Text('_'  * 80)],      
        [sg.Text('Choose A Folder', size=(35, 1))],      
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
            sg.InputText('Default Folder'), sg.FolderBrowse()],      
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
    ]      

    window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)     

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Submit':
            event, values = window.read()      
            break
        if event == 'Theme':
            #sg.theme_all_look_and_feel_themes()
            #sg.theme_previewer()
            #theme_name_list = sg.theme_list()
            #sg.popup(title = 'Themes', [sg.Listbox(theme_name_list)])
            #sg.theme(values['-List'][0])
            #sg.pop
            #sg.Listbox(values=sg.theme_list(), size=(20,12), key = '-List-', enable_event=True)
            new_theme_1 = sg.theme()
            new_theme_1 = theme_browser_window_1(new_theme_1)
            print(new_theme_1)
            sg.theme(new_theme_1)
            #sg.window.update
            break

    window.close()  
    return event, values



def main():

    #while True:
        event, values = main_window(event, values)
        #if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        #    break


sg.popup('Title',
                'The results of the window.',
                'The button clicked was "{}"'.format(event),
                'The values are', values)

main()
exit()
'''

import math

def summe(args):
    summ = 0.0
    for i in args:
        summ += i
    return summ


x = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
print(summe(x))
print(math.fsum(x))
