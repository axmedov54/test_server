import asyncio
import os
import json

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from buttons import *
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy="http://proxy.server:3128")
TOKEN = "8971908237:AAHliNvjidGxoVBU5p2PgE01wnpIgoWwRFg"
bot = Bot(token=TOKEN)

dp = Dispatcher()

BUYURTMALAR_FAYLI = "buyurtmalar.json"
SAVATCHA_FAYLI = "savatcha.json"

    
def buyurtmalarni_yuklash():
    if os.path.exists(BUYURTMALAR_FAYLI):
        try:
            with open(BUYURTMALAR_FAYLI, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def buyurtmalarni_saqlash():
    with open(BUYURTMALAR_FAYLI, "w", encoding="utf-8") as file:
        json.dump(buyurtmalar, file, ensure_ascii=False, indent=4)


buyurtmalar = buyurtmalarni_yuklash()


def savatchani_yuklash():
    """Savatchalarni JSON faylidan yuklaydi."""
    if os.path.exists(SAVATCHA_FAYLI):
        try:
            with open(SAVATCHA_FAYLI, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def savatchani_saqlash():
    with open(SAVATCHA_FAYLI, "w", encoding="utf-8") as file:
        json.dump(savatcha, file, ensure_ascii=False, indent=4)


savatcha = savatchani_yuklash()

taomlar = {
    'osh': {"nomi": 'Osh', "narxi": 45000},
    'manti_uzb': {"nomi": 'Manti', "narxi": 55000},
    'lagmon': {"nomi": "Lag'mon", "narxi": 55000},
    'shorva': {"nomi": "Sho'rva", "narxi": 45000},
    'kabob': {"nomi": 'Kabob', "narxi": 35000},
    'chuchvara': {"nomi": 'Chuchvara', "narxi": 45000},
    'dimlama': {"nomi": 'Dimlama', "narxi": 50000},
    'qozon_kabob': {"nomi": 'Qozon Kabob', "narxi": 68000},
    'somsa': {"nomi": 'Somsa', "narxi": 15000},
    'achichuk': {"nomi": 'Achichuk salat', "narxi": 22000},
    'sushi': {"nomi": 'Sushi', "narxi": 60000},
    'ramen': {"nomi": 'Ramen', "narxi": 65000},
    'onigiri': {"nomi": 'Onigiri', "narxi": 30000},
    'gyoza': {"nomi": 'Gyoza', "narxi": 45000},
    'yakitori': {"nomi": 'Yakitori', "narxi": 45000},
    'bento': {"nomi": 'Bento', "narxi": 75000},
    'katsu_curry': {"nomi": 'Katsu Curry', "narxi": 75000},
    'teriyaki': {"nomi": 'Teriyaki', "narxi": 70000},
    'miso_soup': {"nomi": 'Miso Soup', "narxi": 35000},
    'tempura': {"nomi": 'Tempura', "narxi": 65000},
    'bibimbap': {"nomi": 'Bibimbap', "narxi": 90000},
    'japchae': {"nomi": 'Japchae', "narxi": 85000},
    'fried_chicken_kor': {"nomi": 'Koreyscha qovurilgan tovuq', "narxi": 85000},
    'tteokbokki': {"nomi": 'Tteokbokki', "narxi": 65000},
    'kimchi_jjigae': {"nomi": 'Kimchi Jjigae', "narxi": 70000},
    'bulgogi': {"nomi": 'Bulgogi', "narxi": 95000},
    'samgyeopsal': {"nomi": 'Samgyeopsal', "narxi": 115000},
    'mandu': {"nomi": 'Mandu', "narxi": 45000},
    'naengmyeon': {"nomi": 'Naegmyeon', "narxi": 65000},
    'kimchi': {"nomi": 'Kimchi', "narxi": 25000},
    'doner': {"nomi": 'Doner', "narxi": 55000},
    'kebab': {"nomi": 'Kebab', "narxi": 85000},
    'lahmacun': {"nomi": 'Lahmacun', "narxi": 45000},
    'pide': {"nomi": 'Pide', "narxi": 65000},
    'manti_turk': {"nomi": 'Manti Turk', "narxi": 65000},
    'mercimek_corbasi': {"nomi": 'Mercimek corbasi', "narxi": 40000},
    'menemen': {"nomi": 'Menemen', "narxi": 45000},
    'kofte': {"nomi": 'Kofte', "narxi": 70000},
    'gozleme': {"nomi": 'Gozleme', "narxi": 50000},
    'imam_bayildi': {"nomi": 'Imam bayildi', "narxi": 55000},
    'margherita_pizza': {"nomi": 'Margherita Pizza', "narxi": 60000},
    'spaghetti_carbonara': {"nomi": 'Spaghetti Carbonara', "narxi": 85000},
    'lasagna': {"nomi": 'Lasagna', "narxi": 105000},
    'fettuccine_alfredo': {"nomi": 'Fettuccine Alfredo', "narxi": 85000},
    'pepperoni_pizza': {"nomi": 'Pepperoni Pizza', "narxi": 65000},
    'spaghetti_bolognese': {"nomi": 'Spaghetti Bolognese', "narxi": 90000},
    'risotto': {"nomi": 'Risotto', "narxi": 90000},
    'ravioli': {"nomi": 'Ravioli', "narxi": 95000},
    'bruschetta': {"nomi": 'Bruschetta', "narxi": 40000},
    'caprese_salad': {"nomi": 'Caprese salat', "narxi": 60000},
    'cheeseburger': {"nomi": 'Cheeseburger', "narxi": 30000},
    'hamburger': {"nomi": 'Hamburger', "narxi": 28000},
    'fried_chicken_ff': {"nomi": 'Qovurilgan tovuq', "narxi": 42000},
    'french_fries': {"nomi": 'Kartoshka fri', "narxi": 19000},
    'hot_dog': {"nomi": 'Hot-dog', "narxi": 25000},
    'tacos': {"nomi": 'Tacos', "narxi": 50000},
    'sandwich': {"nomi": 'Sandwich', "narxi": 40000},
    'pizza': {"nomi": 'Pizza', "narxi": 60000},
    'burrito': {"nomi": 'Burrito', "narxi": 55000},
    'chicken_nuggets': {"nomi": 'Chicken nuggets', "narxi": 25000},
}

@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.answer(
        "Salom! Taom turini tanlang",
        reply_markup=menu
    )

@dp.callback_query(F.data == "boshmenyu")
async def bosh_menyu(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "Bosh menyu",
        reply_markup=menu
    )

def buyurtma_taom_idni_topish(buyurtma):
    """Yangi va eski formatdagi buyurtmadan taom ID sini topadi."""
    taom_id = buyurtma.get("id")
    if taom_id in taomlar:
        return taom_id

    # Oldingi buyurtmalarda ID saqlanmagan bo'lishi mumkin.
    for id, taom in taomlar.items():
        if (
            taom["nomi"] == buyurtma.get("nomi")
            and taom["narxi"] == buyurtma.get("narxi")
        ):
            return id

    return None


def buyurtmalar_matni_va_tugmalari(foydalanuvchi_id):
    foydalanuvchi_buyurtmalari = buyurtmalar.get(foydalanuvchi_id, [])

    if not foydalanuvchi_buyurtmalari:
        return (
            "📭 Sizda hali tasdiqlangan buyurtmalar yo'q.",
            InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="🛒 Savatcha", callback_data="savatcha")],
                    [InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")]
                ]
            ),
        )

    hisob = {}
    jami = 0

    for buyurtma in foydalanuvchi_buyurtmalari:
        nomi = buyurtma["nomi"]
        narxi = buyurtma["narxi"]
        soni = max(1, int(buyurtma.get("soni", 1)))
        taom_id = buyurtma_taom_idni_topish(buyurtma)
        kalit = taom_id if taom_id else f"{nomi}_{narxi}"

        if kalit not in hisob:
            hisob[kalit] = {"nomi": nomi, "narxi": narxi, "soni": 0, "id": taom_id}

        hisob[kalit]["soni"] += soni
        jami += narxi * soni

    matn = "📦 Sizning tasdiqlangan buyurtmalaringiz:\n\n"
    tugmalar = []

    for kalit, malumot in hisob.items():
        nomi = malumot["nomi"]
        narxi = malumot["narxi"]
        soni = malumot["soni"]
        matn += f"🍽 {nomi} × {soni} — {narxi * soni:,} so'm\n"

        if malumot["id"]:
            tugmalar.append([
                InlineKeyboardButton(
                    text=f"❌ {nomi} × {soni} ni bekor qilish",
                    callback_data=f"cancel_{malumot['id']}"
                )
            ])

    matn += f"\n💰 Jami: {jami:,} so'm"

    tugmalar.append([
        InlineKeyboardButton(
            text="🗑 Barcha buyurtmalarni bekor qilish",
            callback_data="cancel_all"
        )
    ])
    tugmalar.append([
        InlineKeyboardButton(text="🛒 Savatcha", callback_data="savatcha")
    ])
    tugmalar.append([
        InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
    ])

    return matn, InlineKeyboardMarkup(inline_keyboard=tugmalar)


