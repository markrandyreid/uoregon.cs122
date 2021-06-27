'''
CIS 122 Summer 2021 Assignment 1
Author: Mark Randy Reid
Credit: No Partner
Description: Introduction to programming problem set uses Python numeric data types and 
operations to solve a variety of small problems. 
'''

# Question 1
# Calculate the number of red hats and total cost for both red and blue hats
import math

print('*** Question 1: Calculate total hat cost ***')

cost_red = 12
cost_blue = 5
total_hats = 65
total_blue = math.ceil(total_hats/2) #Part B bug fix: Change....
total_red = total_hats-total_blue
total_red_cost = cost_red * total_red
total_blue_cost = cost_blue * total_blue
total_cost = total_red_cost+total_blue_cost
print('Total Hat Cost:',total_cost)
print()

print('*** Question 2: Steps per time internal***')

hours_day = 24
minutes_day = hours_day*60
seconds_day = minutes_day*60

Daily_steps_1 = 5000
Per_second_ds1 = Daily_steps_1/seconds_day
Per_minute_ds1 = Daily_steps_1/minutes_day
Per_hour_ds1 = Daily_steps_1/hours_day
print('Daily Steps:', Daily_steps_1,'\nPer second:', Per_second_ds1, '\nPer minute', Per_minute_ds1, '\nPer Hour', Per_hour_ds1)

Daily_steps_2 = 10000
Per_second_ds2 = Daily_steps_2/seconds_day
Per_minute_ds2 = Daily_steps_2/minutes_day
Per_hour_ds2 = Daily_steps_2/hours_day
print('\nDaily Steps:', Daily_steps_2,'\nPer second:', Per_second_ds2, '\nPer minute', Per_minute_ds2, '\nPer Hour', Per_hour_ds2)

Daily_steps_3 = 50000
Per_second_ds3 = Daily_steps_3/seconds_day
Per_minute_ds3 = Daily_steps_3/minutes_day
Per_hour_ds3 = Daily_steps_3/hours_day
print('\nDaily Steps:', Daily_steps_3,'\nPer second:', Per_second_ds3, '\nPer minute', Per_minute_ds3, '\nPer Hour', Per_hour_ds3)

Daily_steps_4 = 100000
Per_second_ds4 = Daily_steps_4/seconds_day
Per_minute_ds4 = Daily_steps_4/minutes_day
Per_hour_ds4 = Daily_steps_4/hours_day
print('\nDaily Steps:', Daily_steps_4,'\nPer second:', Per_second_ds4, '\nPer minute', Per_minute_ds4, '\nPer Hour', Per_hour_ds4)


print('\n*** Question 3: Distance Around Circular Stationary Irrigation System***')
r = 300
circular_irrigation_distance = math.pi*r**2
farm_system_total = 4
check_per_day = 3
check_per_week = 5
miles_feet = 5280
total_distance_feet = circular_irrigation_distance*farm_system_total*check_per_day*check_per_week
total_distance_miles = total_distance_feet/miles_feet
print('Weekly Distance (ft):',round(total_distance_feet,2),'\nWeekly Distance (miles):',round(total_distance_miles,2))

