class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = Counter(nums)
        print(count)

        #(num, count)

        maxHeap = [(-cnt, n) for n, cnt in count.items()] 

        heapq.heapify(maxHeap)
        print(maxHeap)

        res = []
        while k > 0:
            count, num = heapq.heappop(maxHeap)
            res.append(num)
            k-=1
            

        return res