import string
import re



def robust_login(r, username, password):
	user = r.login(username, password, disable_warning=True)
	return user


def remove_quotes(original_str):
    
    #&gt;
    final_str= original_str
    
    #if not in english 
    if not original_str == filter(lambda x: x in string.printable, original_str):    
        final_str=""
    
    final_str = re.sub('&gt;.*?\n\n','\r\n ',final_str, flags=re.DOTALL)
    
    
    return final_str
