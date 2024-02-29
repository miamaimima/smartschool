import serial

# Открываем первый последовательный порт для чтения
serial_port_1 = serial.Serial('COM5', 9600)  # Измените на COM3 или другой нужный порт

# Открываем второй последовательный порт для записи
serial_port_2 = serial.Serial('COM3', 9600)  # Измените на COM4 или другой нужный порт

try:
    while True:
        # Читаем данные из первого порта
        data = serial_port_1.readline()
        
        # Если данные прочитаны
        if data:
            # Отправляем данные второму порту
            serial_port_2.write(data)
            
            # Выводим принятые данные на консоль
            print("Принял:", data)

except KeyboardInterrupt:
    # Закрываем последовательные порты при нажатии Ctrl+C
    serial_port_1.close()
    serial_port_2.close()
    print("Программа завершена.")


