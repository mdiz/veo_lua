

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.compat import iteritems
from collections import OrderedDict

import logging
import logging.handlers as Handlers



#https://pymodbus.readthedocs.io/en/latest/source/example/modbus_logging.html
# ----------------------------------------------------------------------- #
# This will simply send everything logged to console
# ----------------------------------------------------------------------- #
#logging.basicConfig()
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)






Serial=2
if Serial == 1:
	from pymodbus.client.sync import ModbusSerialClient as ModbusClient
	client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, baudrate=9600)
	client.connect()
	log.debug(client.state)


	log.debug(client.connect)
	#bound method ModbusSerialClient.connect of <ModbusSerialClient at 0x7fd2e3814eb0 socket=Serial<id=0x7fd2e3814a00, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False), method=rtu, timeout=1


	log.debug("\n\nReading Basic Register List - Floating Point" + "-" * 60 + "\n")
	result = client.read_input_registers(1018, 2, unit=2)
	decoder = BinaryPayloadDecoder.fromRegisters(result.registers,byteorder=Endian.Big,wordorder=Endian.Little)
	myValue=decoder.decode_32bit_float()
	print(myValue)

	"""
	decoded = OrderedDict([
		('32float', decoder.decode_32bit_float()),
		])
	for name, value in iteritems(decoded):
		print(name,value)
	"""

	client.close()


if Serial == 2:
	from pymodbus.client.sync import ModbusSerialClient as ModbusClient
	client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, baudrate=9600)
	client.connect()
	log.debug(client.state)


	log.debug(client.connect)
	#bound method ModbusSerialClient.connect of <ModbusSerialClient at 0x7fd2e3814eb0 socket=Serial<id=0x7fd2e3814a00, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False), method=rtu, timeout=1


	log.debug("\n\nReading Basic Register List - Floating Point" + "-" * 60 + "\n")
	result = client.read_input_registers(103, 2, unit=5)
	decoder = BinaryPayloadDecoder.fromRegisters(result.registers,byteorder=Endian.Big,wordorder=Endian.Little)
	myValue=decoder.decode_32bit_float()
	print(myValue)

	"""
	decoded = OrderedDict([
		('32float', decoder.decode_32bit_float()),
		])
	for name, value in iteritems(decoded):
		print(name,value)
	"""

	client.close()






import serial.tools.list_ports
comport=[comport.device for comport in serial.tools.list_ports.comports()]
if comport:
	#log.debug(comport)
	log.debug(comport[0])
else:
	log.debug("No Comport Device Found")

#from pymodbus.transaction import ModbusRtuFramer
import pymodbus.exceptions


TCP=5
if TCP == 1:
	from pymodbus.client.sync import ModbusTcpClient as ModbusClient
	client = ModbusClient('192.168.11.200', port=502)
	#from pymodbus.client.sync import ModbusTcpClient
	#client = ModbusTcpClient('192.168.11.200', port=502)
	client.connect()
	if client.connect():
		print(client)
		print("Writing/Reading DO " + "-" * 60)
		#This works to read DI if I wrire DO first
		rq = client.write_coil(23,1, unit=1)
		rr = client.read_coils(16, 8, unit=1)
		for i in rr.bits:
	  		print(i)

		print("\nReading DI " + "-" * 60)
		rr = client.read_coils(0, 7, unit=1)
		for i in rr.bits:
	  		print(i)

		print("\nReading AI " + "-" * 60)
		rr = client.read_input_registers(0, 8, unit=1)
		for i in rr.registers:
	  		print(i)
	client.close()

if TCP == 0:
	from pymodbus.client.sync import ModbusSerialClient as ModbusClient
	client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, baudrate=9600)
	client.connect()
	if client.connect():
		print(client)
		try:
			print("\nReading Configuration Registers " + "-" * 60)
			rr = client.read_input_registers(1600, 23, unit=2)
			for i in rr.registers:
				print(i)

			print("\nReading Basic Register List - Integer " + "-" * 60)
			rr = client.read_input_registers(1200, 21, unit=2)
			for i in rr.registers:
				print(i)

			print("\nReading Basic Register List - Floating Point " + "-" * 60)
			rr = client.read_input_registers(1000, 34, unit=2)
			for i in rr.registers:
				print(i)

			print("Writing Configuration Register and Read Back " + "-" * 60)
			#This works to read DI if I wrire DO first
			rq = client.write_register(1602, 800, unit=2)
			rr = client.read_input_registers(1602, 1, unit=2)
			for i in rr.registers:
		  		print(i)

		except pymodbus.exceptions.ConnectionException:
	   		print("Modbus Error: Comport Failed to Connect")


		"""
		https://ctlsys.com/wp-content/uploads/2016/10/WNC-Modbus-Manual-V18c.pdf
		********* READ REGISTERS ********* 

		32 Bit Floating Point Registers
		1019, 1020 VoltA 
		1021, 1022 VoltB 
		1023, 1024 VoltC 
		1025, 1026 VoltAvgLL 

		Integer Registers
		1214 VoltA 
		1215 VoltB 
		1216 VoltC 
		1217 VoltAvgLL 
		"""

	client.close()

"""
decode_32bit_int()

#Decodes a 32 bit signed int from the buffer

decode_32bit_uint()

#Decodes a 32 bit unsigned int from the buffer
"""
