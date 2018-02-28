from xml.dom import minidom
arbol_dom = minidom.parse('C:\\Users\\ASIR\\Desktop\\bookstore.xml');

lista = arbol_dom.getElementsByTagName("bookstore");

for obj in lista:
	print("Nombre: "+obj.getAttribute("name"));
	libros=obj.getElementsByTagName("book");
	for libro in libros:
		print("\tCategoria: "+libro.getAttribute("category"));
		print("\tIdioma: "+libro.getElementsByTagName("title")[0].getAttribute("lang"));
		print("\tTítulo: "+libro.getElementsByTagName("title")[0].firstChild.data);
		print("\tAño: "+libro.getElementsByTagName("year")[0].firstChild.data);
		print("\tPrecio: "+libro.getElementsByTagName("price")[0].firstChild.data);
		autores=libro.getElementsByTagName("author");
		for autor in autores:
			print("\t\tEscritor: "+libro.getElementsByTagName("writer")[0].firstChild.data);
			print("\t\tResumer: "+libro.getElementsByTagName("resumer")[0].firstChild.data);
		