from dataclasses import dataclass

@dataclass(frozen=True)
class Leitor:
    id: int
    nome: str
    email: str