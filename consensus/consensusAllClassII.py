import pandas as pd

def FindConsensusClassII(A,S,H): #At least two votes required for calling consensus HLA
    ClassII_Consensus = set()
    ASH = set.intersection(A,S,H)
    ClassII_Consensus = set.union(ClassII_Consensus, ASH)
    AH = set.intersection(A,H)
    ClassII_Consensus = set.union(ClassII_Consensus, AH)
    SH = set.intersection(S,H)
    ClassII_Consensus = set.union(ClassII_Consensus, SH)
    AS = set.intersection(A,S)
    ClassII_Consensus = set.union(ClassII_Consensus, AS)
    
    return ClassII_Consensus