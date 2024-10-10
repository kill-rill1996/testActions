from aiogram import Router

router = Router()


# @router.message(Command("add_admin"))
# async def add_admin(message: types.Message, state: FSMContext) -> None:
#     """Добавление админа, начало FSM"""
#     await state.set_state(CreateAdminFSM.contact)
#     msg = await message.answer("Отправьте карточку контакта нового администратора через вкладку 'Прикрепить'",
#                                reply_markup=kb.cancel_keyboard().as_markup())
#     await state.update_data(prev_mess=msg)