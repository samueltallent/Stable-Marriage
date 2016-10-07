from Little import Little
from Big import Big
from Utils import Utils

if __name__ == '__main__':
    # print "Hit the main"
    ## Bingley - 0
    ## Collins - 1
    ## Darcy - 2
    ## Wickham - 3
    bigsList = [{'name': 'Bingley', 'id': 0, 'ranking':[6,5,7,4]}, {'name': 'Collins', 'id': 1, 'ranking':[6,5,7,4]},
                  {'name': 'Darcy', 'id': 2, 'ranking':[5,6,4,7]}, {'name': 'Wickham', 'id': 3, 'ranking':[7,6,5,4]}]
    ## Charlotte - 4
    ## Elizabeth - 5
    ## Jane - 6
    ## Lydia - 7
    littlesList =    [{'name': 'Charlotte', 'id': 4, 'ranking':[0,2,1,3]}, {'name': 'Elizabeth', 'id': 5, 'ranking':[3,2,0,1]},
                   {'name': 'Jane', 'id': 6, 'ranking':[0,3,2,1]}, {'name': 'Lydia', 'id': 7, 'ranking':[0,3,2,1]}]
    littles = []
    bigs = []
    for little in littlesList:
        objLittle = Little(name=little['name'], id=little['id'], ranking=little['ranking'])
        Utils.littlesById[little['id']] = objLittle
        littles.append(objLittle)

    # print littles

    for big in bigsList:
        objBig = Big(name=big['name'], id=big['id'], ranking=big['ranking'])
        Utils.bigsById[big['id']] = objBig
        bigs.append(objBig)

    # print "All littles engaged: %s" % Utils.allLittlesMatched(littles)
    Utils.calculatePreferences(littles, bigs)

    # print littles
    # print bigs
    # print ''

