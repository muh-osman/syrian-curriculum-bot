from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from random import randint

bot = Bot(token='5664115796:AAHIfzzVlzqGiiB9ECSj_ajQv2CCA-XQxp8')
dp = Dispatcher(bot)


keyboard0 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("الصف الأول").add("الصف الثاني").add("الصف الثالث").add("الصف الرابع").add("الصف الخامس").add("الصف السادس").add("الصف السابع").add("الصف الثامن").add("الصف التاسع").add("الصف العاشر").add("الصف الحادي عشر").add("بكالوريا")

# كتب الصف الأول
keyboard01 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📖 العربية لغتي - فصل أول").add("📖 التربية الفنية").add("📖 التربية الدينية المسيحية").add("📖 التربية الدينية الاسلامية").add("📖 الرياضيات الفصل الأول").add("📖 التربية الموسيقية").add("📖 العلوم الفصل الأول").add("📖 الدراسات الاجتماعية").add("📖 اللغة الانكليزية كتاب الطالب").add("📖 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الثاني
keyboard02 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📚 العربية لغتي الفصل الاول").add("📚 التربية الفنية").add("📚 التربية الدينية المسيحية").add("📚 التربية الدينية الاسلامية").add("📚 الرياضيات الفصل الأول").add("📚 التربية الموسيقية").add("📚 العلوم الفصل الأول").add("📚 الدراسات الاجتماعية").add("📚 اللغة الانكليزية كتاب الطالب").add("📚 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الثالث
keyboard03 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📒 العربية لغتي الفصل الاول").add("📒 التربية الفنية البصرية والجمالية").add("📒 التربية الدينية المسيحية").add("📒 التربية الدينية الاسلامية").add("📒 الرياضيات").add("📒 التربية الموسيقية").add("📒 العلوم الفصل الأول").add("📒 الدراسات الاجتماعية").add("📒 اللغة الانكليزية كتاب الطالب").add("📒 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الرابع
keyboard04 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📓 التربية الزراعية").add("📓 العربية لغتي فصل أول").add("📓 التربية الفنية").add("📓 التربية الدينية المسيحية").add("📓 التربية الدينية الاسلامية").add("📓 الرياضيات").add("📓 التربية الموسيقية").add("📓 العلوم فصل أول").add("📓 الدراسات الاجتماعية").add("📓 اللغة الانكليزية كتاب الطالب").add("📓 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الخامس
keyboard05 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📔 التربية الزراعية").add("📔 العربية لغتي فصل أول").add("📔 التربية الفنية").add("📔 التربية الدينية المسيحية").add("📔 التربية الدينية الاسلامية").add("📔 الرياضيات").add("📔 التربية الموسيقية").add("📔 العلوم فصل أول").add("📔 الدراسات الاجتماعية").add("📔 تكنولوجيا المعلومات والاتصالات").add("📔 اللغة الانكليزية كتاب الطالب").add("📔 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف السادس
keyboard06 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📕 التربية الزراعية").add("📕 العربية لغتي فصل أول").add("📕 التربية الفنية").add("📕 التربية الدينية المسيحية").add("📕 التربية الدينية الاسلامية").add("📕 الرياضيات").add("📕 التربية الموسيقية").add("📕 العلوم فصل أول").add("📕 الدراسات الاجتماعية").add("📕 تكنولوجيا المعلومات والاتصالات").add("📕 اللغة الانكليزية كتاب الطالب").add("📕 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف السابع
keyboard07 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📗 العربية لغتي فصل أول").add("📗 التربية الفنية").add("📗 علم الأحياء والأرض").add("📗 التربية الدينية المسيحية").add("📗 الجغرافية").add("📗 التاريخ").add("📗 التربية الدينية الاسلامية").add("📗 الرياضيات").add("📗 التربية الموسيقية").add("📗 التربية الوطنية").add("📗 الفيزياء والكيمياء").add("📗 تكنولوجيا المعلومات والاتصالات").add("📗 اللغة الروسية").add("📗 اللغة الانكليزية كتاب الطالب").add("📗 اللغة الانكليزية كتاب الانشطة").add("📗 اللغة الفرنسية").add("العودة الى البداية")

