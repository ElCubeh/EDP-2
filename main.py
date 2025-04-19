from treeset import TreeSet

# Ejemplo básico de uso
if __name__ == "__main__":
    # ---------------------------------------------------------------------------------------
    # PRUEBA 1: Crear un conjunto y realizar operaciones básicas
    # ---------------------------------------------------------------------------------------
    my_set = TreeSet([5, 2, 8, 2, 3])  # Duplicados serán ignorados
    print("Elementos en orden:", list(my_set))
    print("Tamaño inicial:", my_set.size())
    
    my_set.add(7)
    print("¿Contiene 7?", my_set.contains(7))
    
    print("Ceiling de 4:", my_set.ceiling(4))
    print("Floor de 6:", my_set.floor(6))
    
    print("Primer elemento:", my_set.poll_first())
    print("Último elemento:", my_set.poll_last())
    
    print("Tamaño final:", my_set.size())
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA 2: Comportamiento de un conjunto vacío
    # ---------------------------------------------------------------------------------------
    empty_set = TreeSet()
    print("Primer elemento en conjunto vacío:", empty_set.poll_first())  # Debería devolver None
    print("Último elemento en conjunto vacío:", empty_set.poll_last())   # Debería devolver None
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA 3: Clonar el conjunto y verificar que son instancias diferentes
    # ---------------------------------------------------------------------------------------
    cloned_set = my_set.clone()  # Clonamos el conjunto
    print("¿El conjunto original y el clonado son la misma instancia?", id(my_set) == id(cloned_set))  # Debería ser False
    print("Tamaño del conjunto original:", my_set.size())
    print("Tamaño del conjunto clonado:", cloned_set.size())
    print("Elementos del conjunto original:", list(my_set))
    print("Elementos del conjunto clonado:", list(cloned_set))
    
    # ---------------------------------------------------------------------------------------
    # PRUEBA 4: Intentar añadir None y manejar la excepción
    # ---------------------------------------------------------------------------------------
    try:
        my_set.add(None)  # Intentamos añadir None
    except TypeError:
        print("Se arrojó una excepción correctamente al intentar añadir None")

    # ---------------------------------------------------------------------------------------
    # PRUEBA 5: Comportamiento al intentar eliminar un elemento que no existe
    # ---------------------------------------------------------------------------------------
    print("¿Se puede eliminar un elemento que no existe?", my_set.remove(10))  # 10 no existe en el conjunto

    # ---------------------------------------------------------------------------------------
    # PRUEBA 6: Obtener el primer y último elemento en un conjunto vacío
    # ---------------------------------------------------------------------------------------
    empty_set = TreeSet()
    print("Primer elemento en un conjunto vacío:", empty_set.first())  # Debería devolver None
    print("Último elemento en un conjunto vacío:", empty_set.last())   # Debería devolver None

    # ---------------------------------------------------------------------------------------
    # PRUEBA 7: Comportamiento con conjuntos grandes
    # ---------------------------------------------------------------------------------------
    large_set = TreeSet(range(1, 10001))  # Crear un conjunto con 10,000 elementos
    print("Tamaño del conjunto grande:", large_set.size())  # Debería ser 10,000
    print("¿Contiene 5000?", 5000 in large_set)  # Verificar que un elemento está contenido
    print("Primer elemento en conjunto grande:", large_set.first())  # El primer elemento debe ser 1
    print("Último elemento en conjunto grande:", large_set.last())  # El último elemento debe ser 10000

    # ---------------------------------------------------------------------------------------
    # PRUEBA 8: Verificar que poll_first() y poll_last() no devuelvan elementos si el conjunto está vacío
    # ---------------------------------------------------------------------------------------
    print("Poll first en conjunto vacío:", empty_set.poll_first())  # Debería devolver None
    print("Poll last en conjunto vacío:", empty_set.poll_last())   # Debería devolver None

    # ---------------------------------------------------------------------------------------
    # PRUEBA 9: Comportamiento de add_all() para añadir múltiples elementos
    # ---------------------------------------------------------------------------------------
    new_elements = [9, 10, 11]
    print("¿Se añaden varios elementos?", my_set.add_all(new_elements))  # Añadir varios elementos
    print("Tamaño después de añadir varios elementos:", my_set.size())  # Tamaño debería haber aumentado

    # ---------------------------------------------------------------------------------------
    # PRUEBA 10: Comportamiento de los iteradores cuando el conjunto está vacío
    # ---------------------------------------------------------------------------------------
    print("Iterador ascendente en conjunto vacío:", list(empty_set))  # Debería devolver lista vacía
    print("Iterador descendente en conjunto vacío:", list(empty_set.descending_iterator()))  # Debería devolver lista vacía
