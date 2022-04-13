import math
class ClassStat():

    def hpReturn(base,ivv,evv,lvl):
        return math.trunc((((2 * base[1] + ivv[1] + (evv[2] / 4)) * lvl) / 100) + lvl + 10)

    def attackReturn(base,ivv,evv,lvl,atknat):
        return math.trunc((((((2 * base[2] + ivv[2] + (evv[2] / 4)) * lvl) / 100) + 5) * atknat))
        
    def defenseReturn(base,ivv,evv,lvl,defnat):
        return math.trunc((((((2 * base[3] + ivv[3] + (evv[3] / 4)) * lvl) / 100) + 5) * defnat))

    def spattackReturn(base,ivv,evv,lvl,spatknat):
        return math.trunc((((((2 * base[4] + ivv[4] + (evv[4] / 4)) * lvl) / 100) + 5) * spatknat))  

    def spdefenseReturn(base,ivv,evv,lvl,spdefnat):
        return math.trunc((((((2 * base[5] + ivv[5] + (evv[5] / 4)) * lvl) / 100) + 5) * spdefnat))

    def speedReturn(base,ivv,evv,lvl,spdnat):
        return math.trunc((((((2 * base[6] + ivv[6] + (evv[6] / 4)) * lvl) / 100) + 5) * spdnat))