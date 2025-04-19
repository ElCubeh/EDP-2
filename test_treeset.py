import unittest
from treeset import TreeSet

class TestTreeSet(unittest.TestCase):
    def setUp(self):
        # Inicializa un TreeSet con valores [5, 2, 8, 1, 3] antes de cada test
        self.set = TreeSet([5, 2, 8, 1, 3])

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el método add()
    # ---------------------------------------------------------------------------------------
    def test_add(self):
        self.assertTrue(self.set.add(4))   # Añade 4 (nuevo, debe retornar True)
        self.assertFalse(self.set.add(5))  # Intenta añadir 5 (ya existe, debe retornar False)
        self.assertEqual(self.set.size(), 6)  # Tamaño debería ser 5 iniciales + 1 nuevo = 6

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el método contains()
    # ---------------------------------------------------------------------------------------
    def test_contains(self):
        self.assertTrue(self.set.contains(2))   # 2 existe en el conjunto
        self.assertFalse(self.set.contains(10)) # 10 no existe

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el método ceiling()
    #   ceiling(e) = menor elemento >= e
    # ---------------------------------------------------------------------------------------
    def test_ceiling(self):
        self.assertEqual(self.set.ceiling(4), 5)  # El techo de 4 es 5 (primer valor mayor)
        self.assertEqual(self.set.ceiling(8), 8)  # El techo de 8 es él mismo

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el método floor()
    #   floor(e) = mayor elemento <= e
    # ---------------------------------------------------------------------------------------
    def test_floor(self):
        self.assertEqual(self.set.floor(4), 3)  # El piso de 4 es 3 (último valor menor)
        self.assertEqual(self.set.floor(1), 1)  # El piso de 1 es él mismo

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el método size()
    # ---------------------------------------------------------------------------------------
    def test_size(self):
        self.assertEqual(self.set.size(), 5)  # Tamaño inicial (5 elementos)
        self.set.add(10)                      # Añade un nuevo elemento
        self.assertEqual(self.set.size(), 6)  # Tamaño debería ser 6

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica los métodos first() y last()
    # ---------------------------------------------------------------------------------------
    def test_first_last(self):
        self.assertEqual(self.set.first(), 1)  # Primer elemento (mínimo) es 1
        self.assertEqual(self.set.last(), 8)   # Último elemento (máximo) es 8

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica los métodos pollFirst() y pollLast()
    #   Eliminan y retornan el primer/último elemento
    # ---------------------------------------------------------------------------------------
    def test_poll(self):
        self.assertEqual(self.set.poll_first(), 1)  # Elimina y retorna el primero (1)
        self.assertEqual(self.set.poll_last(), 8)   # Elimina y retorna el último (8)
        self.assertEqual(self.set.size(), 3)        # Tamaño después: 5 - 2 = 3

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el método clear()
    # ---------------------------------------------------------------------------------------
    def test_clear(self):
        self.set.clear()              # Vacía el conjunto
        self.assertTrue(self.set.is_empty())  # Debe estar vacío

    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica los iteradores (ascendente y descendente)
    # ---------------------------------------------------------------------------------------
    def test_iterators(self):
        asc = list(self.set)  # Iterador ascendente (in-order)
        self.assertEqual(asc, [1, 2, 3, 5, 8])  # Orden natural esperado
        
        desc = list(self.set.descending_iterator())  # Iterador descendente
        self.assertEqual(desc, [8, 5, 3, 2, 1])      # Orden inverso esperado
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el comportamiento de pollFirst() y pollLast() cuando el conjunto está vacío
    # ---------------------------------------------------------------------------------------
    def test_poll_empty(self):
        empty_set = TreeSet()
        self.assertIsNone(empty_set.poll_first())  # Debería devolver None cuando esté vacío
        self.assertIsNone(empty_set.poll_last())   # Debería devolver None cuando esté vacío
        
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el método clone()
    #   El método clone() debe crear una copia independiente del conjunto original.
    # ---------------------------------------------------------------------------------------
    def test_clone(self):
        cloned_set = self.set.clone()  # Clonamos el conjunto original
        self.assertNotEqual(id(self.set), id(cloned_set))  # Verifica que no sean la misma instancia
        self.assertEqual(self.set.size(), cloned_set.size())  # El tamaño debe ser igual
        self.assertEqual(list(self.set), list(cloned_set))   # Los elementos deben ser iguales
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el comportamiento al añadir elementos nulos
    #   El método add() debería manejar correctamente los valores nulos, si es que se permite.
    # ---------------------------------------------------------------------------------------
    def test_add_null(self):
        with self.assertRaises(TypeError):  # Se espera que arroje una excepción si el valor es nulo
            self.set.add(None)
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el comportamiento al intentar remover un elemento que no existe
    #   El método remove() debería devolver False cuando se intenta remover un elemento que no existe.
    # ---------------------------------------------------------------------------------------
    def test_remove_non_existing(self):
        self.assertFalse(self.set.remove(10))  # 10 no existe en el conjunto
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el comportamiento al intentar obtener el "first" y "last" en un conjunto vacío
    #   Los métodos first() y last() deben devolver None cuando el conjunto esté vacío.
    # ---------------------------------------------------------------------------------------
    def test_first_last_empty(self):
        empty_set = TreeSet()
        self.assertIsNone(empty_set.first())  # Debería devolver None cuando esté vacío
        self.assertIsNone(empty_set.last())   # Debería devolver None cuando esté vacío
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el comportamiento con conjuntos grandes
    #   Se verifica que el conjunto funcione correctamente incluso cuando tiene una gran cantidad de elementos.
    # ---------------------------------------------------------------------------------------
    def test_large_set(self):
        large_set = TreeSet(range(1, 10001))  # Crear un conjunto con 10,000 elementos
        self.assertEqual(large_set.size(), 10000)  # El tamaño debería ser 10,000
        self.assertTrue(5000 in large_set)  # Verificar que un elemento está contenido
        self.assertEqual(large_set.first(), 1)  # El primer elemento debe ser 1
        self.assertEqual(large_set.last(), 10000)  # El último elemento debe ser 10000
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica que poll_first() y poll_last() no devuelvan elementos si el conjunto está vacío
    #   Asegura que poll_first() y poll_last() devuelvan None si el conjunto está vacío
    # ---------------------------------------------------------------------------------------
    def test_poll_empty_set(self):
        empty_set = TreeSet()
        self.assertIsNone(empty_set.poll_first())  # Debería devolver None cuando esté vacío
        self.assertIsNone(empty_set.poll_last())   # Debería devolver None cuando esté vacío
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el comportamiento con add_all() para añadir múltiples elementos
    #   Añadir múltiples elementos a través de add_all() y comprobar que se añaden correctamente.
    # ---------------------------------------------------------------------------------------
    def test_add_all(self):
        new_elements = [9, 10, 11]
        self.assertTrue(self.set.add_all(new_elements))  # Añadir varios elementos
        self.assertEqual(self.set.size(), 8)  # Tamaño debería ser 8 (5 iniciales + 3 nuevos)
        self.assertTrue(self.set.contains(9))  # Verificar que 9 se haya añadido
        self.assertTrue(self.set.contains(10))  # Verificar que 10 se haya añadido
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA: Verifica el comportamiento de los iteradores cuando el conjunto está vacío
    #   Los iteradores deben funcionar correctamente incluso si el conjunto está vacío.
    # ---------------------------------------------------------------------------------------
    def test_iter_empty_set(self):
        empty_set = TreeSet()
        asc = list(empty_set)  # Iterador ascendente
        self.assertEqual(asc, [])  # El conjunto vacío debería devolver una lista vacía
        
        desc = list(empty_set.descending_iterator())  # Iterador descendente
        self.assertEqual(desc, [])  # El conjunto vacío debería devolver una lista vacía
    
if __name__ == '__main__':
    unittest.main()
