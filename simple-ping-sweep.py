import sh

print "Scanning..."

for i in range(201,255):
	address = "192.168.15." + str(i)

	try: 

		sh.ping(address, "-c 1", _out="/dev/null")
		print "ping tp", address, "OK"
	except sh.ErrorReturnCode_1:
		print "no response from", address
