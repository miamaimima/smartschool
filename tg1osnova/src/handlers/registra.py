from aiogram import Router, F, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import sqlalchemy as db
from random import randint
import time

from src.misc import logger
from src.database1.db_methods import user, telegram, engine, familyshcool
from src.keyboards.keyboards import menu, registr, ggmenu





router = Router()



async def is_tgid_in_database(orgcode):
    connection = engine.connect()
    selection_query = familyshcool.select().where(familyshcool.c.orgcode == orgcode)
    result = connection.execute(selection_query)
    exists = result.fetchone() is not None
    connection.close()
    return exists

def names(orgcode):
    connection = engine.connect()
    selection_query = familyshcool.select().where(familyshcool.c.orgcode == orgcode)
    result = connection.execute(selection_query)
    row = result.fetchone()
    if row:
        name, lastname, role, uchenikz = row[1], row[2], row[3], row[4]
    return name, lastname, role, uchenikz

@router.callback_query(F.data == "rg")
async def registr(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    await callback.message.answer(f"Введите код организации, ответным сообщением в формате\n"
                                  "Код: <Ваш код>\n"
                                  "Без кавычек!")
    

def parins(role, name1, name2, tgid, usid, uchenikz, orgid):
    connection = engine.connect()
    insertion_query = user.insert().values(
        user_id = usid,
        name = name1,
        lastname = name2,
        role = role,
        tgid = tgid,
        zuchenik = uchenikz,
        orgid = orgid

    )
    connection.execute(insertion_query)
    connection.commit()

def teleg(tgid):
    connection = engine.connect()
    insertion_query = telegram.insert().values(
        tgid = tgid
    )
    connection.execute(insertion_query)
    connection.commit()

@router.message()
async def contregistr(message: Message, state: FSMContext):
    if message.text.startswith("Код: "):
        orgcod = message.text[len("Код: "):]
        user_id = message.from_user.id
        indb = await is_tgid_in_database(orgcod)
        print(orgcod, indb)
        if indb:
            org_id = orgcod
            name1, name2, role, uchenikz = names(orgcod)
            await message.answer("Вы ввели верный код, вернитесь в главное меню, чтобы проверить информацию о себе во вкладке <Профиль>", reply_markup=ggmenu)
            time.sleep(1)
            start, end = 10000000, 100000000
            tgid = user_id
            usid = randint(start, end)
            parins(role, name1, name2, tgid, usid, uchenikz, org_id)
            teleg(tgid)
        else:
            await message.answer("Ваш код неверен, проверьте написание, либо попросите его у учителя", reply_markup=registr)



