class Producto:

    def __init__(self, nombre: str, precio: float | int, categoria: str, prioridad: int = 3, etiquetas: set = None):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.etiquetas = etiquetas if not None else set()
        self.prioridad = prioridad
        self.comprado = False


class ListaCompra:
    def __init__(self, productos: list[Producto] = None):
        self.productos = productos if not None else []

    def insertar(self, nombre: str, precio: float | int, categoria: str, prioridad: int = 3, etiquetas: list[str] = []):
        '''Añade un producto nuevo a la lista con los parámetros dados'''
        pdto = Producto(nombre, precio, categoria, etiquetas, prioridad)
        self.productos.append(pdto)

    def borrar(self, indice: int):
        '''Borra de la lista el producto que se encuentra en la posición indicada'''
        self.productos.pop(int)

    def actualizar_precio(self, indice: int, precio: float):
        '''Actualiza el precio del producto con el índice dado'''
        raise NotImplementedError

    def cambiar_estado(self, indice: int):
        '''Cambia el estado del producto con el índice dado entre comprado o no'''
        raise NotImplementedError

    def mostrar_productos(self, comprados: bool = True, etiquetas: list[str] = [], categorias: list[str] = []):
        '''
        Muestra por pantalla todos los productos con su información. Si un producto ya ha sido comprado, se marca con una x al comienzo.
        La prioridad se indicará mediante el uso de asteriscos (*), es decir, un artículo con prioridad 5 se representará mediante cinco asteriscos (*****).
        Si comprados es False, no se muestran los productos ya comprados.
        etiquetas es una tupla o lista con etiquetas o aclaraciones.
        Si está vacía, se muestran todos los productos. Si contiene alguna etiqueta, sólo se muestran los productos que tengan todas las etiquetas proporcionadas.
        Categorias es una lista con las categorías que se quieren obtener. Si está vacía, se muestran todos los productos. Si contiene alguna categoría, solo se muestran los productos cuya categoría esté contenida en la lista.

        Ejemplo en que sólo un producto ha sido comprado:
        >>> mostrar_productos()
        [x] Alimentación - Arroz integral - *** - 0.72 € - #risotto #arroz a la cubana
        [ ] Alimentación - Huevos - * - 1.20 € - #arroz a la cubana #tortilla 
        [ ] Cosméticos - Desmaquillante - ***** - 4.50 € - #fiesta #teatro

        >>> mostrar_productos(etiquetas=('arroz a la cubana'))
        [x] Alimentación - Arroz integral - *** - 0.72 € - #risotto #arroz a la cubana
        [ ] Alimentación - Huevos - * - 1.20 € - #arroz a la cubana #tortilla
        '''
        raise NotImplementedError
