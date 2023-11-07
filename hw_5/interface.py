import zope.interface


class PaginatorInterface(zope.interface.Interface):
    """Интерфейс класса для пагинации списка элементов"""

    object_list = zope.interface.Attribute("""Список элементов для пагинации""")
    chunk_size = zope.interface.Attribute("""Количество элементов в одном чанке""")

    def paginate():
        """Получение спагинированного списка"""


@zope.interface.implementer(PaginatorInterface)
class SimplePaginator:
    def __init__(self, object_list: list, chunk_size: int):
        self.object_list = object_list
        self.chunk_size = chunk_size

    def paginate(self):
        return [self.object_list[i:i+self.chunk_size] for i in range(0, len(self.object_list), self.chunk_size)]


print(type(PaginatorInterface))    # <class 'zope.interface.interface.InterfaceClass'>
print(PaginatorInterface.__doc__)    # Интерфейс класса для пагинации списка элементов
print(PaginatorInterface.implementedBy(SimplePaginator))    # True

simple_paginator = SimplePaginator([i for i in range(100)], 10)
print(PaginatorInterface.providedBy(simple_paginator))    # True

print(simple_paginator.paginate())
