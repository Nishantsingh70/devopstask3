import susprocess as sp:
    if(sp.getoutput("curl -o /dev/null -s -w \"%{http_code}\n\" php_code") == "200"): 
        pass
    elif(sp.getoutput("curl -o /dev/null -s -w \"%{http_code}\n\" html_code")== "200"):
        pass
    else:
        with open("/status" , "w") as f:
            f.write("SEND EMAIL")

