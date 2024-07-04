# name = ["a","b","c","d"]
# print(name[1])
# print(type(name))
#수열 만들기
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers(range(10)))
# print(list(range(0, 10, 2)))

nums = [1,2,3,4,5]
nums = list(range(1,6))
sum_nums= nums[0]+nums[1]+nums[2]+nums[3]+nums[4]
average = sum_nums/len(nums)
print(average)

# 리스트에 요소 추가하기
num_list = [1,2,3,4,5]
num_list.append(6)
num_list.remove(5)
print(num_list)