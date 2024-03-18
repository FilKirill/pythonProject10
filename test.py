from requests import get, post, delete
from pprint import pprint

pprint(post('http://localhost:5050/api/v2/user', json={
    'surname': 'selcov',
    'name': 'Dima',
    'age': '13',
    'position': 'Lake', 'speciality': 'Fisher', 'address': 'module_192312312459129', 'email': 'bk10@qwe.com',
    'hashed_password': '123'}).json())
pprint(get('http://localhost:5050/api/v2/user').json())  # {'id': 9}
pprint(get('http://localhost:5050/api/v2/user/9').json())
pprint(delete('http://localhost:5050/api/v2/user/9').json())  # {'success': 'OK'}
pprint(get('http://localhost:5050/api/v2/user/9').json())  # {'message': 'User 9 not found'}
