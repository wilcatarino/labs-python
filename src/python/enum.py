from enum import IntEnum


class SomeGreatType(IntEnum):
    SOMETHING = 1
    ANOTHERTHING = 2


print(SomeGreatType.SOMETHING)
print(SomeGreatType.SOMETHING.value)
print(SomeGreatType.ANOTHERTHING)
print(SomeGreatType.ANOTHERTHING.value)
