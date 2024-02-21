import dataclasses


@dataclasses.dataclass
class TextFormUser:
    full_name: str
    user_email: str
    current_city: str
    current_street: str
    current_house: str
    current_flat: str
    permanent_city: str
    permanent_street: str
    permanent_house: str
    permanent_flat: str


Alex = TextFormUser(
    full_name="Alex Davydov",
    user_email="Gredtx@gmail.com",
    current_city="Stavropol",
    current_street="South",
    current_house="88 b",
    current_flat=" 12 a",
    permanent_city="Moscow",
    permanent_street="Bolshaya Sadovaya",
    permanent_house="302-bis",
    permanent_flat=" 50",
)
