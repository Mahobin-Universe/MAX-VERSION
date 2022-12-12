import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')

        os.system('xdg-open https://www.facebook.com/profile.php?id=100084560436367')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from max import check_my_key
 
        check_my_key()
 
 
 
elif bit == "32bit":
 
        from max import check_my_key
 
 
        check_my_key()