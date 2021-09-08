


base_price = 29500

#get data form
# get sql

price_data_list = []
for item in range(0,1500,250):
    price_data_list.append(base_price + item)
for item in range(-250,-1500,-250):
    price_data_list.append(base_price + item)


sql_list = []
price_data_list.sort()
print(price_data_list)
for item in price_data_list:
    str_item = ("js{0} FLOAT,".format(item))
    f = "".join(str_item.split("'"))
    sql_list.append(f)

f_sql = " ".join(str(i) for i in sql_list )
print(f_sql)



