from reportlab.pdfgen import canvas

c = canvas.Canvas('reporte_pizzas.pdf')

c.setFont('Times-BoldItalic',40)
c.drawString(100, 720, "REPORTE EJECUTIVO")
c.drawString(120, 660, "DE MAVEN PIZZAS")

c.drawImage('logo_pizza.jpeg',110,200,width=400,height=400)

c.setFont('Courier',12)
c.drawString(50,50, 'Jimena Monteagudo Ruiz')
c.drawString(510,50, '20/11/22')

c.showPage()

c.setFont('Helvetica-Bold',15)
c.setFillColorRGB(0, 0, 1)
c.drawString(210,720,'INTRODUCCIÓN INFORME')
c.setFillColorRGB(0, 0, 0)

intro = c.beginText(50,680)
intro.setFont('Times-Roman',12)
intro.textLines('Con este reporte ejecutivo se pretende dar a conocer algunos datos relevantes sobre esta empresa.\nSe han recogido datos durante un año acerca de los tipos de pizza, los tamaños y las cantidades de cada\npedido que se realizaba en nuestra pizzería.\nDe esta forma, hemos conseguido calcular una estimación bastante precisa sobre las cantidades que se\ndeberán comprar semanalmente de cada tipo de ingrediente.\nAsimismo, se incluye un estudio acerca de el número de pizzas de cada tipo que se piden por semana.')
c.drawText(intro)

c.setFont('Helvetica-Bold',15)
c.setFillColorRGB(0, 0, 1)
c.drawString(180,540, 'PREDICCIÓN COMPRA SEMANAL')

tabla_intro = c.beginText(50,500)
tabla_intro.setFont('Times-Roman',12)
c.setFillColorRGB(0, 0, 0)
tabla_intro.textLines('A continuación se muestra una tabla con la predicción semanal de cuántos ingredientes debemos comprar.\n En la columna de la derecha encontramos todos los ingredientes disponbles que hay en la pizzería.\nEn la columna de la derecha encontramos la cantidad a comprar de cada uno de ellos.')
c.drawText(tabla_intro)

c.drawImage('tabla1.jpeg',110,50,width=150,height=400)
c.drawImage('tabla2.jpeg',310,50,width=150,height=400)
c.drawString(550,30, '1')

c.showPage()

c.setFont('Helvetica-Bold',15)
c.setFillColorRGB(0, 0, 1)
c.drawString(190,720, 'PIZZAS PEDIDAS EN EL AÑO')

grafica1 = c.beginText(50,680)
grafica1.setFont('Times-Roman',12)
c.setFillColorRGB(0, 0, 0)
grafica1.textLines('En la siguiente gráfica se ha realizado un estudio acerca de cuántas pizzas se han comprado de\ncada tipo a lo largo de 2016.\nDe esta forma hemos llegado a dibujar esta gráfica. En el eje x podemos observar los distintos tipos\nde pizzas disponibles. Mientras que en el eje y observamos la cantidad que se compra de cada una\na la semana.')
c.drawText(grafica1)

c.drawImage('grafica_pizzas_año.jpeg',85,120,width=400,height=400)
c.drawString(550,30, '2')

c.showPage()

c.setFont('Helvetica-Bold',15)
c.setFillColorRGB(0, 0, 1)
c.drawString(190,720, 'DINERO GANADO POR PIZZA')

grafica2 = c.beginText(50,680)
grafica2.setFont('Times-Roman',12)
c.setFillColorRGB(0, 0, 0)
grafica2.textLines('En la siguiente gráfica se han recogido los datos del dinero ganado con cada pizza durante el año 2016.\nEn el eje x se presentan los distintos tipos de pizzas con sus tamaños.\nEn el eje y vemos la cantidad de dinero ganada con cada una de ellas.')
c.drawText(grafica2)

c.drawImage('grafica_dinero.jpeg',30,250,width=500,height=300)
c.drawString(550,30, '3')

c.save()