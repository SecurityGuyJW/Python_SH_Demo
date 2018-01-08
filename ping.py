import sh
#************************************************************************************
#*									  	    *
#*		Code below show cases ping function via SH repository		    *
#*										    *
#*										    *
#************************************************************************************

import sh

ip = "8.8.8.8"

#ping google DNS server with 5 echos, output is not automatically displayed
#we have to store it in a variable

var = sh.ping('-c','5',ip)

print(var)
