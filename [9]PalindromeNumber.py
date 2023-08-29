class Solution:
    def isPalindrome(self, x: int) -> bool:
        toList = [*str(x)]

        if len(toList) == 2:
            return True if toList[0] == toList[1] else False

        if len(toList) % 2 == 0:
            mid = len(toList) // 2
            suffix = toList[mid:len(toList)]
            preffix = toList[0:mid]
        else:
            mid = len(toList) // 2
            suffix = toList[mid:len(toList)]
            preffix = toList[0:mid+1]
        return suffix[::-1] == preffix


a = Solution()
print(a.isPalindrome(1001))
