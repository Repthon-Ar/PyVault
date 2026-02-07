import os
from .security import VaultSecurity

class PyVault:
    @staticmethod
    async def upload(client, file_path, storage_id, bot_username=None, encrypt=False):
        """
        يرفع الملف ويولد رابطاً دائماً.
        :param client: Telethon Client
        :param storage_id: ID القناة أو 'me' للرسائل المحفوظة
        :param bot_username: يوزر البوت (اختياري)
        """
        if not os.path.exists(file_path):
            return {"ok": False, "error": "File not found"}

        target = file_path
        key = None
        if encrypt:
            key = VaultSecurity.generate_key()
            target = VaultSecurity.encrypt_file(file_path, key)

        try:
            msg = await client.send_file(storage_id, target)
            safe_id = VaultSecurity.encode_id(msg.id)

            if bot_username:
                url = f"https://t.me/{bot_username.replace('@', '')}?start=file_{safe_id}"
            else:
                chat_id = str(storage_id).replace("-100", "")
                url = f"https://t.me/c/{chat_id}/{msg.id}" if not str(storage_id).isalpha() else f"https://t.me/{storage_id}/{msg.id}"

            if encrypt and os.path.exists(target):
                os.remove(target)

            return {
                "ok": True,
                "url": url,
                "file_id": msg.id,
                "key": key.decode() if key else None
            }
        except Exception as e:
            return {"ok": False, "error": str(e)}