# كتب الصف الثامن
keyboard08 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📘 اللغة العربية").add("📘 الجبر").add("📘 الهندسة").add("📘 التربية الفنية").add("📘 علم الأحياء والأرض").add("📘 التربية الدينية المسيحية").add("📘 الجغرافية").add("📘 التاريخ").add("📘 التربية الدينية الاسلامية").add("📘 التربية الموسيقية").add("📘 التربية الوطنية").add("📘 الفيزياء والكيمياء").add("📘 تكنولوجيا المعلومات والاتصالات").add("📘 اللغة الروسية").add("📘 اللغة الفرنسية كتاب الطالب").add("📘 اللغة الانكليزية كتاب الطالب").add("📘 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف التاسع
keyboard09 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("📙 الجبر").add("📙 اللغة العربية").add("📙 التربية الفنية").add("📙 علم الأحياء والأرض").add("📙 التربية الدينية المسيحية").add("📙 جغرافية الوطن العربي وسوريا").add("📙 الهندسة").add("📙 التاريخ").add("📙 التربية الدينية الاسلامية").add("📙 التربية الموسيقية").add("📙 التربية الوطنية").add("📙 الفيزياء والكيمياء").add("📙 اللغة الروسية").add("📙 تكنولوجيا المعلومات والاتصالات").add("📙 اللغة الفرنسية كتاب الطالب").add("📙 اللغة الانكليزية كتاب الطالب").add("📙 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف العاشر
keyboard10 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("🔖 الجبر").add("🔖 اللغة العربية").add("🔖 التربية الفنية").add("🔖 التربية الدينية المسيحية").add("🔖 التربية الدينية الاسلامية").add("🔖 الهندسة").add("🔖 الهندسة2").add("🔖 التربية الوطنية").add("🔖 تكنولوجيا المعلومات والاتصالات").add("🔖 علم الأحياء والبيئة أدبي").add("🔖 علم الأحياء والبيئة علمي").add("🔖 الكيمياء أدبي").add("🔖 الكيمياء علمي").add("🔖 الجغرافية أدبي").add("🔖 الجغرافية علمي").add("🔖 التاريخ أدبي").add("🔖 التاريخ علمي").add("🔖 الفلسفة أدبي").add("🔖 الفلسفة علمي").add("🔖 الفيزياء أدبي").add("🔖 الفيزياء علمي").add("🔖 اللغة الروسية").add("🔖 اللغة الفرنسية كتاب الطالب").add("🔖 الفرنسي أدبي").add("🔖 اللغة الانكليزية كتاب الطالب").add("🔖 اللغة الانكليزية كتاب الانشطة").add("العودة الى البداية")

# كتب الصف الحادي عشر
keyboard11 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("✏ الفلسفة أدبي").add("✏ الفلسفة علمي").add("✏ اللغة العربية أدبي").add("✏ اللغة العربية علمي").add("✏ الرياضيات أدبي").add("✏ الرياضيات فصل أول علمي").add("✏ الرياضيات فصل ثاني علمي").add("✏ الفيزياء علمي").add("✏ الكيمياء علمي").add("✏ علم الأحياء والأرض علمي").add("✏ الجغرافية أدبي").add("✏ التاريخ أدبي").add("✏ التربية الوطنية").add("✏ التربية الدينية المسيحية").add("✏ التربية الدينية الاسلامية").add("✏ التربية الفنية").add("✏ تكنولوجيا المعلومات والاتصالات").add("✏ اللغة الروسية").add("✏ اللغة الفرنسية كتاب الطالب").add("✏ اللغة الفرنسية كتاب الأنشطة").add("✏ اللغة الانكليزية كتاب الطالب أدبي").add("✏ اللغة الانكليزية كتاب الانشطة أدبي").add("✏ اللغة الانكليزية كتاب الطالب علمي").add("✏ اللغة الانكليزية كتاب الانشطة علمي").add("العودة الى البداية")

# كتب البكالوريا
keyboard12 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("🎓 التربية الدينية المسيحية").add("🎓 التربية الدينية الاسلامية").add("🎓 التربية الوطنية").add("🎓 اللغة العربية أدبي").add("🎓 الجغرافية أدبي").add("🎓 التاريخ أدبي").add("🎓 الفلسفة فصل أول").add("🎓 الفلسفة فصل ثاني").add("🎓 اللغة العربية علمي").add("🎓 علم الأحياء علمي").add("🎓 الكيمياء علمي").add("🎓 الفيزياء علمي").add("🎓 الرياضيات فصل أول علمي").add("🎓 الرياضيات فصل ثاني علمي").add("🎓 اللغة الروسية أدبي").add("🎓 اللغة الروسية علمي").add("🎓 اللغة الفرنسية كتاب الطالب").add("🎓 اللغة الفرنسية كتاب الأنشطة").add("🎓 اللغة الانكليزية كتاب الانشطة أدبي").add("🎓 اللغة الانكليزية كتاب الطالب أدبي").add("🎓 اللغة الانكليزية كتاب الطالب علمي").add("🎓 اللغة الانكليزية كتاب الانشطة علمي").add("العودة الى البداية")


# Start Bot
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await bot.send_message(message.from_user.id, "مرحبا 👋\n يرجى اختيار الصف", reply_markup=keyboard0)


@dp.message_handler()
async def kb_answer(message: types.Message):

    # الصف الأول
    if message.text == "الصف الأول":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard01)

    elif message.text == "📖 العربية لغتي - فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/arabic-1.pdf", reply_markup=keyboard01)

    elif message.text == "📖 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/art.pdf", reply_markup=keyboard01)

    elif message.text == "📖 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/christianity.pdf", reply_markup=keyboard01)

    elif message.text == "📖 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/islamic.pdf", reply_markup=keyboard01)

    elif message.text == "📖 الرياضيات الفصل الأول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/math-1.pdf", reply_markup=keyboard01)

    elif message.text == "📖 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/music.pdf", reply_markup=keyboard01)

    elif message.text == "📖 العلوم الفصل الأول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/science-1.pdf", reply_markup=keyboard01)

    elif message.text == "📖 الدراسات الاجتماعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/social.pdf", reply_markup=keyboard01)

    elif message.text == "📖 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/PTTW-G1-SB.pdf", reply_markup=keyboard01)

    elif message.text == "📖 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/01/PTTW-G1-AB.pdf", reply_markup=keyboard01)


