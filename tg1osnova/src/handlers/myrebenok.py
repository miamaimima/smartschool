from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.misc import logger
from src.database1.db_methods import user, familyshcool
import sqlalchemy as db
import time


router = Router()

@router.message(F.text == "🐙 Мой ребенок")
@logger.catch
async def myrebenok(message: Message, state: FSMContext):
    print(123121312)
    #await message.answer("Ваш профиль ->", reply_markup=back)
        # Get user ID
    user_id = message.from_user.id
    name = None
    lastname = None
    insch = None

        # Connect to the database
    engine = db.create_engine('sqlite:///new.db')
    connection = engine.connect()

            # Execute query to get user data by ID
    selection_query = user.select().where(user.c.tgid == user_id)
    result = connection.execute(selection_query)
    for row in result:
        resone = row[4]
        print(row)
    print(resone)
    selquery_two = familyshcool.select().where(familyshcool.c.orgcode == resone)
    result2 = connection.execute(selquery_two)
    for row2 in result2:
        restwo = row2[4]
        print(row2)
    print(restwo)
    selquery_three = familyshcool.select().where(familyshcool.c.orgcode == restwo)
    result3 = connection.execute(selquery_three)
    for row3 in result3:
        name, lastname = row3[1], row3[2]
        print(row3, name, lastname)
    selinsch = user.select().where(user.c.orgid == restwo)
    result4 = connection.execute(selinsch)
    for row4 in result4:
        insch = row4[6]
        print(row3, insch)


    insch2: str
    if insch % 2 == 1:
        insch2 = 'в школе'
    if insch % 2 == 0:
        insch2 = 'не в школе' 
    await message.answer(f'{name} {lastname}\nНа данный момент {insch2}')
        
    time.sleep(0.5)


            # Close the database connection
    connection.close()
