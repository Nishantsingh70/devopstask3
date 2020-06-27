import os
if(os.system("$(curl -o /dev/null -s -w \"%{http_code}\" 192.168.99.108:31000/*.php)") == "200"): 
    pass
elif(os.system("$(curl -o /dev/null -s -w \"%{http_code}\" 192.168.99.108:31000/*.html)") == "200"):
    pass
else:
    with open("/status" , "w") as f:
         f.write("SEND EMAIL")

