import PySimpleGUI as sg




layout = [
    [
    sg.Column([[sg.Multiline('',size=(50, 20), key='MessagesBox')]]),
    ],
    [
        sg.Column([[sg.Button('Ok', size=(4,0))]]),
        sg.Column([[sg.InputText('',size=20, key='MessageInput')]]),
        #sg.Text('', key=('Text')),
    ],

]

window = sg.Window(
    'ChatPy',
    layout,
    resizable=False,
    size=(640,360),
    return_keyboard_events=True,
    margins=(0,0),
)

def main():
    testing = False
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Ok':
            window['MessagesBox'].update(value = values['MessageInput'])

if __name__ == "__main__":
    main()