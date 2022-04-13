import math
class ClassEv():

    def desired(base,evv,ivv,opt,lvl,des,mod):
        d = ((2*base[opt+1]+ivv[opt+1]+(evv[opt+1]/4))*lvl/100)
        return math.trunc((((des/mod)-(d))*400/lvl)/4)*4

