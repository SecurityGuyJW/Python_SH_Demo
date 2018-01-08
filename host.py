#************************************************************************************
#*									  	    *
#*		Code below show cases host function via SH repository		    *
#*										    *
#*										    *
#************************************************************************************

import sh

#Website being probed must be online
#Inorder to get the output the result must be stored in variable

var = sh.host('google.com')

print(var)


