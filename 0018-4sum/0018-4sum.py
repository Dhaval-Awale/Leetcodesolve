from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        output = set()
        event_horizon = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    diff = target - (nums[i] + nums[j] + nums[k])

                    if diff in event_horizon:
                        list_repr = [diff, nums[i], nums[j], nums[k]]
                        list_repr.sort()
                        tuple_repr = tuple(list_repr)
                        output.add(tuple_repr)

            event_horizon.add(nums[i])

        return [list(o) for o in output]