# الصف الثاني
    elif message.text == "الصف الثاني":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard02)

    elif message.text == "📚 العربية لغتي الفصل الاول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/arabic-1.pdf", reply_markup=keyboard02)

    elif message.text == "📚 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/art.pdf", reply_markup=keyboard02)

    elif message.text == "📚 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/christianity.pdf", reply_markup=keyboard02)

    elif message.text == "📚 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/islamic.pdf", reply_markup=keyboard02)

    elif message.text == "📚 الرياضيات الفصل الأول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/math-1.pdf", reply_markup=keyboard02)

    elif message.text == "📚 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/music.pdf", reply_markup=keyboard02)

    elif message.text == "📚 العلوم الفصل الأول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/science-1.pdf", reply_markup=keyboard02)

    elif message.text == "📚 الدراسات الاجتماعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/social.pdf", reply_markup=keyboard02)

    elif message.text == "📚 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/PTTW-G2-SB.pdf", reply_markup=keyboard02)

    elif message.text == "📚 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/02/PTTW-G2-AB.pdf", reply_markup=keyboard02)


# الصف الثالث
    elif message.text == "الصف الثالث":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard03)

    elif message.text == "📒 العربية لغتي الفصل الاول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/arabic-1.pdf", reply_markup=keyboard03)

    elif message.text == "📒 التربية الفنية البصرية والجمالية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/art.pdf", reply_markup=keyboard03)

    elif message.text == "📒 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/christianity.pdf", reply_markup=keyboard03)

    elif message.text == "📒 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/islamic.pdf", reply_markup=keyboard03)

    elif message.text == "📒 الرياضيات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/math.pdf", reply_markup=keyboard03)

    elif message.text == "📒 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/music.pdf", reply_markup=keyboard03)

    elif message.text == "📒 العلوم الفصل الأول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/science-1.pdf", reply_markup=keyboard03)

    elif message.text == "📒 الدراسات الاجتماعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/social.pdf", reply_markup=keyboard03)

    elif message.text == "📒 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/PTTW-G3-SB.pdf", reply_markup=keyboard03)

    elif message.text == "📒 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/03/PTTW-G3-AB.pdf", reply_markup=keyboard03)


