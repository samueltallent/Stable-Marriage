from Little import Little

class Utils:
    littlesById = {}
    bigsById = {}

    @staticmethod
    def allLittlesMatched(littlesList):
        for little in littlesList:
            # print "Little: %s" % little.name
            print 'Little (%s) Engaged: %s' % (little.name, little.engaged)
            if not little.engaged:
                return False
        return True

    @staticmethod
    def still_free_littles(littles):
        non_engaged_littles = []
        for little in littles:
            if not little.engaged:
                non_engaged_littles.append(little)
        return non_engaged_littles

    @staticmethod
    def print_pairs(people):
        for person in people:
            if person.engaged:
                print "%s is engaged to %s" % (person.name, person.fiance.name)
                print "%s got their #%s choice" % (person.name, person.ranking.index(person.fiance.id))
                # print "Fiance's ranking: %s" % person.fiance.ranking
                # print "Person's id: %s" % person.id
                # print "INDEX OF PERSON IN FIANCE's RANKING: %s" % person.fiance.ranking.index(person.id)
                print "%s got their #%s choice\n" % (person.fiance.name, person.fiance.ranking.index(person.id))

    @staticmethod
    def calculatePreferences(littles, bigs):
        non_engaged_littles = Utils.still_free_littles(littles)
        while len(non_engaged_littles) > 0:
            little = non_engaged_littles[0]
            preferred_big_id = little.options[0]
            del little.options[0]
            big = None
            big = [temp_big for temp_big in bigs if temp_big.id == preferred_big_id][0]
            print "%s's current preference is: %s" % (little.name, big.name)
            # for temp_big in bigs:
            #     # print temp_big
            #     if temp_big.id == preferred_big_id:
            #         big = temp_big
            if not big.engaged:
                big.engaged = True
                little.engaged = True
                big.fiance = little
                little.fiance = big
                print "%s and %s are now 'engaged'" % (big.name, little.name)
            else:
                if big.prefers(little):
                    other_little = big.fiance
                    other_little.engaged = False
                    other_little.fiance = None
                    big.fiance = little
                    little.engaged = True
                    little.fiance = big

            non_engaged_littles = Utils.still_free_littles(littles)
            # big = [big for big in bigs if big['id'] == little['ranking']]

            # print "Determined: " + big.name + " to be the top choice for: " + little.name

            # break
        # print "Printing when fed littles"
        # Utils.print_pairs(littles)

        # print "Now printing when fed bigs"
        Utils.print_pairs(bigs)


        # for big in bigs:
        #     little_to_propose_to = Utils.littlesById[big.ranking[0]]
        #     Utils.propose(big, little_to_propose_to)
        #
        # for little in littles:
        #     if not little.engaged:
        #         big_to_propose_to = Utils.bigsById[little.ranking[0]]
        #         print "To propose to: %s" % big_to_propose_to
        #         while len(little.ranking) and not big_to_propose_to.engaged:
        #             if big_to_propose_to.engaged:
        #                 del little.ranking[0]
        #                 big_to_propose_to = little.ranking[0]
        #                 Utils.propose(big_to_propose_to, little)

    ## A big proposes to a little, if the little likes the proposer better than their current engagement, they switch
    # @staticmethod
    # def propose(big, little):
    #     if little.engaged:
    #         current_big = little.fiance
    #         ranking_of_current = little.ranking.index(current_big.id)
    #         ranking_of_proposer = little.ranking.index(big.id)
    #         print "Little (%s) proposed to by: %s, current fiance: %s" % (little.name, big.name, current_big.name)
    #         if ranking_of_proposer > ranking_of_current:
    #             big.engaged = True
    #             little.engaged = True
    #             little.fiance = big
    #             big.fiance = little
    #             current_big.engaged = False
    #             current_big.fiance = None
    #             current_big.options = current_big.ranking
    #     else:
    #         little.engaged = True
    #         big.engaged = True
    #         little.fiance = big
    #         big.fiance = little