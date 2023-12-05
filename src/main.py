from machine import Pin, I2C
from time import sleep
import BME280

# Configuração dos pinos para o I2C
sda = machine.Pin(20)
scl = machine.Pin(21)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

while True:
    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature  # Temperatura em Celsius
    pres = bme.pressure     # Pressão

    print('Temperature:', temp, '  Pressure:', pres)
    sleep(4)

