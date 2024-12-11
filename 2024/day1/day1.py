nums1 = []
nums2 = []
total_diff = 0
sim_score = 0

with open('/Users/tyleremanuel/Documents/Advent-of-Code/2024/day1/input.txt', 'r') as file:
    for line in file:
        nums = line.split("   ")
        nums1.append(nums[0].strip())
        nums2.append(nums[1].strip())

nums1.sort()
nums2.sort()

for i in range(len(nums1)):
    total_diff += abs(int(nums1[i]) - int(nums2[i]))

print(total_diff)

nums_map = {}
for num1 in nums1:
    nums_map[num1] = 0

for num2 in nums2:
    if num2 in nums_map:
        nums_map[num2] += 1

for num in nums1:
    sim_score += int(num) * int(nums_map[num])

print(sim_score)