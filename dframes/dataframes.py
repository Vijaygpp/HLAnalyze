import pandas as pd


def dataframes():
    #Declare empty Class I HLA data frame
    AthlatesClassI = pd.DataFrame(columns=['DNA-Normal', 'DNA-Tumor', 'RNA-Tumor'], index=range(6))
    AthlatesClassI = AthlatesClassI.fillna("")
    #return AthlatesClassI #[0]

    #Declare empty Class II HLA data frame
    AthlatesClassII = pd.DataFrame(columns=['DNA-Normal', 'DNA-Tumor', 'RNA-Tumor'], index=range(12))
    AthlatesClassII =AthlatesClassII.fillna("")
    #return AthlatesClassII #[1]

    #Declare empty Optitype HLA data frame
    OptiTypeNormalTumorRNA = pd.DataFrame(columns=['DNA-Normal', 'DNA-Tumor', 'RNA-Tumor'], index=range(6))
    OptiTypeNormalTumorRNA = OptiTypeNormalTumorRNA.fillna("")
    #print(OptiTypeNormalTumorRNA)
    #return OptiTypeNormalTumorRNA #[2]

    #Declare empty Polysolver HLA data frame
    PolysolverNormalTumorRNA = pd.DataFrame(columns=['DNA-Normal', 'DNA-Tumor', 'RNA-Tumor'], index=range(6))
    PolysolverNormalTumorRNA = PolysolverNormalTumorRNA.fillna("")
    print(PolysolverNormalTumorRNA)
    #return PolysolverNormalTumorRNA #[3]

    #Declare empty Seq2HLA Class I HLA data frame
    Seq2HLAClassINormalTumorRNA = pd.DataFrame(columns=['DNA-Normal', 'DNA-Tumor', 'RNA-Tumor'], index=range(6))
    Seq2HLAClassINormalTumorRNA = Seq2HLAClassINormalTumorRNA.fillna("")
    print(Seq2HLAClassINormalTumorRNA)
    #return Seq2HLAClassINormalTumorRNA #[4]

    #Declare empty Seq2HLA Class II HLA data frame
    Seq2HLAClassIINormalTumorRNA = pd.DataFrame(columns=['DNA-Normal', 'DNA-Tumor', 'RNA-Tumor'], index=range(12))
    Seq2HLAClassIINormalTumorRNA = Seq2HLAClassIINormalTumorRNA.fillna("")
    print(Seq2HLAClassIINormalTumorRNA)
    #return Seq2HLAClassIINormalTumorRNA #[5]

    #Declare empty HLAMiner ClassI RNA Tumor HLA list
    HLAMinerClassIRNATumorHLA = []
    #return HLAMinerClassIRNATumorHLA  #[6]

    #Declare empty HLAMiner ClassII RNA Tumor HLA list
    HLAMinerClassIIRNATumorHLA = []
    #return HLAMinerClassIIRNATumorHLA  #[7]
    
    return [AthlatesClassI, AthlatesClassII, OptiTypeNormalTumorRNA, PolysolverNormalTumorRNA, Seq2HLAClassINormalTumorRNA, Seq2HLAClassIINormalTumorRNA, HLAMinerClassIRNATumorHLA, HLAMinerClassIIRNATumorHLA]
    print("dataframes completed %%%%%%%%%%%%%%%%%%%%%")
