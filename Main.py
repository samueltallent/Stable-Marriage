from Little import Little
from Utils import allLittlesMatched


if __name__ == '__main__':
    print "Hit the main"
    littlesList= [{'name': 'Sally', 'id': 0, 'ranking':[5,4,3]}, {'name': 'Joe', 'id': 1, 'ranking':[4,3,5]}, {'name': 'Billy', 'id': 2, 'ranking':[3,4,5]}]
    bigsList =    [{'name': 'Frank', 'id': 3, 'ranking':[1,2,0]}, {'name': 'Bob', 'id': 4, 'ranking':[0,2,1]}, {'name': 'Ellie', 'id': 5, 'ranking':[1,0,2]}]
    littles = []
    bigs = []
    for little in littlesList:
        objLittle = Little(name=little['name'], id=little['id'], ranking=little['ranking'])
        littles.append(objLittle)

    print littles

    for big in bigsList:
        objBig = Little(name=big['name'], id=big['id'], ranking=big['ranking'])
        bigs.append(objBig)

    print "All littles engaged: %s" % allLittlesMatched(littles)

    # print littles
    # print bigs
    # print ''

