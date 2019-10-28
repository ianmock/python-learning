premium_ground = 125.00

def ground_shipping(weight):
  if weight <= 2:
    cost = 20 + weight * 1.50
  elif weight > 2 and weight <= 6:
    cost = 20 + weight * 3.00
  elif weight > 6 and weight <= 10:
    cost = 20 + weight * 4.00
  elif weight > 10:
    cost = 20 + weight * 4.75
  return cost

def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00
  elif weight > 10:
    cost = weight * 14.25
  return cost

def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) < premium_ground:
    cost = ground_shipping(weight)
    ship_method = "ground shipping"
  elif drone_shipping(weight) < ground_shipping(weight) < premium_ground :
    cost = drone_shipping(weight)
    ship_method = "drone shipping"
  elif premium_ground < ground_shipping(weight) < drone_shipping(weight):
    cost = premium_ground
    ship_method = "premium shipping"
  return "The cheapest shipping method is " + str(ship_method) + " and will cost $" + str(cost) + " ."

print(ground_shipping(8.4))
print(drone_shipping(1.5))
print(cheapest_shipping(41.5))