# fastcampus - FBS13

- python 3.8.2
- django 3.0.7

```shell
# git clone git@github.com:jeonyh0924/DabangAPI.git <폴더 이름>
# cd <폴더 이름>
pyenv virtualenv 3.8.2 <가상환경 이름>
pyenv local <가상환경 이름>
pip install django

pip install -r requiremens.text
cd app
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser

```


```python
# 유저 토큰 발행 
http://localhost:8000/api/users/token/ 
# username, password

# 유저 토큰 삭제
http://localhost:8000/api/users/token/

# user CRUD path
http://localhost:8000/api/users/

# card CRUD path
http://localhost:8000/api/card/
```











#### django 는 토큰을 아예 안보내면 403에러를 낸다.
