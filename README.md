
Demo of common linux commands performed through python.


1. My favorite way to use linux command in python via the SH repository, you need to pip install SH.

 
2. Calling objects from this repository are done in sh.cat, sh.cut format.


3. Parametters accepted must be in the same order as you would in a linux shell.


   a. find . -name "SOME_FILE.TXT"  Translates to sh.find('.','-name',' SOME_FILE.TXT')
   
   b. cut -d '-' f 3                Translates to sh.cut('-d','-',f3, SOME_FILE.TXT)
   
   c. wget google.com               Translates to sh.wget("google.com")
   
   d. host google.com               Translates t0 sh.host("google.com")
   
   
   
4. All files to be manipulated must exist in the system, and the directory must be exact.


5. I like taking the piped output and storing it into variable for more robust manipulation

  
   a. var = sh.find('.','-name',' SOME_FILE.TXT')
   
   b. var = sh.cut('-d','-',f3, SOME_FILE.TXT)
   
   c. var = sh.wget("google.com")
   
   d. var = sh.host("google.com")
