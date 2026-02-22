

def getBondPrice_Z(face, couponRate, times, yc):
    
    coupon = couponRate * face

    bondPrice = 0

    last_t = max(times)
    
    for t, y in zip(times, yc):
        pvm = (1+y) ** (-t)
        cf = coupon
        if t == last_t:
            cf += face
        
        bondPrice += cf * pvm

    return bondPrice
