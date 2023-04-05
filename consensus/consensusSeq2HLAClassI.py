import pandas as pd

#Find consensus HLA intrapatient. Seq2HLA Class I
def getconsensusSeq2HLAClassI(Seq2HLAClassINormalTumorRNA):
    Seq2HLAClassINormalTumorRNA_Consensus = set()
    Seq2HLAClassINormalTumorRNA_NTR = set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassINormalTumorRNA["RNA-Tumor"]))
    print("Seq2HLAClassINormalTumorRNA_NTR", Seq2HLAClassINormalTumorRNA_NTR)
    Seq2HLAClassINormalTumorRNA_Consensus = set.union(Seq2HLAClassINormalTumorRNA_Consensus, Seq2HLAClassINormalTumorRNA_NTR)
    type(Seq2HLAClassINormalTumorRNA_NTR)
    print("Common HLA (Seq2HLAClassINormalTumorRNADNA-Normal, Seq2HLAClassINormalTumorRNADNA-Tumor, Seq2HLAClassINormalTumorRNARNA-Tumor):", set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassINormalTumorRNA["RNA-Tumor"])))

    Seq2HLAClassINormalTumorRNA_NT = set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassINormalTumorRNA["DNA-Tumor"]))
    print("Seq2HLAClassINormalTumorRNA_NT", Seq2HLAClassINormalTumorRNA_NT)
    Seq2HLAClassINormalTumorRNA_Consensus = set.union(Seq2HLAClassINormalTumorRNA_Consensus, Seq2HLAClassINormalTumorRNA_NT)
    type(Seq2HLAClassINormalTumorRNA_NT)
    print("Common HLA (Seq2HLAClassINormalTumorRNADNA-Normal, Seq2HLAClassINormalTumorRNADNA-Tumor):", set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassINormalTumorRNA["DNA-Tumor"])))

    Seq2HLAClassINormalTumorRNA_TR = set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassINormalTumorRNA["RNA-Tumor"]))
    print("Seq2HLAClassINormalTumorRNA_TR", Seq2HLAClassINormalTumorRNA_TR)
    Seq2HLAClassINormalTumorRNA_Consensus = set.union(Seq2HLAClassINormalTumorRNA_Consensus, Seq2HLAClassINormalTumorRNA_TR)
    type(Seq2HLAClassINormalTumorRNA_TR)
    print("Common HLA (Seq2HLAClassINormalTumorRNADNA-Tumor, Seq2HLAClassINormalTumorRNARNA-Tumor):", set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Tumor"]), set(Seq2HLAClassINormalTumorRNA["RNA-Tumor"])))

    Seq2HLAClassINormalTumorRNA_NR = set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassINormalTumorRNA["RNA-Tumor"]))
    print("Seq2HLAClassINormalTumorRNA_NR", Seq2HLAClassINormalTumorRNA_NR)
    Seq2HLAClassINormalTumorRNA_Consensus = set.union(Seq2HLAClassINormalTumorRNA_Consensus, Seq2HLAClassINormalTumorRNA_NR)
    type(Seq2HLAClassINormalTumorRNA_NR)
    print("Common HLA (Seq2HLAClassINormalTumorRNADNA-Normal, Seq2HLAClassINormalTumorRNARNA-Tumor):", set.intersection(set(Seq2HLAClassINormalTumorRNA["DNA-Normal"]), set(Seq2HLAClassINormalTumorRNA["RNA-Tumor"])))
    print("Seq2HLAClassINormalTumorRNA_Consensus", sorted(Seq2HLAClassINormalTumorRNA_Consensus))

    return [Seq2HLAClassINormalTumorRNA_Consensus]