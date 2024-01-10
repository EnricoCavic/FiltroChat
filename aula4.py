# Filtro de p***ria no chat

PATH = 'palavras.txt'
ENCODING = 'utf-8'
MAXIMUM_INFRACTIONS = 10

with open(PATH,'r', encoding=ENCODING) as file:
    termList = file.read().splitlines()

NICKNAME = input('Entre com seu nickname:')

def censorText(_textToCensor):
    global currentInfractions 

    for term in termList:
        if(term not in _textToCensor):continue

        currentInfractions += 1
        term_len = len(term)
        line_index_in_text = _textToCensor.index(term)
        
        censoredText = _textToCensor[:line_index_in_text]
        for i in term:
            censoredText += '*'
        
        censoredText += _textToCensor[line_index_in_text + term_len:]
        _textToCensor = censoredText

    return _textToCensor

currentInfractions = 0
while currentInfractions < MAXIMUM_INFRACTIONS:
    print('---=//=---' * 5)
    input_text = input(f'[{NICKNAME}]:')

    if(input_text == 'exit'):
        break
    
    print(censorText(input_text))

print('Você foi banido do chat de texto')


