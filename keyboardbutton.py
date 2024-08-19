from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💻 Computers"),   KeyboardButton(text="📱 Phones")],
        [
            KeyboardButton(text="💁🏻‍♂️ Biz haqimizda"),    KeyboardButton(text="📍 joylashuv")],
        [
            KeyboardButton(text="☎️ admin")]

    ],
    resize_keyboard=True,
    input_field_placeholder="Choise button..."
)
