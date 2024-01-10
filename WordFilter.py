# Filtro de p***ria no chat

PATH = 'palavras.txt'
ENCODING = 'utf-8'
MAXIMUM_INFRACTIONS = 10

with open(PATH,'r', encoding=ENCODING) as file:
    termList = file.read().splitlines()

NICKNAME = input('Entre com seu nickname:')

def censorText(_textToCensor):
    global current_infractions 
    casefold_text = _textToCensor.casefold()
    
    for term in termList:
        if(term not in casefold_text):continue

        current_infractions += 1
        term_len = len(term)
        line_index_in_text = casefold_text.index(term)
        
        censored_text = _textToCensor[:line_index_in_text]
        for i in term:
            censored_text += '*'
        
        censored_text += _textToCensor[line_index_in_text + term_len:]
        _textToCensor = censored_text

    return _textToCensor

current_infractions = 0
while current_infractions < MAXIMUM_INFRACTIONS:
    print('---=//=---' * 5)
    input_text = input(f'[{NICKNAME}]:')

    if(input_text == 'exit'):
        break
    
    print(censorText(input_text))

print('Você foi banido do chat de texto')


