# REPORTE EJECUTIVO PDF

En este repositorio se encuentran los archivos necesarios para hacer un pdf con un reporte ejecutivo acerca de las ventas de Maven Pizzas en 2016.

## Archivos Adjuntados

- order_details.csv: Detalles sobre los pedidos que se han realizado a lo largo del año. En él encontramos el identificador del pedido, el identificador de la pizza pedida y la cantidad pedida. Deberemos limpiar los datos, ya que no están en el formato correcto.

- pizza_types.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su nombre completo, la categoría en la que está y los ingredientes necesarios para prepararla.

- pizzas.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su tipo, su tamaño y su precio.

- pizzas_pedidas_2016.csv: Dataframe creado tras ejecutar el archivo pizzas_año.py. Te ofrece un cálculo de cada tipo de pizza a lo largo de todo 2016.

- dinero_ganado_2016.csv: Dataframe con el dinero ganado durante el año 2016 por la venta de cada tipo de pizza.

- requirements.txt: En este archivo encontramos las librerías que se necesitan instalar para poder ejecutar los archivos.

- crear_pdf.py: En este archivo encontramos el código necesario para crear el pdf del reporte ejecutivo de la pizzería. En él añadimos una predicción de los ingredientes que se tendrán que comprar cada semana, una gráfica con el dinero ganado por cada pizza en el año, que se obtiene de dinero_ganado_2016.csv y una gráfica con los pedidos de cada tipo de pizza en todo el año, que se obtiene de pizzas_pedidas_2016.csv.

- pizzas_año.py: Código neceario para crear un dataframe con los tipos de pizza que hay y el número que se han pedido de cada tipo a lo largo del año. También crea las gráficas con los datos de pizzas_pedidas_2016.csv y dinero_ganado_2016.csv y las guarda como imágenes.

- reporte_pizzas.pdf: Reporte ejecutivo en formato pdf de la pizzería Maven Pizzas en el año 2016 creado al ejecutar crear_pdf.py.

- tabla1.jpeg: Imagen de la predicción de ingredientes añadida al pdf.

- tabla2.jpeg: Imagen de la predicción de ingredientes añadida al pdf.

- logo_pizza.jpeg: Imagen del logo de la pizzería añadida al pdf.

- grafica_pizzas_año.jpeg: Imagen de la gráfica con los datos de pizzas_pedidas_2016.csv añadida al pdf.

- grafica_dinero.jpeg: Imagen de la gráfica con los datos de dinero_ganado_2016.csv añadida al pdf.

## Modo de Ejecución

1- Instalar el requirements.txt

2- Ejecutar el archivo pizzas_año.py para obtener el csv pizzas_pedidas_2016.csv, grafica_pizzas_año.jpeg y grafica_dinero.jpeg

3- Ejecutar el archivo crear_pdf.py para obetener el reporte ejecutivo en formato pdf.