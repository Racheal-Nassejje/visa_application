#Solar Energy Usage Tracker

#Data Types and Variables
#Define variation for daily solar energy generated and consumed
daily_energy_generated = float(input("Enter the daily solar energy generated (in kmh): "))
daily_energy_cosumed = float(input("Enter the daily solar energy comsumed (in kwh): "))

#Basic Operators 
#Calculate the energy surplus or deficit
energy_balance = daily_energy_generated - daily_energy_cosumed

#Boolean_values
#Determine if the household is energy efficient (consumption <= 80% of generation)
efficiency_threshold = 0.8 * daily_energy_generated
is_energy_efficient = daily_energy_cosumed <= efficiency_threshold

#Output the results
print("\n--- Solar Energy Usage Report ---")
print (f" Daily energy generated: {daily_energy_generated} kwh")
print (f"Daily energy consumed: {daily_energy_cosumed} kwh")
print(f"Energy balance (surplus/deficit): {energy_balance} kwh")
