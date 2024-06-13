from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from loader import db


number = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='📞Mening raqamim',request_contact=True)],
        [KeyboardButton(text="⬅️ Ortga")]
    ]
)



payments = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='Naqd pul')],
        [KeyboardButton(text="Click")],
        [KeyboardButton(text="Payme")],
        [KeyboardButton(text="⬅️ Ortga")]
    ]
)



konfirmeyshn = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text ="✅ Tasdiqlash")],
        [KeyboardButton(text ="❌ Bekor qilish")],
    ]
)
