from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)
goblin = Actor(
    char="g",
    color=(63, 127, 63),
    name="Goblin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)
zardo = Actor(
    char="Z",
    color=(0, 127, 0),
    name="Lizhard",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=24, base_defense=3, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=1500),
)
drake = Actor(
    char="d",
    color=(0, 127, 0),
    name="young drake",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=24, base_defense=6, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=10000),
)
vampirespawn = Actor(
    char="v",
    color=(0, 127, 0),
    name="Vampire Broodling",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=42, base_defense=0, base_power=16),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=2500),
)
vampire = Actor(
    char="V",
    color=(0, 127, 0),
    name="Vampire",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=56, base_defense=8, base_power=18),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=2500),
)
ogre = Actor(
    char="O",
    color=(0, 127, 0),
    name="Ogre",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=80, base_defense=6, base_power=32),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50000),
)


confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)
rusty_saber = Item(
    char="/", color=(0, 191, 255), name="A rusty Saber", equippable=equippable.Saber()
)

longsword = Item(
    char="/", color=(0, 191, 255), name="A rusty Saber", equippable=equippable.Saber()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Longsword())



leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)
plate_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="A Set of Plate Mail..",
    equippable=equippable.PlateMail(),
)
bronze_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="A Set of Plate Mail..",
    equippable=equippable.BronzeMail(),
)
chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)
