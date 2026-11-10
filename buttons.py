from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍚 O‘zbek taomlari", callback_data="o'zbek taomlari"),
            InlineKeyboardButton(text="🍣 Yapon taomlari", callback_data="yapon taomlari"),
        ],
        [
            InlineKeyboardButton(text="🍜 Koreys taomlari", callback_data="koreys taomlari"),
            InlineKeyboardButton(text="🍕 Italyan taomlari", callback_data="italyan taomlari"),
        ],
        [
            InlineKeyboardButton(text="🥙 Turk taomlari", callback_data="turk taomlari"),
            InlineKeyboardButton(text="🍔🍟 Fast Food", callback_data="fast food"),
        ],
        [
            InlineKeyboardButton(text="🛒 Savatcha", callback_data="savatcha"),
            InlineKeyboardButton(text="📦 Buyurtmalar", callback_data="buyurtmalar"),
        ],
    ],
)


#  ----------------o'zbek taomlar--------------------


ozbek_milliy_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍚 Osh", callback_data="osh"),
            InlineKeyboardButton(text="🥟 Manti", callback_data="manti_uzb")
        ],
        [
            InlineKeyboardButton(text="🍜 Lag‘mon", callback_data="lag'mon"),
            InlineKeyboardButton(text="🥣 Sho‘rva", callback_data="sho'rva")
        ],
        [
            InlineKeyboardButton(text="🍢 Kabob", callback_data="kabob"),
            InlineKeyboardButton(text="🥟 Chuchvara", callback_data="chuchvara")
        ],
        [
            InlineKeyboardButton(text="🥘 Dimlama", callback_data="dimlama"),
            InlineKeyboardButton(text="🥩 Qozon kabob", callback_data="qozon kabob")
        ],
        [
            InlineKeyboardButton(text="🫓 Somsa", callback_data="somsa"),
            InlineKeyboardButton(text="🥗 Achichuk", callback_data="achichuk")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
        ],
    ],
)


#  ----------------yapon taomlar--------------------


yapon_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍣 Sushi", callback_data="sushi"),
            InlineKeyboardButton(text="🍜 Ramen", callback_data="ramen")
        ],
        [
            InlineKeyboardButton(text="🍜 🍙 Onigiri", callback_data="onigiri"),
            InlineKeyboardButton(text="🥟 Gyoza", callback_data="gyoza")
        ],
        [
            InlineKeyboardButton(text="🍗 Yakitori", callback_data="yakitori"),
            InlineKeyboardButton(text="🍱 Bento", callback_data="bento")
        ],
        [
            InlineKeyboardButton(text="🍛 Katsu Curry", callback_data="katsu curry"),
            InlineKeyboardButton(text="🥩 Teriyaki", callback_data="teriyaki")
        ],
        [
            InlineKeyboardButton(text="🥣 Miso Soup", callback_data="miso soup"),
            InlineKeyboardButton(text="🍤 Tempura", callback_data="tempura")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
        ],
    ],
)


#  ----------------koreys taomlar--------------------


koreys_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍚 Bibimbap", callback_data="bibimbap"),
            InlineKeyboardButton(text="🍜 Japchae", callback_data="japchae")
        ],
        [
            InlineKeyboardButton(text="🍗 Korean Fried Chicken", callback_data="fried_chicken_kor"),
            InlineKeyboardButton(text="🥘 Tteokbokki", callback_data="tteokbokki")
        ],
        [
            InlineKeyboardButton(text="🍲 Kimchi Jjigae", callback_data="kimchi jjigae"),
            InlineKeyboardButton(text="🥩 Bulgogi", callback_data="bulgogi")
        ],
        [
            InlineKeyboardButton(text="🥓 Samgyeopsal", callback_data="samgyeopsal"),
            InlineKeyboardButton(text="🥟 Mandu", callback_data="mandu")
        ],
        [
            InlineKeyboardButton(text="🍜 Naengmyeon", callback_data="naegmyeon"),
            InlineKeyboardButton(text="🥬 Kimchi", callback_data="kimchi")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
        ],
    ],
)


#  ----------------turk taomlar--------------------


turk_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🥙 Döner", callback_data="doner"),
            InlineKeyboardButton(text="🥩 Kebab", callback_data="kebab")
        ],
        [
            InlineKeyboardButton(text="🫓 Lahmacun", callback_data="lahmacun"),
            InlineKeyboardButton(text="🍕 Pide", callback_data="pide")
        ],
        [
            InlineKeyboardButton(text="🥟 Manti", callback_data="manti_turk"),
            InlineKeyboardButton(text="🍲 Mercimek Çorbası", callback_data="mercimek corbasi")
        ],
        [
            InlineKeyboardButton(text="🍳 Menemen", callback_data="menemen"),
            InlineKeyboardButton(text="🥩 Köfte", callback_data="kofte")
        ],
        [
            InlineKeyboardButton(text="🫓 Gözleme", callback_data="gozleme"),
            InlineKeyboardButton(text="🍆 İmam Bayıldı", callback_data="imam bayildi")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
        ],
    ],
)


#  ----------------italyan taomlar--------------------


italyan_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍕 Margherita Pizza", callback_data="margherita pizza"),
            InlineKeyboardButton(text="🍝 Spaghetti Carbonara", callback_data="spaghetti carbonara")
        ],
        [
            InlineKeyboardButton(text="🍝 Lasagna", callback_data="lasagna"),
            InlineKeyboardButton(text="🍝 Fettuccine Alfredo", callback_data="fettuccine alfredo")
        ],
        [
            InlineKeyboardButton(text="🍕 Pepperoni Pizza", callback_data="pepperoni pizza"),
            InlineKeyboardButton(text="🍝 Spaghetti Bolognese", callback_data="spaghetti bolognese")
        ],
        [
            InlineKeyboardButton(text="🍚 Risotto", callback_data="risotto"),
            InlineKeyboardButton(text="🥟 Ravioli", callback_data="ravioli")
        ],
        [
            InlineKeyboardButton(text="🍅 Bruschetta", callback_data="bruschetta"),
            InlineKeyboardButton(text="🥗 Caprese Salad", callback_data="caprese salad")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
        ],
    ],
)


#  ----------------fast food--------------------


fastfood_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍔 Cheeseburger", callback_data="cheeseburger"),
            InlineKeyboardButton(text="🍔 Hamburger", callback_data="hamburger")
        ],
        [
            InlineKeyboardButton(text="🍗 Fried Chicken", callback_data="fried_chicken_ff"),
            InlineKeyboardButton(text="🍟 French Fries", callback_data="french fries")
        ],
        [
            InlineKeyboardButton(text="🌭 Hot Dog", callback_data="hot dog"),
            InlineKeyboardButton(text="🌮 Tacos", callback_data="tacos")
        ],
        [
            InlineKeyboardButton(text="🥪 Sandwich", callback_data="sandwich"),
            InlineKeyboardButton(text="🍕 Pizza", callback_data="pizza")
        ],
        [
            InlineKeyboardButton(text="🌯 Burrito", callback_data="burrito"),
            InlineKeyboardButton(text="🧀 Chicken Nuggets", callback_data="chicken nuggets")
        ],
        [
            InlineKeyboardButton(text="🔙 Bosh menyu", callback_data="boshmenyu")
        ],
    ],
)
