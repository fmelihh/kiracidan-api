from dynaconf import settings
from typing import Dict

# TODO 1: generate token ve decode token metotları fonksiyonellikleri sağlanacak
# TODO 2: test case lerinden geçecek şekilde kodlar oluşturulacak.
# TODO 3: class attributeleri settings.toml dosyasından okunup ona göre fonskiyonlara yerleştirilecek.


class TokenGenerator:
    def __init__(self, message: Dict):
        # çoğaltılabilir
        self.exp = settings.TOKEN_EXP
        self.secret = settings.SECRET

    def generate_token(self) -> str:
        return ""

    def decode_token(self, token: str) -> Dict:
        return {}
