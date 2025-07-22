def three_sum_closest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return current_sum
                
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                
            if current_sum < target:
                left += 1
            else:
                right -= 1
                
    return closest_sum

def main():
    # 测试用例1：大数和小数混合，测试数值范围
    nums1 = [-1000, -500, 0, 500, 1000, 1500]
    target1 = 100
    result1 = three_sum_closest(nums1, target1)
    print("测试用例1: 大数和小数混合")
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {result1}")
    print(f"解释: 最接近的和是 0 (-500 + 0 + 500 = 0)")
    print()

    # 测试用例2：有多个可能的解，测试算法选择最接近的解
    nums2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target2 = 3
    result2 = three_sum_closest(nums2, target2)
    print("测试用例2: 多个相同的数")
    print(f"输入: nums = {nums2}, target = {target2}")
    print(f"输出: {result2}")
    print(f"解释: 最接近的和是 3 (1 + 1 + 1 = 3)")

if __name__ == "__main__":
    main()
