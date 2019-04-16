def waterremaining(arr):
    if len(arr) <= 2:
        return -1
    leftMax = [arr[0]]
    for i in range(1, len(arr)):
        leftMax.append(max(leftMax[i-1],arr[i]))
    rightMax = [0] * len(arr)
    rightMax[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr)-2, -1,-1):
        rightMax[i] = max(rightMax[i+1],arr[i])
    totalUnits = 0
    for i in range(len(arr)):
        possible = min(leftMax[i],rightMax[i])
        if possible > arr[i]:
            totalUnits += (possible - arr[i])
    return totalUnits
        

if __name__ == "__main__":
    assert waterremaining([3,0,1,3,0,5]) == 8
    assert waterremaining([2,1,2]) == 1