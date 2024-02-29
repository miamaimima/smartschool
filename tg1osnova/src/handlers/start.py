from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import sqlalchemy as db
from random import randint

from src.misc import logger
from src.database1.db_methods import user, telegram, engine, familyshcool
from src.keyboards.keyboards import menu, registr, menuforrod
router = Router()
async def is_tgid_in_database(tgid):
    connection = engine.connect()
    selection_query = telegram.select().where(telegram.c.tgid == tgid)
    result = connection.execute(selection_query)
    exists = result.fetchone() is not None
    connection.close()
    return exists


def zuchenik(tgid):
    connection = engine.connect()
    selection_query = user.select().where(user.c.tgid == tgid)
    result = connection.execute(selection_query)
    row = result.fetchone()
    if row:
        uchenikz = row[7]
    return uchenikz



@router.message(Command('start'), F.text)
@logger.catch
async def start(message: Message):
    user_id = message.from_user.id

# Connect to the datab
    idus = await is_tgid_in_database(user_id)
    print(idus)
    try:
        if idus is not None and idus:
            await message.answer("Вы зарегестрированы")
        else:
            await message.answer(
                text='Приветствуем тебя, дорогой друг, в официальном Телеграмм-боте проекта "Умная школа", для начала работы нужно зарегистрироваться!', 
                reply_markup=registr)
            
            
    except Exception as e:
        print("Error:", e)



@router.message(F.text == "Назад")
@logger.catch
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    uchz = zuchenik(user_id)
    if uchz != 0:
        await message.answer("Главное меню", reply_markup=menuforrod)
    else:
        await message.answer("Главное меню", reply_markup=menu)


@router.message(F.text == "Главное меню")
@logger.catch
async def back(message: Message, state: FSMContext):
    user_id = message.from_user.id
    uchz = zuchenik(user_id)
    if uchz != 0:
        await message.answer("Главное меню", reply_markup=menuforrod)
    else:
        await message.answer("Главное меню", reply_markup=menu)