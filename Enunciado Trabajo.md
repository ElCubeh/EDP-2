Ejercicio:

Debe implementarse en Python una versión reducida de la clase TreeSet<E> de Java.  Asimismo, debe implementarse un conjunto de pruebas de dicha clase usando unittest. 

La implementación debe garantizar un coste de orden logaritmo en base 2 de n, para las operaciones de inserción, extracción y búsqueda y debe cubrir los métodos que se relacionan a continuación:

Constructor Summary

Constructors 

Constructor and Description

TreeSet()

Constructs a new, empty tree set, sorted according to the natural ordering of its elements.

TreeSet(Collection<? extends E > c)

Constructs a new tree set containing the elements in the specified collection, sorted according to the natural ordering of its elements.

 

Method Summary

Methods 

Modifier and Type

Method and Description

boolean

add(E  e)

Adds the specified element to this set if it is not already present.

boolean

addAll(Collection<? extends E > c)

Adds all of the elements in the specified collection to this set.

E

ceiling(E  e)

Returns the least element in this set greater than or equal to the given element, or null if there is no such element.

void

clear()

Removes all of the elements from this set.

Object

clone()

Returns a shallow copy of this TreeSet instance.

boolean

contains(Object o)

Returns true if this set contains the specified element.

Iterator<E>

descendingIterator()

Returns an iterator over the elements in this set in descending order.

E

first()

Returns the first (lowest) element currently in this set.

E

floor(E  e)

Returns the greatest element in this set less than or equal to the given element, or null if there is no such element.

E

higher(E  e)

Returns the least element in this set strictly greater than the given element, or null if there is no such element.

boolean

isEmpty()

Returns true if this set contains no elements.

Iterator<E>

iterator()

Returns an iterator over the elements in this set in ascending order.

E

last()

Returns the last (highest) element currently in this set.

E

lower(E  e)

Returns the greatest element in this set strictly less than the given element, or null if there is no such element.

E

pollFirst()

Retrieves and removes the first (lowest) element, or returns null if this set is empty.

E

pollLast()

Retrieves and removes the last (highest) element, or returns null if this set is empty.

boolean

remove(Object o)

Removes the specified element from this set if it is present.

int

size()

Returns the number of elements in this set (its cardinality).
