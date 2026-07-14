class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = {}
        window = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = 0
        need_count = len(need)

        left = 0

        res = ""
        res_len = float("inf")

        for right in range(len(s)):

            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == need_count:

                if right - left + 1 < res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return res


# Time: O(m + n)
# Space: O(m + n)


# 🧠 Memory Trick
# need = What we must have
# window = What we currently have

# When:
# have == need_count