import httplib
conn = httplib.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", "/posts/1")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print(data1)
conn.request("GET", "/")
r2 = conn.getresponse()
print r2.status, r2.reason
data2 = r2.read()
conn.close()