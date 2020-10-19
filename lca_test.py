import lca

def testEmpty():
    root = lca.Node(1)


    assert (lca.findLCA(root, 6, 7)) == -1, "Should be -1"
    assert (lca.findLCA(root, 3, 2)) == -1, "Should be -1"
    assert (lca.findLCA(root, 4, 5)) == -1, "Should be -1"
    return


def testNormal():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    root.right.left = lca.Node(6)
    root.right.right = lca.Node(7)


    assert (lca.findLCA(root, 6, 7)) == 3, "Should be 3"
    assert (lca.findLCA(root, 3, 2)) == 1, "Should be 1"
    assert (lca.findLCA(root, 4, 5)) == 2, "Should be 2"
    return

def testOneMissing():
    root = lca.Node(1)
    root.left = lca.Node(2)
    root.right = lca.Node(3)
    root.left.left = lca.Node(4)
    root.left.right = lca.Node(5)
    root.right.left = lca.Node(6)


    assert (lca.findLCA(root, 6, 7)) == -1, "Should be -1"
    return

testEmpty()
testOneMissing
testNormal