class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = 0
        for log in logs:
            if log == "./":
                continue
            if log == "../":
                operations = max(0, operations-1)
            else:
                operations += 1
        return operations
