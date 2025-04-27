# 滑动窗口算法示例

def max_sum_subarray(arr, k):
    """
    计算长度为k的子数组的最大和
    示例：arr = [2, 1, 5, 1, 3, 2], k = 3
    输出：9 (子数组 [5, 1, 3] 的和最大)
    """
    if len(arr) < k:
        return -1
    
    # 计算第一个窗口的和
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # 滑动窗口
    for i in range(len(arr) - k):
        # 减去左边界的值，加上右边界的值
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def longest_substring_without_repeating(s):
    """
    找到不包含重复字符的最长子串
    示例：s = "abcabcbb"
    输出：3 (最长子串是 "abc")
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # 如果当前字符已经在集合中，移动左指针
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # 添加当前字符到集合
        char_set.add(s[right])
        # 更新最大长度
        max_length = max(max_length, right - left + 1)
    
    return max_length

def min_subarray_sum_greater_than_target(nums, target):
    """
    找到和大于等于target的最短子数组
    示例：nums = [2,3,1,2,4,3], target = 7
    输出：2 (子数组 [4,3] 的和为7)
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # 当当前和大于等于target时，尝试缩小窗口
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

def find_anagrams(s, p):
    """
    找到字符串中所有字母异位词的起始索引
    示例：s = "cbaebabacd", p = "abc"
    输出：[0, 6] (在索引0和6处找到"abc"的异位词)
    """
    if len(s) < len(p):
        return []
    
    p_count = [0] * 26
    s_count = [0] * 26
    result = []
    
    # 初始化p的字符计数
    for char in p:
        p_count[ord(char) - ord('a')] += 1
    
    # 初始化第一个窗口
    for i in range(len(p)):
        s_count[ord(s[i]) - ord('a')] += 1
    
    if s_count == p_count:
        result.append(0)
    
    # 滑动窗口
    for i in range(len(p), len(s)):
        # 移除左边界的字符
        s_count[ord(s[i - len(p)]) - ord('a')] -= 1
        # 添加右边界的字符
        s_count[ord(s[i]) - ord('a')] += 1
        
        if s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

# 测试示例
if __name__ == "__main__":
    # 测试最大子数组和
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"最大子数组和 (k={k}):", max_sum_subarray(arr, k))
    
    # 测试最长无重复字符子串
    s = "abcabcbb"
    print("最长无重复字符子串:", longest_substring_without_repeating(s))
    
    # 测试最小子数组和
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(f"和大于等于{target}的最短子数组长度:", min_subarray_sum_greater_than_target(nums, target))
    
    # 测试字母异位词
    s = "cbaebabacd"
    p = "abc"
    print(f"'{p}'的字母异位词起始索引:", find_anagrams(s, p)) 