class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None	# puntero al nodo padre en el árbol
        self.height = 1	 # altura del nodo en el árbol (dist. máxima a hoja) NUEVO PARA AVL

class AVLTree:
    def __init__(self):
        self.root=None

    def __repr__(self):
        if self.root==None: return ''
        content='\n' # contendrá el string final
        cur_nodes=[self.root] # todos los nodos en el nivel actual
        cur_height=self.root.height # altura de los nodos en el nivel actual
        sep=' '*(2**(cur_height-1)) # separador de tamaño variable entre elementos
        while True:
            cur_height+=-1 # decrementa la altura actual
            if len(cur_nodes)==0: break
            cur_row=' '
            next_row=''
            next_nodes=[]

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n==None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None,None])
                    continue

                if n.value!=None:       
                    buf=' '*((5-len(str(n.value)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.value),buf)+sep
                else:
                    cur_row+=' '*5+sep

                if n.left_child!=None:  
                    next_nodes.append(n.left_child)
                    next_row+=' /'+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

                if n.right_child!=None: 
                    next_nodes.append(n.right_child)
                    next_row+='\ '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes=next_nodes
            sep=' '*(len(sep)/2) # reducir tamaño del separador a la mitad
        return content

    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
                cur_node.left_child.parent=cur_node # establecer padre
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value,cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
                cur_node.right_child.parent=cur_node # establecer padre
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print ("¡El valor ya existe en el árbol!")

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print ('%s, h=%d'%(str(cur_node.value),cur_node.height))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)

    def delete_value(self,value):
        return self.delete_node(self.find(value))

    def delete_node(self,node):
        ## -----
        # Mejoras desde la lección anterior

        # Protección contra eliminación de nodos no existentes
        if node==None or self.find(node.value)==None:
            print ("¡Nodo a eliminar no encontrado en el árbol!")
            return None 
        ## -----

        # devuelve el nodo con valor mínimo en el árbol con raíz en el nodo de entrada
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current

        # devuelve el número de hijos del nodo especificado
        def num_children(n):
            num_children=0
            if n.left_child!=None: num_children+=1
            if n.right_child!=None: num_children+=1
            return num_children

        # obtener el padre del nodo a eliminar
        node_parent=node.parent

        # obtener el número de hijos del nodo a eliminar
        node_children=num_children(node)

        # dividir la operación en diferentes casos basados en la
        # estructura del árbol y el nodo a eliminar

        # CASO 1 (nodo sin hijos)
        if node_children==0:

            if node_parent!=None:
                # eliminar referencia al nodo desde el padre
                if node_parent.left_child==node:
                    node_parent.left_child=None
                else:
                    node_parent.right_child=None
            else:
                self.root=None

        # CASO 2 (nodo con un solo hijo)
        if node_children==1:

            # obtener el nodo hijo único
            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child

            if node_parent!=None:
                # reemplazar el nodo a eliminar con su hijo
                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child

            # corregir el puntero del padre en el nodo
            child.parent=node_parent

        # CASO 3 (nodo con dos hijos)
        if node_children==2:

            # obtener el sucesor inorder del nodo eliminado
            successor=min_value_node(node.right_child)

            # copiar el valor del sucesor inorder al nodo que
            # contenía el valor que queríamos eliminar
            node.value=successor.value

            # eliminar el sucesor inorder ahora que su valor fue
            # copiado al otro nodo
            self.delete_node(successor)

            # salir de la función para no llamar a _inspect_deletion dos veces
            return

        if node_parent!=None:
            # ajustar la altura del padre del nodo actual
            node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))

            # comenzar a recorrer el árbol hacia arriba verificando si hay
            # secciones que ahora incumplen las reglas de equilibrio AVL
            self._inspect_deletion(node_parent)

    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value==cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search(value,cur_node.right_child)
        return False 

    # Funciones añadidas para AVL...

    def _inspect_insertion(self,cur_node,path=[]):
        if cur_node.parent==None: return
        path=[cur_node]+path

        left_height =self.get_height(cur_node.parent.left_child)
        right_height=self.get_height(cur_node.parent.right_child)

        if abs(left_height-right_height)>1:
            path=[cur_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return

        new_height=1+cur_node.height 
        if new_height>cur_node.parent.height:
            cur_node.parent.height=new_height

        self._inspect_insertion(cur_node.parent,path)

    def _inspect_deletion(self,cur_node):
        if cur_node==None: return

        left_height =self.get_height(cur_node.left_child)
        right_height=self.get_height(cur_node.right_child)

        if abs(left_height-right_height)>1:
            y=self.taller_child(cur_node)
            x=self.taller_child(y)
            self._rebalance_node(cur_node,y,x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self,z,y,x):
        if y==z.left_child and x==y.left_child:
            self._right_rotate(z)
        elif y==z.left_child and x==y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y==z.right_child and x==y.right_child:
            self._left_rotate(z)
        elif y==z.right_child and x==y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: ¡Configuración de nodos z,y,x no reconocida!')

    def _right_rotate(self,z):
        sub_root=z.parent 
        y=z.left_child
        t3=y.right_child
        y.right_child=z
        z.parent=y
        z.left_child=t3
        if t3!=None: t3.parent=z
        y.parent=sub_root
        if y.parent==None:
                self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y        
        z.height=1+max(self.get_height(z.left_child),
            self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),
            self.get_height(y.right_child))

    def _left_rotate(self,z):
        sub_root=z.parent 
        y=z.right_child
        t2=y.left_child
        y.left_child=z
        z.parent=y
        z.right_child=t2
        if t2!=None: t2.parent=z
        y.parent=sub_root
        if y.parent==None: 
            self.root=y
        else:
            if y.parent.left_child==z:
                y.parent.left_child=y
            else:
                y.parent.right_child=y
        z.height=1+max(self.get_height(z.left_child),
            self.get_height(z.right_child))
        y.height=1+max(self.get_height(y.left_child),
            self.get_height(y.right_child))

    def get_height(self,cur_node):
        if cur_node==None: return 0
        return cur_node.height

    def taller_child(self,cur_node):
        left=self.get_height(cur_node.left_child)
        right=self.get_height(cur_node.right_child)
        return cur_node.left_child if left>=right else cur_node.right_child
