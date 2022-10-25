from fastapi import FastAPI, Cookie, Depends, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
# from sqlalchemy.orm import Session
import uvicorn
from datetime import datetime

from starlette import status
from starlette.responses import Response
from starlette.staticfiles import StaticFiles
#from starlette.templating import Jinja2Templates

#from models.models import BaseModel
from pydantic import BaseModel

from db.db_for_todo import db_get_all_gamers

app = FastAPI()  # noqa: pylint=invalid-name

table_users = {
    'a': 'bukva A'
    , 'b': 'bukva B'
}
print(db_get_all_gamers())
templ = Jinja2Templates(directory='templates')

class Users(BaseModel):
    username: str

list_table = [
     {'name': 'Прополоть огород', 'done': True, 'text': 'Эта задача была изначально(1)'}
   , {'name': 'Вырастить сына', 'done': True, 'text': 'Эта задача была изначально(2)'}
   , {'name': 'Прыгнуть повыше', 'done': False,'text': 'Эта задача была изначально(3)'}
]


def add_to_list_table(name: str, text: str):
    list_table.append({'name': name, 'done': False, 'text': text})


def chenge_doner_list_table(doner: bool, index: int):
    list_table[index]['done'] = doner


@app.get("/all_gamers_list", response_class=PlainTextResponse)
def all_gamers_list():
    retu = db_get_all_gamers()
    return retu


@app.get("/", response_class=HTMLResponse)
def home():
    return templ.TemplateResponse('opener.html', {"request": {'a':None, 'b': None}, 'a': 0, 'list_table': list_table})


@app.get("/registration", response_class=HTMLResponse)
def registration():
    return templ.TemplateResponse('registration.html', {"request": {}})


@app.post("/new_user", response_class=HTMLResponse)
def new_user(response: Response, new_users_name: str = Form(...), password: str = Form(...)):
    response.set_cookie(key="usernamer", value=new_users_name)
    return f'Ваше имя: {new_users_name}, а пароль {password}'+'<br><br><br><a href="/"> Обратно на открывающую страницу</a><br>'


@app.get("/registration_check", response_class=HTMLResponse)
def registration_check(usernamer = Cookie(default='')):
    registration_flg = len(usernamer) > 0
    return templ.TemplateResponse('registration_check.html', {"request": {}, "registration_flg": registration_flg, "usernamer": usernamer})


@app.post("/change_done", response_class=HTMLResponse)
def change_done(doner: str= Form(...)):
    print(doner)
    ll = doner.split('_')
    chenge_doner_list_table(bool(int(ll[0])), int(ll[1])-1)
    return home()


@app.post("/create_item", response_class=HTMLResponse)
def create_item(request: Request, task_name: str = Form(...), texter: str = Form(...)):
    add_to_list_table(task_name, texter)
    return home()


@app.get("/po", response_class=HTMLResponse)
def root():
    return """
        <h1>Тренируем отправку формы</h1>
        <form action="/concat" method="post" class="form-contact">
        <p><label></label><input type="text" name="username" value="" requied />
        <p><input type="submit" value="Otpraviti" />
        </form>
        zavershaushii text
    """


@app.get("/add", response_class=PlainTextResponse)
def add():
    return "Это add"


@app.post("/poster", response_class=PlainTextResponse)
def concat(user: Users):
    return table_users[user.username]


@app.post("/concat", response_class=PlainTextResponse)
def concat(username: str):
    return "это страница /concat" + username


@app.get("/item/{item_id}")
def read_item(item_id: int, q: str = None):
    return item_id+1


@app.get('/alpha')
def alpha(text: str = 'text'):
    result = {'text': text, 'is_alpha' : text.isalpha()}
    return result


DICT = {}
@app.get("/push/{item_id}/{content}")
def push(item_id: int, content: str):
    DICT[item_id] = content
    return DICT


@app.post('/create-user')
def create_user(id: str = 'default1', name: str = 'default2'):
    # код для аутентификации, валидации, обновления базы данных

    data = {'id': id, 'name': name}
    result = {'status_code': '0', 'status_message': 'Success', 'data': data}
    return result


@app.get("/set_cooke")
def root(response: Response):
    now = datetime.now()    # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    response.set_cookie(key="huinya", value='ebanaya')
    return  {"message": "куки установлены"}


@app.get("/read_cooke")
def root(last_visit = Cookie(), huinya = Cookie()):
    return  {"last_visit": last_visit, 'huinya': huinya}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host="127.0.0.1", reload=True)

#"""