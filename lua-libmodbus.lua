-- Lua / lua-libmodbus / libmodbus Testing





mb = require("libmodbus")
print("using libmodbus runtime version: ", mb.version())
print("using lua-libmodbus compiled against libmodbus: ", mb.VERSION_STRING)


-- ********* SET COMMPORT ********* 


local dev=mb.new_rtu ("/dev/ttyUSB0", 9600, "n", 8, 1)
--local dev=mb.new_rtu (device, baud, parity, databits, stopbits)
--device (required)
--baud rate, defaults to 19200
--parity defaults to EVEN
--databits defaults to 8
--stopbits defaults to 1
print(dev:get_byte_timeout())
print(dev:get_response_timeout())
print(dev)

dev:set_debug()
ok, err = dev:connect()
if not ok then error("Couldn't connect: " .. err) end


-- ********* SET SLAVE ********* 


dev:set_slave(2)


-- ********* READ REGISTERS ********* 

--[[
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
--]]



print("*********Context Methods - 32 Bit Float Testing Without Offset*********")

local base_address = 1019
local regs, err
regs, err = dev:read_registers(base_address, 8)
if not regs then error("read failed: " .. err) end
print('read_registers 32bit Float Dec')
for r,v in ipairs(regs) do
	print(string.format("register (offset %d) %d: %d (%#x): %#x (%d)",
		r, r, r + base_address - 1, r + base_address -1, v, v))
end

local base_address = 0x3FB
local regs, err
regs, err = dev:read_registers(base_address, 8)
if not regs then error("read failed: " .. err) end
print('read_registers 32bit Float Hex')
for r,v in ipairs(regs) do
	print(string.format("register (offset %d) %d: %d (%#x): %#x (%d)",
		r, r, r + base_address - 1, r + base_address -1, v, v))
end


local base_address = 1019
local regs, err
regs, err = dev:read_input_registers(base_address, 8)
if not regs then error("read failed: " .. err) end
print('read_input_registers 32bit Float Dec')
for r,v in ipairs(regs) do
	print(string.format("register (offset %d) %d: %d (%#x): %#x (%d)",
		r, r, r + base_address - 1, r + base_address -1, v, v))
end

local base_address = 0x3FB
local regs, err
regs, err = dev:read_input_registers(base_address, 0x3FC)
if not regs then error("read failed: " .. err) end
print('read_input_registers 32bit Float Hex')
for r,v in ipairs(regs) do
	print(string.format("register (offset %d) %d: %d (%#x): %#x (%d)",
		r, r, r + base_address - 1, r + base_address -1, v, v))
end





print("*********Functions - 32 Bit Float Testing Without Offset*********")

local regs, err
regs, err=mb.get_f32(1019,1020)
if not regs then error("read failed: " .. err) end
print(err)
print("get_f32 32bit Float Dec = "..regs)

local regs, err
regs, err=mb.get_f32(0x3FB,0x3FC)
if not regs then error("read failed: " .. err) end
print(err)
print("get_f32 32bit Float Hex = "..regs)

local regs, err
regs, err=mb.get_f32le(1019,1020)
if not regs then error("read failed: " .. err) end
print(err)
print("get_f32le 32bit Float Reverse Dec = "..regs)

local regs, err
regs, err=mb.get_f32le(0x3FB,0x3FC)
if not regs then error("read failed: " .. err) end
print(err)
print("get_f32le 32bit Float Reverse Hex = "..regs)





print("32 Bit Float Testing With Offset")

local regs, err
regs, err=mb.get_f32(1018,1019)
if not regs then error("read failed: " .. err) end
print(err)
print("get_f32 32bit Float Dec = "..regs)

local regs, err
regs, err=mb.get_f32(0x3FA,0x3FB)
if not regs then error("read failed: " .. err) end
print(err)
print("get_f32 32bit Float Hex = "..regs)

local regs, err
regs, err=mb.get_f32le(1018,1019)
if not regs then error("read failed: " .. err) end
print(err)
print("get_f32le 32bit Float Reverse Dec = "..regs)

local regs, err
regs, err=mb.get_f32le(0x3FA,0x3FB)
if not regs then error("read failed: " .. err) end
print(err)
print("3get_f32le 2bit Float Reverse Hex = "..regs)


