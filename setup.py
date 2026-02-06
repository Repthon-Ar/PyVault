from setuptools import setup, find_packages

setup(
    name="PyVault",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests", "cryptography", "telethon"],
    description="Encrypted media upload library without API"
)