def savatcha_matni_va_tugmalari(foydalanuvchi_id):
    foydalanuvchi_savatchasi = savatcha.get(foydalanuvchi_id, {})

    # Faqat mavjud taom IDlari va musbat sonlarni qoldiramiz.
    foydalanuvchi_savatchasi = {
        taom_id: int(soni)
        for taom_id, soni in foydalanuvchi_savatchasi.items()
        if taom_id in taomlar and str(soni).isdigit() and int(soni) > 0
    }
    savatcha[foydalanuvchi_id] = foydalanuvchi_savatchasi

    if not foydalanuvchi_savatchasi:
        return (
            "🛒 Savatchangiz hozircha bo'sh.\nTaom tanlab, savatchaga qo'shing.",
            InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")]
                ]
            ),
        )

    matn = "🛒 Savatchangiz:\n\n"
    jami = 0
    tugmalar = []

    for taom_id, soni in foydalanuvchi_savatchasi.items():
        taom = taomlar[taom_id]
        summa = taom["narxi"] * soni
        jami += summa
        matn += f"🍽 {taom['nomi']} × {soni} — {summa:,} so'm\n"

        tugmalar.append([
            InlineKeyboardButton(text="➖", callback_data=f"cart_minus_{taom_id}"),
            InlineKeyboardButton(text=f"{soni} ta", callback_data="cart_noop"),
            InlineKeyboardButton(text="➕", callback_data=f"cart_plus_{taom_id}"),
        ])
        tugmalar.append([
            InlineKeyboardButton(
                text=f"🗑 {taom['nomi']}ni olib tashlash",
                callback_data=f"cart_remove_{taom_id}"
            )
        ])

    matn += f"\n💰 Umumiy summa: {jami:,} so'm"

    tugmalar.append([
        InlineKeyboardButton(text="✅ Buyurtmani tasdiqlash", callback_data="cart_confirm")
    ])
    tugmalar.append([
        InlineKeyboardButton(text="🧹 Savatchani bo'shatish", callback_data="cart_clear")
    ])
    tugmalar.append([
        InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
    ])

    return matn, InlineKeyboardMarkup(inline_keyboard=tugmalar)


