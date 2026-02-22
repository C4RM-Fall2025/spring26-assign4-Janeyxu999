
def getBondDuration(y, face, couponRate, m, ppy = 1):
    m_eff = m * ppy
    couponRate = couponRate / ppy
    y_eff = y / ppy

    pvcfsum = 0
    WeightedTimeSum = 0

    for t in range(1, m_eff + 1):
        pvm = (1+y_eff) ** (-t)
        cf = face * couponRate_eff

        if t == m_eff:
            cf += face

        pvcf = cf * pvm
        pvcfsum += pvcf

        WeightedTimeSum += pvcf * (t / ppy)

    BondDuration = WeightedTimeSum / pvcfsum
    return BondDuration
