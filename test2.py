from dataclasses import dataclass


class material:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name


structure_def = {
    "name": str,
    "material": material
}

"""
class class_in:
    def __init__(self, name, material) -> None :
        self.name = name
        self.material = material
"""


@dataclass()
class class_in:
    name = str
    material = material


class Purchase_Order:
    def __init__(self, bemenet: class_in) -> None:
        self.bemenet = bemenet


mat1 = material(1, "name ")

po1_bemenet = class_in()
class_in.name = "Attila"
class_in.material = mat1

po1 = Purchase_Order(po1_bemenet)

print(po1.bemenet.name)