# الصف الرابع

    elif message.text == "الصف الرابع":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard04)

    elif message.text == "📓 التربية الزراعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/agriculture.pdf", reply_markup=keyboard04)

    elif message.text == "📓 العربية لغتي فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/arabic-1.pdf", reply_markup=keyboard04)

    elif message.text == "📓 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/art.pdf", reply_markup=keyboard04)

    elif message.text == "📓 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/christianity.pdf", reply_markup=keyboard04)

    elif message.text == "📓 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/islamic.pdf", reply_markup=keyboard04)

    elif message.text == "📓 الرياضيات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/math.pdf", reply_markup=keyboard04)

    elif message.text == "📓 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/music.pdf", reply_markup=keyboard04)

    elif message.text == "📓 العلوم فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/science-1.pdf", reply_markup=keyboard04)

    elif message.text == "📓 الدراسات الاجتماعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/social.pdf", reply_markup=keyboard04)

    elif message.text == "📓 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/EFS-4-SB.pdf", reply_markup=keyboard04)

    elif message.text == "📓 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/04/EFS-4-AB.pdf", reply_markup=keyboard04)


# الصف الخامس
    elif message.text == "الصف الخامس":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard05)

    elif message.text == "📔 التربية الزراعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/agriculture.pdf", reply_markup=keyboard05)

    elif message.text == "📔 العربية لغتي فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/arabic-1.pdf", reply_markup=keyboard05)

    elif message.text == "📔 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/art.pdf", reply_markup=keyboard05)

    elif message.text == "📔 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/christianity.pdf", reply_markup=keyboard05)

    elif message.text == "📔 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/islamic.pdf", reply_markup=keyboard05)

    elif message.text == "📔 الرياضيات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/math.pdf", reply_markup=keyboard05)

    elif message.text == "📔 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/music.pdf", reply_markup=keyboard05)

    elif message.text == "📔 العلوم فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/science-1.pdf", reply_markup=keyboard05)

    elif message.text == "📔 الدراسات الاجتماعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/social.pdf", reply_markup=keyboard05)

    elif message.text == "📔 تكنولوجيا المعلومات والاتصالات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/technology.pdf", reply_markup=keyboard05)

    elif message.text == "📔 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/EFS-5-SB.pdf", reply_markup=keyboard05)

    elif message.text == "📔 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/05/EFS-5-AB.pdf", reply_markup=keyboard05)


