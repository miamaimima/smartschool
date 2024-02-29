import serial
import time
import sys
sys.path.append(r"C:\Users\mai\Documents\proejctschool\tg1osnova\src\database1")
from db_methods import user, familyshcool, engine
ser = serial.Serial('COM3', 9600)
def inschoolrebenok():
 


    try:
        data = ser.readline().decode().strip()
        returneddata = data.split(" ")
        return returneddata
    except KeyboardInterrupt:
        ser.close()





def update_database(card_id, new_value):
    connection = engine.connect()
    update_query = user.update().where(user.c.idcard == card_id).values(
        inshcool = new_value
    )
    connection.execute(update_query)
    connection.commit()

while True:
    data = inschoolrebenok()
    print(data)
    if data[0] == 'door1':
        idcard = data[1] + data[2] + data[3] + data[4]
        updatedata = int(data[5][5:])
        update_database(idcard, updatedata)
    #update_database(card_id, new_value)
    time.sleep(3)