def savatchani_korsatish(foydalanuvchi_id):
    matn, klaviatura = savatcha_matni_va_tugmalari(foydalanuvchi_id)
    return matn, klaviatura


@dp.callback_query(F.data.startswith("cart_add_"))
async def cart_add_handler(callback_query: CallbackQuery):
    taom_id = callback_query.data.replace("cart_add_", "", 1)
    await savatchaga_qoshish(callback_query, taom_id)


# Old food messages with buy_ callback_data also add the item to the cart.
@dp.callback_query(F.data.startswith("buy_"))
async def old_buy_button_handler(callback_query: CallbackQuery):
    taom_id = callback_query.data.replace("buy_", "", 1)
    await savatchaga_qoshish(callback_query, taom_id)


async def savatchaga_qoshish(callback_query: CallbackQuery, taom_id: str):
    taom = taomlar.get(taom_id)
    if taom is None:
        await callback_query.answer("Taom topilmadi!", show_alert=True)
        return

    foydalanuvchi_id = str(callback_query.from_user.id)
    if foydalanuvchi_id not in savatcha:
        savatcha[foydalanuvchi_id] = {}

    hozirgi_soni = int(savatcha[foydalanuvchi_id].get(taom_id, 0))
    if hozirgi_soni >= 99:
        await callback_query.answer("Bir taomdan ko'pi bilan 99 ta qo'shish mumkin.", show_alert=True)
        return

    savatcha[foydalanuvchi_id][taom_id] = hozirgi_soni + 1
    savatchani_saqlash()

    await callback_query.answer(
        f"{taom['nomi']} savatchaga qo'shildi. Soni: {hozirgi_soni + 1} ta"
    )


@dp.callback_query(F.data == "savatcha")
async def savatcha_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    foydalanuvchi_id = str(callback_query.from_user.id)
    matn, klaviatura = savatchani_korsatish(foydalanuvchi_id)
    await callback_query.message.answer(matn, reply_markup=klaviatura)


@dp.callback_query(F.data.startswith("cart_plus_"))
async def cart_plus_handler(callback_query: CallbackQuery):
    taom_id = callback_query.data.replace("cart_plus_", "", 1)
    foydalanuvchi_id = str(callback_query.from_user.id)
    foydalanuvchi_savatchasi = savatcha.setdefault(foydalanuvchi_id, {})

    if taom_id not in taomlar or taom_id not in foydalanuvchi_savatchasi:
        await callback_query.answer("Bu taom savatchada topilmadi.", show_alert=True)
        return

    if int(foydalanuvchi_savatchasi[taom_id]) >= 99:
        await callback_query.answer("Bir taomdan ko'pi bilan 99 ta qo'shish mumkin.", show_alert=True)
        return

    foydalanuvchi_savatchasi[taom_id] = int(foydalanuvchi_savatchasi[taom_id]) + 1
    savatchani_saqlash()
    await callback_query.answer("Miqdor oshirildi.")
    matn, klaviatura = savatchani_korsatish(foydalanuvchi_id)
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


