

"""
import re
import subprocess
device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb")
devices = []
for i in df.split('\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
            devices.append(dinfo)
print(devices)


$ lsusb

	Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
	Bus 003 Device 003: ID 0bda:58fe Realtek Semiconductor Corp. Integrated_Webcam_HD
	Bus 003 Device 007: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC
	Bus 003 Device 005: ID 27c6:533c Shenzhen Goodix Technology Co.,Ltd. FingerPrint
	Bus 003 Device 004: ID 8087:0026 Intel Corp. 
	Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
	Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
	Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

$ lsusb -D /dev/bus/usb/003/007

	idVendor           0x0403 Future Technology Devices International, Ltd
	idProduct          0x6001 FT232 Serial (UART) IC
	bEndpointAddress     0x02  EP 2 OUT









$ dmesg | grep tty

[    0.151334] printk: console [tty0] enabled
[    4.441788] dw-apb-uart.2: ttyS4 at MMIO 0x4010002000 (irq = 20, base_baud = 7500000) is a 16550A
[ 6109.460813] usb 3-8: FTDI USB Serial Device converter now attached to ttyUSB0
[ 8476.388355] ftdi_sio ttyUSB0: FTDI USB Serial Device converter now disconnected from ttyUSB0
[ 8498.106169] usb 3-8: FTDI USB Serial Device converter now attached to ttyUSB0

"""

import serial.tools.list_ports
comport=[comport.device for comport in serial.tools.list_ports.comports()]
if comport:
	print(comport)
	print(comport[0])
else:
	print("No Comport Device Found")

from pymodbus.transaction import ModbusRtuFramer
import pymodbus.exceptions

TCP=0
if TCP == 1:
	from pymodbus.client.sync import ModbusTcpClient as ModbusClient
	client = ModbusClient('192.168.11.200', port=502)
	#from pymodbus.client.sync import ModbusTcpClient
	#client = ModbusTcpClient('192.168.11.200', port=502)
	client.connect()
	if client:
		print(client)
		print("Writing/Reading DO ************************************************")
		#This works to read DI if I wrire DO first
		rq = client.write_coil(23,1, unit=1)
		rr = client.read_coils(16, 8, unit=1)
		for i in rr.bits:
	  		print(i)

		print("\nReading DI ************************************************")
		rr = client.read_coils(0, 7, unit=1)
		for i in rr.bits:
	  		print(i)

		print("\nReading AI ************************************************")
		rr = client.read_input_registers(0, 8, unit=1)
		for i in rr.registers:
	  		print(i)
	client.close()






if TCP == 0:
	from pymodbus.client.sync import ModbusSerialClient as ModbusClient
	client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, baudrate=9600)
	client.connect()
	if client:
		print(client)
		print("\nReading AI ************************************************")
		try:
			rr = client.read_input_registers(1214, 1, unit=2)
			#for i in rr.registers:
			#	print(i)
		except pymodbus.exceptions.ConnectionException:
		#except:
   			print("Modbus Error: [Connection] Failed to connect")





		"""
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

	"""Traceback (most recent call last):
  File "/home/mikedismore/Dropbox (Voyant Solutions)/XVS Development/Veo/veo_lua/My_Synchronous_Client_Test.py", line 44, in <module>
    rr = client.read_input_registers(1214, 1, unit=2)
  File "/usr/local/lib/python3.8/dist-packages/pymodbus/client/common.py", line 125, in read_input_registers
    return self.execute(request)
  File "/usr/local/lib/python3.8/dist-packages/pymodbus/client/sync.py", line 107, in execute
    raise ConnectionException("Failed to connect[%s]" % (self.__str__()))
pymodbus.exceptions.ConnectionException: Modbus Error: [Connection] Failed to connect[ModbusSerialClient(rtu baud[9600])]
"""