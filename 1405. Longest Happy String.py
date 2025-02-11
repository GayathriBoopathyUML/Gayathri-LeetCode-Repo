import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for i in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if i[0] != 0:
                heapq.heappush(max_heap, (i))
        # print(max_heap)
        result = []
        while max_heap:
            first_count, first_char = (heapq.heappop(max_heap))
            if len(result) >= 2 and result[-1] == result[-2] == first_char:
                if not max_heap:  # No other option left
                    break
                second_count, second_char = heapq.heappop(max_heap)  # Use the second most frequent character
                result.append(second_char)
                second_count += 1  # Reduce count (since it's negative)
                if second_count != 0:
                    heapq.heappush(max_heap, (second_count, second_char))  # Push back if still available
                heapq.heappush(max_heap, (first_count, first_char))  # Push first_char back for next round
            else:
                # Append the most frequent character to the result
                result.append(first_char)
                first_count += 1  # Increase count (since it's negative)
                if first_count != 0:
                    heapq.heappush(max_heap, (first_count, first_char))  # Push back if still available
        

        return(''.join(result))