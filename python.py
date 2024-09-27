#write a program that convert specified dauys into years, weeks and days.
var= int(input("enter number of days"))
var_year= var//365

var_remaining_years = var%365

var_months= var_remaining_years//30

var_remaining_days= var_remaining_years%30

print("input no have {} years, {} months, {} days".format(var_year,var_months,var_remaining_days))

#write a program to calculate the distance