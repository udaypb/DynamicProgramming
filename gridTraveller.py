import time
class numberOfWaysToTravelInGrid:
    def __init__(self):
        self.timeout = time.time() + 5 # 1 minute for each iteration
        self.timeoutFlag = False
    ''' ways to go from 0, 0 to n,m, in each step we can go right or down:
    So if you go down from each cell, your new grid to explore reduces by row - 1
    If you go right from each cell, your new grid in each step reduces by col - 1
    
    '''
    '''Recursive approach - Brute force approach --- explore all cells'''
    ''' Time: O(2^(n + m)) which is exponential'''
    def gridTraveler(self, rows, cols):
        #valid 1x1 grid -> there is only one way
        if rows ==1 and cols == 1:
            return 1
        #invalid
        if rows == 0 or cols == 0:
            return 0
        if time.time() < self.timeout:
            return self.gridTraveler(rows - 1, cols) + self.gridTraveler(rows, cols - 1)
        else:
            self.timeoutFlag = True
            return -1



grids = [(3, 3), (4, 4), (50, 45)]
i  = 0
while i < len(grids):
    gridTravel = numberOfWaysToTravelInGrid()
    print('ways to travel from 0,0 to {},{}'.format(grids[i][0], grids[i][1]))
    ans = gridTravel.gridTraveler(grids[i][0], grids[i][1])
    if gridTravel.timeoutFlag:
        print('Timed out..... It could be exponential time or quadratic time')
    else:
        print('---> ', ans)
    i += 1