@dp.callback_query(F.data.startswith("cart_minus_"))
async def cart_minus_handler(callback_query: CallbackQuery):
    taom_id = callback_query.data.replace("cart_minus_", "", 1)
    foydalanuvchi_id = str(callback_query.from_user.id)
    foydalanuvchi_savatchasi = savatcha.setdefault(foydalanuvchi_id, {})

    if taom_id not in taomlar or taom_id not in foydalanuvchi_savatchasi:
        await callback_query.answer("Bu taom savatchada topilmadi.", show_alert=True)
        return

    yangi_soni = int(foydalanuvchi_savatchasi[taom_id]) - 1
    if yangi_soni <= 0:
        foydalanuvchi_savatchasi.pop(taom_id, None)
        await callback_query.answer("Taom savatchadan olib tashlandi.")
    else:
        foydalanuvchi_savatchasi[taom_id] = yangi_soni
        await callback_query.answer("Miqdor kamaytirildi.")

    savatchani_saqlash()
    matn, klaviatura = savatchani_korsatish(foydalanuvchi_id)
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


@dp.callback_query(F.data.startswith("cart_remove_"))
async def cart_remove_handler(callback_query: CallbackQuery):
    taom_id = callback_query.data.replace("cart_remove_", "", 1)
    foydalanuvchi_id = str(callback_query.from_user.id)
    foydalanuvchi_savatchasi = savatcha.setdefault(foydalanuvchi_id, {})

    if taom_id not in foydalanuvchi_savatchasi:
        await callback_query.answer("Bu taom savatchada yo'q.", show_alert=True)
        return

    foydalanuvchi_savatchasi.pop(taom_id)
    savatchani_saqlash()
    await callback_query.answer("Taom savatchadan olib tashlandi.")
    matn, klaviatura = savatchani_korsatish(foydalanuvchi_id)
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


@dp.callback_query(F.data == "cart_noop")
async def cart_noop_handler(callback_query: CallbackQuery):
    await callback_query.answer()


@dp.callback_query(F.data == "cart_clear")
async def cart_clear_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        "⚠️ Savatchadagi barcha taomlarni olib tashlamoqchimisiz?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="✅ Ha, savatchani bo'shatish", callback_data="cart_clear_yes")],
                [InlineKeyboardButton(text="↩️ Yo'q, ortga qaytish", callback_data="cart_clear_no")]
            ]
        )
    )


@dp.callback_query(F.data == "cart_clear_no")
async def cart_clear_no_handler(callback_query: CallbackQuery):
    foydalanuvchi_id = str(callback_query.from_user.id)
    await callback_query.answer()
    matn, klaviatura = savatcha_matni_va_tugmalari(foydalanuvchi_id)
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


@dp.callback_query(F.data == "cart_clear_yes")
async def cart_clear_yes_handler(callback_query: CallbackQuery):
    foydalanuvchi_id = str(callback_query.from_user.id)
    savatcha[foydalanuvchi_id] = {}
    savatchani_saqlash()
    await callback_query.answer("Savatcha bo'shatildi.")
    matn, klaviatura = savatcha_matni_va_tugmalari(foydalanuvchi_id)
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


@dp.callback_query(F.data == "cart_confirm")
async def cart_confirm_handler(callback_query: CallbackQuery):
    foydalanuvchi_id = str(callback_query.from_user.id)
    foydalanuvchi_savatchasi = savatcha.get(foydalanuvchi_id, {})

    if not foydalanuvchi_savatchasi:
        await callback_query.answer("Savatchangiz bo'sh.", show_alert=True)
        return

    if foydalanuvchi_id not in buyurtmalar:
        buyurtmalar[foydalanuvchi_id] = []

    for taom_id, soni in foydalanuvchi_savatchasi.items():
        taom = taomlar.get(taom_id)
        if taom and int(soni) > 0:
            buyurtmalar[foydalanuvchi_id].append({
                "id": taom_id,
                "nomi": taom["nomi"],
                "narxi": taom["narxi"],
                "soni": int(soni)
            })

    buyurtmalarni_saqlash()
    savatcha[foydalanuvchi_id] = {}
    savatchani_saqlash()

    await callback_query.answer("Buyurtma tasdiqlandi!")
    matn, klaviatura = buyurtmalar_matni_va_tugmalari(foydalanuvchi_id)
    await callback_query.message.edit_text(
        "✅ Buyurtmangiz tasdiqlandi va Buyurtmalar bo'limiga o'tkazildi.\n\n" + matn,
        reply_markup=klaviatura
    )


@dp.callback_query(F.data == "buyurtmalar")
async def buyurtmalar_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    foydalanuvchi_id = str(callback_query.from_user.id)
    matn, klaviatura = buyurtmalar_matni_va_tugmalari(foydalanuvchi_id)

    await callback_query.message.answer(matn, reply_markup=klaviatura)


