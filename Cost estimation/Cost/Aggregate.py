from construction_cost import Area, Cost, Total_cost

print("\n")
print("Total amount of Aggregate required=")


print(Area*0.608,"Ton")

# Amount of aggregate required per 1 ft2 = 0.608 ton & 7.4%

# -------------------------------------------------------------
print("Aggregate Amount=")
Aggregate=(7.4/100)*Total_cost
format_Aggregate="{0:.2f}".format(Aggregate)
print(format_Aggregate," Rs.")
