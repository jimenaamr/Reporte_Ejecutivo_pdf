import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_detalle_pedidos = pd.read_csv('order_details.csv',sep = ";", encoding = "LATIN_1")
df_tipos_pizza = pd.read_csv('pizza_types.csv',sep = ",", encoding = "LATIN_1")

df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('one','1')
df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('One','1')
df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('two','2')
df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('Two','2')


df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('-','_')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('@','a')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('3','e')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('0','o')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace(' ','_')

df_detalle_pedidos['quantity'].fillna(1, inplace = True)
df_detalle_pedidos = df_detalle_pedidos[df_detalle_pedidos['pizza_id'].notna()]

lista_pedidos_validos = list(df_detalle_pedidos['pizza_id'])
lista_pizzas_validas = []

for pedido in lista_pedidos_validos:
    if pedido[-2:] == '_s' or pedido[-2:] == '_m' or pedido[-2:] == '_l':
        lista_pizzas_validas.append(pedido[:-2])
    elif pedido[-3:] == '_xl':
        lista_pizzas_validas.append(pedido[:-3])
    elif pedido[-4:] == '_xxl':
        lista_pizzas_validas.append(pedido[:-4])

lista_tipos_pizza = list(df_tipos_pizza['pizza_type_id'])
lista_cantidades_validas = list(df_detalle_pedidos['quantity'])

for i in range(len(lista_pedidos_validos)):
        lista_cantidades_validas[i] = int(lista_cantidades_validas[i])
        if lista_cantidades_validas[i] < 0:
            lista_cantidades_validas[i] *= -1

dic_cantidad_pedida = {}
for tipo in lista_tipos_pizza:
    dic_cantidad_pedida[tipo] = 0

for i in range(len(lista_pizzas_validas)):
    dic_cantidad_pedida[lista_pizzas_validas[i]] += lista_cantidades_validas[i]

df = pd.DataFrame([[key, dic_cantidad_pedida[key]] for key in dic_cantidad_pedida.keys()], columns=['Pizza', 'Cantidad pedida'])
df.to_csv('pizzas_pedidas_2016.csv')

ax = sns.barplot(x = 'Pizza', y = 'Cantidad pedida', data = df)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.savefig('grafica_pizzas_año.jpeg',bbox_inches='tight')

df_dinero = pd.read_csv('dinero_ganado_2016.csv',sep = ",", encoding = "LATIN_1")
fig = plt.figure(figsize=(12,5))
ax2 = sns.barplot(x = 'Pizza', y = 'Dinero Ganado', data = df_dinero)
plt.xticks(rotation=90, fontsize=5)
plt.savefig('grafica_dinero.jpeg',bbox_inches='tight')
