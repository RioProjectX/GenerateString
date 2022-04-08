from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

Selamat datang {}

Jika kamu tidak percaya bot ini, 
1) Silahkan Tinggalkan Bot Ini
2) Bot Ini Aman 100% Udah BPOM YA GES YA

Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih
By @fckualot
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Kembali 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Maintaned By ✨", url="https://t.me/fckualot")],
        [
            InlineKeyboardButton("Cara Menggunakan Saya ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Info Bot Lain ♥", url="https://t.me/rioprojects")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @stringriobot

Group Support : [Gabung](https://t.me/riogroupsupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @fckualot
    """