@dp.callback_query(F.data.startswith("cancel_"))
async def cancel_order_handler(callback_query: CallbackQuery):
    foydalanuvchi_id = str(callback_query.from_user.id)
    foydalanuvchi_buyurtmalari = buyurtmalar.get(foydalanuvchi_id, [])

    if callback_query.data == "cancel_all":
        if not foydalanuvchi_buyurtmalari:
            await callback_query.answer("Bekor qilinadigan buyurtma yo'q.", show_alert=True)
            return

        await callback_query.answer()
        await callback_query.message.edit_text(
            "⚠️ Barcha buyurtmalaringizni bekor qilishni tasdiqlaysizmi?",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="✅ Ha, barchasini bekor qilish", callback_data="confirm_cancel_all")],
                    [InlineKeyboardButton(text="↩️ Yo'q, ortga qaytish", callback_data="back_to_buyurtmalar")]
                ]
            )
        )
        return

    else:
        taom_id = callback_query.data.replace("cancel_", "", 1)
        if taom_id not in taomlar:
            await callback_query.answer("Taom topilmadi!", show_alert=True)
            return

        eski_soni = len(foydalanuvchi_buyurtmalari)
        buyurtmalar[foydalanuvchi_id] = [
            buyurtma for buyurtma in foydalanuvchi_buyurtmalari
            if buyurtma_taom_idni_topish(buyurtma) != taom_id
        ]

        if len(buyurtmalar[foydalanuvchi_id]) == eski_soni:
            await callback_query.answer("Bu taom buyurtmalaringizda yo'q.", show_alert=True)
            return

        buyurtmalarni_saqlash()
        await callback_query.answer("Tanlangan taom buyurtmadan olib tashlandi!")

    matn, klaviatura = buyurtmalar_matni_va_tugmalari(foydalanuvchi_id)
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


@dp.callback_query(F.data == "confirm_cancel_all")
async def confirm_cancel_all_handler(callback_query: CallbackQuery):
    foydalanuvchi_id = str(callback_query.from_user.id)
    buyurtmalar[foydalanuvchi_id] = []
    buyurtmalarni_saqlash()

    await callback_query.answer("Barcha buyurtmalar bekor qilindi!")
    matn, klaviatura = buyurtmalar_matni_va_tugmalari(foydalanuvchi_id)
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


@dp.callback_query(F.data == "back_to_buyurtmalar")
async def back_to_buyurtmalar_handler(callback_query: CallbackQuery):
    foydalanuvchi_id = str(callback_query.from_user.id)
    matn, klaviatura = buyurtmalar_matni_va_tugmalari(foydalanuvchi_id)

    await callback_query.answer()
    await callback_query.message.edit_text(matn, reply_markup=klaviatura)


#  ----------------o'zbek taomlar--------------------


@dp.callback_query(F.data == "o'zbek taomlari")
async def ozbek_taomlari_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "O'zbek milliy taomlari:",
        reply_markup=ozbek_milliy_buttons
    )

@dp.callback_query(F.data == "osh")
async def osh_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxZXtlkys65JX_O4pMCTQa2lj5UIZzChlIn4nTQ6iC1g&s=10",
        caption="🍽 Osh\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_osh")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "manti_uzb")
async def manti_uzb_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStu2S6Zae_7TPY0eg70kQyCpd9w5-j8EN10kpsElQWRA&s=10",
        caption="🍽 Manti\n💰 Narxi: 55 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_manti_uzb")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "lag'mon")
async def lagmon_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTs7tRJuj0jJNXLuxDOIkmgMBxSbY4a_6K3vOAUJVLbzA&s=10",
        caption="🍽 Lag'mon\n💰 Narxi: 55 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_lagmon")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "sho'rva")
async def shorva_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMABrq0YDDBxV2B2lLpYX-BilLghtS2fn0s0P6CljcZA&s=10",
        caption="🍽 Sho'rva\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_shorva")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "kabob")
async def kabob_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEGNSKFr9tmHhUD8kKPi3nRQqRHYOTvzHR1aQnq1a5jw&s=10",
        caption="🍽 Kabob\n💰 Narxi: 35 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_kabob")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "chuchvara")
async def chuchvara_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnOUuZXDRySNxHQTTqg_qarPuk-pf-X8moY5t5CxJOUw&s=10",
        caption="🍽 Chuchvara\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_chuchvara")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "dimlama")
async def dimlama_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS85wKb04eUF08cjnrysiV2bMDKgDOUL7LQVOfIQFqFRQ&s=10",
        caption="🍽 Dimlama\n💰 Narxi: 50 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_dimlama")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "qozon kabob")
async def qozon_kabob_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_rBdpwW-mDf0Gk9NRkC-s77Ur2hx8rAdKIaW1nY_Z0Q&s=10",
        caption="🍽 Qozon Kabob\n💰 Narxi: 68 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_qozon_kabob")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "somsa")
async def somsa_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfeMIO6-6HiKcJ2F5z3EYy-_sBMOsPlJdXFffvrOb_WA&s=10",
        caption="🍽 Somsa\n💰 Narxi: 15 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_somsa")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "achichuk")
