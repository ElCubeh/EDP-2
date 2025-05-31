from treeset import TreeSet

if __name__ == "__main__":
    # PRUEBA 1: Operaciones básicas
    my_set = TreeSet([5, 2, 8, 2, 3])
    print("Elementos en orden:", list(my_set))
    print("Tamaño inicial:", my_set.size())
    
    my_set.add(7)
    print("¿Contiene 7?", my_set.contains(7))
    
    print("Ceiling de 4:", my_set.ceiling(4))
    print("Floor de 6:", my_set.floor(6))
    
    print("Primer elemento:", my_set.poll_first())
    print("Último elemento:", my_set.poll_last())
    
    print("Tamaño final:", my_set.size())
    
    # PRUEBA 2: Conjunto vacío
    empty_set = TreeSet()
    print("Primer elemento en conjunto vacío:", empty_set.poll_first())
    print("Último elemento en conjunto vacío:", empty_set.poll_last())
    
    # PRUEBA 3: Clonación
    cloned_set = my_set.clone()
    print("¿El conjunto original y el clonado son la misma instancia?", id(my_set) == id(cloned_set))
    print("Tamaño del conjunto original:", my_set.size())
    print("Tamaño del conjunto clonado:", cloned_set.size())
    print("Elementos del conjunto original:", list(my_set))
    print("Elementos del conjunto clonado:", list(cloned_set))
    
    # PRUEBA 4: Añadir None
    try:
        my_set.add(None)
    except TypeError:
        print("Se arrojó una excepción correctamente al intentar añadir None")

    # PRUEBA 5: Eliminar elemento inexistente
    print("¿Se puede eliminar un elemento que no existe?", my_set.remove(10))
    
    # PRUEBA 6: Primer/último en vacío
    empty_set = TreeSet()
    print("Primer elemento en un conjunto vacío:", empty_set.first())
    print("Último elemento en un conjunto vacío:", empty_set.last())
    
    # PRUEBA 7: Conjunto grande
    large_set = TreeSet(range(1, 10001))
    print("Tamaño del conjunto grande:", large_set.size())
    print("¿Contiene 5000?", large_set.contains(5000))
    print("Primer elemento en conjunto grande:", large_set.first())
    print("Último elemento en conjunto grande:", large_set.last())
    
    # PRUEBA 8: Poll en vacío
    print("Poll first en conjunto vacío:", empty_set.poll_first())
    print("Poll last en conjunto vacío:", empty_set.poll_last())
    
    # PRUEBA 9: Añadir múltiples elementos
    new_elements = [9, 10, 11]
    print("¿Se añaden varios elementos?", my_set.add_all(new_elements))
    print("Tamaño después de añadir varios elementos:", my_set.size())
    
    # PRUEBA 10: Iteradores en vacío
    print("Iterador ascendente en conjunto vacío:", list(empty_set))
    print("Iterador descendente en conjunto vacío:", list(empty_set.descending_iterator()))
