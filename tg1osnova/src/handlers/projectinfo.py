from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.misc import logger
from src.keyboards.keyboards import menu, registr, back



router = Router()




@router.message(F.text == "🏫 Наш проект")
@logger.catch
async def projectinf(message: Message, state: FSMContext):
    await message.answer('тут что то будет', reply_markup=back)


        
