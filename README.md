# 🛡️ PyVault 
**The Ultimate Permanent Media Uploader & Encrypter for Python.**

`PyVault` is a powerful, lightweight Python library designed for developers who need a reliable way to upload images and videos permanently without the hassle of owning a server or managing complex API keys. It bridges your local environment (or Telegram Userbots) with permanent storage solutions.

---

## ✨ Features
* 🚀 **Instant Upload:** Full support for Images, Videos, Audio, and Documents.
* ♾️ **Permanent Links:** Uses reliable backends (like Catbox) to ensure your links never expire.
* 🔒 **Military-Grade Encryption:** Optional AES encryption for files before uploading to ensure total privacy.
* 🔗 **Clean URLs:** Integrated URL shortening to keep your links professional and hide the backend source.
* 🤖 **Telethon Ready:** Built-in support for **Telegram Userbots** and **Bots**.
* 🛠️ **Zero Config:** No registration, no API keys, and no configuration required. Just install and upload.

---

## 📂 Project Structure
```text
PyVault/
├── pyvault/
│   ├── __init__.py      # Package initialization
│   ├── core.py          # Main engine (Upload & Shorten)
│   └── security.py      # Security module (Encryption)
├── setup.py             # Installation script
└── requirements.txt     # Dependencies
```

---

## 🚀 Installation
​You can install the library locally using:
```bash
pip install PyVault
```
----

## 💻 Usage Examples
​1. Simple Upload (Public)
```python
from pyvault import PyVault

# Upload any file in one line
result = PyVault.upload("my_video.mp4")

if result["ok"]:
    print(f"🔗 Permanent Link: {result['url']}")
```

---

Encrypted Upload (Private)
```python
# The file will be encrypted before uploading. Only someone with the key can decrypt it.
result = PyVault.upload("secret_data.png", encrypt=True)

if result["ok"]:
    print(f"🔗 Encrypted Link: {result['url']}")
    print(f"🔑 Decryption Key: {result['key']}")
```

---

Integration with Telethon (Userbot)
```python
from telethon import events
from pyvault import PyVault

@client.on(events.NewMessage(outgoing=True, pattern=r'\.up'))
async def handler(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        # Download from Telegram
        path = await client.download_media(reply.media)
        
        # Upload to Vault
        res = PyVault.upload(path)
        await event.edit(f"✅ **Uploaded Successfully!**\n\n🔗 Link: {res['url']}")
```

# 🛠️ Requirements

° ​requests

° ​cryptography

° ​telethon (optional for bot integration)

---

​🤝 Contributing
​Contributions are welcome! If you have ideas to improve PyVault, feel free to open an issue or submit a pull request.
​Developed with ❤️ to empower developers worldwide.
