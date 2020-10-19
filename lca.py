class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def findPath( root, path, k):

    if root is None:
        return False

    path.append(root.data)

    if root.data == k:
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False

def findLCA(root, value1, value2):
    path1 = []
    path2 = []

    if(not findPath(root, path1, value1) or not findPath(root, path2, value2)):
        return -1
    #print(path1)
    #print(path2)
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            #print("NOT SAME: %d" %path1[i])
            #print("NOT SAME: %d" %path2[i])
            break
        #print("SAME: %d" %path1[i])
        #print("SAME: %d" %path2[i])
        i += 1
    
    return path1[i-1]


