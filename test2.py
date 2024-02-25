from dataclasses import dataclass

# Class material


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
    def __init__(self, input: class_in) -> None:
        self.input = input


mat1 = material(1, "name ")

po1_input = class_in()
class_in.name = "Attila"
class_in.material = mat1

po1 = Purchase_Order(po1_input)

print(po1.bemenet.name)
