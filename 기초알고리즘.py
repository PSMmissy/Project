product_priceA = 20000
product_priceB = 30000
product_priceC = 35000



print("A 가격: %d" %product_priceA)
print("B 가격: %d" %product_priceB)
print("C 가격: %d \n" %product_priceC)

VAT = 0.2


vat_A = product_priceA*VAT 
vat_B = product_priceB*VAT
vat_C = product_priceC*VAT

print("A의 부가세: %d" %vat_A)
print("B의 부가세: %d" %vat_B)
print("C의 부가세: %d \n" %vat_C)

real_priceA = vat_A + product_priceA
real_priceB = vat_B + product_priceB
real_priceC = vat_C + product_priceC

print("A 실제가격: %d" %real_priceA)
print("B 실제가격: %d" %real_priceB)
print("C 실제가격: %d\n" %real_priceC)