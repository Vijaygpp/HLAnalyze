import pandas as pd

#Final Consensus HLA list Class I

def FindConsensusClassI(A,O,P,S,H): #At least two votes required for calling consensus HLA
    ClassI_Consensus = set()
    AOPSH = set.intersection(A,O,P,S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, AOPSH)
    #_________________________________________AOPSH 5 choose 4 = 10 combinations
    AOPS = set.intersection(A,O,P,S)
    ClassI_Consensus = set.union(ClassI_Consensus, AOPS)

    AOPH = set.intersection(A,O,P,H)
    ClassI_Consensus = set.union(ClassI_Consensus, AOPH)

    AOSH = set.intersection(A,O,S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, AOSH)

    APSH = set.intersection(A,P,S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, APSH)

    OPSH = set.intersection(O,P,S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, OPSH)

    #_________________________________________AOPSH 5 choose 3 = 10 combinations
    AOP = set.intersection(A,O,P)
    ClassI_Consensus = set.union(ClassI_Consensus, AOP)

    AOH = set.intersection(A,O,H)
    ClassI_Consensus = set.union(ClassI_Consensus, AOH)

    AOS = set.intersection(A,O,S)
    ClassI_Consensus = set.union(ClassI_Consensus, AOS)

    ASH = set.intersection(A,S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, ASH)

    APH = set.intersection(A,P,H)
    ClassI_Consensus = set.union(ClassI_Consensus, APH)

    APS = set.intersection(A,P,S)
    ClassI_Consensus = set.union(ClassI_Consensus, APS)

    OPS = set.intersection(O,P,S)
    ClassI_Consensus = set.union(ClassI_Consensus, OPS)

    OPH = set.intersection(O,P,H)
    ClassI_Consensus = set.union(ClassI_Consensus, OPH)

    OSH = set.intersection(O,S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, OSH)

    PSH = set.intersection(P,S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, PSH)

    #_________________________________________AOPSH 5 choose 2 = 10 combinations
    AO = set.intersection(A,O)
    ClassI_Consensus = set.union(ClassI_Consensus, AO)
    AP = set.intersection(A,P)
    ClassI_Consensus = set.union(ClassI_Consensus, AP)
    AS = set.intersection(A,S)
    ClassI_Consensus = set.union(ClassI_Consensus, AS)
    AH = set.intersection(A,H)
    ClassI_Consensus = set.union(ClassI_Consensus, AH)
    OP = set.intersection(O,P)
    ClassI_Consensus = set.union(ClassI_Consensus, OP)
    OS = set.intersection(O,S)
    ClassI_Consensus = set.union(ClassI_Consensus, OS)
    OH = set.intersection(O,H)
    ClassI_Consensus = set.union(ClassI_Consensus, OH)
    PS = set.intersection(P,S)
    ClassI_Consensus = set.union(ClassI_Consensus, PS)
    PH = set.intersection(P,H)
    ClassI_Consensus = set.union(ClassI_Consensus, PH)
    SH = set.intersection(S,H)
    ClassI_Consensus = set.union(ClassI_Consensus, SH)
    
    return ClassI_Consensus