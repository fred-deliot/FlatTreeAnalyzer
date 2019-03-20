import ROOT
import collections

ana_tex = "t#bar{t}t#bar{t}"

### variable list
variables = {
	'Jet1_tau21':{'name':'Jet1_trk08_tau21','title':'Jet1 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau32':{'name':'Jet1_trk08_tau32','title':'Jet1 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_tau31':{'name':'Jet1_trk08_tau31','title':'Jet1 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet1_SD_Cor_pt':{'name':'Jet1_trk08_SD_Corr_pt','title':'Jet1 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet1_SD_Cor_eta':{'name':'Jet1_trk08_SD_Corr_eta','title':'Jet1 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_SD_Cor_m':{'name':'Jet1_trk08_SD_Corr_m','title':'Jet1 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet1_SD_Cor_MetCor_pt':{'name':'Jet1_trk08_SD_Corr_MetCorr_pt','title':'Jet1 p_{T} (SD+MET cor) [TeV]','bin':65,'xmin':0.0,'xmax':15, 'divide':1000},
        'Jet1_SD_Cor_MetCor_eta':{'name':'Jet1_trk08_SD_Corr_MetCorr_eta','title':'Jet1 #eta (SD+MET cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet1_SD_Cor_MetCor_m':{'name':'Jet1_trk08_SD_Corr_MetCorr_m','title':'Jet1 mass (SD+MET cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet2_tau21':{'name':'Jet2_trk08_tau21','title':'Jet2 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau32':{'name':'Jet2_trk08_tau32','title':'Jet2 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_tau31':{'name':'Jet2_trk08_tau31','title':'Jet2 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet2_SD_Cor_pt':{'name':'Jet2_trk08_SD_Corr_pt','title':'Jet2 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet2_SD_Cor_eta':{'name':'Jet2_trk08_SD_Corr_eta','title':'Jet2 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet2_SD_Cor_m':{'name':'Jet2_trk08_SD_Corr_m','title':'Jet2 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet2_SD_Cor_MetCor_pt':{'name':'Jet2_trk08_SD_Corr_MetCorr_pt','title':'Jet2 p_{T} (SD+MET cor) [TeV]','bin':65,'xmin':0.0,'xmax':15, 'divide':1000},
        'Jet2_SD_Cor_MetCor_eta':{'name':'Jet2_trk08_SD_Corr_MetCorr_eta','title':'Jet2 #eta (SD+MET cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet2_SD_Cor_MetCor_m':{'name':'Jet2_trk08_SD_Corr_MetCorr_m','title':'Jet2 mass (SD+MET cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet3_tau21':{'name':'Jet3_trk08_tau21','title':'Jet3 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet3_tau32':{'name':'Jet3_trk08_tau32','title':'Jet3 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet3_tau31':{'name':'Jet3_trk08_tau31','title':'Jet3 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet3_SD_Cor_pt':{'name':'Jet3_trk08_SD_Corr_pt','title':'Jet3 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet3_SD_Cor_eta':{'name':'Jet3_trk08_SD_Corr_eta','title':'Jet3 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet3_SD_Cor_m':{'name':'Jet3_trk08_SD_Corr_m','title':'Jet3 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet3_SD_Cor_MetCor_pt':{'name':'Jet3_trk08_SD_Corr_MetCorr_pt','title':'Jet3 p_{T} (SD+MET cor) [TeV]','bin':65,'xmin':0.0,'xmax':15, 'divide':1000},
        'Jet3_SD_Cor_MetCor_eta':{'name':'Jet3_trk08_SD_Corr_MetCorr_eta','title':'Jet3 #eta (SD+MET cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet3_SD_Cor_MetCor_m':{'name':'Jet3_trk08_SD_Corr_MetCorr_m','title':'Jet3 mass (SD+MET cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},

        'Jet4_tau21':{'name':'Jet4_trk08_tau21','title':'Jet4 #tau_{2,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet4_tau32':{'name':'Jet4_trk08_tau32','title':'Jet4 #tau_{3,2}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet4_tau31':{'name':'Jet4_trk08_tau31','title':'Jet4 #tau_{3,1}','bin':50,'xmin':0.0,'xmax':1.0},
        'Jet4_SD_Cor_pt':{'name':'Jet4_trk08_SD_Corr_pt','title':'Jet4 p_{T} (SD cor) [TeV]','bin':65,'xmin':2,'xmax':15, 'divide':1000},
        'Jet4_SD_Cor_eta':{'name':'Jet4_trk08_SD_Corr_eta','title':'Jet4 #eta (SD cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet4_SD_Cor_m':{'name':'Jet4_trk08_SD_Corr_m','title':'Jet4 mass (SD cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},
        'Jet4_SD_Cor_MetCor_pt':{'name':'Jet4_trk08_SD_Corr_MetCorr_pt','title':'Jet4 p_{T} (SD+MET cor) [TeV]','bin':65,'xmin':0.0,'xmax':15, 'divide':1000},
        'Jet4_SD_Cor_MetCor_eta':{'name':'Jet4_trk08_SD_Corr_MetCorr_eta','title':'Jet4 #eta (SD+MET cor)','bin':50,'xmin':-5.0,'xmax':5.0},
        'Jet4_SD_Cor_MetCor_m':{'name':'Jet4_trk08_SD_Corr_MetCorr_m','title':'Jet4 mass (SD+MET cor) [GeV]','bin':100,'xmin':0.0,'xmax':500},


        'rapiditySeparation_j1j2':{'name':'rapiditySeparation_trk08_j1j2','title':'Rapidity Separation (Jet1, Jet2)','bin':50,'xmin':0.0,'xmax':10.0},
        'rapiditySeparation_j1j3':{'name':'rapiditySeparation_trk08_j1j3','title':'Rapidity Separation (Jet1, Jet3)','bin':50,'xmin':0.0,'xmax':10.0},
        'rapiditySeparation_j1j4':{'name':'rapiditySeparation_trk08_j1j4','title':'Rapidity Separation (Jet1, Jet4)','bin':50,'xmin':0.0,'xmax':10.0},
        'transverseMomentumAsymmetry_j1j2':{'name':'transverseMomentumAsymmetry_trk08_j1j2','title':'Transverse Momentum Asymmetry (Jet1, Jet2)','bin':50,'xmin':0.0,'xmax':1.0},
        'transverseMomentumAsymmetry_j1j3':{'name':'transverseMomentumAsymmetry_trk08_j1j3','title':'Transverse Momentum Asymmetry (Jet1, Jet3)','bin':50,'xmin':0.0,'xmax':1.0},
        'transverseMomentumAsymmetry_j1j4':{'name':'transverseMomentumAsymmetry_trk08_j1j4','title':'Transverse Momentum Asymmetry (Jet1, Jet4)','bin':50,'xmin':0.0,'xmax':1.0},

        'Mj1j2j3j4_trk08' :{'name':'Mj1j2j3j4_trk08','title':'m_{j1j2j3j4} [TeV] (trk08)','bin':125,'xmin':0.0,'xmax':30.0, 'divide':1000},
        'Mj1j2j3j4_trk08_Corr' :{'name':'Mj1j2j3j4_trk08_Corr','title':'m_{j1j2j3j4} [TeV] (trk08 cor)','bin':125,'xmin':0.0,'xmax':30.0, 'divide':1000},
        'Mj1j2j3j4_trk08_MetCorr' :{'name':'Mj1j2j3j4_trk08_MetCorr','title':'m_{j1j2j3j4} [TeV] (trk08 metcor)','bin':125,'xmin':0.0,'xmax':30.0, 'divide':1000},
        'Mj1j2j3j4_trk08_Corr_MetCorr' :{'name':'Mj1j2j3j4_trk08_Corr_MetCorr','title':'m_{j1j2j3j4} [TeV] (trk08 corr metcor)','bin':125,'xmin':0.0,'xmax':30.0, 'divide':1000},

        'Mj1j2j3j4_pf08' :{'name':'Mj1j2j3j4_pf08','title':'m_{j1j2j3j4} [TeV] (pf08)','bin':125,'xmin':0.0,'xmax':30.0, 'divide':1000},
        'Mj1j2j3j4_pf08_MetCorr' :{'name':'Mj1j2j3j4_pf08_MetCorr','title':'m_{j1j2j3j4} [TeV] (pf08 metcor)','bin':125,'xmin':0.0,'xmax':30.0, 'divide':1000},

        'Jet1_dR_lep' :{'name':'Jet1_trk08_dR_lep','title':'min #DeltaR(l,j1)','bin':50,'xmin':0,'xmax':5},
        'Jet2_dR_lep' :{'name':'Jet2_trk08_dR_lep','title':'min #DeltaR(l,j2)','bin':50,'xmin':0,'xmax':5},
        'Jet3_dR_lep' :{'name':'Jet3_trk08_dR_lep','title':'min #DeltaR(l,j3)','bin':50,'xmin':0,'xmax':5},
        'Jet4_dR_lep' :{'name':'Jet4_trk08_dR_lep','title':'min #DeltaR(l,j4)','bin':50,'xmin':0,'xmax':5},


	'njets' :{'name':'numberOfJets','title':'number of jets','bin':12,'xmin':4,'xmax':16},
	'nbjets':{'name':'numberOfBJets','title':'number of b-jets','bin':10,'xmin':0,'xmax':10},	
	'ht'	:{'name':'Ht','title':'Ht','bin':65,'xmin':500,'xmax':7000},

}

variables2D = {}


colors = {}
colors['tttt'] = ROOT.kRed
colors['ttzz']  = ROOT.kBlue
colors['ttwz']  = ROOT.kBlue+1
colors['ttww']  = ROOT.kBlue+4
colors['ttzbb'] = ROOT.kGreen
colors['ttbb']  = ROOT.kGreen+3
colors['tthbb'] = ROOT.kMagenta+2
colors['bbbbj'] = ROOT.kOrange-2

signal_groups = collections.OrderedDict()
signal_groups['tttt']  = ['mgp8_pp_tttt_5f']

background_groups = collections.OrderedDict()
#@@
#background_groups['ttzbb']  = ['mgp8_pp_ttz_5f_zbb']
#background_groups['tthbb']  = ['mgp8_pp_tth01j_5f_hbb']
#background_groups['ttbb']   = ['mgp8_pp_ttbb_4f']
#background_groups['ttzz']   = ['mgp8_pp_ttzz_5f']
#background_groups['ttwz']   = ['mgp8_pp_ttwz_5f']
#background_groups['bbbbj']  = ['mgp8_pp_bbbbj_QCD']
#background_groups['ttww']   = ['mgp8_pp_ttww_4f']

# global parameters
intLumi = 3.0e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
#runFull = False
runFull = True

#####################
# base pre-selections
#####################

selbase  = 'Jet1_trk08_SD_Corr_pt > 0. '

selbase_ml = 'Ht > 500. && missingET > 40.'
selbase_ml += '&& ( (SSee >0) || (SSem > 0) || (SSmm > 0) || (SSeee > 0) || (SSeem > 0) || (SSemm > 0) || (SSmmm > 0) )'

selSR1 = selbase_ml + '&&((SSee >0) || (SSem > 0) || (SSmm > 0)) && numberOfBJets ==2 && numberOfJets>=6'
selSR2 = selbase_ml + '&& ((SSee >0) || (SSem > 0) || (SSmm > 0)) && numberOfBJets >=3 && numberOfJets>=5'
selSR3 = selbase_ml + '&& ((SSeee >0) || (SSeem > 0) || (SSemm > 0) || (SSmmm > 0)) && numberOfBJets ==2 && numberOfJets>=6'
selSR4 = selbase_ml + '&& ((SSeee >0) || (SSeem > 0) || (SSemm > 0) || (SSmmm > 0)) && numberOfBJets >=3 && numberOfJets>=5'
selSR5 = selbase_ml + '&& numberOfBJets >=4 && numberOfJets>=6'


# add mass-dependent list of event #selections here if needed...

selections = collections.OrderedDict()

selections['tttt'] = []
selections['tttt'].append(selbase_ml)
selections['tttt'].append(selSR1)
selections['tttt'].append(selSR2)
selections['tttt'].append(selSR3)
selections['tttt'].append(selSR4)
selections['tttt'].append(selSR5)