async def achichuk_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaOt5252jPs_LUCcEzKswG81Ipv_HZIlhhwLcQhK-6Ig&s=10",
        caption="🍽 Achichuk salat\n💰 Narxi: 22 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=ozbek_milliy_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_achichuk")
                ]
            ]
        )
    )


#  ----------------yapon taomlari --------------------


@dp.callback_query(F.data == "yapon taomlari")
async def yapon_taomlari_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "Yapon taomlari:",
        reply_markup=yapon_buttons
    )

@dp.callback_query(F.data == "sushi")
async def sushi_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQz4okCc52kBVqrkpmB09WPI-BfLXNf-EUFQZ67D6Eyog&s=10",
        caption="🍽 Sushi\n💰 Narxi: 60 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_sushi")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "ramen")
async def ramen_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr7C6Aiir-blAbuoJu0aePm5_hqFyKktxqOaYOybI4Iw&s=10",
        caption="🍽 Ramen\n💰 Narxi: 65 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_ramen")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "onigiri")
async def onigiri_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsqHFZmpwFFL1tVGZseSvxzA61dKejIlgqZW0Ox8QE7g&s=10",
        caption="🍽 Onigiri\n💰 Narxi: 30 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_onigiri")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "gyoza")
async def gyoza_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfnQHqOdBhF2pyFHdit13BBJokkogqWYH-50Uv7HpXug&s=10",
        caption="🍽 Gyoza\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_gyoza")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "yakitori")
async def yakitori_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNn95E-dSs_xb01GUa4j5-YaJ0SVba51gmep6hc-91BA&s=10",
        caption="🍽 Yakitori\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_yakitori")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "bento")
async def bento_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTljiDGH7iVmQA54yKE3q5FMtShtFN3xLhqGBG3BiMUWg&s=10",
        caption="🍽 Bento\n💰 Narxi: 75 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_bento")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "katsu curry")
async def katsu_curry_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMKqltqBaxuBiQH2IiCYDTEbjWPSaVH9eQf-vl9maG8A&s=10",
        caption="🍽 Katsu Curry\n💰 Narxi: 75 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_katsu_curry")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "teriyaki")
async def teriyaki_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHfXuwdzY_87Slqg3vmUruUqXTyGN8CMHJ_OxmscIIBw&s=10",
        caption="🍽 Teriyaki\n💰 Narxi: 70 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_teriyaki")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "miso soup")
async def miso_soup_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbJR9dq0U9OyEWnueJozYNNdsKahOLzZVHOa1BsPvFwQ&s=10",
        caption="🍽 Miso Soup\n💰 Narxi: 35 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_miso_soup")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "tempura")
async def tempura_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ60iUevhE98FsbDlSrV_7gnnbzFTpBUeSqfRrJguZ-vQ&s=10",
        caption="🍽 Tempura\n💰 Narxi: 65 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=yapon_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_tempura")
                ]
            ]
        )
    )


        #  ---------------koreys taomlari --------------------


@dp.callback_query(F.data == "koreys taomlari")
async def koreys_taomlari_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "Koreys taomlari:",
        reply_markup=koreys_buttons
    )

@dp.callback_query(F.data == "bibimbap")
async def bibimbap_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnwSFngtC1GVeW-sVlf8kUHoqIffnPJ3Ohwhpmbk26yw&s=10",
        caption="🍽 Bibimbap\n💰 Narxi: 90 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_bibimbap")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "japchae")
async def japchae_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6yPQIDsBo8_kLx26JCa_uuHkJH7-njhzHORhC94QMLw&s=10",
        caption="🍽 Japchae\n💰 Narxi: 85 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_japchae")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "fried_chicken_kor")
async def fried_chicken_kor_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiB_BAWq4t0DmkFis4HIUYDjjsKfusS9_YsKA_MDu-wg&s=10",
        caption="🍽 Koreyscha qovurilgan tovuq\n💰 Narxi: 85 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_fried_chicken_kor")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "tteokbokki")
async def tteokbokki_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_JJ9CCknrEOj0UgxdDiKO-RmyP6SnzWKweM6UNfYcjQ&s=10",
        caption="🍽 Tteokbokki\n💰 Narxi: 65 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_tteokbokki")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "kimchi jjigae")
async def kimchi_jjigae_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROXZThAsmslRqKLoydFRmsl22MzapbklAvzzdGh6BWYg&s=10",
        caption="🍽 Kimchi Jjigae\n💰 Narxi: 70 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_kimchi_jjigae")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "bulgogi")
async def bulgogi_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDPJj8Gq0jAW9gTfim1w2eoiYGw_uIW9spjafYEzLmeg&s=10",
        caption="🍽 Bulgogi\n💰 Narxi: 95 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_bulgogi")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "samgyeopsal")
