class Solution(object):
    def maxSubarrayLength(self, nums, k):
        from collections import defaultdict

        # Initialize the frequency dictionary and the left pointer of the window
        freq = defaultdict(int)
        left = 0
        max_length = 0

        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Add the current number to the frequency dictionary
            freq[nums[right]] += 1

            # If the frequency of the current number exceeds k, move the left pointer
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Update the maximum length of the good subarray
            max_length = max(max_length, right - left + 1)

        return max_length
