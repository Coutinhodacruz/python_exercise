def searchRange(nums, target):
    def binarySearch(number, targetNumber, leftNumber, rightNumber):
        while leftNumber <= rightNumber:
            midNumber = (leftNumber + rightNumber) // 2
            if number[midNumber] == targetNumber:
                return midNumber
            elif number[midNumber] < targetNumber:
                leftNumber = midNumber + 1
            else:
                rightNumber = midNumber - 1
        return -1

    n = len(nums)
    idx = binarySearch(nums, target, 0, n - 1)
    if idx == -1:
        return [-1, -1]

    start, end = idx, idx
    left, right = 0, idx - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            start = mid
            right = mid - 1
        else:
            left = mid + 1

    left, right = idx + 1, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            end = mid
            left = mid + 1
        else:
            right = mid - 1

    return [start, end]
