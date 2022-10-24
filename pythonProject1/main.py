from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uvicorn

from starlette import status
from starlette.responses import Response
from starlette.staticfiles import StaticFiles
#from starlette.templating import Jinja2Templates

#from models.models import BaseModel
from pydantic import BaseModel

app = FastAPI()  # noqa: pylint=invalid-name

table_users = {
    'a': 'bukva A'
    , 'b': 'bukva B'
}

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


@app.get("/", response_class=HTMLResponse)
def home():
    return templ.TemplateResponse('opener.html', {"request": {'a':None, 'b': None}, 'a': 0, 'list_table': list_table})


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


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host="127.0.0.1", reload=True)