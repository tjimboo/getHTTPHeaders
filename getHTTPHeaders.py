"""
Print the HTTP headers for the web site
Requires Request Library
"""
# First import the request library 
import requests

# Get the response codes
url  = input("What web site do you want check?: ")
if url.startswith ('https://'):
    print("")
else:
    url = "https://" + url

r = requests.get(url, verify=True) 

# Print the HTTP headers in instructions
if "strict-transport-security" in r.headers: 
    print("HSTS:",r.headers['strict-transport-security'])
else:
    print("No HSTS header in response") 

if "Content-Security-Policy" in r.headers: 
    print("CSP:",r.headers['Content-Security-Policy'])  
else:
    print("No CSP header in response") 

if "x-xss-protection" in r.headers: 
    print("x-xss-protection:",r.headers['x-xss-protection']) 
else:
    print("No X-XSS header in response") 

if "x-frame-options" in r.headers: 
    print("x-frame-options:",r.headers['x-frame-options'])  
else:
    print("No x-frame-options header in response") 

if "x-content-type-options" in r.headers: 
    print("x-content-type-options:",r.headers['x-content-type-options'])    
else:
    print("No x-content-type-options header in response") 

if "Cache-Control" in r.headers: 
    print("Cache-Control:",r.headers['Cache-Control'])   
else:
    print("No Cache-Control header in response") 

if "expect-ct" in r.headers: 
    print("Expect-CT:",r.headers['expect-ct'])  
else:
    print("No Expect-CT header in response") 

if "referrer-policy" in r.headers: 
    print("referrer-policy:",r.headers['referrer-policy']) 
else:
    print("No referrer-policy header in response")

if "feature-policy" in r.headers: 
    print("feature-policy:",r.headers['feature-policy']) 
else:
    print("No feature-policy header in response") 

# Check done
print("Check on", url + " was successful")
