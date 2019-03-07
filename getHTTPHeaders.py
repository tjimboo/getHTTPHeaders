"""
Print the HTTP headers for a web site

"""
# First import the request library 
import requests

# Get the response codes
url  = input("What web site do you want check?: ")
r = requests.get(url, verify=True) 

# Print the HTTP headers in instructions
if "strict-transport-security" in r.headers: 
    print("HSTS:",r.headers['strict-transport-security'])
else:
    print("No HSTS header in repsonse") 

if "Content-Security-Policy" in r.headers: 
    print("CSP:",r.headers['Content-Security-Policy'])  
else:
    print("No CSP header in repsonse") 

if "x-xss-protection" in r.headers: 
    print("x-xss-protection:",r.headers['x-xss-protection']) 
else:
    print("No X-XSS header in repsonse") 

if "x-frame-options" in r.headers: 
    print("x-frame-options:",r.headers['x-frame-options'])  
else:
    print("No x-frame-options header in repsonse") 

if "x-content-type-options" in r.headers: 
    print("x-content-type-options:",r.headers['x-content-type-options'])    
else:
    print("No x-content-type-options header in repsonse") 

if "Cache-Control" in r.headers: 
    print("Cache-Control:",r.headers['Cache-Control'])   
else:
    print("No Cache-Control header in repsonse") 

if "expect-ct" in r.headers: 
    print("Expect-CT:",r.headers['expect-ct'])  
else:
    print("No Expect-CT header in repsonse") 

if "referrer-policy" in r.headers: 
    print("referrer-policy:",r.headers['referrer-policy']) 
else:
    print("No referrer-policy header in repsonse")

if "feature-policy" in r.headers: 
    print("feature-policy:",r.headers['feature-policy']) 
else:
    print("No feature-policy header in repsonse") 

# Check done
print("Check on", url + " was successful")