# الصف السادس
    elif message.text == "الصف السادس":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard06)

    elif message.text == "📕 التربية الزراعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/agriculture.pdf", reply_markup=keyboard06)

    elif message.text == "📕 العربية لغتي فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/arabic-1.pdf", reply_markup=keyboard06)

    elif message.text == "📕 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/art.pdf", reply_markup=keyboard06)

    elif message.text == "📕 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/Christianity.pdf", reply_markup=keyboard06)

    elif message.text == "📕 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/islamic.pdf", reply_markup=keyboard06)

    elif message.text == "📕 الرياضيات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/math.pdf", reply_markup=keyboard06)

    elif message.text == "📕 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/music.pdf", reply_markup=keyboard06)

    elif message.text == "📕 العلوم فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/science-1.pdf", reply_markup=keyboard06)

    elif message.text == "📕 الدراسات الاجتماعية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/social.pdf", reply_markup=keyboard06)

    elif message.text == "📕 تكنولوجيا المعلومات والاتصالات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/Technology.pdf", reply_markup=keyboard06)

    elif message.text == "📕 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/EFS-6-SB.pdf", reply_markup=keyboard06)

    elif message.text == "📕 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/06/EFS-6-AB.pdf", reply_markup=keyboard06)


# الصف السابع
    elif message.text == "الصف السابع":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard07)

    elif message.text == "📗 العربية لغتي فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Arabic-1.pdf", reply_markup=keyboard07)

    elif message.text == "📗 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Art.pdf", reply_markup=keyboard07)

    elif message.text == "📗 علم الأحياء والأرض":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Biology.pdf", reply_markup=keyboard07)

    elif message.text == "📗 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Christianity.pdf", reply_markup=keyboard07)

    elif message.text == "📗 الجغرافية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Geography.pdf", reply_markup=keyboard07)

    elif message.text == "📗 التاريخ":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/History.pdf", reply_markup=keyboard07)

    elif message.text == "📗 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Islamic.pdf", reply_markup=keyboard07)

    elif message.text == "📗 الرياضيات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Math.pdf", reply_markup=keyboard07)

    elif message.text == "📗 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Music.pdf", reply_markup=keyboard07)

    elif message.text == "📗 التربية الوطنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/National.pdf", reply_markup=keyboard07)

    elif message.text == "📗 الفيزياء والكيمياء":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Physics-Chemistry.pdf", reply_markup=keyboard07)

    elif message.text == "📗 تكنولوجيا المعلومات والاتصالات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Technology.pdf", reply_markup=keyboard07)

    elif message.text == "📗 اللغة الروسية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/Russian.pdf", reply_markup=keyboard07)

    elif message.text == "📗 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/PTTW-G7-SB-21-10-2019.pdf", reply_markup=keyboard07)

    elif message.text == "📗 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/PTTW-G7-AB-21-10-2019.pdf", reply_markup=keyboard07)

    elif message.text == "📗 اللغة الفرنسية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/07/French-SB.pdf", reply_markup=keyboard07)


# الصف الثامن
    elif message.text == "الصف الثامن":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard08)

    elif message.text == "📘 اللغة العربية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Arabic.pdf", reply_markup=keyboard08)

    elif message.text == "📘 الجبر":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Algebra.pdf", reply_markup=keyboard08)

    elif message.text == "📘 الهندسة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Geometry.pdf", reply_markup=keyboard08)

    elif message.text == "📘 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Art.pdf", reply_markup=keyboard08)

    elif message.text == "📘 علم الأحياء والأرض":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Biology.pdf", reply_markup=keyboard08)

    elif message.text == "📘 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Christianity.pdf", reply_markup=keyboard08)

    elif message.text == "📘 الجغرافية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Geography.pdf", reply_markup=keyboard08)

    elif message.text == "📘 التاريخ":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/History.pdf", reply_markup=keyboard08)

    elif message.text == "📘 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Islamic.pdf", reply_markup=keyboard08)

    elif message.text == "📘 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Music.pdf", reply_markup=keyboard08)

    elif message.text == "📘 التربية الوطنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/National.pdf", reply_markup=keyboard08)

    elif message.text == "📘 الفيزياء والكيمياء":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Physics-Chemistry.pdf", reply_markup=keyboard08)

    elif message.text == "📘 تكنولوجيا المعلومات والاتصالات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Technology.pdf", reply_markup=keyboard08)

    elif message.text == "📘 اللغة الروسية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/Russian.pdf", reply_markup=keyboard08)

    elif message.text == "📘 اللغة الفرنسية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/French-SB.pdf", reply_markup=keyboard08)

    elif message.text == "📘 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/PTTW-G8-SB-21-10-2019.pdf", reply_markup=keyboard08)

    elif message.text == "📘 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/08/PTTW-G8-AB-21-10-19.pdf", reply_markup=keyboard08)


