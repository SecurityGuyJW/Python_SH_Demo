#************************************************************************************
#*									  	    *
#*		Code below show cases find function via SH repository		    *
#*										    *
#*										    *
#************************************************************************************

import sh

#This code is dependent on a personal computer, meaning that it will initially throw an error if ran at its current state, modify the --> some_text_file string.html <-- to whatever file you are trying to find on a linux box. The directory will be piped into the value var, and printed.


var = sh.find('.','-name','some_file.html')

print(var)


