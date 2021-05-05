from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(commands="start", state="*")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Start\.\.\.",  # Add start message here.
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message_handler(commands="help", state="*")
async def cmd_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Help\.\.\.",  # Add help message here.
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message_handler(commands=["cancel", "stop"], state="*")
@dp.message_handler(Text(equals=["отменить", "отмена"], ignore_case=True), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Action canceled\.", reply_markup=types.ReplyKeyboardRemove())
