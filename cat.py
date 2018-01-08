#************************************************************************************
#*									  	    *
#*		Code below show cases cat function via SH repository		    *
#*										    *
#*										    *
#************************************************************************************


import sh

#the cat function is piped into the var variable.
var = sh.cat('index_000.txt')

#output of the text file is displayed.
print(var)


