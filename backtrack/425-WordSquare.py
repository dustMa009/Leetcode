class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        index = []
        index.append([(0, 0)])
        index.append([(0, 0), (0, 1), (1, 1)])
        index.append([(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)])
        index.append([(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)])
        a = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 2), (1, 3), (1, 4),
            (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
        index.append(a)
        
        res = []
        def backtrack(res, index, i, cur, remain):
            # res: the resulting list of word squares
            # index: the order of backtracking positions in a k * k square
            # i: currennt position in the word square
            # cur: current state of the word square for example ["abc", "b", "c", ""]
            # remain: remaining choice of all remaining positions
            (x, y) = index[i]
            # bask case
            if i + 1 == len(index):
                for j in remain[x]:
                    tmp = cur.copy()
                    tmp[x] += j
                    res.append(tmp)
                return
            
            # backtracking
            # pivot: possible values at position (x, y) in word square
            # pdt: narrow down the remaining choices in list remain after pivot is chosen 
            pivot = ""
            pdt = []
            for j in range(len(remain[x])):
                # update pivot and pdt when a new starting letter is found
                if j == 0 or remain[x][j][0] != remain[x][j-1][0]:
                    pivot = remain[x][j][0]
                    pdt = []
                pdt.append(remain[x][j][1:])
                # backtrack when the pivot is about to change
                if j + 1 == len(remain[x]) or remain[x][j][0] != remain[x][j+1][0]:
                    # if the position(x,y) is on the diagonal of the word matrix
                    if x == y:
                        remaind = remain.copy()
                        remaind[x] = pdt
                        curt = cur.copy()
                        curt[x] += pivot
                        backtrack(res, index, i+1, curt, remaind)
                    # if the position(x,y) is not on the diagonal
                    else:
                        curt = cur.copy()
                        curt[x] += pivot
                        curt[y] += pivot
                        ry = []
                        for k in remain[y]:
                            if k[0] == pivot:
                                ry.append(k[1:])
                        if not ry:
                            continue
                        else:
                            remaind = remain.copy()
                            remaind[x] = pdt
                            remaind[y] = ry
                            backtrack(res, index, i+1, curt, remaind)
            return
                        
        n = len(words[0])
        words.sort()
        cur = ["" for i in range(n)]
        remain = [words for i in range(n)]
        backtrack(res, index[n - 1], 0, cur, remain)
        return res
        