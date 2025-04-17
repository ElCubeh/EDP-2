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

if __name__ == '__main__':
    unittest.main()
