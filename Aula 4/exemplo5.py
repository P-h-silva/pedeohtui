import time 
from datetime import datetime
while True:
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M:%S")
    print("Hora atual:", hora_atual, end="\r")
    #\r atualiza na mesma linha
    time.sleep(1)
    # sleep espera por 1 segundo.