async def samgyeopsal_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIkFgfl9JyMrMOKoLFn4Rpsxlp9KVU01J1E0jRBRe7Yg&s=10",
        caption="🍽 Samgyeopsal\n💰 Narxi: 115 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_samgyeopsal")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "mandu")
async def mandu_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx0Y6iEJWJuXKfCZ9iV4XeJy85ie5bItn4daQR6_eZyw&s=10",
        caption="🍽 Mandu\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_mandu")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "naegmyeon")
async def naengmyeon_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbX_Y3KPFRRjk5K9oqJLfUr2BdeuIHcFuIwjXqVy8uVw&s=10",
        caption="🍽 Naegmyeon\n💰 Narxi: 65 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_naengmyeon")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "kimchi")
async def kimchi_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlNXDt-USq5B7gs7uf2y4VeFLRn57zzfGt-W1l4OUpYA&s=10",
        caption="🍽 Kimchi\n💰 Narxi: 25 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=koreys_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_kimchi")
                ]
            ]
        )
    )


    #  ---------------turk taomlari --------------------


@dp.callback_query(F.data == "turk taomlari")
async def turk_taomlari_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "Turk taomlari:",
        reply_markup=turk_buttons
    )

@dp.callback_query(F.data == "doner")
async def doner_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeAjmOWs9IkCra7xrd9_-ndsKRxE10lwpEP65Fb4elAQ&s=10",
        caption="🍽 Doner\n💰 Narxi: 55 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_doner")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "kebab")
async def kebab_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDIbIICSVZcbphyUiuwJlPkbCyPxwiQj8gzpQx9-VkLA&s=10",
        caption="🍽 Kebab\n💰 Narxi: 85 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_kebab")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "lahmacun")
async def lahmacun_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEtJJwIPCpd-tfreVpuYOX51Wzd1OpmnM7Wu3vk2yIsg&s=10",
        caption="🍽 Lahmacun\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_lahmacun")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "pide")
async def pide_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh4nw2RxV62N-MBuTYCESD74Yht7JZ5RCueJEhDGU6oQ&s=10",
        caption="🍽 Pide\n💰 Narxi: 65 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_pide")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "manti_turk")
async def manti_turk_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1Z4b4XmIZetA9kxxlnxFJsHCBQY3DwJCjDjr0rl_Ehg&s=10",
        caption="🍽 Manti Turk\n💰 Narxi: 65 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_manti_turk")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "mercimek corbasi")
async def mercimek_corbasi_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGeA6btZy9VMb1X3La3SPzs5QdyJHj0KTaNcaNkD54Vg&s=10",
        caption="🍽 Mercimek corbasi\n💰 Narxi: 40 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_mercimek_corbasi")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "menemen")
async def menemen_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEVcW-XyHjvaDGG_Hs4GSFRIsD8koDjH9x5PR_HRWt5g&s=10",
        caption="🍽 Menemen\n💰 Narxi: 45 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_menemen")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "kofte")
async def kofte_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFrZxXuZ7BG5G-iczJmwWUwLoLAoL8JK2qtVK-D3WBpQ&s=10",
        caption="🍽 Kofte\n💰 Narxi: 70 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_kofte")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "gozleme")
async def gozleme_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMEYDLgoEtw7Zd0W5fNfuBrUJuiSzf2kxNQH4Gf2UJ-Q&s=10",
        caption="🍽 Gozleme\n💰 Narxi: 50 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_gozleme")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "imam bayildi")
async def imam_bayildi_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDqi_uVQPysQTR-mUAbeq7XnPxv39FxV9YTfw1hdbC1w&s=10",
        caption="🍽 Imam bayildi\n💰 Narxi: 55 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=turk_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_imam_bayildi")
                ]
            ]
        )
    )


#  ---------------italyan taomlari --------------------


@dp.callback_query(F.data == "italyan taomlari")
async def italyan_taomlari_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "Italyan taomlari:",
        reply_markup=italyan_buttons
    )

@dp.callback_query(F.data == "margherita pizza")
async def margherita_pizza_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTNWgs49aTLgrdqDfvrXmWGgcd2TaAkMcy-qzFAR8LiQ&s=10",
        caption="🍽 Margherita Pizza\n💰 Narxi: 60 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_margherita_pizza")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "spaghetti carbonara")
async def spaghetti_carbonara_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVJBcu9bF958145-yu8JW18YaS3pQ_CrXdqdZjitiUTw&s=10",
        caption="🍽 Spaghetti Carbonara\n💰 Narxi: 85 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_spaghetti_carbonara")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "lasagna")
async def lasagna_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJBTmnINcbcghAUhnIBOnaf68UF5Z8gY6IWUk7aF_ztw&s=10",
        caption="🍽 Lasagna\n💰 Narxi: 105 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_lasagna")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "fettuccine alfredo")
