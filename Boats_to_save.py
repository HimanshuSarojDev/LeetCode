class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        r = n-1
        l = 0
        Boats = 0
        while(r>=l):
            if people[l]+ people[r]<=limit:
                l +=1
                r-=1
            else:
                r -=1
            Boats+=1
        return Boats

