from treeset import TreeSet

# Ejemplo básico de uso
if __name__ == "__main__":
    my_set = TreeSet([5, 2, 8, 2, 3])  # Duplicados serán ignorados
    
    print("Elementos en orden:", list(my_set))
    print("Tamaño inicial:", my_set.size())
    
    my_set.add(7)
    print("Contiene 7?", my_set.contains(7))
    
    print("Ceiling de 4:", my_set.ceiling(4))
    print("Floor de 6:", my_set.floor(6))
    
    print("Primer elemento:", my_set.poll_first())
    print("Último elemento:", my_set.poll_last())
    
    print("Tamaño final:", my_set.size())
