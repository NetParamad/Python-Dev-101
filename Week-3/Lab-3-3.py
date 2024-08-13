# รับชื่อสินค้า ราคาต่อหน่วย และจำนวน |  3 รายการสินค้า  | หากซื้อ 50 - 99 ชิ้น ให้ส่วนลด 5% ,
# หากซื้อ 100 ชิ้นขึ้นไป ให้ส่วนลด 10%  
# โดยให้แสดง  
# - ชื่อสินค้า ราคาต่อหน่วย จำนวน เป็นเงิน ส่วนลด  ....(เติมเองให้เหมาะสม ดูเข้าใจง่าย)
#     ..สินค้ารายการที่ 1.. 
# ..สินค้ารายการที่ 2..
# ..สินค้ารายการที่ 3..
# - รวมเป็นเงิน - vat(7%)  - รวมทั้งสิ้น (จัดทำให้สวยงาม)
def main(product1, price1, amount1, product2, price2, amount2, product3, price3, amount3):
    amount1 = int(amount1)
    amount2 = int(amount2)
    amount3 = int(amount3)
    price1 = int(price1)
    price2 = int(price2)
    price3 = int(price3)
    product1 = str(product1)
    product2 = str(product2)
    product3 = str(product3)


    amountAll = (amount1+amount2+amount3)
    total = ((price1*amount1)+(price2*amount2)+(price3*amount3))
    discount = 0
    if amountAll >= 100:
        discount = 10/100*total
    elif amountAll >= 50 and amountAll <= 99:
        discount = 5/100*total
    else:
        discount = 0
    total = total - discount


    print(f"{product1} ราคา {price1} จำนวน {amount1}")
    print(f"{product2} ราคา {price2} จำนวน {amount2}")
    print(f"{product3} ราคา {price3} จำนวน {amount3}")
    print(f"ส่วนลด {discount} ")
    print(f"vat(7%) {total*7/100} ")
    print(f"รวมเป็นเงิน {total} vat(7%) รวมทั้งสิ้น {total + (total*7/100)}")

product1 = input("ชื่อสินค้า 1 : ")
price1 = input(f"ราคาต่อหน่วย {product1} : ")
amount1 = input(f"จำนวน {product1} : ")

product2 = input("ชื่อสินค้า 2 : ")
price2 = input(f"ราคาต่อหน่วย {product2} : ")
amount2 = input(f"จำนวน {product2} : ")

product3 = input("ชื่อสินค้า 3 : ")
price3 = input(f"ราคาต่อหน่วย {product3} : ")
amount3 = input(f"จำนวน {product3} : ")

main(product1, price1, amount1, product2, price2, amount2, product3, price3, amount3)
    


