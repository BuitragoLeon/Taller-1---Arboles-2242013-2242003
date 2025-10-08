# -------------------------------------------------------------
# Implementación de la librería BigTree en Python 
# Autor: Johan Felipe Prado Guerrero (2242004) y Juan Nicolás Buitrago (2242013)
# Materia: Estructura de Datos y Análisis de Algoritmos
# -------------------------------------------------------------

# Importar las clases necesarias de la librería
from bigtree import Node, print_tree, tree_to_dict

# -------------------------------------------------------------
# Crear la raíz del árbol
# -------------------------------------------------------------
# El nodo raíz representa la empresa
empresa = Node("Johan and Nicolas Company")

# -------------------------------------------------------------
# Agregar hijos al nodo raíz (nivel 1)
# -------------------------------------------------------------
# Cada hijo representa un departamento de la empresa
finanzas = Node("Departamento de Finanzas", parent=empresa)
recursos_humanos = Node("Departamento de Recursos Humanos", parent=empresa)
tecnologia = Node("Departamento de Tecnología", parent=empresa)
ventas = Node("Departamento de Ventas", parent=empresa)

# -------------------------------------------------------------
# Agregar hijos a algunos departamentos (nivel 2)
# -------------------------------------------------------------
# Finanzas tiene dos subáreas
Node("Contabilidad", parent=finanzas)
Node("Presupuesto", parent=finanzas)

# Recursos Humanos tiene dos subáreas
Node("Selección de Personal", parent=recursos_humanos)
Node("Capacitación", parent=recursos_humanos)

# Tecnología tiene tres subáreas
Node("Desarrollo de Software", parent=tecnologia)
Node("Infraestructura", parent=tecnologia)
Node("Soporte Técnico", parent=tecnologia)

# Ventas tiene dos subgrupos
Node("Ventas Nacionales", parent=ventas)
Node("Ventas Internacionales", parent=ventas)

# -------------------------------------------------------------
# Imprimir el árbol en pantalla
# -------------------------------------------------------------
print("Árbol Organizacional de la Empresa:\n")
print_tree(empresa)

