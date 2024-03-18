from requests import get, post
from pprint import pprint




pprint(post('http://localhost:5050/api/v2/user', json={
    'surname': 'selcov',
     'name': 'Dima',
     'age': '13',
     'position': 'Lake', 'speciality': 'Fisher', 'address': 'module_192312312459129', 'email': 'bk10@qwe.com',
     'hashed_password': '123'}).json())
pprint(get('http://localhost:5050/api/v2/user').json())