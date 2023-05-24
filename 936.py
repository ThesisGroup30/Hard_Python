class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(target), len(stamp)
        stamp_arr = list(stamp)
        target_arr = list(target)
        stamped = [False] * n
        res = []

        def can_stamp(start: int) -> bool:
            changed = False

            for i in range(m):
                if target_arr[start + i] == '?':
                    continue
                if target_arr[start + i] != stamp_arr[i]:
                    return False
                changed = True

            if changed:
                for i in range(start, start + m):
                    target_arr[i] = '?'
                stamped[start:start + m] = [True] * m
                return True

            return False

        num_stamped = 0

        while num_stamped < n:
            stamped_before = num_stamped

            for i in range(n - m + 1):
                if stamped[i]:
                    continue

                if can_stamp(i):
                    res.append(i)
                    num_stamped += m

            if num_stamped == stamped_before:
                return []

        return res[::-1]
