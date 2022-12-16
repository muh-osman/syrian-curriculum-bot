from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from random import randint

bot = Bot(token='5664115796:AAHIfzzVlzqGiiB9ECSj_ajQv2CCA-XQxp8')
dp = Dispatcher(bot)

keyboard0 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("الصف الأول").add("الصف الثاني").add("الصف الثالث").add("الصف الرابع").add("الصف الخامس").add("الصف السادس").add("الصف السابع").add("الصف الثامن").add("الصف التاسع").add("الصف العاشر").add("الصف الحادي عشر").add("بكالوريا")

# كتب الصف الأول
keyboard1 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("العربية لغتي - فصل أول").add("التربية الفنية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("الرياضيات الفصل الأول").add("التربية الموسيقية").add("العلوم الفصل الأول").add("الدراسات الاجتماعية").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الثاني
keyboard2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("العربية لغتي الفصل الاول").add("التربية الفنية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("الرياضيات الفصل الأول").add("التربية الموسيقية").add("العلوم الفصل الأول").add("الدراسات الاجتماعية").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الثالث
keyboard3 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("العربية لغتي الفصل الاول").add("التربية الفنية البصرية والجمالية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("الرياضيات").add("التربية الموسيقية").add("العلوم الفصل الأول").add("الدراسات الاجتماعية").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الرابع
keyboard4 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("التربية الزراعية").add("العربية لغتي فصل أول").add("التربية الفنية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("الرياضيات").add("التربية الموسيقية").add("العلوم فصل أول").add("الدراسات الاجتماعية").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الخامس
keyboard5 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("التربية الزراعية").add("العربية لغتي فصل أول").add("التربية الفنية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("الرياضيات").add("التربية الموسيقية").add("العلوم فصل أول").add("الدراسات الاجتماعية").add("تكنولوجيا المعلومات والاتصالات").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف السادس
keyboard6 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("التربية الزراعية").add("العربية لغتي فصل أول").add("التربية الفنية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("الرياضيات").add("التربية الموسيقية").add("العلوم فصل أول").add("الدراسات الاجتماعية").add("تكنولوجيا المعلومات والاتصالات").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف السابع
keyboard7 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("العربية لغتي فصل أول").add("التربية الفنية").add("علم الأحياء والأرض").add("التربية الدينية المسيحية").add("الجغرافية").add("التاريخ").add("التربية الدينية الاسلامية").add("الرياضيات").add("التربية الموسيقية").add("التربية الوطنية").add("الفيزياء والكيمياء").add("تكنولوجيا المعلومات والاتصالات").add("اللغة الروسية").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("اللغة الفرنسية").add("العودة الى البداية")

# كتب الصف الثامن
keyboard8 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("اللغة العربية").add("الجبر").add("الهندسة").add("التربية الفنية").add("علم الأحياء والأرض").add("التربية الدينية المسيحية").add("الجغرافية").add("التاريخ").add("التربية الدينية الاسلامية").add("التربية الموسيقية").add("التربية الوطنية").add("الفيزياء والكيمياء").add("تكنولوجيا المعلومات والاتصالات").add("اللغة الروسية").add("اللغة الفرنسية كتاب الطالب").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف التاسع
keyboard9 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("الجبر").add("اللغة العربية").add("التربية الفنية").add("علم الأحياء والأرض").add("التربية الدينية المسيحية").add("جغرافية الوطن العربي وسوريا").add("الهندسة").add("التاريخ").add("التربية الدينية الاسلامية").add("التربية الموسيقية").add("التربية الوطنية").add("الفيزياء والكيمياء").add("اللغة الروسية").add("تكنولوجيا المعلومات والاتصالات").add("اللغة الفرنسية كتاب الطالب").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف العاشر
keyboard10 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("الجبر").add("اللغة العربية").add("التربية الفنية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("الهندسة").add("الهندسة2").add("التربية الوطنية").add("تكنولوجيا المعلومات والاتصالات").add("علم الأحياء والبيئة أدبي").add("علم الأحياء والبيئة علمي").add("الكيمياء أدبي").add("الكيمياء علمي").add("الجغرافية أدبي").add("الجغرافية علمي").add("التاريخ أدبي").add("التاريخ علمي").add("الفلسفة أدبي").add("الفلسفة علمي").add("الفيزياء أدبي").add("الفيزياء علمي").add("اللغة الروسية").add("اللغة الفرنسية كتاب الطالب").add("الفرنسي أدبي").add("اللغة الانكليزية كتاب الطالب").add("اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الحادي عشر
keyboard11 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("الفلسفة أدبي").add("الفلسفة علمي").add("اللغة العربية أدبي").add("اللغة العربية علمي").add("الرياضيات أدبي").add("الرياضيات فصل أول علمي").add("الرياضيات فصل ثاني علمي").add("الفيزياء علمي").add("الكيمياء علمي").add("علم الأحياء والأرض علمي").add("الجغرافية أدبي").add("التاريخ أدبي").add("التربية الوطنية").add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("التربية الفنية").add("تكنولوجيا المعلومات والاتصالات").add("اللغة الروسية").add("اللغة الفرنسية كتاب الطالب").add("اللغة الفرنسية كتاب الأنشطة").add("اللغة الانكليزية كتاب الطالب أدبي").add("اللغة الانكليزية كتاب الانشطة أدبي").add("اللغة الانكليزية كتاب الطالب علمي").add("اللغة الانكليزية كتاب الانشطة علمي").add("العودة الى البداية")

# كتب البكالوريا
keyboard12 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("التربية الدينية المسيحية").add("التربية الدينية الاسلامية").add("التربية الوطنية").add("اللغة العربية أدبي").add("الجغرافية أدبي").add("التاريخ أدبي").add("الفلسفة فصل أول").add("الفلسفة فصل ثاني").add("اللغة العربية علمي").add("علم الأحياء علمي").add("الكيمياء علمي").add("الفيزياء علمي").add("الرياضيات فصل أول علمي").add("الرياضيات فصل ثاني علمي").add("اللغة الروسية أدبي").add("اللغة الروسية علمي").add("اللغة الفرنسية كتاب الطالب").add("اللغة الفرنسية كتاب الأنشطة").add("اللغة الانكليزية كتاب الطالب أدبي").add("اللغة الانكليزية كتاب الانشطة أدبي").add("اللغة الانكليزية كتاب الطالب علمي").add("اللغة الانكليزية كتاب الانشطة علمي").add("العودة الى البداية")

# Start Bot


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "مرحبا 👋\n يرجى اختيار الصف", reply_markup=keyboard0)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == "الصف الأول":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard1)
        if message.text == "العربية لغتي - فصل أول":
            await message.answer_document("./image_processing.jpg")
        elif message.text == "التربية الفنية":
            await message.answer_document("PTTW-G1-AB.pdf")







    elif message.text == "الصف الثاني":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard2)

    elif message.text == "الصف الثالث":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard3)

    elif message.text == "الصف الرابع":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard4)

    elif message.text == "الصف الخامس":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard5)

    elif message.text == "الصف السادس":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard6)

    elif message.text == "الصف السابع":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard7)

    elif message.text == "الصف الثامن":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard8)

    elif message.text == "الصف التاسع":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard9)

    elif message.text == "الصف العاشر":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard10)

    elif message.text == "الصف الحادي عشر":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard11)

    elif message.text == "بكالوريا":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard12)





    elif message.text == "العودة الى البداية":
        await bot.send_message(message.from_user.id, "يرجى اختيار الصف", reply_markup=keyboard0)

    else:
        await bot.send_message(message.from_user.id, "يرجى الاختيار من القائمة ⌘")


executor.start_polling(dp)
