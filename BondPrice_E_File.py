

def getBondPrice_E(face, couponRate, yc):
    
    coupon = couponRate * face
    
    bondPrice = 0

    for t, y in enumerate(yc, start = 1):
        pvm = (1+y) ** (-t)

        cf = coupon
        if t == len(yc):
            cf += face

        bondPrice += cf * pvm

    return bondPrice
