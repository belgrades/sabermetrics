__author__ = "Fernando Crema"
__copyright__ = "Copyright 2019, The Sabermetrics Python Package Project."
__credits__ = ["Fernando Crema @FernandoCremaG", "Antonio Jesús Torres @ajtorresd"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Fernando Crema"
__email__ = "fernando.crema@sabermetrics.dev"
__status__ = "Production"

from random import random


def simulation(H, AB, p_h, p_hr, target_hr, target_avg, M=10000):
    less_target, ab_target_hr_global = 0, []
    
    for i in range(M):
        hr, h_tot, ab_tot, ab_to_target_hr = 0, H, AB, 0

        while hr < target_hr:
            h_rand = random()
            ab_tot += 1
            ab_to_target_hr += 1

            # Hit from the batter
            # P(Hit) = p_h
            if h_rand <= p_h:
                h_tot += 1

                hr_rand = random()

                # P(HR | Hit) = p_hr
                # HR from the batter
                if hr_rand <= p_hr:
                    hr += 1

        # Check if the average is less than target

        if h_tot*1.0/ab_tot < target_avg:
            less_target += 1

        # Check the number of at bats until average target
        ab_target_hr_global.append(ab_to_target_hr)
            

    return less_target * 1.0 / M, ab_target_hr_global
        
    

if __name__ == "__main__":
    H = 2704
    AB = 8552

    # Case A: Current Slump
    
    p_hr_slump = 1.0/(17)
    p_h_slump = 0.295

    prob_fail, at_bats = simulation(H, AB, p_h_slump, p_hr_slump, 10, .310)

    print("Case A: Current slump 2018-2019")
    print("\t Average: {0:.3f} \n\t HR Rate1Hit: {1:.4f} ".format(p_h_slump, p_hr_slump))
    print("\t Probability of failing (current performance): {0:.4f}".format(prob_fail))
    print("\t Average at bats to achieve goal assuming current performance: {0:.3f}".format(sum(at_bats)/len(at_bats)))

    # Case B: Career
    
    p_hr_career = 466*1.0 / 2704
    p_h_career = 2704*1.0 / 8552

    prob_fail, at_bats = simulation(H, AB, p_h_career, p_hr_career, 10, .310)

    print("Case B: Career 2003-2019")
    print("\t Average: {0:.3f} \n\t HR rate|Hit: {1:.4f} ".format(p_h_career, p_hr_career))
    print("\t Probability of failing (career): {0:.4f}".format(prob_fail))
    print("\t Average at bats to achieve goal assuming career performance: {0:.3f}".format(sum(at_bats)/len(at_bats)))

    # Case C: Hard Slump
    
    p_hr_hard = 1.0/25.0
    p_h_hard =  0.250

    prob_fail, at_bats = simulation(H, AB, p_h_hard, p_hr_hard, 10, .310)

    print("Case C: Hard slump")
    print("\t Average: {0:.3f} \n\t HR Rate|Hit: {1:.4f} ".format(p_h_hard,p_hr_hard))
    print("\t Probability of failing (Hard slump): {0:.4f}".format(prob_fail))
    print("\t Average at bats to achieve goal assuming hard slump: {0:.3f}".format(sum(at_bats)/len(at_bats)))
    

