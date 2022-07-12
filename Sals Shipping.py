# Ground Shipping
"""
Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Ground Shipping Premium
Flat charge: $125.00
"""

"""
Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

"""
weight = 1.5 # weight of package to be sent
ground_premium_shipping = 125
print("Premium Ground Shipping is: " + str(ground_premium_shipping))
print("Ground Shipping")

if weight <=2:
    print(weight * 1.5 + 20)
elif weight > 2 and weight <= 6:
    print(weight * 3 + 20)
elif weight > 6 and weight <= 10:
    print(weight * 4 + 20)
elif weight > 10:
    print(weight * 4.75 + 20)

print("Drone Shipping")
if weight <=2:
    print(round(weight * 4.5,2))
elif weight > 2 and weight <= 6:
    print(round(weight * 9,2))
elif weight > 6 and weight <= 10:
    print(round(weight * 12,2))
elif weight > 10:
    print(round(weight * 14.25,2))