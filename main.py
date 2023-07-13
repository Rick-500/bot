from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import TOKEN
import requests
from PIL import Image
from aiogram import Bot, Dispatcher, executor, types


from guides import characters

# Создаем экземпляры классов Bot и Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""

    await message.answer(
        "привет! Я геншин гид , и я тебе помогу со сборками на  персонажей и отрядами для бездны. У меня есть такие команды: /start, /characters, /spralabyss",
    )
    ############################################################################################################################################
@dp.message_handler(commands=['spralabyss'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "выберите какой этаж бездны вы хотите /11flor /12flor")

@dp.message_handler(commands=['12flor'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "зал /12z1 /12z2 /12z3")

@dp.message_handler(commands=['12z1'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "половина /12z1p1 /12z1p2")

# \

@dp.message_handler(commands=['12z2'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "половина /12z2p1 /12z2p2")

@dp.message_handler(commands=['12z3'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "половина /12z3p1 /12z3p2")

############################################################################################################################################
@dp.message_handler(commands=['12z1p1'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path = "12a1a1.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "На этом этапе вас ждут: 3 крио попрыгуньи, 3 пиро попрыгуньи и 6 перевозных конструкций. Здесь идеально подйдёт кадзуха, сахароза или венти")

@dp.message_handler(commands=['12z1p2'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="12a1a2.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "на этом этаже вас ждут: 1 крио мааг бездный, 1 гидро маг бкездны а после их появяться 2 крио предвестников бездны и 1 крио предвестник бездны. Здесь хорошо подойдёт пачка с сйно, любой пиро дд и райден националка ")


@dp.message_handler(commands=['12z2p1'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="12a2a1.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "здесь тебя поджидает пернатый плесенник, против него можно взять любык дд, но лучше не брать аль хайтама и тигнари")


@dp.message_handler(commands=['12z2p2'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="12a2a2.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "здесь тебя поджидает монифистация грома, протирв неё хорошо подходит любой пиро дд, тигнари, аль хайтам и его также можно убить с помощью реакции стимуляция(электро по бутанизации)")


@dp.message_handler(commands=['12z3p1'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="12a3a1.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "здесь тебя поджидают 2 священных рогатых крокодила и 2 священный клыкастых зверя,протирв их хорошо подходит любой пиро дд, тигнари, аль хайтам и его также можно убить с помощью реакции стимуляция(электро по бутанизации) ")


@dp.message_handler(commands=['12z3p2'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="12a3a2.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "здесь тебя поджидает чудовищный креститель, возбмите стихии который контят пиро крио гидро")

#############################################################################################################################################
@dp.message_handler(commands=['11flor'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "зал /11z1 /11z2 /11z3")


@dp.message_handler(commands=['11z1'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "половина /11z1p1 /11z1p2")

@dp.message_handler(commands=['11z2'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "половина /11z2p1 /11z2p2")

@dp.message_handler(commands=['11z3'], state="*")
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer(
        "половина /11z3p1 /11z3p2")
#############################################################################################################################################

@dp.message_handler(commands=['11z1p1'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="11a1a1.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "здесь тебе надо будет защищать монолит артерий от многих мелких противников, хорошо подойдёт анемо гг, кадзуха, сахароза и венти, из дд лучше брать сплешь пиро, такие как: янь фей, кли или ху тао")

@dp.message_handler(commands=['11z1p2'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="11a1a2.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "6 целей со средним ХП, идеально подойдёт ёимия или тигнари")

@dp.message_handler(commands=['11z2p1'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path ="11a2a1.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "здесь тебя поджидает электро вестник бездны, хорошо подойдёт ёимия и тигнари")


@dp.message_handler(commands=['11z2p2'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path = "11a2a2.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "6 целей со средним ХП, идеально подойдёт ёимия или тигнари")


@dp.message_handler(commands=['11z3p1'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path = "11a3a1.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "2 цели с высоким показателем, ХП идеально подойдёт ёимия или тигнари")


@dp.message_handler(commands=['11z3p2'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    image_path = "11a3a2.png"
    image = types.InputFile(image_path)
    await message.reply_photo(image)
    await message.answer(
        "здеь тебя поджидают 3 мага бездны: крио, гидро, пиро. После их заспавниться 2 гидро вестника бездны. Хорошо подойдёт кадзуха, нахида, тингари, сахароза")


#############################################################################################################################################
@dp.message_handler(commands=['characters'], state="*")
async def character_info(message: types.Message, state: FSMContext):
    await message.answer("Напиши название персонажа")
    await state.set_state("wait_for_character_name")


characters = {
    'эмбер': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-jember-v-genshin-impact/',
    'кэйа': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-kjeja-v-genshin-impact/',
    'лиза': 'вот гайд на его: https://wotpack.ru/liza-v-genshin-impact-gajd-luchshie-bildy/',
    'беннет': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-benneta-v-genshin-impact/',
    'саю': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-saju-v-genshin-impact/',
    'сайно': 'вот гайд на его: https://wotpack.ru/sajno-v-genshin-impact-luchshij-bild/',
    'сяо': 'вот гайд на его: https://wotpack.ru/gajd-dlja-sjao-v-genshin-impact-luchshie-bildy-prokachka-svjazki/',
    'сара': 'вот гайд на его: https://wotpack.ru/sara-v-genshin-impact-gajd-luchshie-bildy/',
    'райден': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-baal-sjogun-rajdjen-v-genshin-impact/',
    'джинн': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-dzhin-v-genshin-impact/',
    'мона': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-monu-professionalnogo-astrologa/',
    'дилюк': 'вот гайд на его: https://wotpack.ru/genshin-impact-gajd-na-diljuka-bild-vozvyshenie-i-osnovnye-sborki/',
    'ке цин': 'вот гайд на его: https://wotpack.ru/gajd-dlja-kje-cin-v-genshin-impact/',
    'аль хайтам': 'вот гайд на его: https://wotpack.ru/al-hajtam-v-genshin-impact-luchshij-bild/',
    'нилу': 'вот гайд на его: https://wotpack.ru/nilu-v-genshin-impact-luchshij-bild/',
    'нахида': 'вот гайд на его: https://wotpack.ru/nahida-v-genshin-impact-luchshij-bild/',
    'джун ли': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-chzhun-li-vlastelina-kamnja/',
    'венти': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-venti-odnogo-iz-semi-arhontov/',
    'альбедо': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-albedo-genija-i-princa-mela/',
    'аяка': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-ajaki-v-genshin-impact/',
    'аято': 'вот гайд на его: https://wotpack.ru/ajato-v-genshin-impact-luchshij-bild/',
    'бай чжу': 'вот гайд на его: https://wotpack.ru/baj-chzhu-v-genshin-impact-luchshij-bild/',
    'барбара': 'вот гайд на его: https://wotpack.ru/genshin-impact-gajd-na-barbaru-bild-i-luchshie-sborki/',
    'бэй доу': 'вот гайд на его: https://wotpack.ru/genshin-impact-gajd-na-bjej-dou-luchshij-bild/',
    'гань юй': 'вот гайд на его: https://wotpack.ru/gajd-dlja-gan-juj-v-genshin-impact-luchshie-bildy-prokachka-svjazki/',
    'горо': 'вот гайд на его: https://wotpack.ru/goro-v-genshin-impact-luchshij-bild/',
    'диона': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-diony-v-genshin-impact/',
    'дори': 'вот гайд на его: https://wotpack.ru/dori-v-genshin-impact-luchshij-bild/',
    'дехья': 'вот гайд на его: https://wotpack.ru/djehja-v-genshin-impact-luchshij-bild/',
    'е лань': 'вот гайд на его: https://wotpack.ru/e-lan-v-genshin-impact-luchshij-bild/',
    'ёимия': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-jomii-v-genshin-impact/',
    'Итто': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-arataki-itto-v-genshin-impact/',
    'кавех': 'вот гайд на его: https://wotpack.ru/kaveh-v-genshin-impact-luchshij-bild/',
    'кадзуха': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-kazuhi-v-genshin-impact/',
    'кандакия': 'вот гайд на его: https://wotpack.ru/kandakija-v-genshin-impact-luchshij-bild/',
    'кирара': 'вот гайд на его: https://wotpack.ru/kirara-v-genshin-impact-luchshij-bild/',
    'кли': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-kli-v-genshin-impact/',
    'кокоми': 'вот гайд на его: https://wotpack.ru/gajd-dlja-kokomi-v-genshin-impact/',
    'коллеи': 'вот гайд на его: https://wotpack.ru/kollei-v-genshin-impact-luchshij-bild/',
    'лайла': 'вот гайд на его: https://wotpack.ru/lajla-v-genshin-impact-luchshij-bild/',
    'мика': 'вот гайд на его: https://wotpack.ru/mika-v-genshin-impact-luchshij-bild/',
    'нин гуан': 'вот гайд на его: https://wotpack.ru/genshin-impact-luchshij-bild-na-nin-guan/',
    'ноэлль': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-nojell-v-genshin-impact/',
    'розария': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-rozarii-v-genshin-impact/',
    'рейзор': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-rjejzora-v-genshin-impact/',
    'сахароза': 'вот гайд на его: https://wotpack.ru/saharoza-v-genshin-impact-gajd-luchshie-bildy/',
    'синь цю': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-sin-cju-v-genshin-impact/',
    'куки': 'вот гайд на его: https://wotpack.ru/kuki-sinobu-v-genshin-impact-luchshij-bild/',
    'синь янь': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-sin-jan-muzykanta-buntarja/',
    'странник': 'вот гайд на его: https://wotpack.ru/strannik-skaramuchcha-v-genshin-impact-luchshij-bild/',
    'сян лин': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-sjan-lin-izvestnogo-povara-iz-li-juje/',
    'тарталия': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-tartalju-odinnadcatogo-iz-odinnadcati-predvestnikov-fatui/',
    'тигнари': 'вот гайд на его: https://wotpack.ru/tignari-v-genshin-impact-luchshij-bild/',
    'тома': 'вот гайд на его: https://wotpack.ru/toma-v-genshin-impact-gajd-luchshie-bildy/',
    'фарузан': 'вот гайд на его: https://wotpack.ru/faruzan-v-genshin-impact-luchshij-bild/',
    'фишль': 'вот гайд на его: https://wotpack.ru/genshin-impact-bild-na-fishl-tainstvennuju-princessu-osuzhdenija/',
    'ху тао': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-hu-tao-v-genshin-impact/',
    'хейдзо': 'вот гайд на его: https://wotpack.ru/sikanoin-hjejdzo-v-genshin-impact-luchshij-bild/',
    'ци ци': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-ci-ci-v-genshin-impact/',
    'чун юнь': 'вот гайд на его: https://wotpack.ru/genshin-impact-chun-jun-gajd-luchshie-bildy/',
    'шень хэ': 'вот гайд на его: https://wotpack.ru/shjen-hje-v-genshin-impact-luchshij-bild/#i-11',
    'элой': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-jeloj-v-genshin-impact/',
    'эола': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-jeoly-v-genshin-impact/',
    'юнь цзынь': 'вот гайд на его: https://wotpack.ru/jun-czin-v-genshin-impact-luchshij-bild/',
    'янь фей': 'вот гайд на его: https://wotpack.ru/luchshij-bild-dlja-jan-fjej-v-genshin-impact/#i-11',
    'яо яо': 'вот гайд на его: https://wotpack.ru/jao-jao-v-genshin-impact-luchshij-bild/',
    'яэ мико': 'вот гайд на его: https://wotpack.ru/jaje-miko-v-genshin-impact-luchshij-bild/',
}


@dp.message_handler(state="wait_for_character_name")
async def character_info(message: types.Message, state: FSMContext):
    character_name = message.text
    character_name = character_name.lower()
    character_info = get_character_info(character_name)

    if character_info:
        await message.reply(character_info)
        await state.reset_state()
    else:
        await message.reply("нет такого персонажа. Введи ещё раз")


def get_character_info(character_name):
    character_info = characters.get(character_name)

    return character_info


# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
