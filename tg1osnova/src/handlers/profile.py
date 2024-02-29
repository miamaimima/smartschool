from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.misc import logger
from src.database1.db_methods import user
from src.keyboards.keyboards import menu, registr, back
import sqlalchemy as db
import time

router = Router()

@router.message(F.text == "👤 Профиль")
@logger.catch
async def get_user_profile(message: Message, state: FSMContext):
    try:
        #await message.answer("Ваш профиль ->", reply_markup=back)

            # Get user ID
        user_id = message.from_user.id

            # Connect to the database
        engine = db.create_engine('sqlite:///new.db')
        connection = engine.connect()

            # Execute query to get user data by ID
        selection_query = user.select().where(user.c.tgid == user_id)
        result = connection.execute(selection_query)

            # Print debug information
        print(f"User ID: {user_id}")

            # Process the result and send it to the user
        for row in result:
            user_id = row[0]
            name = row[1]
            lastname = row[2]
            role = row[3]
            orgid = row[4]
            tgid = row[5]
        time.sleep(0.5)

                # Print debug information
        
                # Send user data to the user
        await message.answer(f"Ваш ID: {user_id}\n"
                                f"Вы: {role}\n"
                                f"Имя: {name}\n"
                                f"Фамилия: {lastname}\n"
                                f"ID карты пропуска: {orgid}\n"
                                f"Телеграмм ID: {tgid}", reply_markup=back)

            # Close the database connection
        connection.close()
    except Exception as e:
        # Print the exception for debugging
        print(f"Exception: {e}")