async def fettuccine_alfredo_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS56hBy2HZ_kn7Kxf4abRhYxdsR-q-iJPcsAuewqwBuEA&s=10",
        caption="🍽 Fettuccine Alfredo\n💰 Narxi: 85 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_fettuccine_alfredo")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "pepperoni pizza")
async def pepperoni_pizza_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQF6zN1wWEctpAI5aHHm-fBhqEiHWBqID27c2Gtu3gog&s=10",
        caption="🍽 Pepperoni Pizza\n💰 Narxi: 65 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_pepperoni_pizza")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "spaghetti bolognese")
async def spaghetti_bolognese_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMtJJmnPKbCCAFkd7UBNz9GOjud4dGJhElz3qGwzSdNQ&s=10",
        caption="🍽 Spaghetti Bolognese\n💰 Narxi: 90 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_spaghetti_bolognese")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "risotto")
async def risotto_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpYLrFu0joT8UDWQXm99Q0GPyRyhFZeEihklM7ENUqig&s=10",
        caption="🍽 Risotto\n💰 Narxi: 90 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_risotto")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "ravioli")
async def ravioli_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNSvo49XZvcLIp9VJn5lwTQjoiYhLXos-ru7aw-VlFWw&s=10",
        caption="🍽 Ravioli\n💰 Narxi: 95 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_ravioli")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "bruschetta")
async def bruschetta_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQApd0220xT2W-_I6O8wtPYkJZWRhZXQ7l0oAae_RZN9w&s=10",
        caption="🍽 Bruschetta\n💰 Narxi: 40 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_bruschetta")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "caprese salad")
async def caprese_salad_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSr-1lWsbQhDpCU2lV47UyjuuiKg0o5v11_6NIXE4eudg&s=10",
        caption="🍽 Caprese salat\n💰 Narxi: 60 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=italyan_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_caprese_salad")
                ]
            ]
        )
    )


#  ---------------fast food --------------------


@dp.callback_query(F.data == "fast food")
async def fastfood_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        "Fast Food:",
        reply_markup=fastfood_buttons
    )

@dp.callback_query(F.data == "cheeseburger")
async def cheeseburger_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS04SQtGqoj7x1Ug1j1G6hiSpsILzI_2hk3kqSA9bPHAg&s=10",
        caption="🍽 Cheeseburger\n💰 Narxi: 30 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_cheeseburger")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "hamburger")
async def hamburger_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThimdqKnbDAstdWeUPE41YfWFnDNzN5va8j4Y67tvZzg&s=10",
        caption="🍽 Hamburger\n💰 Narxi: 28 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_hamburger")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "fried_chicken_ff")
async def fried_chicken_ff_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH1xwkAzBLkSflGF_Tl8iOMKp0Zzu010lRdo8Bty9IPg&s=10",
        caption="🍽 Qovurilgan tovuq\n💰 Narxi: 42 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_fried_chicken_ff")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "french fries")
async def french_fries_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwn16qcQVv_D668Gzq1YGyWJQUfDeXGIxj0keiKgiSww&s=10",
        caption="🍽 Kartoshka fri\n💰 Narxi: 19 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_french_fries")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "hot dog")
async def hot_dog_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYyk3TWIBeb5Ojwj4CCU4Fktm7nhJQMbR1fGacB9ezEw&s=10",
        caption="🍽 Hot-dog\n💰 Narxi: 25 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_hot_dog")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "tacos")
async def tacos_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrEjTTC9hprfqnU9nMCBVZ9aJ2gfnQxZtWhggOxP63qg&s=10",
        caption="🍽 Tacos\n💰 Narxi: 50 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_tacos")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "sandwich")
async def sandwich_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQizs_OdDn0xuO4LF5Zu1nvwq0sTUsJ3n71otH7qS-nZQ&s=10",
        caption="🍽 Sandwich\n💰 Narxi: 40 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_sandwich")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "pizza")
async def pizza_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_4aGn1VO584EPbMq-rpavYLrYDRt71DqO9uQioHpGyQ&s=10",
        caption="🍽 Pizza\n💰 Narxi: 60 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_pizza")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "burrito")
async def burrito_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-d5-smMSdgBvC8UwLzB9ONVbeUPtPVvmMRkFUjXqfuw&s=10",
        caption="🍽 Burrito\n💰 Narxi: 55 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_burrito")
                ]
            ]
        )
    )

@dp.callback_query(F.data == "chicken nuggets")
async def chicken_nuggets_handler(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiPM5vUxvhDpWIWSqFm4N8mF6Rmbxb_SWEytBQdFMPXw&s=10",
        caption="🍽 Chicken nuggets\n💰 Narxi: 25 000 so'm",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=fastfood_buttons.inline_keyboard + [
                [
                    InlineKeyboardButton(text="➕ Savatchaga qo'shish", callback_data="cart_add_chicken_nuggets")
                ]
            ]
        )
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())