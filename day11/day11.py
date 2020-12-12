import numpy as np
import cv2

def getArr(M, i, j):
    return np.concatenate((M[i - 1,j - 1:j + 2], M[i,j - 1:j + 2:2], M[i + 1,j - 1:j + 2]))

def part1(data):
    n, m = data.shape[0] + 2, data.shape[1] + 2

    curr = np.zeros((n, m))
    curr[1:n - 1,1:m - 1] = data

    prev = np.zeros((n, m))
    while not np.all(prev == curr):
        prev = np.copy(curr)
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if prev[i, j] == 1: #empty
                    anyOccupied = np.any(getArr(prev, i, j) == -1)
                    curr[i, j] = 1 if anyOccupied else -1
                elif prev[i, j] == -1: #occupied
                    moreThan4 = np.sum(getArr(prev, i, j) == -1) >= 4
                    curr[i, j] = 1 if moreThan4 else -1

    return np.sum(curr == -1)

def getAlleys(M, LR, UD, i, j):
    n, m = M.shape

    offset = j - i
    diag = np.diagonal(M, offset)
    pivot = min(i, j)
    up_diag = np.flip(diag[:pivot])
    up_mask = up_diag != 0
    lo_diag = diag[pivot + 1:]
    lo_mask = lo_diag != 0

    anti_j = (m - 1) - j
    anti_off = anti_j - i
    anti = np.diagonal(LR, anti_off)
    anti_pivot = min(i, anti_j)
    anti_up_diag = np.flip(anti[:anti_pivot])
    anti_up_mask = anti_up_diag != 0
    anti_lo_diag = anti[anti_pivot + 1:]
    anti_lo_mask = anti_lo_diag != 0

    left = LR[i, m - j:]
    left_mask = left != 0
    right = M[i, j + 1:]
    right_mask = right != 0

    top = UD[n - i:, j]
    top_mask = top != 0
    bot = M[i + 1:, j]
    bot_mask = bot != 0

    ret = np.zeros(8)
    ret[0] = 0 if not up_mask.any() else up_diag[up_mask.argmax()] #top left
    ret[1] = 0 if not lo_mask.any() else lo_diag[lo_mask.argmax()] #bot right
    ret[2] = 0 if not top_mask.any() else top[top_mask.argmax()] #top mid
    ret[3] = 0 if not bot_mask.any() else bot[bot_mask.argmax()] #bot mid
    ret[4] = 0 if not anti_up_mask.any() else anti_up_diag[anti_up_mask.argmax()] #top right
    ret[5] = 0 if not anti_lo_mask.any() else anti_lo_diag[anti_lo_mask.argmax()] #bot left
    ret[6] = 0 if not left_mask.any() else left[left_mask.argmax()] #mid left
    ret[7] = 0 if not right_mask.any() else right[right_mask.argmax()] #mid right

    return ret

def part2(data):
    n, m = data.shape[0] + 2, data.shape[1] + 2

    curr = np.zeros((n, m))
    curr[1:n - 1,1:m - 1] = data

    prev = np.zeros((n, m))
    while not np.all(prev == curr):
        prev = np.copy(curr)
        lr = np.fliplr(prev)
        ud = np.flipud(prev)
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if prev[i, j] == 1: #empty
                    anyOccupied = np.any(getAlleys(prev, lr, ud, i, j) == -1)
                    curr[i, j] = 1 if anyOccupied else -1
                elif prev[i, j] == -1: #occupied
                    moreThan5 = np.sum(getAlleys(prev, lr, ud, i, j) == -1) >= 5
                    curr[i, j] = 1 if moreThan5 else -1

    return np.sum(curr == -1)

if __name__ == "__main__":
    with open('day11.txt', 'r', newline='') as file:
        data = np.stack([np.array([1 if char == 'L' else 0 for char in s.rstrip()]) for s in file.readlines()])
        #print(part1(data))
        print(part2(data))