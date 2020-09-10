from pymodbus.client.sync import ModbusTcpClient



#Read Coil Status 1-8
#Read Coil Status 17-8
#Read Input Registers 30001-8
#Write Single Coil 17
#Wrire Mulitple Coils 17-8


client = ModbusTcpClient('192.168.86.200')
#client.write_coil(17, True)
	#ModbusIOException('No Response received from the remote unit/Unable to decode response', 5)
#client.read_input_registers(30001, count=1)
	#ModbusIOException('No Response received from the remote unit/Unable to decode response', 4)
client.read_input_registers(1, count=1)
	#ModbusIOException('No Response received from the remote unit/Unable to decode response', 4)
#result = client.read_coils(1,1)
print(result.bits[0])
client.close()