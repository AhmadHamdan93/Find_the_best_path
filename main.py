import t1
import t2

begging_counter = 133859
finishing_counter = 135964  # 3500 > 1200 --- 2300

distances = [50,]#51,52,53,54,55,56,57,58,59,60, 110,111,112,113,114,115,116,117,118,119,120, 170,172,175]
target_distance = 1384
number_of_days = 20

# find first sol
t1.target_sum = target_distance
t1.allowed_numbers = distances
t1.array_size = number_of_days

best_individual_1 = t1.genetic_algorithm()

# =----------------

# Print the result
print("Array 1:", best_individual_1)
sum_of_array_1 = sum(best_individual_1)
print("Sum: 1", sum_of_array_1)



# find second array
t2.target_sum = finishing_counter - begging_counter - sum_of_array_1
t2.number_range = (10, 1000)
t2.array_size = number_of_days - 1

best_individual_2 = t2.genetic_algorithm_2()

# Print the result
print("Array: 2", best_individual_2)
sum_of_array_2 = sum(best_individual_2)
print("Sum: 2", sum_of_array_2)

print('------------------------')
print('------------------------')
print('------------------------')
result = begging_counter
print('day  ','begging','---->','finishing')
print()
for i in range(number_of_days):
    print(i+1,'):  ',result,'---->',result + best_individual_1[i])
    result = result + best_individual_1[i]
    if i < number_of_days -1:
        result = result + best_individual_2[i]
