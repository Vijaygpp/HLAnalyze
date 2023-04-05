import pandas as pd

#Find consensus HLA intrapatient. Seq2HLA Class II
def getconsensusSeq2HLAClassII(Seq2HLAClassIINormalTumorRNA):
    Seq2HLAClassIINormalTumorRNA_Consensus = set()
    Seq2HLAClassIINormalTumorRNA_NTR = set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassIINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassIINormalTumorRNA["RNA-Tumor"]))
    print("Seq2HLAClassIINormalTumorRNA_NTR", Seq2HLAClassIINormalTumorRNA_NTR)
    Seq2HLAClassIINormalTumorRNA_Consensus = set.union(Seq2HLAClassIINormalTumorRNA_Consensus, Seq2HLAClassIINormalTumorRNA_NTR)
    type(Seq2HLAClassIINormalTumorRNA_NTR)
    print("Common HLA (Seq2HLAClassIINormalTumorRNADNA-Normal, Seq2HLAClassIINormalTumorRNADNA-Tumor, Seq2HLAClassIINormalTumorRNARNA-Tumor):", set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassIINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassIINormalTumorRNA["RNA-Tumor"])))

    Seq2HLAClassIINormalTumorRNA_NT = set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassIINormalTumorRNA["DNA-Tumor"]))
    print("Seq2HLAClassIINormalTumorRNA_NT", Seq2HLAClassIINormalTumorRNA_NT)
    Seq2HLAClassIINormalTumorRNA_Consensus = set.union(Seq2HLAClassIINormalTumorRNA_Consensus, Seq2HLAClassIINormalTumorRNA_NT)
    type(Seq2HLAClassIINormalTumorRNA_NT)
    print("Common HLA (Seq2HLAClassIINormalTumorRNADNA-Normal, Seq2HLAClassIINormalTumorRNADNA-Tumor):", set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassIINormalTumorRNA["DNA-Tumor"])))

    Seq2HLAClassIINormalTumorRNA_TR = set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassIINormalTumorRNA["RNA-Tumor"]))
    print("Seq2HLAClassIINormalTumorRNA_TR", Seq2HLAClassIINormalTumorRNA_TR)
    Seq2HLAClassIINormalTumorRNA_Consensus = set.union(Seq2HLAClassIINormalTumorRNA_Consensus, Seq2HLAClassIINormalTumorRNA_TR)
    type(Seq2HLAClassIINormalTumorRNA_TR)
    print("Common HLA (Seq2HLAClassIINormalTumorRNADNA-Tumor, Seq2HLAClassIINormalTumorRNARNA-Tumor):", set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassIINormalTumorRNA["RNA-Tumor"])))

    Seq2HLAClassIINormalTumorRNA_NR = set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassIINormalTumorRNA["RNA-Tumor"]))
    print("Seq2HLAClassIINormalTumorRNA_NR", Seq2HLAClassIINormalTumorRNA_NR)
    Seq2HLAClassIINormalTumorRNA_Consensus = set.union(Seq2HLAClassIINormalTumorRNA_Consensus, Seq2HLAClassIINormalTumorRNA_NR)
    type(Seq2HLAClassIINormalTumorRNA_NR)
    print("Common HLA (Seq2HLAClassIINormalTumorRNADNA-Normal, Seq2HLAClassIINormalTumorRNARNA-Tumor):", set.intersection(set(Seq2HLAClassIINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassIINormalTumorRNA["RNA-Tumor"])))
    print("Seq2HLAClassIINormalTumorRNA_Consensus", sorted(Seq2HLAClassIINormalTumorRNA_Consensus))

    return [Seq2HLAClassIINormalTumorRNA_Consensus]