# الصف التاسع
    elif message.text == "الصف التاسع":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard09)

    elif message.text == "📙 الجبر":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Algebra.pdf", reply_markup=keyboard09)

    elif message.text == "📙 اللغة العربية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Arabic.pdf", reply_markup=keyboard09)

    elif message.text == "📙 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Art.pdf", reply_markup=keyboard09)

    elif message.text == "📙 علم الأحياء والأرض":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Biology.pdf", reply_markup=keyboard09)

    elif message.text == "📙 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Christianity.pdf", reply_markup=keyboard09)

    elif message.text == "📙 جغرافية الوطن العربي وسوريا":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Geography.pdf", reply_markup=keyboard09)

    elif message.text == "📙 الهندسة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Geometry.pdf", reply_markup=keyboard09)

    elif message.text == "📙 التاريخ":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/History.pdf", reply_markup=keyboard09)

    elif message.text == "📙 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Islamic.pdf", reply_markup=keyboard09)

    elif message.text == "📙 التربية الموسيقية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Music.pdf", reply_markup=keyboard09)

    elif message.text == "📙 التربية الوطنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/National.pdf", reply_markup=keyboard09)

    elif message.text == "📙 الفيزياء والكيمياء":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Physics-Chemistry.pdf", reply_markup=keyboard09)

    elif message.text == "📙 اللغة الروسية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Russian.pdf", reply_markup=keyboard09)

    elif message.text == "📙 تكنولوجيا المعلومات والاتصالات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/Technology.pdf", reply_markup=keyboard09)

    elif message.text == "📙 اللغة الفرنسية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/French-SB.pdf", reply_markup=keyboard09)

    elif message.text == "📙 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/EFS-9-SB.pdf", reply_markup=keyboard09)

    elif message.text == "📙 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/09/EFS-9-AB.pdf", reply_markup=keyboard09)


# الصف العاشر
    elif message.text == "الصف العاشر":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard10)

    elif message.text == "🔖 الجبر":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Algebra.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 اللغة العربية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Arabic.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Art.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Christianity.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Islamic.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الهندسة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Geometry.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الهندسة2":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Geometry2.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 التربية الوطنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/National.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 تكنولوجيا المعلومات والاتصالات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Technology.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 علم الأحياء والبيئة أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Lit-Biology.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 علم الأحياء والبيئة علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Sci-Biology.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الكيمياء أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Lit-Chemistry.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الكيمياء علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Sci-Chemistry.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الجغرافية أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Lit-Geography.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الجغرافية علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Sci-Geography.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 التاريخ أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Lit-History.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 التاريخ علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Sci-History.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الفلسفة أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Lit-Philosophy.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الفلسفة علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Sci-philosophy.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الفيزياء أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Lit-Physics.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الفيزياء علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Sci-Physics.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 اللغة الروسية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/Russian.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 اللغة الفرنسية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/French-SB.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 الفرنسي أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/French-lit.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 اللغة الانكليزية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/EFS-10-SB.pdf", reply_markup=keyboard10)

    elif message.text == "🔖 اللغة الانكليزية كتاب الانشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/10/EFS-10-AB.pdf", reply_markup=keyboard10)


