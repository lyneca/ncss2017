import requests
for i in range(0, 60):
    r = requests.get('http://ncss.edu.au/ckeditor_assets/attachments/%s/db2.pdf' % i)
    print(str(i) + ':', r.status_code)
