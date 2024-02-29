from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.misc import logger
from src.database1.db_methods import user
from src.keyboards.keyboards import menu, registr, back
import sqlalchemy as db
from src.Arduino.ardin import temperature


router = Router()





@router.message(F.text == "🔴 Меню школы")
@logger.catch
async def get_user_profile(message: Message, state: FSMContext):
    try:
        rth = temperature()
        temp, hei = rth[0], rth[1]
        await message.answer(f"Главное меню!\n"
                            f"Температура в школе: {temp}C\n"
                            f"Влажность в школе {hei}%")
        
            
    except Exception as e:
        # Print the exception for debugging
        print(f"Exception: {e}")


        
