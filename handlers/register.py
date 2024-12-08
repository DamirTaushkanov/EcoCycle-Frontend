import requests

from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from .router import router

class RedState(StatesGroup):
    set_username = State()
    set_password = State()

@router.message(StateFilter(None), Command("start"))
async def username(message: Message, state: FSMContext):
    await message.answer(text="username:")
    await state.set_state(RedState.set_username)
@router.message(RedState.set_username)
async def password(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer(text="password:")
    await state.set_state(RedState.set_password)
@router.message(RedState.set_password)
async def create_user(message: Message, state: FSMContext):
    username = (await state.get_data())['username']
    data = {
        "username" : username,
        "password" : message.text
    }
    requests.post('http://127.0.0.1:8000/api/account/register/', data=data)
    await message.answer(text="Success")