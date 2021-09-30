# How to use
```
sendemail(  from_addr   = '', 
            to_addr_list = [''],
            cc_addr_list = [''], 
            subject      = '', 
            message      = '', 
            login        = '', 
            password     = '')
```
* Fill in the relevant details in the above function call in the python script.
* Initially it is configured for gmail, you can add one more argument `smtpserver` and change the server to any other mail servers.
* Then run: `python3 send_email.py`