# الصف الحادي عشر
    elif message.text == "الصف الحادي عشر":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard11)

    elif message.text == "✏ الفلسفة أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Lit-Philosophy.pdf", reply_markup=keyboard11)

    elif message.text == "✏ الفلسفة علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Sci-philosophy.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة العربية أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Lit-Arabic.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة العربية علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Sci-Arabic.pdf", reply_markup=keyboard11)

    elif message.text == "✏ الرياضيات أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Lit-math.pdf", reply_markup=keyboard11)

    elif message.text == "✏ الرياضيات فصل أول علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Sci-math1.pdf", reply_markup=keyboard11)

    elif message.text == "✏ الرياضيات فصل ثاني علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Sci-math2.pdf", reply_markup=keyboard11)

    elif message.text == "✏ الفيزياء علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Sci-Physics.pdf", reply_markup=keyboard11)

    elif message.text == "✏ الكيمياء علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Sci-Chemistry.pdf", reply_markup=keyboard11)

    elif message.text == "✏ علم الأحياء والأرض علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Sci-Biology.pdf", reply_markup=keyboard11)

    elif message.text == "✏ الجغرافية أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Lit-Geography.pdf", reply_markup=keyboard11)

    elif message.text == "✏ التاريخ أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Lit-History.pdf", reply_markup=keyboard11)

    elif message.text == "✏ التربية الوطنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/National.pdf", reply_markup=keyboard11)

    elif message.text == "✏ التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Christianity.pdf", reply_markup=keyboard11)

    elif message.text == "✏ التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Islamic.pdf", reply_markup=keyboard11)

    elif message.text == "✏ التربية الفنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/art.pdf", reply_markup=keyboard11)

    elif message.text == "✏ تكنولوجيا المعلومات والاتصالات":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Technology.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة الروسية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/Russian.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة الفرنسية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/French-SB.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة الفرنسية كتاب الأنشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/French-WB.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة الانكليزية كتاب الطالب أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/E-G11-Lit-SB.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة الانكليزية كتاب الانشطة أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/E-G11-Lit-SB.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة الانكليزية كتاب الطالب علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/E-G11-Scientific-SB.pdf", reply_markup=keyboard11)

    elif message.text == "✏ اللغة الانكليزية كتاب الانشطة علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/11/E-G11-Scientific-AB.pdf", reply_markup=keyboard11)


# بكالوريا
    elif message.text == "بكالوريا":
        await bot.send_message(message.from_user.id, "يرجى اختيار كتاب ⌘", reply_markup=keyboard12)

    elif message.text == "🎓 التربية الدينية المسيحية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Christianity.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 التربية الدينية الاسلامية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Islamic.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 التربية الوطنية":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/National.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة العربية أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Lit-Arabic.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 الجغرافية أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Lit-Geography.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 التاريخ أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Lit-History.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 الفلسفة فصل أول":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Lit-Philosophy-1.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 الفلسفة فصل ثاني":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Lit-Philosophy-2.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة العربية علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Sci-Arabic.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 علم الأحياء علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Sci-Biology.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 الكيمياء علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Sci-Chemistry.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 الفيزياء علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Sci-Physics.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 الرياضيات فصل أول علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Sci-Math-1.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 الرياضيات فصل ثاني علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Sci-Math-2.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الروسية أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Lit-Russian.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الروسية علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/Sci-Russian.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الفرنسية كتاب الطالب":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/French-SB.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الفرنسية كتاب الأنشطة":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/French-WB.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الانكليزية كتاب الانشطة أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/E-G12-Lit-AB.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الانكليزية كتاب الطالب أدبي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/E-G12-Lit-SB.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الانكليزية كتاب الطالب علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/E-G12-Scientific-SB.pdf", reply_markup=keyboard12)

    elif message.text == "🎓 اللغة الانكليزية كتاب الانشطة علمي":
        await bot.send_message(message.from_user.id, "http://moed.gov.sy/curricula-new/12/E-G12-Scientific-AB.pdf", reply_markup=keyboard12)


# العودة الى البداية
    elif message.text == "العودة الى البداية":
        await bot.send_message(message.from_user.id, "يرجى اختيار الصف", reply_markup=keyboard0)

    else:
        await bot.send_message(message.from_user.id, "يرجى الاختيار من القائمة ⌘")


executor.start_polling(dp)
