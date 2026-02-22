

def getBondPrice(y, face, couponRate, m, ppy=1):
    m_eff = m * ppy
    couponRate_eff = couponRate / ppy
    y_eff = y / ppy

    pvcfsum = 0
    
    for t in range(1, m_eff+1):
        pvm = (1+y_eff) ** (-t)

        cf = face * couponRate_eff
        if t == m_eff:
            cf += face

        pvcfsum += cf * pvm
    
    return pvcfsum
        
