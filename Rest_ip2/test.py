from requests import get

print(get('http://localhost:5001/api/jobs').json())
