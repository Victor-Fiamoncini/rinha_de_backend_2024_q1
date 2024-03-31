from dataclasses import dataclass
from rinha_de_backend_2024_q1.domain.exceptions import InconsistentBalanceException


@dataclass(frozen=True)
class MakeNewInput:
    value: int
    type_of: str
    description: str
    owner: "ClientEntity"


class TransactionEntity:
    def __init__(
        self,
        value: int,
        type_of: str,
        description: str,
        owner: "ClientEntity",
    ):
        self.value = value
        self.type_of = type_of
        self.description = description
        self.owner = owner

    @staticmethod
    def make_new(input: MakeNewInput):
        if input.type_of == "d":
            new_balance = input.owner.balance - input.value

            if new_balance < (input.owner.limit * -1):
                raise InconsistentBalanceException(
                    "The amount debited will exceed the client's limit"
                )

        return TransactionEntity(
            value=input.value,
            type_of=input.type_of,
            description=input.description,
            owner=input.owner,
        )


from rinha_de_backend_2024_q1.domain.entities.client_entity import ClientEntity
