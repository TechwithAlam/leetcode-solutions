class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        need = {}
        window = {}

        for ch in p:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        ans = []

        for right in range(len(s)):

            window[s[right]] = window.get(s[right], 0) + 1

            if right - left + 1 > len(p):

                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            if right - left + 1 == len(p):

                if need == window:
                    ans.append(left)

        return ans

# Time: O(n + m)
# Space: O(1)