#!/usr/bin/env python
#
#  By Cameron Bravo <bravo@slac.stanford.edu>, modified by Aster Taylor <ataylor@slac.stanford.edu>
#
#      Used to analyze histogramed data (HD) produced
#      by running makeHD on a .bin to produce a HD.root
#      from a icalScan run directory.
#
import numpy as np
import ROOT as r
from copy import deepcopy
from optparse import OptionParser
from DAQMap import layerToFeb

oPar = OptionParser()
oPar.add_option("-i", "--inDir", type="string", dest="inDir",
        default=".",help="Specify Input Filename", metavar="inDir")
oPar.add_option("-o", "--outfilename", type="string", dest="outfilename",
        default="null",help="Specify Output Filename", metavar="outfilename")
oPar.add_option("-n", "--inName", type="int", dest="inName", default=0,
        help="Run ID", metavar="inName")
(options, args) = oPar.parse_args()

r.gROOT.SetBatch(True)

inDir = options.inDir

everything={}
means={}
rmss={}
mean_g_dict={}
rms_g_dict={}
nIndices=[]

for layer in xrange(1,15):
    for module in xrange(4):
        if layer < 9 and module > 1: continue
        inFile = r.TFile( inDir )
        if hasattr(inFile, "smData_%s_%s_hh" %(layer,module))==False: continue
        index= layer+.1*module
        everything[index] = [{},{}] 
        smData0_hh = deepcopy(getattr(inFile,"smData_%s_%s_hh" %(layer,module)))
        for chan in xrange(640):
            print "Channel:", chan
            if layer<5 and chan>512: continue
            means[chan] = {}
            rmss[chan] = {}
            print "Opening File"
            print layer, module, index
            scData0_h = deepcopy(smData0_hh.ProjectionY('scData0_ch%i_h'%(chan), chan+1, chan+1, "e"))
            sampleMean = scData0_h.GetMean()
            sampleNoise = scData0_h.GetRMS()
            gaus_f = r.TF1('gaus_f','gaus', sampleMean-4*sampleNoise, sampleMean+4*sampleNoise)
            gaus_f.SetParameter(0, 10.0)
            gaus_f.SetParameter(1, sampleMean)
            gaus_f.SetParameter(2, sampleNoise)
            scData0_h.Fit(gaus_f, 'QR')
            mean = gaus_f.GetParameter(1)
            rms = gaus_f.GetParameter(2)
            means[chan] = mean
            print mean
            rmss[chan] = rms
            print rms
            inFile.Close()
            pass
        everything[index][0].update(means)
        everything[index][1].update(rmss)
        
        #feb=int(layerToFeb[index])
        #hybrid=int((layerToFeb[index]-feb)*10.0)
        #nIndex=feb+0.1*hybrid
        #nIndices.append(nIndex)
        nIndex=index
        nIndices.append(index)

        chList=[]
        meanList=[]
        rmsList=[]
        null=[]
        for chan in xrange(640):
            if layer<5 and chan>512: continue
            chList.append(float(chan))
            meanList.append(float(everything[index][0][chan]))
            rmsList.append(float(everything[index][1][chan]))
            null.append(0)
            pass

        mean_g = r.TGraphErrors( len(chList), np.array(chList), np.array(meanList), np.array(null), np.array(rmsList) )
        #mean_g.SetName('baseline_%i.%i_ge'%(feb,hybrid))
        #mean_g.SetTitle('Baseline vs Channel for %i.%i;Channel;Baseline'%(feb,hybrid))
        mean_g.SetName('baseline_%i.%i_ge'%(layer,module))
        mean_g.SetTitle('Baseline vs Channel for %i.%i;Channel;Baseline'%(layer,module))
        mean_g.SetMarkerStyle(3)
        mean_g_dict[nIndex]=mean_g

        rms_g = r.TGraph( len(chList), np.array(chList), np.array(rmsList) )
        #rms_g.SetName('ENC_%i.%i_g'%(feb,hybrid))
        #rms_g.SetTitle('ENCs vs Channel for %i.%i;Channel;ENC'%(feb,hybrid))
        rms_g.SetName('ENC_%i.%i_g'%(layer,module))
        rms_g.SetTitle('ENCs vs Channel for %i.%i;Channel;ENC'%(layer,module))
        rms_g.SetMarkerStyle(3)
        rms_g_dict[nIndex]=rms_g
        pass
    pass

if options.inName==0: 
    outFile = r.TFile(options.outfilename,"RECREATE")
else: 
    outFile=r.TFile("fits/hpssvt_00%s_baselineFits.root"%options.inName, "RECREATE")
outFile.cd()

fDirs={}
nIndices.sort()
print nIndices

for layer in xrange(1,15):
    for module in xrange(4):
        if layer < 9 and module > 1: continue
        index=layer+module*0.1
        print "Writing:", index
        fDirs[index]=outFile.mkdir('%i.%i'%(layer,module))
        fDirs[index].cd()
        mean_g_dict[index].Write()
        rms_g_dict[index].Write()

outFile.Close()

exit
