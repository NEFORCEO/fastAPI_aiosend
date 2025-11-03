from aiosend import CryptoPay, TESTNET


def get_cp(token: str) -> CryptoPay:
    return CryptoPay(token=token, network=TESTNET)