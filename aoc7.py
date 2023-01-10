from treelib import Node, Tree

tree = Tree()
with open('aoc7.txt') as f:
    lines = f.readlines()

allDirectories = {}
allDirectoryNumbers = {}
currentDirectory = 0
tree.create_node("/", 0)
allDirectories[0] = "/"
allDirectoryNumbers["/"] = 0

n = 1
while len(lines) > n:
    if lines[n][2] == "l":
        if len(lines) > n+1:
            n += 1
        else:
            break
        while not lines[n].startswith("$ cd"):
            if not lines[n].startswith("dir"):
                tree.create_node(lines[n].split()[0], lines[n].split()[0], parent=currentDirectory)
            n += 1
            if len(lines) == n:
                n += 1
                break
    else:
        if lines[n].startswith("$ cd .."):
            currentDirectory = tree.parent(currentDirectory).identifier
        elif lines[n] == "$ cd /":
            currentDirectory = 0
        else:
            allDirectories[len(allDirectories)] = lines[n].split()[2]
            tree.create_node("dir " + lines[n].split()[2], len(allDirectories) - 1, parent=currentDirectory)
            currentDirectory = len(allDirectories) - 1
        n += 1

tree.show()

sumBelow100000 = 0
totalSizeOfOutermostDirectory = 0
n = 0
while len(tree.leaves()) > n:
    if tree.leaves()[n].tag.isdigit():
        totalSizeOfOutermostDirectory += int(tree.leaves()[n].tag)
    n += 1

freeSpace = 70000000 - totalSizeOfOutermostDirectory
spaceToFreeUp = 30000000 - freeSpace

closestToFreeUp = spaceToFreeUp
directoryToDelete = 0

x = 1
while len(allDirectories) > x:
    y = 0
    dirsum = 0
    while len(tree.subtree(x).leaves()) > y:
        if tree.subtree(x).leaves()[y].tag.isdigit():
            dirsum += int(tree.subtree(x).leaves()[y].tag)
        y += 1
    if dirsum >= spaceToFreeUp and dirsum - spaceToFreeUp < closestToFreeUp:
        closestToFreeUp = dirsum - spaceToFreeUp
        directoryToDelete = dirsum
    if dirsum <= 100000:
        sumBelow100000 += dirsum
    x += 1

print(f"1st Answer: {sumBelow100000}")
print(f"2nd Answer: {directoryToDelete}")



