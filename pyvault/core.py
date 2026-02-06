import requests
import os
from .security import VaultSecurity

class PyVault:
    @staticmethod
    def _shorten(url):
        try:
            res = requests.get(f"https://is.gd/create.php?format=simple&url={url}")
            return res.text if res.status_code == 200 else url
        except:
            return url

        @staticmethod
    def upload(file_path, encrypt=False):
        """يرفع الصور والفيديوهات"""
        if not os.path.exists(file_path):
            return {"ok": False, "error": "الملف غير موجود"}

        target = file_path
        key = None

        if encrypt:
            key = VaultSecurity.generate_key()
            target = VaultSecurity.encrypt_file(file_path, key)
        try:
            with open(target, 'rb') as f:
                files = {
                    'reqtype': (None, 'fileupload'),
                    'fileToUpload': (os.path.basename(target), f)
                }
                response = requests.post("https://catbox.moe/user/api.php", files=files, timeout=60)
            
            if response.status_code == 200 and "https" in response.text:
                raw_url = response.text.strip()
                short_url = PyVault._shorten(raw_url)
                
                if encrypt and os.path.exists(target):
                    os.remove(target)

                return {
                    "ok": True,
                    "url": short_url,
                    "raw_url": raw_url,
                    "key": key.decode() if key else None
                }
            return {"ok": False, "error": f"فشل الرفع: {response.text}"}
        except Exception as e:
            return {"ok": False, "error": str(e)}
