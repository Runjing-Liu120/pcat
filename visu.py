# common imports
from __init__ import *

# internal functions
from util import *

def plot_post(pathprobcatl):
    
    hdun = pf.open(pathprobcatl)

    print 'Loading PCAT output file %s...' % pathprobcatl
    print pf.info(pathprobcatl)

    gdat = gdatstrt()
    
    gdat.numbener = hdun[0].header['numbener']
    gdat.numbevtt = hdun[0].header['numbevtt']
    gdat.numbpopl = hdun[0].header['numbpopl']
    gdat.numbpsfipara = hdun[0].header['numbpsfipara']
    gdat.numbformpara = hdun[0].header['numbformpara']
    
    gdat.indxener = arange(gdat.numbener)
    gdat.indxevtt = arange(gdat.numbevtt)
    gdat.indxpopl = arange(gdat.numbpopl)
    
    gdat.numbsamp = hdun[0].header['numbsamp']
    gdat.numbburn = hdun[0].header['numbburn']
    gdat.numbswep = hdun[0].header['numbswep']
    gdat.factthin = hdun[0].header['factthin']
    gdat.numbpopl = hdun[0].header['numbpopl']
    gdat.numbproc = hdun[0].header['numbproc']

    gdat.maxmgang = hdun[0].header['maxmgang']
    gdat.lgalcntr = hdun[0].header['lgalcntr']
    gdat.bgalcntr = hdun[0].header['bgalcntr']
    gdat.numbflux = hdun[0].header['numbflux']

    gdat.minmlgal = hdun[0].header['minmlgal']
    gdat.maxmlgal = hdun[0].header['maxmlgal']
    gdat.minmbgal = hdun[0].header['minmbgal']
    gdat.maxmbgal = hdun[0].header['maxmbgal']
    
    gdat.minmflux = hdun[0].header['minmflux']
    gdat.maxmflux = hdun[0].header['maxmflux']
    gdat.minmsind = hdun[0].header['minmsind']
    gdat.maxmsind = hdun[0].header['maxmsind']

    gdat.datatype = hdun[0].header['datatype']
    gdat.regitype = hdun[0].header['regitype']
    gdat.psfntype = hdun[0].header['psfntype']
    gdat.exprtype = hdun[0].header['exprtype']
    gdat.pixltype = hdun[0].header['pixltype']
    gdat.fdfntype = hdun[0].header['fdfntype']

    if gdat.pixltype == 'heal':
        gdat.numbsideheal = hdun[0].header['numbsideheal']
    else:
        gdat.numbsidecart = hdun[0].header['numbsidecart']

    gdat.trueinfo = hdun[0].header['trueinfo']
    
    gdat.margsize = hdun[0].header['margsize']
    gdat.strgtime = hdun[0].header['strgtime']
    gdat.strgcnfg = hdun[0].header['strgcnfg']

    gdat.stdvfdfnnorm = hdun[0].header['stdvfdfnnorm']
    gdat.stdvfdfnslop = hdun[0].header['stdvfdfnslop']
    gdat.stdvpsfipara = hdun[0].header['stdvpsfipara']
    gdat.stdvback = hdun[0].header['stdvback']
    gdat.stdvlbhl = hdun[0].header['stdvlbhl']
    gdat.stdvflux = hdun[0].header['stdvflux']
    gdat.radispmrlbhl = hdun[0].header['radispmrlbhl']
    gdat.fracrand = hdun[0].header['fracrand']

    if gdat.trueinfo and gdat.datatype == 'mock':
        gdat.mockpsfntype = hdun[0].header['mockpsfntype']

    gdat.strgexpr = hdun[0].header['strgexpr']
    gdat.strgback = []
    gdat.lablback = []
    gdat.nameback = []
    k = 0
    while True:
        try:
            gdat.strgback.append(hdun[0].header['strgback%04d' % k])
            gdat.lablback.append(hdun[0].header['lablback%04d' % k])
            gdat.nameback.append(hdun[0].header['nameback%04d' % k])
            k += 1
        except:
            break
    gdat.strgexpo = hdun[0].header['strgexpo']

    gdat.levi = hdun[0].header['levi']
    gdat.info = hdun[0].header['info']
    
    gdat.indxenerincl = hdun['indxenerincl'].data
    gdat.indxevttincl = hdun['indxevttincl'].data

    gdat.maxmnumbpnts = hdun['maxmnumbpnts'].data
        
    gdat.listlgalhist = hdun['lgalhist'].data
    gdat.listbgalhist = hdun['bgalhist'].data
    gdat.listganghist = hdun['ganghist'].data
    gdat.listaanghist = hdun['aanghist'].data
    gdat.listspechist = hdun['spechist'].data
    gdat.listsindhist = hdun['sindhist'].data
    
    pntsprob = hdun['pntsprob'].data
    
    listllik = hdun['llik'].data
    listlpri = hdun['lpri'].data
    
    gmrbstat = hdun['gmrbstat'].data
    listmodlcnts = hdun['modlcnts'].data
    
    if gdat.trueinfo and gdat.datatype == 'mock':
        gdat.mockfdfntype = hdun[0].header['mockfdfntype']
        if gdat.mockfdfntype == 'powr':
            gdat.mockfdfnslop = hdun['mockfdfnslop'].data
        if gdat.mockfdfntype == 'brok':
            gdat.mockfdfnsloplowr = hdun['mockfdfnsloplowr'].data
            gdat.mockfdfnslopuppr = hdun['mockfdfnslopuppr'].data
            gdat.mockfdfnbrek = hdun['mockfdfnbrek'].data
        gdat.mocknormback = hdun['mocknormback'].data
        gdat.mocknumbpnts = hdun['mocknumbpnts'].data

    # prior boundaries
    gdat.minmnormback = hdun['minmnormback'].data
    gdat.maxmnormback = hdun['maxmnormback'].data

    gdat.meansdfn = hdun['meansdfn'].data
    gdat.stdvsdfn = hdun['stdvsdfn'].data
        
    # bins
    gdat.binsener = hdun['binsener'].data
    gdat.indxenerfdfn = array([hdun[0].header['indxenerfdfn']])
   
    # hyperprior limits
    gdat.minmfdfnnorm = hdun['minmfdfnnorm'].data 
    gdat.maxmfdfnnorm = hdun['maxmfdfnnorm'].data
    if gdat.fdfntype == 'powr':
        gdat.minmfdfnslop = hdun['minmfdfnslop'].data
        gdat.maxmfdfnslop = hdun['maxmfdfnslop'].data
    if gdat.fdfntype == 'brok':
        gdat.minmfdfnbrek = hdun['minmfdfnbrek'].data
        gdat.maxmfdfnbrek = hdun['maxmfdfnbrek'].data
        gdat.minmfdfnsloplowr = hdun['minmfdfnsloplowr'].data
        gdat.maxmfdfnsloplowr = hdun['maxmfdfnsloplowr'].data
        gdat.minmfdfnslopuppr = hdun['minmfdfnslopuppr'].data
        gdat.maxmfdfnslopuppr = hdun['maxmfdfnslopuppr'].data
        
    # utilities
    gdat.listsamp = hdun['listsamp'].data
    gdat.probprop = hdun['probprop'].data
    gdat.listindxprop = hdun['indxprop'].data
    gdat.listchrototl = hdun['listchrototl'].data
    gdat.listchrollik = hdun['listchrollik'].data
    gdat.listaccp = hdun['accp'].data
    gdat.listindxparamodi = hdun['indxparamodi'].data
    gdat.listauxipara = hdun['auxipara'].data
    gdat.listlaccfrac = hdun['laccfrac'].data
    gdat.listnumbpair = hdun['numbpair'].data
    gdat.listjcbnfact = hdun['jcbnfact'].data
    gdat.listcombfact = hdun['combfact'].data
    gdat.listpntsfluxmean = hdun['listpntsfluxmean'].data

    # posterior distributions
    gdat.listnumbpnts = hdun['numbpnts'].data
    gdat.listfdfnnorm = hdun['fdfnnorm'].data
    if gdat.fdfntype == 'powr':
        gdat.listfdfnslop = hdun['fdfnslop'].data
    if gdat.fdfntype == 'brok':
        gdat.listfdfnsloplowr = hdun['fdfnsloplowr'].data
        gdat.listfdfnslopuppr = hdun['fdfnslopuppr'].data
        gdat.listfdfnbrek = hdun['fdfnbrek'].data
    gdat.listpsfipara = hdun['psfipara'].data
    gdat.listnormback = hdun['normback'].data

    gdat.makeplot = True

    # setup the sampler
    setp(gdat) 

    # truth gdat.information
    if gdat.datatype == 'mock':
        gdat.truenumbpnts = hdun['mocknumbpnts'].data
        gdat.truelgal = []
        gdat.truebgal = []
        gdat.truespec = []
        gdat.truesind = []
        for l in gdat.indxpopl:
            gdat.truelgal.append(hdun['mocklgalpop%d' % l].data)
            gdat.truebgal.append(hdun['mockbgalpop%d' % l].data)
            gdat.truespec.append(hdun['mockspecpop%d' % l].data)
            gdat.truesind.append(hdun['mocksindpop%d' % l].data)
        if gdat.mockfdfntype == 'powr':
            gdat.mockfdfnslop = hdun['mockfdfnslop'].data
        if gdat.mockfdfntype == 'brok':
            gdat.mockfdfnbrek = hdun['mockfdfnbrek'].data
            gdat.mockfdfnsloplowr = hdun['mockfdfnsloplowr'].data
            gdat.mockfdfnslopuppr = hdun['mockfdfnslopuppr'].data
        gdat.truenormback = hdun['mocknormback'].data
        gdat.truepsfipara = hdun['mockpsfipara'].data
        
    gdat.listlgal = [[] for l in gdat.indxpopl]
    gdat.listbgal = [[] for l in gdat.indxpopl]
    gdat.listspec = [[] for l in gdat.indxpopl]
    gdat.listsind = [[] for l in gdat.indxpopl]
    gdat.listgang = [[] for l in gdat.indxpopl]
    gdat.listaang = [[] for l in gdat.indxpopl]
    for l in gdat.indxpopl:
        lgal = hdun['lgalpop%d' % l].data
        bgal = hdun['bgalpop%d' % l].data
        spec = hdun['specpop%d' % l].data
        sind = hdun['sindpop%d' % l].data
        gang = hdun['gangpop%d' % l].data
        aang = hdun['aangpop%d' % l].data
        for j in gdat.indxsamptotl:
            indxpnts = where(spec[j, gdat.indxenerfdfn[0], :] > 0.)[0]
            print 'hey'
            print 'indxpnts'
            print indxpnts
            numbpnts = indxpnts.size
            gdat.listlgal[l].append(lgal[j, indxpnts])
            gdat.listbgal[l].append(bgal[j, indxpnts])
            # temp
            gdat.listspec[l].append(spec[j, :, indxpnts].T)
            gdat.listsind[l].append(sind[j, indxpnts])
            gdat.listgang[l].append(gang[j, indxpnts])
            gdat.listaang[l].append(aang[j, indxpnts])

    # Gelman-Rubin test
    if gdat.numbproc > 1 and gdat.numbsamp > 1:
        print 'Making the Gelman-Rubin TS plot...'
        tim0 = time.time()
        
        figr, axis = plt.subplots()
        bins = linspace(1., amax(gmrbstat), 40)
        print 'hey'
        print 'bins'
        print bins
        print 'gmrbstat'
        print gmrbstat
        print
        axis.hist(gmrbstat, bins=bins)
        axis.set_title('Gelman-Rubin Convergence Test')
        axis.set_xlabel('PSRF')
        axis.set_ylabel('$N_{pix}$')
        figr.savefig(gdat.pathplot + 'gmrbdist_' + gdat.rtag + '.pdf')
        plt.close(figr)
        
        tim1 = time.time()
        print 'Done in %.3g seconds.' % (tim1 - tim0)

    print 'Calculating the autocorrelation of the chain...'
    tim0 = time.time()
   
    numbsampatcr =  max(min(100, gdat.numbsamp / 2), 1)
    atcr = empty((numbsampatcr, gdat.numbpixlsave, gdat.numbproc))
    for b in gdat.indxproc:
        atcr[:, :, b] = tdpy.mcmc.retr_atcr(listmodlcnts[:, b, :], numbdela=numbsampatcr)
    figr, axis = plt.subplots()
    axis.plot(arange(numbsampatcr), mean(mean(atcr, axis=1), axis=1))
    axis.set_title('Autocorrelation')
    axis.set_xlabel('Sample index')
    axis.set_ylabel(r'$\tilde{\eta}$')
    figr.savefig(gdat.pathplot + 'atcr_' + gdat.rtag + '.pdf')
    plt.close(figr)
    
    tim1 = time.time()
    print 'Done in %.3g seconds.' % (tim1 - tim0)

    print 'Calculating proposal and acceptance rates...'
    tim0 = time.time()

    mcmctimebins = linspace(0., gdat.numbswep, 100)
    figr, axgr = plt.subplots(gdat.numbprop, 1, figsize=(10, 15), sharex='all')
    for g, axis in enumerate(axgr):
        axis.hist(where(gdat.listindxprop == g)[0], bins=mcmctimebins)
        axis.hist(where((gdat.listindxprop == g) & (gdat.listaccp == True))[0], bins=mcmctimebins)
        axis.set_ylabel('%d' % g)
        if g == gdat.numbprop - 1:
            axis.set_xlabel('$i_{samp}$')
    figr.savefig(gdat.pathplot + 'propeffi_' + gdat.rtag + '.pdf')
    figr.subplots_adjust(hspace=0.)
    plt.close(figr)
    
    print 'hey'
    print 'gdat.listindxprop'
    print gdat.listindxprop
    indxsampsplt = where(gdat.listindxprop == gdat.indxpropsplt)[0]
    indxsampmerg = where(gdat.listindxprop == gdat.indxpropmerg)[0]
            
    listname = ['laccfrac', 'numbpair', 'combfact', 'jcbnfact']
    listvarb = [gdat.listlaccfrac, gdat.listnumbpair, gdat.listcombfact, gdat.listjcbnfact]
    for k in range(4):
        figr, axis = plt.subplots()
        
        print 'hey'
        print 'indxsampsplt'
        print indxsampsplt
        print 'indxsampmerg'
        print indxsampmerg
        print

        axis.hist(listvarb[k][indxsampsplt])
        axis.hist(listvarb[k][indxsampmerg])
        axis.set_ylabel('$N_{samp}$')
        axis.set_xlabel(listname[k])
        figr.subplots_adjust(bottom=0.2)
        figr.savefig(gdat.pathplot + listname[k] + gdat.rtag + '.pdf')
        plt.close(figr)
    
    tim1 = time.time()
    print 'Done in %.3g seconds.' % (tim1 - tim0)
    print 'Calculating proposal execution times...'
    tim0 = time.time()

    plot_chro(gdat)
    
    tim1 = time.time()
    print 'Done in %.3g seconds.' % (tim1 - tim0)
    print 'Making the grid posterior plot...'
    tim0 = time.time()
    
    numbpararand = min(sum(gdat.maxmnumbpnts) * gdat.numbcomp, 50)
    print 'hey'
    print 'numbpararand'
    print numbpararand
    print 
    indxparatemp = concatenate([arange(gdat.indxsampcompinit), sort(choice(arange(gdat.indxsampcompinit, gdat.numbpara), size=numbpararand, replace=False))])
    path = gdat.pathplot + 'listsamp_' + gdat.rtag + '_'
    tdpy.mcmc.plot_grid(path, gdat.listsamp[:, indxparatemp], ['%d' % k for k in indxparatemp], numbplotside=10)

    numbpntspost = 3
    if gdat.trueinfo and gdat.datatype == 'mock' and gdat.mocknumbpnts[0] == numbpntspost and gdat.numbpopl == 1:
        numbpara = numbpntspost * gdat.numbcompcolr + gdat.numbener
        listpost = zeros((gdat.numbsamp, numbpara))
        for j in gdat.indxsamptotl:
            for k in range(numbpntspost):
                listpost[j, 0*numbpntspost+k] = gdat.listlgal[0][j][k]
                listpost[j, 1*numbpntspost+k] = gdat.listbgal[0][j][k]
                listpost[j, 2*numbpntspost+k] = gdat.listspec[0][j][gdat.indxenerfdfn[0], k]
                listpost[j, 3*numbpntspost+k] = gdat.listsind[0][j][k]
        for i in gdat.indxener:
            listpost[:, 4*numbpntspost+i] = gdat.listnormback[:, 0, i]
        truepost = zeros(numbpara)
        truepost[0*numbpntspost:1*numbpntspost] = gdat.truelgal[0][k]
        truepost[1*numbpntspost:2*numbpntspost] = gdat.truebgal[0][k]
        truepost[2*numbpntspost:3*numbpntspost] = gdat.truespec[0][0, gdat.indxenerfdfn, k]
        truepost[3*numbpntspost:4*numbpntspost] = gdat.truesind[0][k]
        truepost[4*numbpntspost:] = gdat.truenormback[0, :]
        path = gdat.pathplot + 'postdist_' + gdat.rtag
        strgpost = ['$%s_%d$' % (strg, indxpnts + 1) for strg in ['l', 'b', 'f', 's'] for indxpnts in arange(numbpnts)]
        strgpost += ['$A_{%d}$' % i for i in gdat.indxener]
        tdpy.mcmc.plot_grid(path, listpost, strgpost, truepara=truepost, numbtickbins=3)
           
    tim1 = time.time()
    print 'Done in %.3g seconds.' % (tim1 - tim0)
    print 'Parsing the sample bundle and making frames...'
    tim0 = time.time()
    
    # flux match with the true catalog
    print 'hey'
    print 'gdat.indxsamptotl'
    print gdat.indxsamptotl
    if gdat.trueinfo:
        for l in gdat.indxpopl:
            discspecmtch = zeros(gdat.truenumbpnts) + gdat.numbsamp
            listindxmodl = []
            for p in gdat.indxsamptotl:
                indxmodl, indxtruepntsmiss = pair_catl(gdat, l, gdat.listlgal[l][p], gdat.listbgal[l][p], gdat.listspec[l][p])
                listindxmodl.append(indxmodl)
                discspecmtch[indxtruepntsmiss] -= 1.
            discspecmtch /= gdat.numbsamp
            postspecmtch = zeros((3, gdat.numbener, gdat.truenumbpnts[l]))
            for i in gdat.indxener:
                gdat.listspecmtch = zeros((gdat.numbsamp, gdat.truenumbpnts[l]))
                for p in gdat.indxsamptotl:
                    indxpntstrue = where(listindxmodl[p] >= 0)[0]
                    print 'hey'
                    print 'indxpntstrue'
                    print indxpntstrue
                    print 'gdat.listspecmtch'
                    print gdat.listspecmtch.shape
                    print 'gdat.listspec[l][j]'
                    print gdat.listspec[l][j].shape
                    print 'listindxmodl[j]'
                    print listindxmodl[j].shape
                    print
                    gdat.listspecmtch[p, indxpntstrue] = gdat.listspec[l][p][i, listindxmodl[p][indxpntstrue]]
                postspecmtch[0, i, :] = percentile(gdat.listspecmtch, 16., axis=0)
                postspecmtch[1, i, :] = percentile(gdat.listspecmtch, 50., axis=0)
                postspecmtch[2, i, :] = percentile(gdat.listspecmtch, 84., axis=0)
            plot_scatspec(gdat, l, postspecmtch=postspecmtch)

    tim1 = time.time()
    print 'Done in %.3g seconds.' % (tim1 - tim0)
    print 'Making posterior distribution plots...'

    if gdat.pixltype == 'heal':
        reso = 60. / gdat.numbsideheal
        numbbinslgcr = int((gdat.maxmlgal - gdat.minmlgal) / reso)
        numbbinsbgcr = int((gdat.maxmbgal - gdat.minmbgal) / reso)
        pntsprobcart = zeros((numbbinslgcr, numbbinsbgcr, gdat.numbpopl, gdat.numbener, gdat.numbflux))
        for l in gdat.indxpopl:
            for i in gdat.indxener:
                for h in range(gdat.numbflux):
                    pntsprobcart[:, :, l, i, h] = tdpy.util.retr_cart(pntsprob[l, i, :, h], 
                                                                      indxpixlrofi=gdat.indxpixlrofi, \
                                                                      numbsideinpt=gdat.numbsideheal, \
                                                                      minmlgal=gdat.minmlgal, \
                                                                      maxmlgal=gdat.maxmlgal, \
                                                                      minmbgal=gdat.minmbgal, \
                                                                      maxmbgal=gdat.maxmbgal, \
                                                                      reso=reso)
    else:
        pntsprobcart = pntsprob.reshape((gdat.numbpopl, gdat.numbener, gdat.numbsidecart, gdat.numbsidecart, gdat.numbflux))
        pntsprobcart = swapaxes(swapaxes(pntsprobcart, 0, 2), 1, 3)
        
    # stacked posteiors binned in position and flux
    plot_pntsprob(gdat, pntsprobcart, ptag='quad')
    plot_pntsprob(gdat, pntsprobcart, ptag='full', full=True)
    plot_pntsprob(gdat, pntsprobcart, ptag='cumu', cumu=True)
  
    if gdat.exprtype == 'ferm':
        retr_fgl3(gdat)

    # flux distribution
    for l in gdat.indxpopl:
        plot_histspec(gdat, l, listspechist=gdat.listspechist[:, l, :, :])

    # color distribution
    for l in gdat.indxpopl:
        plot_histsind(gdat, l, listsindhist=gdat.listsindhist[:, l, :])

    # fraction of emission components
    if gdat.numbback == 2:
        postpntsfluxmean = retr_postvarb(gdat.listpntsfluxmean)
        postnormback = retr_postvarb(gdat.listnormback)
        plot_compfrac(gdat, postpntsfluxmean=postpntsfluxmean, postnormback=postnormback)

    # PSF parameters
    path = gdat.pathplot + 'psfipara_' + gdat.rtag
    if gdat.psfntype == 'singgaus' or gdat.psfntype == 'singking':
        gdat.listpsfipara[:, gdat.indxpsfiparainit] = rad2deg(gdat.listpsfipara[:, gdat.indxpsfiparainit])
        if gdat.trueinfo:
            gdat.truepsfipara[gdat.indxpsfiparainit] = rad2deg(gdat.truepsfipara[gdat.indxpsfiparainit])
    elif gdat.psfntype == 'doubgaus' or gdat.psfntype == 'gausking':
        gdat.listpsfipara[:, gdat.indxpsfiparainit+1] = rad2deg(gdat.listpsfipara[:, gdat.indxpsfiparainit+1])
        gdat.listpsfipara[:, gdat.indxpsfiparainit+2] = rad2deg(gdat.listpsfipara[:, gdat.indxpsfiparainit+2])
        if gdat.trueinfo:
            gdat.truepsfipara[gdat.indxpsfiparainit+1] = rad2deg(gdat.truepsfipara[gdat.indxpsfiparainit+1])
            gdat.truepsfipara[gdat.indxpsfiparainit+2] = rad2deg(gdat.truepsfipara[gdat.indxpsfiparainit+2])
    elif gdat.psfntype == 'doubking':
        gdat.listpsfipara[:, gdat.indxpsfiparainit+1] = rad2deg(gdat.listpsfipara[:, gdat.indxpsfiparainit+1])
        gdat.listpsfipara[:, gdat.indxpsfiparainit+3] = rad2deg(gdat.listpsfipara[:, gdat.indxpsfiparainit+3])
        if gdat.trueinfo:
            gdat.truepsfipara[gdat.indxpsfiparainit+1] = rad2deg(gdat.truepsfipara[gdat.indxpsfiparainit+1])
            gdat.truepsfipara[gdat.indxpsfiparainit+3] = rad2deg(gdat.truepsfipara[gdat.indxpsfiparainit+3])
    if gdat.trueinfo and gdat.psfntype == 'doubking':
        truepara = gdat.truepsfipara
    else:
        truepara = array([None] * gdat.numbpsfipara)
    tdpy.mcmc.plot_grid(path, gdat.listpsfipara, gdat.strgpsfipara, truepara=truepara, numbplotside=gdat.numbformpara, \
        numbbins=gdat.numbbins, numbtickbins=3)
    
    for k in range(gdat.numbpsfipara):
        path = gdat.pathplot + 'psfipara%d_' % k + gdat.rtag + '_'
        tdpy.mcmc.plot_trac(path, gdat.listpsfipara[:, k], gdat.strgpsfipara[k])
    
    # log-likelihood
    path = gdat.pathplot + 'llik_' + gdat.rtag
    tdpy.mcmc.plot_trac(path, listllik.flatten(), '$P(D|y)$')

    # log-prior
    path = gdat.pathplot + 'lpri_' + gdat.rtag
    tdpy.mcmc.plot_trac(path, listlpri.flatten(), '$P(y)$')

    # number, expected number of PS and flux conditional prior power law index 
    for l in range(gdat.numbpopl):
        
        # number of point sources
        path = gdat.pathplot + 'numbpntsdist_pop%d_' % l + gdat.rtag
        if gdat.trueinfo and gdat.truenumbpnts != None:
            truepara = gdat.truenumbpnts[l]
        else:
            truepara = None
        tdpy.mcmc.plot_trac(path, gdat.listnumbpnts[:, l], '$N$', truepara=truepara)

        # mean number of point sources
        path = gdat.pathplot + 'fdfnnorm_pop%d_' % l + gdat.rtag
        truepara = None
        tdpy.mcmc.plot_trac(path, gdat.listfdfnnorm[:, l], '$\mu$', truepara=truepara, scalpara='logt')

        # flux distribution
        titl = gdat.binsenerstrg[gdat.indxenerfdfn]
        if gdat.fdfntype == 'powr':
            # power law index
            path = gdat.pathplot + 'fdfnslop_pop%d_' % l + gdat.rtag
            # temp
            if False and gdat.trueinfo and gdat.mockfdfntype == 'powr':
                truepara = gdat.mockfdfnslop[l]
            else:
                truepara = None
            labl =  r'$\alpha$'
            tdpy.mcmc.plot_trac(path, gdat.listfdfnslop[:, l], labl, truepara=truepara, titl=titl)
        
        if gdat.fdfntype == 'brok':
            # lower power law index
            path = gdat.pathplot + 'fdfnsloplowr_pop%d_' % l + gdat.rtag
            if False and gdat.trueinfo and gdat.mockfdfntype == 'brok':
                truepara = gdat.mockfdfnsloplowr[l]
            else:
                truepara = None
            labl =  r'$\alpha_1$'
            tdpy.mcmc.plot_trac(path, gdat.listfdfnsloplowr[:, l], labl, truepara=truepara, titl=titl)
        
            # uppr power law index
            path = gdat.pathplot + 'fdfnslopuppr_pop%d_' % l + gdat.rtag
            if False and gdat.trueinfo and gdat.mockfdfntype == 'brok':
                truepara = gdat.mockfdfnslopuppr[l]
            else:
                truepara = None
            labl =  r'$\alpha_2$'
            tdpy.mcmc.plot_trac(path, gdat.listfdfnslopuppr[:, l], labl, truepara=truepara, titl=titl)
        
            # break flux
            path = gdat.pathplot + 'fdfnbrek_pop%d_' % l + gdat.rtag
            if False and gdat.trueinfo and gdat.mockfdfntype == 'brok':
                truepara = gdat.mockfdfnbrek[l]
            else:
                truepara = None
            labl =  r'$f_b$'
            tdpy.mcmc.plot_trac(path, gdat.listfdfnbrek[:, l], labl, truepara=truepara, titl=titl)
        
    # background normalization
    for i in gdat.indxener:
        for c in gdat.indxback:
            path = gdat.pathplot + gdat.nameback[c] + '%d_' % i + gdat.rtag
            if gdat.trueinfo and gdat.datatype == 'mock':
                truepara = gdat.truenormback[c, i]
            else:
                truepara = None
            titl = gdat.binsenerstrg[i]
            labl = gdat.lablback[c] + '$_{%d}$' % i
            tdpy.mcmc.plot_trac(path, gdat.listnormback[:, c, i], labl, truepara=truepara, titl=titl)

    # plot log-likelihood
    figr, axrw = plt.subplots(2, 1, figsize=(7, 12))
    figr.suptitle(r'$D_{KL} = %.5g, \ln P(D) = %.5g$' % (gdat.info, gdat.levi))
    for k, axis in enumerate(axrw):
        if k == 0:
            if amin(listllik) != amax(listllik):
                axis.hist(listllik.flatten())
                axis.set_ylabel(r'$N_{samp}$')
                axis.set_xlabel(r'$\ln P(D|x)$')
        else:
            if amin(listlpri) != amax(listlpri):
                axis.hist(listlpri.flatten())
                axis.set_ylabel(r'$N_{samp}$')
                axis.set_xlabel(r'$\ln P(x)$')
    figr.savefig(gdat.pathplot + 'leviinfo_' + gdat.rtag + '.pdf')
    plt.close(figr)

    #make_anim()

    tim1 = time.time()
    print 'Plots are produced in %.3g seconds.' % (tim1 - tim0)


def plot_chro(gdat):

    binstime = logspace(log10(amin(gdat.listchrototl[where(gdat.listchrototl > 0)] * 1e3)), log10(amax(gdat.listchrototl * 1e3)), 50)
    figr, axcl = plt.subplots(gdat.numbprop, 1, figsize=(10, 5 * gdat.numbprop))
    for k in range(gdat.numbprop):
        indxswepchro = where((gdat.listindxprop == k) & (gdat.listchrototl[:, 0] > 0))[0]
        if indxswepchro.size > 0:
            axcl[k].hist(gdat.listchrototl[indxswepchro, 0] * 1e3, binstime, log=True, label=gdat.strgprop[k])
        axcl[k].set_xlim([amin(binstime), amax(binstime)])
        axcl[k].set_ylim([0.5, None])
        axcl[k].set_ylabel(gdat.strgprop[k])
        axcl[k].set_xscale('log')
    axcl[-1].set_xlabel('$t$ [ms]')
    figr.savefig(gdat.pathplot + 'chroprop_' + gdat.rtag + '.pdf')
    plt.close(figr)

    labl = ['Total', 'Proposal', 'Prior', 'Likelihood']
    figr, axcl = plt.subplots(2, 1, figsize=(14, 10))
    for k in range(1, 4):
        axcl[0].hist(gdat.listchrototl[where(gdat.listchrototl[:, k] > 0)[0], k] * 1e3, binstime, log=True, label=labl[k])

    indxswepchro = where(gdat.listchrototl[:, 0])[0]
    if indxswepchro.size > 0:
        axcl[1].hist(gdat.listchrototl[indxswepchro, 0] * 1e3, binstime, log=True, label=labl[0], color='black')
    axcl[1].set_title(r'$\langle t \rangle$ = %.3g ms' % mean(gdat.listchrototl[where(gdat.listchrototl[:, 0] > 0)[0], 0] * 1e3))
    axcl[0].set_xlim([amin(binstime), amax(binstime)])
    axcl[1].set_xlabel('$t$ [ms]')
    axcl[0].set_xscale('log')
    axcl[1].set_xscale('log')
    axcl[0].set_ylim([0.5, None])
    axcl[1].set_ylim([0.5, None])
    axcl[0].legend(loc=1)
    axcl[1].legend(loc=2)
    figr.savefig(gdat.pathplot + 'chrototl_' + gdat.rtag + '.pdf')
    plt.close(figr)

    listlabl = ['Setup', 'Pixel', 'Mesh', 'PS Flux', 'Total Flux', 'Counts', 'Likelihood']
    figr, axcl = plt.subplots(gdat.numbchrollik, 1, figsize=(10, 26))
    
    maxmchrollik = amax(gdat.listchrollik * 1e3)
    if maxmchrollik > 0.:
        minmchrollik = amin(gdat.listchrollik[where(gdat.listchrollik > 0)] * 1e3)
        if maxmchrollik != minmchrollik:
            binstime = logspace(log10(minmchrollik), log10(maxmchrollik), 50)
            for k in range(gdat.numbchrollik):
                axcl[k].hist(gdat.listchrollik[where(gdat.listchrollik[:, k] > 0)[0], k] * 1e3, binstime, log=True, label=listlabl[k])
                axcl[k].set_xlim([amin(binstime), amax(binstime)])
                axcl[k].set_ylim([0.5, None])
                axcl[k].set_ylabel(listlabl[k])
                axcl[k].set_xscale('log')
            axcl[-1].set_xlabel('$t$ [ms]')
            figr.savefig(gdat.pathplot + 'chrollik_' + gdat.rtag + '.pdf')
            plt.close(figr)


def plot_compfrac(gdat, gdatmodi=None, postpntsfluxmean=None, postnormback=None):
    
    if postpntsfluxmean != None:
        post = True
    else:
        post = False
        
    listlinestyl = ['-', '--', '-.', ':']
    listcolr = ['black', 'b', 'b', 'b']
    listlabl = ['Data', 'PS', 'Iso', 'FDM']

    figr, axis = plt.subplots()
    
    listydat = empty((gdat.numbback + 2, gdat.numbener))
    listyerr = zeros((2, gdat.numbback + 2, gdat.numbener))
    
    listydat[0, :] = gdat.datafluxmean
    if post:
        listydat[1, :] = postpntsfluxmean[0, :]
        listyerr[:, 1, :] = retr_errrvarb(postpntsfluxmean)
        for c in gdat.indxback:
            listydat[c+2, :] = postnormback[0, c, :] * gdat.backfluxmean[c]
            listyerr[:, c+2, :] = retr_errrvarb(postnormback[:, c, :]) * gdat.backfluxmean[c]
    else:
        listydat[1, :] = mean(sum(gdat.thispntsflux * gdat.expo, 2) / sum(gdat.expo, 2), 1)
        for c in gdat.indxback:
            listydat[c+2, :] = gdatmodi.thissampvarb[gdat.indxsampnormback[c, :]] * gdat.backfluxmean[c]
    
    xdat = gdat.meanener
    for k in range(gdat.numbback + 2):
        ydat = gdat.meanener**2 * listydat[k, :]
        yerr = gdat.meanener**2 * listyerr[:, k, :]
        axis.errorbar(xdat, ydat, yerr=yerr, marker='o', markersize=5, ls=listlinestyl[k], color=listcolr[k], label=listlabl[k])

    # Fermi-LAT results
    # temp
    if False and gdat.trueinfo:
        if gdat.datatype == 'mock':
            pass
        else:
            if gdat.exprtype == 'ferm':
                listname = ['data', 'pion', 'invc', 'brem', 'pnts', 'isot']
                listmrkr = ['o', 's', 'p', '*', 'D', '^']
                listcolr = ['g', 'g', 'g', 'g', 'g', 'g']
                listlabl = ['Fermi-LAT Data', r'Fermi-LAT $\pi^0$', 'Fermi-LAT ICS', 'Fermi-LAT Brem', 'Fermi-LAT PS', 'Fermi-LAT Iso']
                for k, name in enumerate(listname):
                    path = os.environ["PCAT_DATA_PATH"] + '/fermspec' + name + '.csv'
                    data = loadtxt(path)
                    enertemp = data[:, 0] # [GeV]
                    fluxtemp = data[:, 1] * 1e-3 # [GeV/cm^2/s/sr]
                    fluxtemp = interp(gdat.meanener, enertemp, fluxtemp)
                    #fluxtemp = interpolate.interp1d(enertemp, fluxtemp)(gdat.meanener)
                    axis.plot(gdat.meanener, fluxtemp, marker=listmrkr[k], color=listcolr[k], label=listlabl[k])


    axis.set_xlim([amin(gdat.binsener), amax(gdat.binsener)])
    axis.set_yscale('log')
    axis.set_xlabel('E [GeV]')
    axis.set_xscale('log')
    axis.set_ylabel('$E^2dN/dAdtd\Omega dE$ [GeV/cm$^2$/s/sr]')
    axis.legend()

    if post:
        path = gdat.pathplot + 'compfracspec_' + gdat.rtag + '.pdf'
    else:
        path = gdat.pathplot + 'compfracspec_' + gdat.rtag + '_%09d.pdf' % gdat.cntrswep
    plt.savefig(path)
    plt.close(figr)
   
    listlablbackflux = ['PS', 'Iso', 'FDM']
    listexpl = [0.1, 0, 0]

    listsize = zeros(gdat.numbback + 1)
    for k in range(gdat.numbback + 1):
        if gdat.numbener == 1:
            listsize[k] = gdat.diffener * listydat[k+1, :]
        else:
            listsize[k] = trapz(listydat[k+1, :], gdat.meanener)
    listsize *= 100. / sum(listsize)
        
    figr, axis = plt.subplots()

    axis.pie(listsize, explode=listexpl, labels=listlablbackflux, autopct='%1.1f%%')
    axis.axis('equal')

    if post:
        path = gdat.pathplot + 'compfrac_' + gdat.rtag + '.pdf'
    else:
        path = gdat.pathplot + 'compfrac_' + gdat.rtag + '_%09d.pdf' % gdat.cntrswep
    plt.savefig(path)
    plt.close(figr)
     

def plot_histsind(gdat, l, gdatmodi=None, listsindhist=None):
    
    if listsindhist == None:
        post = False
    else:
        post = True
        
    figr, axis = plt.subplots()
    if post:
        xdat = gdat.meansind
        postsindhist = retr_postvarb(listsindhist)
        ydat = postsindhist[0, :]
        yerr = retr_errrvarb(postsindhist)
        axis.errorbar(xdat, ydat, ls='', yerr=yerr, lw=1, marker='o', markersize=5, color='black')
    else:
        axis.hist(gdatmodi.thissampvarb[gdat.thisindxsampsind[l]], gdat.binssind, alpha=0.5, color='b', log=True, label='Sample')
    if gdat.trueinfo:
        axis.hist(gdat.truesind[l], gdat.binssind, alpha=0.5, color='g', log=True, label=gdat.truelabl)
        if gdat.datatype == 'mock':
            axis.hist(gdat.fgl3sind[gdat.indxfgl3rofi], gdat.binssind, alpha=0.1, color='red', log=True, label='3FGL')
    axis.set_yscale('log')
    axis.set_xlabel('$s$')
    axis.set_xlim([gdat.minmsind, gdat.maxmsind])
    axis.set_ylabel('$N$')
    axis.set_ylim([0.1, None])
    axis.legend()
    if post:
        path = gdat.pathplot + 'histsind_pop%d_' % l + gdat.rtag + '.pdf'
    else:
        path = gdat.pathplot + 'histsind_pop%d_' % l + gdat.rtag + '_%09d.pdf' % gdat.cntrswep
    plt.savefig(path)
    plt.close(figr)
    

def plot_histspec(gdat, l, gdatmodi=None, plotspec=False, listspechist=None):
   
    if listspechist == None:
        post = False
    else:
        post = True
    
    if plotspec:
        numbcols = gdat.numbener
    else:
        numbcols = 1

    figr, axcl = plt.subplots(1, numbcols, figsize=(7 * numbcols, 7))
    if plotspec:
        indxenertemp = gdat.indxener
    else:
        indxenertemp = gdat.indxenerfdfn
        axcltemp = []
        for i in gdat.indxener:
            if i == gdat.indxenerfdfn:
                axcltemp.append(axcl)
            else:
                axcltemp.append(None)
        axcl = axcltemp

    for i in indxenertemp:
        axis = axcl[i]
        if post:
            xdat = gdat.meanspec[i, :]
            postspechist = retr_postvarb(listspechist[:, :, i])
            ydat = postspechist[0, :]
            yerr = retr_errrvarb(postspechist)
            axis.errorbar(xdat, ydat, ls='', yerr=yerr, lw=1, marker='o', markersize=5, color='black')
        else:
            spec = gdatmodi.thissampvarb[gdat.thisindxsampspec[l]][i, :]
            axis.hist(spec, gdat.binsspec[i, :], alpha=0.5, color='b', log=True, label='Sample')
            if i == gdat.indxenerfdfn:
                if gdat.fdfntype == 'powr':
                    fdfnslop = gdatmodi.thissampvarb[gdat.indxsampfdfnslop[l]]  
                    fluxhistmodl = retr_fdfnpowr(gdat, gdatmodi.thissampvarb[gdat.indxsampfdfnnorm[l]], fdfnslop)
                if gdat.fdfntype == 'brok':
                    fdfnbrek = gdatmodi.thissampvarb[gdat.indxsampfdfnbrek[l]]  
                    fdfnsloplowr = gdatmodi.thissampvarb[gdat.indxsampfdfnsloplowr[l]]  
                    fdfnslopuppr = gdatmodi.thissampvarb[gdat.indxsampfdfnslopuppr[l]]  
                    fluxhistmodl = retr_fdfnbrok(gdat, gdatmodi.thissampvarb[gdat.indxsampfdfnnorm[l]], fdfnbrek, fdfnsloplowr, fdfnslopuppr)
                axis.plot(gdat.meanspec[i, :], fluxhistmodl, ls='--', alpha=0.5, color='b')
        if gdat.trueinfo:
            truehist = axis.hist(gdat.truespec[l][0, i, :], gdat.binsspec[i, :], alpha=0.5, color='g', log=True, label=gdat.truelabl)
            if gdat.datatype == 'mock':
                if gdat.exprtype == 'ferm':
                    axis.hist(gdat.fgl3spec[0, i, gdat.indxfgl3rofi], gdat.binsspec[i, :], color='red', alpha=0.1, log=True, label='3FGL')
        axis.set_yscale('log')
        axis.set_xlabel('$f$ ' + gdat.strgfluxunit)
        axis.set_xscale('log')
        axis.set_title(gdat.enerstrg[i])
        if gdat.trueinfo:
            axis.set_ylim([0.1, 1e3])
        axis.set_xlim([gdat.minmspec[i], gdat.maxmspec[i]])
        if plotspec:
            if i == 0:
                axis.set_ylabel('$N$')
            if i == numbcols / 2:
                axis.legend()
        else:
            axis.set_ylabel('$N$')
            axis.legend()
    figr.subplots_adjust(bottom=0.2, left=0.2)
    if plotspec:
        strg = 'spec'
    else:
        strg = 'flux'
    if post:
        path = gdat.pathplot + 'hist%s_pop%d_' % (strg, l) + gdat.rtag + '.pdf'
    else:
        path = gdat.pathplot + 'hist%s_pop%d_' % (strg, l) + gdat.rtag + '_%09d.pdf' % gdat.cntrswep
    plt.savefig(path)
    plt.close(figr)
    

def plot_scatspec(gdat, l, gdatmodi=None, postspecmtch=None):
    
    if postspecmtch != None:
        post = True
    else:
        post = False

    figr, axrw = plt.subplots(1, gdat.numbener, figsize=(7 * gdat.numbener, 6))
    if gdat.numbener == 1:
        axrw = [axrw]
    for i, axis in enumerate(axrw):

        xdat = gdat.truespec[l][0, i, :]
        xerr = retr_errrvarb(gdat.truespec[l][:, i, :])
        yerr = zeros((2, xdat.size))
 
        labl = '$f_{samp}$ ' + gdat.strgfluxunit
        axis.plot(gdat.meanspec[i, :], gdat.meanspec[i, :], ls='--', color='black', alpha=0.2)
        if postspecmtch != None:
            yerr[0, :] = postspecmtch[0, i, :]
            ydat = postspecmtch[1, i, :]
            yerr[1, :] = postspecmtch[2, i, :]
            yerr = fabs(yerr - ydat)
        else:
            ydat = gdatmodi.thisspecmtch[i, :]

        indx = where(ydat > 0.)[0]
        if indx.size > 0:
            axis.errorbar(xdat[indx], ydat[indx], ls='', yerr=yerr[:, indx], xerr=xerr[:, indx], lw=1, marker='o', markersize=5, color='black')
    
        if gdat.indxtruepntstimevari[l].size > 0:
            axis.errorbar(xdat[gdat.indxtruepntstimevari[l]], ydat[gdat.indxtruepntstimevari[l]], ls='', yerr=yerr[:, gdat.indxtruepntstimevari[l]], \
                lw=1, marker='o', markersize=5, color='red')
    
        axis.set_xlabel('$f_{true}$ ' + gdat.strgfluxunit)
        if i == 0:
            axis.set_ylabel(labl)
        axis.set_xscale('log')
        axis.set_yscale('log')
        axis.set_title(gdat.enerstrg[i])

        ylim = [gdat.minmspec[i], gdat.maxmspec[i]]
        
        axis.set_ylim(ylim)
        axis.set_xlim([gdat.minmspec[i], gdat.maxmspec[i]])
        axis.set_title(gdat.binsenerstrg[i])

    figr.subplots_adjust(left=0.2, wspace=0.4, bottom=0.2)

    if postspecmtch != None:
        path = gdat.pathplot + 'scatspec%d_' % l + gdat.rtag + '.pdf'
    elif gdatmodi.thisspecmtch != None:
        path = gdat.pathplot + 'scatspec%d_' % l + gdat.rtag + '_%09d.pdf' % gdat.cntrswep

    plt.savefig(path)
    plt.close(figr)


def plot_scatpixl(gdat, gdatmodi, l):
    
    figr, axgr = plt.subplots(gdat.numbevtt, gdat.numbener, figsize=(gdat.numbener * 7, gdat.numbevtt * 7))
    if gdat.numbevtt == 1:
        axgr = [axgr]
    for m, axrw in enumerate(axgr):
        if gdat.numbener == 1:
            axrw = [axrw]
        for i, axis in enumerate(axrw):
            
            slop, intc, coef, pval, stdv = sp.stats.linregress(gdat.datacnts[i, :, m], gdat.thismodlcnts[i, :, m])
            axis.scatter(gdat.datacnts[i, :, m], gdat.thismodlcnts[i, :, m], alpha=0.5)

            axislimt = [0., amax(gdat.datacnts[i, :, m]) * 1.5]
            axis.set_xlim(axislimt)
            axis.set_ylim(axislimt)
            
            axis.text(0.5, 0.9, '$m = %.3g, b = %.3g, r = %.3g$' % (slop, intc, coef), va='center', ha='center', transform=axis.transAxes, fontsize=16)
            if m == gdat.numbevtt - 1:
                axis.set_xlabel('Data Counts')
            if i == 0:
                labl = 'Model Counts'
                if gdat.exprtype == 'ferm':
                    labl += ', ' + gdat.evttstrg[m]
                axis.set_ylabel(labl)
            if m == 0:
                axis.set_title(gdat.enerstrg[i])
            
    figr.subplots_adjust(hspace=0.4, wspace=0.4, top=0.8)
    plt.savefig(gdat.pathplot + 'scatpixl%d_' % l + gdat.rtag + '_%09d.pdf' % gdat.cntrswep)
    plt.close(figr)
    
    
def plot_discspec(gdat, gdatmodi, l, discspecmtch=None):
    
    figr, axrw = plt.subplots(1, gdat.numbener, figsize=(7 * gdat.numbener, 6))
    if gdat.numbener == 1:
        axrw = [axrw]
    for i, axis in enumerate(axrw):
        xdat = gdat.truespec[l][0, i, :]
        xerr = retr_errrvarb(gdat.truespec[l][:, i, :])
        yerr = zeros((2, xdat.size))
        if discspecmtch != None:
            ydat = discspecmtch[i, :]
            labl = '$f_{hit}$'
            ylim = [0., 1.]
        if postspecmtch != None or gdatmodi.thisspecmtch != None:
            labl = '$f_{samp}$ ' + gdat.strgfluxunit
            axis.set_yscale('log')
            axis.plot(gdat.meanspec[i, :], gdat.meanspec[i, :], ls='--', color='black', alpha=0.2)
            if postspecmtch != None:
                yerr[0, :] = postspecmtch[0, i, :]
                ydat = postspecmtch[1, i, :]
                yerr[1, :] = postspecmtch[2, i, :]
                yerr = fabs(yerr - ydat)
            else:
                ydat = gdatmodi.thisspecmtch[i, :]
        axis.errorbar(xdat, ydat, ls='', yerr=yerr, lw=1, marker='o', markersize=5, color='black')
        axis.set_xlabel('$f_{true}$ ' + gdat.strgfluxunit)
        if i == 0:
            axis.set_ylabel(labl)
        axis.set_xscale('log')
        axis.set_title(gdat.enerstrg[i])
        if i == gdat.indxenerfdfn[0]:
            ylim = [gdat.minmspec[i], gdat.maxmspec[i]]
        axis.set_ylim(ylim)
        axis.set_xlim([gdat.minmspec[i], gdat.maxmspec[i]])
        axis.set_title(gdat.binsenerstrg[i])
    figr.subplots_adjust(wspace=0.4, bottom=0.2)
    path = gdat.pathplot + 'discspec%d_' % l + gdat.rtag + '_%09d.pdf' % gdat.cntrswep
    plt.savefig(path)
    plt.close(figr)

    
def plot_look(gdat):

    indxpixlproxsize = zeros(gdat.numbpixl)
    figr, axis = plt.subplots(figsize=(10, 6))
    for h in range(gdat.numbfluxprox):
        for j in gdat.indxpixl:
            indxpixlproxsize[j] = gdat.indxpixlprox[h][j].size
        binspixlsize = logspace(log10(amin(indxpixlproxsize)), log10(amax(indxpixlproxsize)), 100)
        axis.hist(indxpixlproxsize, binspixlsize, log=True, label='Flux bin %d' % h)
    axis.set_title("Number of pixels in the pixel lookup tables")
    axis.set_xlabel('Number of pixels')
    axis.set_ylabel("Number of tables")
    plt.subplots_adjust(bottom=0.2)
    plt.savefig(gdat.pathplot + 'look.pdf')
    plt.close()
    
    
def plot_psfn_type():
    
    devi = linspace(0., 5., 100)
    y = zeros((x.size, 5))

    figr, axis = plt.subplots(figsize=(10, 6))
    singgaus = retr_singgaus(devi, 0.25)
    axis.plot(devi, singgaus, label='Single Gaussian')

    singking = retr_singking(devi, 0.25, 10.)
    axis.plot(devi, singking, label='Single King')

    doubgaus = retr_doubgaus(devi, 0.1, 0.25, 1.)
    axis.plot(devi, doubgaus, label='Double Gaussian')

    gausking = retr_gausking(devi, 0.1, 0.25, 1., 10.)
    axis.plot(devi, gausking, label='Gaussian + King')

    doubking = retr_doubking(devi, 0.1, 0.25, 10., 1., 5.)
    axis.plot(devi, doubking, label='Double King')

    axis.legend()
    axis.set_xscale('log')
    axis.set_yscale('log')
    axis.set_ylim([1e-3, None])
    plt.show()
    
def plot_minmfluxinfo(minmfluxarry, listinfo, listlevi):
    
    figr, axis = plt.subplots(figsize=(14, 10))
    ax_ = axis.twinx()
    axis.plot(minmfluxarry, listinfo, label='Relative entropy')
    axis.legend(bbox_to_anchor=[0.2, 1.08], loc=2)
    
    ax_.plot(minmfluxarry, listlevi, label='Log-evidence', color='g')
    ax_.legend(bbox_to_anchor=[0.8, 1.08])

    axis.set_ylabel('$D_{KL}$ [nats]')
    ax_.set_ylabel(r'$\log P(D)$ [nats]')
    axis.set_xlabel('$f_{min}$ [1/cm$^2$/s/GeV]')
    axis.set_xscale('log')
    figr.savefig(os.environ["PCAT_DATA_PATH"] + '/imag/minmfluxinfo.pdf')
    plt.close(figr)
    
    
def plot_evidtest():
    
    minmgain = -1.
    maxmgain = 5.
    minmdevi = 0.
    maxmdevi = 5.
    gain = linspace(minmgain, maxmgain, 100)
    devi = linspace(minmdevi, maxmdevi, 100)

    evid = log(sqrt(1. + exp(2. * gain[None, :])) *                exp(-devi[:, None]**2 / 2. / (1. + 1. / exp(2. * gain[None, :]))))
    
    figr, axis = plt.subplots(figsize=(7, 7))
    figr.suptitle('Log-Bayesian Evidence For Lower-Dimension Model', fontsize=18)
    imag = axis.imshow(evid, extent=[minmgain, maxmgain, minmdevi, maxmdevi], cmap='winter', origin='lower')
    cset1 = plt.contourf(gain, devi, evid, cmap='winter')
    axis.set_xlabel('Information gain')
    axis.set_ylabel('Goodness of fit')
    plt.colorbar(imag, ax=axis, fraction=0.03)
    #figr.subplots_adjust(top=0.8)

    plt.savefig(gdat.pathplot + 'evidtest_' + gdat.rtag + '.pdf')
    plt.close(figr)
    
    
def plot_pntsprob(gdat, pntsprobcart, ptag, full=False, cumu=False):
    
    if cumu:
        numbrows = 1
        numbcols = 1
    else:
        numbcols = 2
        if full:
            numbrows = gdat.numbflux / 2
        else:
            numbrows = 2
        
    if gdat.exprtype == 'ferm':
        strgvarb = '$f$'
        strgunit = ' [cm$^2$ s GeV]'
    if gdat.exprtype == 'sdss':
        strgvarb = '$C$'
        strgunit = ' [counts]'
    titl = strgvarb + strgunit

    for l in gdat.indxpopl:
        figr, axgr = plt.subplots(numbrows, numbcols, figsize=(numbcols * 10, numbrows * 10), sharex='all', sharey='all')
        if numbrows == 1:
            axgr = [axgr]            
        figr.suptitle(titl, fontsize=18)
        for a, axrw in enumerate(axgr):
            if numbcols == 1:
                axrw = [axrw]
            for b, axis in enumerate(axrw):
                h = a * 2 + b
                if full:
                    indxlowr = h
                    indxuppr = h + 1
                elif cumu:
                    indxlowr = 0
                    indxuppr = gdat.numbflux
                else:
                    if h < 3:
                        indxlowr = 2 * h
                        indxuppr = 2 * (h + 1)
                    else:
                        indxlowr = 2 * h
                        indxuppr = gdat.numbflux
                temp = sum(pntsprobcart[:, :, l, gdat.indxenerfdfn[0], indxlowr:indxuppr], 2)
                imag = axis.imshow(temp, origin='lower', cmap='Reds', norm=mpl.colors.LogNorm(vmin=0.01, vmax=1), extent=gdat.exttrofi)
                plt.colorbar(imag, fraction=0.05, ax=axis)

                # superimpose true PS
                if gdat.trueinfo:
                    indxpnts = where((gdat.binsspec[gdat.indxenerfdfn, indxlowr] < gdat.truespec[l][0, gdat.indxenerfdfn, :]) & \
                        (gdat.truespec[l][0, gdat.indxenerfdfn, :] < gdat.binsspec[gdat.indxenerfdfn, indxuppr]))[0]
                    mar1 = axis.scatter(gdat.truelgal[l][indxpnts], gdat.truebgal[l][indxpnts], s=100, alpha=0.5, marker='x', lw=2, color='g')
                axis.set_xlabel(gdat.longlabl)
                axis.set_ylabel(gdat.latilabl)
                axis.set_xlim([gdat.frambndrmarg, -gdat.frambndrmarg])
                axis.set_ylim([-gdat.frambndrmarg, gdat.frambndrmarg])
                axis.axvline(gdat.frambndr, ls='--', alpha=0.3, color='black')
                axis.axvline(-gdat.frambndr, ls='--', alpha=0.3, color='black')
                axis.axhline(gdat.frambndr, ls='--', alpha=0.3, color='black')
                axis.axhline(-gdat.frambndr, ls='--', alpha=0.3, color='black')
                axis.set_title(tdpy.util.mexp(gdat.binsspec[gdat.indxenerfdfn, indxlowr]) + ' $<$ ' + \
                    strgvarb + ' $<$ ' + tdpy.util.mexp(gdat.binsspec[gdat.indxenerfdfn, indxuppr]))
        figr.subplots_adjust(hspace=0.2, wspace=0.2)
        figr.savefig(gdat.pathplot + 'pntsbind' + ptag + '%d%d' % (l, gdat.indxenerincl[gdat.indxenerfdfn]) + '_' + gdat.rtag + '.pdf')
        plt.close(figr)
       
    
def plot_king(gdat):

    angl = rad2deg(gdat.angldisp)

    figr, axgr = plt.subplots(1, 2, figsize=(12, 6))
    figr.suptitle('King Function', fontsize=20)
    for k, axis in enumerate(axgr):
        if k == 0:
            sigmlist = [0.25]
            gammlist = [1.01, 2.5, 10.]
            lloc = 3
        else:
            sigmlist = [0.1, 0.25, 1.]
            gammlist = [2.]
            lloc = 1
        for sigm in sigmlist:
            for gamm in gammlist:
                axis.plot(angl, retr_singking(angl, sigm, gamm), label=r'$\sigma = %.4g, \gamma = %.3g$' % (sigm, gamm))
        axis.legend(loc=lloc)
        axis.set_yscale('log')
        axis.set_xlabel(r'$\theta$ ' + gdat.strganglunit)
        axis.set_xlabel(r'$\mathcal{K}(\theta)$')
        
    figr.subplots_adjust(bottom=0.2)
    plt.savefig(gdat.pathplot + 'king.pdf')
    plt.close(figr)
    
    
def plot_psfn(gdat, gdatmodi):
    
    figr, axgr = plt.subplots(gdat.numbevtt, gdat.numbener, figsize=(7 * gdat.numbener, 7 * gdat.numbevtt))
    figr.suptitle(r'Point Spread Function, d$P$/d$\Omega$ [1/sr]', fontsize=20)
    if gdat.numbevtt == 1:
        axgr = [axgr]
    for m, axrw in enumerate(axgr):
        if gdat.numbener == 1:
            axrw = [axrw]
        for i, axis in enumerate(axrw):
            axis.plot(gdat.angldispplot, gdatmodi.thispsfn[i, :, m], label='Sample')
            if gdat.trueinfo:
                if gdat.exprtype == 'ferm':
                    labl = 'Fermi-LAT'
                if gdat.exprtype == 'sdss':
                    labl = 'SDSS'
                axis.plot(gdat.angldispplot, gdat.truepsfn[i, :, m], label=labl, color='g', ls='--')
            axis.set_yscale('log')
            if m == gdat.numbevtt - 1:
                axis.set_xlabel(r'$\theta$ ' + gdat.strganglunit)
            if i == 0 and gdat.exprtype == 'ferm':
                axis.set_ylabel(gdat.evttstrg[m])
            if m == 0:
                axis.set_title(gdat.enerstrg[i])  
            if i == gdat.numbener - 1 and m == gdat.numbevtt - 1:
                axis.legend(loc=2)
            indxsamp = gdat.indxsamppsfipara[i*gdat.numbformpara+m*gdat.numbener*gdat.numbformpara]
    
            if gdat.psfntype == 'singgaus':
                strg = r'$\sigma = %.3g$ ' % gdatmodi.thissampvarb[indxsamp]
            elif gdat.psfntype == 'singking':
                strg = r'$\sigma = %.3g$ ' % rad2deg(gdatmodi.thissampvarb[indxsamp]) + gdat.strganglunit + '\n'
                strg += r'$\gamma = %.3g$' % gdatmodi.thissampvarb[indxsamp+1]
            elif gdat.psfntype == 'doubgaus':
                strg = r'$f = %.3g$' % gdatmodi.thissampvarb[indxsamp] + '\n'
                strg += r'$\sigma = %.3g$ ' % rad2deg(gdatmodi.thissampvarb[indxsamp+1]) + gdat.strganglunit + '\n'
                strg += r'$\sigma = %.3g$ ' % rad2deg(gdatmodi.thissampvarb[indxsamp+2]) + gdat.strganglunit
            elif gdat.psfntype == 'gausking':
                strg = r'$f_G = %.3g$' % gdatmodi.thissampvarb[indxsamp] + '\n'
                strg += r'$\sigma_G = %.3g$ ' % rad2deg(gdatmodi.thissampvarb[indxsamp+1]) + gdat.strganglunit + '\n'
                strg += r'$\sigma_K = %.3g$ ' % rad2deg(gdatmodi.thissampvarb[indxsamp+2]) + gdat.strganglunit + '\n'
                strg += r'$\gamma = %.3g$' % gdatmodi.thissampvarb[indxsamp+3]
            elif gdat.psfntype == 'doubking':
                strg = r'$f_c = %.3g$' % gdatmodi.thissampvarb[indxsamp] + '\n'
                strg += r'$\sigma_c = %.3g$ ' % rad2deg(gdatmodi.thissampvarb[indxsamp+1]) + gdat.strganglunit + '\n'
                strg += r'$\gamma_c = %.3g$' % gdatmodi.thissampvarb[indxsamp+2] + '\n'
                strg += r'$\sigma_t = %.3g$ ' % rad2deg(gdatmodi.thissampvarb[indxsamp+3]) + gdat.strganglunit + '\n'
                strg += r'$\gamma_t = %.3g$' % gdatmodi.thissampvarb[indxsamp+4]
            axis.text(0.75, 0.75, strg, va='center', ha='center', transform=axis.transAxes, fontsize=18)
            
            if gdat.exprtype == 'ferm':
                axis.set_ylim([1e-3, 1e6])
            if gdat.exprtype == 'sdss':
                axis.set_ylim([1e4, 1e11])

    plt.savefig(gdat.pathplot + 'psfnprof_' + gdat.rtag + '_%09d.pdf' % gdat.cntrswep)
    plt.close(figr)
    
    
def plot_fwhm(gdat, gdatmodi):
    
    figr, axis = plt.subplots()

    tranfwhm = transpose(thisfwhm)
    imag = axis.imshow(rad2deg(tranfwhm), origin='lower', extent=[binsener[0], binsener[-1], 0, 4], cmap='BuPu', interpolation='none', alpha=0.4)
    plt.colorbar(imag, ax=axis, fraction=0.05)
    axis.set_xscale('log')
    axis.set_ylabel('PSF Class')
    axis.set_xlabel(r'$E_\gamma$ [GeV]')
    axis.set_yticks([0.5, 1.5, 2.5, 3.5])
    axis.set_yticklabels(['0', '1', '2', '3'])
    axis.set_xticks(binsener)
    axis.set_xticklabels(['%.2g' % binsener[i] for i in gdat.indxener])
    axis.set_title('PSF FWHM')
    for i in gdat.indxener:
        for m in indxevtt:
            axis.text(meanener[i], indxevttincl[m]+0.5, r'$%.3g^\circ$' % rad2deg(tranfwhm[m, i]), ha='center', va='center', fontsize=14)

    figr.subplots_adjust(bottom=0.2)
    plt.savefig(gdat.pathplot + 'fwhmcnts_' + gdat.rtag + '_%09d.pdf' % gdat.cntrswep)
    plt.close(figr)
    
    
def plot_backcntsmean(gdat, gdatmodi):
    
    figr, axis = plt.subplots()

    tragdat.numbbackcntsrofimean = transpose(backcntsmean)
    
    imag = axis.imshow(tragdat.numbbackcntsrofimean, origin='lower', extent=[binsener[0], binsener[-1], 0, 4],                      cmap='BuPu', interpolation='none', alpha=0.4)
    plt.colorbar(imag, ax=axis, fraction=0.05)
    axis.set_xscale('log')
    axis.set_ylabel('PSF Class')
    axis.set_xlabel(r'$E_\gamma$ [GeV]')
    axis.set_yticks([0.5, 1.5, 2.5, 3.5])
    axis.set_yticklabels(['0', '1', '2', '3'])
    axis.set_title('Mean FDM counts inumbside a PSF FWHM')
    for i in gdat.indxener:
        for m in indxevtt:
            axis.text(meanener[i], indxevttincl[m]+0.5, '%.3g' % tragdat.numbbackcntsrofimean[m, i], ha='center', va='center')
            
    figr.subplots_adjust(bottom=0.2)
    plt.savefig(gdat.pathplot + 'backcnts_' + gdat.rtag + '_%09d.pdf' % gdat.cntrswep)
    plt.close(figr)
    
    
def plot_datacntshist(gdat):

    figr, axgr = plt.subplots(gdat.numbevtt, gdat.numbener, figsize=(7 * gdat.numbener, 7 * gdat.numbevtt))
    if gdat.numbevtt == 1:
        axgr = [axgr]
    for m, axrw in enumerate(axgr):
        if gdat.numbener == 1:
            axrw = [axrw]
        for i, axis in enumerate(axrw):
            
            datacntstemp = gdat.datacnts[i, :, m]
            
            maxmdatacntstemp = amax(datacntstemp)
            minmdatacntstemp = amin(datacntstemp[where(datacntstemp > 0.)])
            gdat.binscntstemp = linspace(minmdatacntstemp, maxmdatacntstemp, 20)
            meancntstemp = (gdat.binscntstemp[1:] + gdat.binscntstemp[0:-1]) / 2.
            diffcntstemp = gdat.binscntstemp[1:] - gdat.binscntstemp[0:-1]
            
            datacntshist = axis.hist(datacntstemp, gdat.binscntstemp, color='b')[0]

            init = [meancntstemp[argmax(datacntshist)], 1.]
            
            axis.set_xlim([amin(gdat.binscntstemp), amax(gdat.binscntstemp)])
            if m == gdat.numbevtt - 1:
                axis.set_xlabel(r'$k$')
            #axis.set_xscale('log')
            if m == 0:
                axis.set_title(gdat.binsenerstrg[i])
            if i == 0 and gdat.exprtype == 'ferm':
                axis.set_ylabel(gdat.evttstrg[m])
        
    figr.subplots_adjust(wspace=0.3, hspace=0.2)
    plt.savefig(gdat.pathplot + 'datacntshist' + gdat.rtag + '.pdf')
    plt.close(figr)
    
    
def plot_intr():
    
    with plt.xkcd():

        from matplotlib import patheffects
        mpl.rcParams['path.effects'] = [patheffects.withStroke(linewidth=0)]

        figr, axis = plt.subplots(figsize=(14, 6))

        catl = arange(80)
        probcatl = pss.pmf(catl, 30.) + 0.5 * pss.pmf(catl, 60.)
        axis.plot(catl, probcatl)
        axis.set_xticks([10, 30, 60])
        axis.set_xticklabels(["Crackpot's Catalog", "Best-fit catalog", "Not-so-best-fit catalog"])
        axis.set_yticks([])
        text = axis.set_title("Exploring the catalog space with Probabilistic cataloging")
        text.set_position([.5, 1.05])
        axis.set_xlabel('Catalog index')
        axis.set_ylabel("Probability")
        
        axis.tick_params(axis='x', colors='#B6E954')
        axis.tick_params(axis='y', colors='#B6E954')
        axis.spines['bottom'].set_color('#B6E954')
        axis.spines['top'].set_color('#B6E954') 
        axis.spines['right'].set_color('#B6E954')
        axis.spines['left'].set_color('#B6E954')
        axis.yaxis.label.set_color('#B6E954')
        axis.xaxis.label.set_color('#B6E954')
        axis.title.set_color('#B6E954')

        axis.set_axis_bgcolor('black')
        figr.set_facecolor('black')
        figr.subplots_adjust(bottom=0.15, top=0.9)
        plt.savefig(os.environ["PCAT_DATA_PATH"] + '/imag/talkintr.pdf', facecolor=figr.get_facecolor())
        plt.close()  
        
        
def plot_eval(gdat):

    figr, axis = plt.subplots()
    for k in range(gdat.numbfluxprox + 1):
        if k == 0 or k == gdat.numbfluxprox:
            alph = 1.
            if k == 0:
                labl = 'Dimmest PS'
                colr = 'b'
            else:
                labl = 'Brightest PS'
                colr = 'g'
        else:
            alph = 0.2
            labl = None
            colr = 'black'
        axis.plot(gdat.angldispplot, gdat.binsfluxprox[k] * gdat.truepsfn[0, :, 0], label=labl, color=colr, alpha=alph)
        if k > 0:
            axis.axvline(gdat.maxmangleval[k-1], ls='--', alpha=alph, color=colr)
    axis.set_yscale('log')
    axis.set_xlabel(r'$\theta$ ' + gdat.strganglunit)
    axis.set_ylabel('$f$ [1/cm$^2$/s/sr/GeV]')
    axis.set_title('PSF Evaluation Radius')  
    axis.axhline(gdat.specfraceval * amax(gdat.binsfluxprox[0] * gdat.truepsfn[0, :, 0]), color='red', ls=':', label='Flux floor')
    axis.legend(loc=3)
    plt.savefig(gdat.pathplot + 'eval_' + gdat.rtag + '.pdf')
    plt.close(figr)


def plot_3fgl_thrs(gdat):

    path = os.environ["PCAT_DATA_PATH"] + '/detthresh_P7v15source_4years_PL22.fits'
    fluxthrs = pf.getdata(path, 0)

    bgalfgl3 = linspace(-90., 90., 481)
    lgalfgl3 = linspace(-180., 180., 960)

    bgalexpo = linspace(-90., 90., 400)
    lgalexpo = linspace(-180., 180., 800)

    #fluxthrs = interp2d(lgalfgl3, bgalfgl3, fluxthrs)(lgalexpo, bgalexpo)
    fluxthrs = griddata([lgalfgl3, bgalfgl3], fluxthrs, [gdat.lgalheal, gdat.bgalheal])

    cntsthrs = fluxthrs * gdat.expo

    jbgal = where(abs(bgalexpo) < 10.)[0]
    jlgal = where(abs(lgalexpo) < 10.)[0]
    extent = [-10, 10, -10, 10]
    
    figr, axis = plt.subplots(figsize=(12, 12))
    axis.set_xlabel(gdat.longlabl)
    axis.set_ylabel(gdat.latilabl)

    axis.set_title('3FGL Detection Flux Threshold [1/cm$^2$/s], 1.0 GeV - 10. GeV')
    imag = plt.imshow(fluxthrs[amin(jbgal):amax(jbgal)+1, amin(jlghprofi):amax(jlghprofi)+1], origin='lower', cmap='Reds', extent=gdat.exttrofi)
    plt.colorbar(imag, fraction=0.05)
    plt.savefig(gdat.pathplot + 'thrs_' + gdat.rtag + '.pdf')
    plt.close(figr)
    
    
def plot_fgl3(gdat):
    
    numbbins = 40
    figr, axis = plt.subplots()
    bins = logspace(log10(amin(gdat.fgl3timevari[where(gdat.fgl3timevari > 0.)[0]])), log10(amax(gdat.fgl3timevari)), numbbins)
    axis.hist(gdat.fgl3timevari, bins=bins, label='All', log=True)
    axis.hist(gdat.fgl3timevari[gdat.indxfgl3rofi], bins=bins, label='ROI', log=True)
    axis.axvline(72.44, ls='--', alpha=0.5, color='black')
    axis.set_xlabel('3FGL time variability index')
    axis.set_xscale('log')
    axis.legend()
    axis.set_ylim([0.1, None])
    plt.savefig(gdat.pathplot + 'fgl3timevari.pdf')
    plt.close(figr)
    

    figr, axis = plt.subplots()
    indxfgl3scut = where(isfinite(gdat.fgl3scut))[0]
    bins = linspace(amin(gdat.fgl3scut[indxfgl3scut]), amax(gdat.fgl3scut[indxfgl3scut]), numbbins)
    axis.hist(gdat.fgl3scut[indxfgl3scut], bins=bins, label='All', log=True)
    axis.hist(gdat.fgl3scut[intersect1d(indxfgl3scut, gdat.indxfgl3rofi)], bins=bins, label='ROI', log=True)
    axis.set_xlabel('3FGL spectral cutoff')
    axis.legend()
    axis.set_ylim([0.1, None])
    plt.savefig(gdat.pathplot + 'fgl3scut.pdf')
    plt.close(figr)
    
    figr, axis = plt.subplots()
    indxfgl3scur = where(isfinite(gdat.fgl3scur))[0]
    bins = linspace(amin(gdat.fgl3scur[indxfgl3scur]), amax(gdat.fgl3scur[indxfgl3scur]), numbbins)
    axis.hist(gdat.fgl3scur[indxfgl3scur], bins=bins, label='All', log=True)
    axis.hist(gdat.fgl3scur[intersect1d(indxfgl3scur, gdat.indxfgl3rofi)], bins=bins, label='ROI', log=True)
    axis.set_xlabel('3FGL spectral curvature')
    axis.legend()
    axis.set_ylim([0.1, None])
    plt.savefig(gdat.pathplot + 'fgl3scur.pdf')
    plt.close(figr)
    
    figr, axis = plt.subplots()
    indxfgl3sind = where(isfinite(gdat.fgl3sind))[0]
    bins = linspace(amin(gdat.fgl3sind[indxfgl3sind]), amax(gdat.fgl3sind[indxfgl3sind]), numbbins)
    axis.hist(gdat.fgl3sind[indxfgl3sind], bins=bins, label='All', log=True)
    axis.hist(gdat.fgl3sind[intersect1d(indxfgl3sind, gdat.indxfgl3rofi)], bins=bins, label='ROI', log=True)
    axis.set_xlabel('3FGL spectral index')
    axis.legend()
    axis.set_ylim([0.1, None])
    plt.savefig(gdat.pathplot + 'fgl3sind.pdf')
    plt.close(figr)
    
    strgfgl3spectype = ['LogParabola', 'PLExpCutoff', 'PLSuperExpCutoff', 'PowerLaw']

def make_anim():

    listname = ['errrpnts0A', 'datacnts0A', 'resicnts0A', 'modlcnts0A', 'histspec', 'scatspec', 'psfnprof', 'compfrac0', 'compfracspec', 'scatpixl']
    
    for name in listname:
    
        strg = '%s*0.pdf' % name
        listfile = fnmatch.filter(os.listdir(gdat.pathplot), strg)[int(numbburn/numbswepplot):]
        
        print fnmatch.filter(os.listdir(gdat.pathplot), strg)
        print listfile

        nfile = len(listfile)
        jfile = choice(arange(nfile), replace=False, size=nfile)

        cmnd = 'convert -delay 20 '
        for k in range(nfile):
            cmnd += '%s ' % listfile[jfile[k]]
        cmnd += ' %s.gif' % name
        os.system(cmnd)

        
def plot_histcnts(gdat, l, gdatmodi=None):

    figr, axgr = plt.subplots(gdat.numbevtt, gdat.numbener, figsize=(7 * gdat.numbener, 7 * gdat.numbevtt))
    if gdat.numbevtt == 1:
        axgr = [axgr]
    for m, axrw in enumerate(axgr):
        if gdat.numbener == 1:
            axrw = [axrw]
        for i, axis in enumerate(axrw):
            if gdat.trueinfo:
                truehist = axis.hist(gdat.truecnts[l][i, :, m], gdat.binscnts[i, :], alpha=0.5, color='g', log=True, label=gdat.truelabl)
                if gdat.datatype == 'mock':
                    if gdat.exprtype == 'ferm':
                        axis.hist(gdat.fgl3cnts[i, gdat.indxfgl3rofi, m], gdat.binscnts[i, :], alpha=0.1, color='red', log=True, label='3FGL')
            axis.hist(gdatmodi.thiscnts[l][i, :, m], gdat.binscnts[i, :], alpha=0.5, color='b', log=True, label='Sample')
            if m == gdat.numbevtt - 1:
                axis.set_xlabel(r'$k$')
            axis.set_xscale('log')
            if gdat.trueinfo:
                axis.set_ylim([0.1, 1e3])
            if m == 0:
                axis.set_title(gdat.binsenerstrg[i])
            if i == 0 and gdat.exprtype == 'ferm':
                axis.set_ylabel(gdat.evttstrg[m])
            if m == gdat.numbevtt / 2 and i == gdat.numbener / 2:
                axis.legend()
        
    figr.subplots_adjust(wspace=0.3)
    plt.savefig(gdat.pathplot + 'histcnts%d_' % l + gdat.rtag + '_%09d.pdf' % gdat.cntrswep)
    plt.close(figr)
    

def plot_diagfram(gdat, gdatmodi, indxenerplot, indxevttplot):

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'diagthis')
    axis, cbar = retr_imag(gdat, axis, gdat.thispntsfluxmodi, indxenerplot, indxevttplot)
    plt.savefig(path)
    plt.close(figr)

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'diagnext')
    axis, cbar = retr_imag(gdat, axis, gdat.nextpntsfluxmodi, indxenerplot, indxevttplot)
    plt.savefig(path)
    plt.close(figr)

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'diagdiff')
    axis, cbar = retr_imag(gdat, axis, gdat.diffpntsfluxmodi, indxenerplot, indxevttplot)
    plt.savefig(path)
    plt.close(figr)


def plot_nextstat(gdat, gdatmodi, indxenerplot, indxevttplot):

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'nextstat')
    axis, cbar = retr_imag(gdat, axis, gdat.datacnts, indxenerplot, indxevttplot)
   
    mrkrsize = retr_mrkrsize(gdat, fabs(gdatmodi.modispec), indxenerplot) * 10
    for k in range(gdat.numbmodipnts):
        if gdatmodi.modispec[indxenerplot, k] > 0:
            colr = 'yellow'
        else:
            colr = 'red'
        if gdat.exprtype == 'ferm':
            xaxi = gdatmodi.modilgal[k]
            yaxi = gdatmodi.modibgal[k]
        else:
            xaxi = gdatmodi.modilgal[k] * 3600.
            yaxi = gdatmodi.modibgal[k] * 3600.
        axis.scatter(xaxi, yaxi, s=mrkrsize, alpha=gdat.mrkralph, marker='o', linewidth=2, color=colr)
        text = r'%s, lnL = %.3g' % (gdat.strgprop[gdat.thisindxprop], gdat.deltllik)
        if gdat.thisindxprop == gdat.indxpropsplt or gdat.thisindxprop == gdat.indxpropmerg:
            text += ', lnF = %.3g, lnJ = %.3g, lnC = %.3g, %d' % (gdat.laccfrac, gdat.thisjcbnfact, gdat.thiscombfact, gdat.listaccp[j])
        axis.text(0.6, 1.1, text, va='center', ha='center', transform=axis.transAxes, fontsize=18)

    plt.savefig(path)
    plt.close(figr)


def plot_datacnts(gdat, indxpoplplot, gdatmodi, indxenerplot, indxevttplot):

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'datacnts')
    axis, cbar = retr_imag(gdat, axis, gdat.datacnts, indxenerplot, indxevttplot, satuuppr=gdat.datacntssatu)
    supr_fram(gdat, gdatmodi, axis, indxenerplot, indxpoplplot)
    plt.savefig(path)
    plt.close(figr)
    
    
def plot_modlcnts(gdat, indxpoplplot, gdatmodi, indxenerplot, indxevttplot):

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'modlcnts')
    axis, cbar = retr_imag(gdat, axis, gdat.thismodlcnts, indxenerplot, indxevttplot, satuuppr=gdat.datacntssatu)
    supr_fram(gdat, gdatmodi, axis, indxenerplot, indxpoplplot)
    plt.savefig(path)
    plt.close(figr)
    
    
def plot_resicnts(gdat, indxpoplplot, gdatmodi, indxenerplot, indxevttplot):

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'resicnts')
    axis, cbar = retr_imag(gdat, axis, gdat.thisresicnts, indxenerplot, indxevttplot, \
        satulowr=-gdat.resicntssatu, satuuppr=gdat.resicntssatu, cmap='RdBu')
    supr_fram(gdat, gdatmodi, axis, indxenerplot, indxpoplplot)
    plt.savefig(path)
    plt.close(figr)
    
    
def plot_errrpnts(gdat, gdatmodi, indxenerplot, indxevttplot):

    # temp
    #satulowr = -1.
    #satuuppr = 1.
    satulowr = None
    satuuppr = None

    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'errrpnts')
    axis, cbar = retr_imag(gdat, axis, gdatmodi.thiserrrpnts, indxenerplot, indxevttplot, satulowr=satulowr, satuuppr=satuuppr, cmap='RdBu', logt=True, mean=True)
    plt.savefig(path)
    plt.close(figr)
    
    
def plot_catlfram(gdat, gdatmodi, indxpoplplot, indxenerplot, indxevttplot):
    
    figr, axis, path = init_fram(gdat, indxevttplot, indxenerplot, 'catlfram')

    if gdat.trueinfo:
        for l in gdat.indxpopl:
            numbpnts = int(gdat.truenumbpnts[l])
            for a in range(numbpnts):
                if indxevttplot == None:
                    cnts = sum(gdat.truecnts[l][indxenerplot, a, :])
                    sigm = sqrt(sum(gdat.truesigm[l][indxenerplot, a, :]**2))
                else:
                    cnts = gdat.truecnts[l][indxenerplot, a, indxevttplot]
                    sigm = gdat.truesigm[l][indxenerplot, a, indxevttplot]
                axis.text(gdat.truelgal[l][a] + 0.7, gdat.truelgal[l][a] - 0.7, '%d/%.2f' % (cnts, sigm), color='g', fontsize=13)

    for l in gdat.indxpopl:
        numbpnts = int(gdatmodi.thissampvarb[gdat.indxsampnumbpnts[l]])
        for a in range(numbpnts):
            if indxevttplot == None:
                cnts = sum(gdatmodi.thiscnts[l][indxenerplot, a, :])
            else:
                cnts = gdatmodi.thiscnts[l][indxenerplot, a, indxevttplot]
            axis.text(gdatmodi.thissampvarb[gdat.thisindxsamplgal[l][a]] - 0.5, gdatmodi.thissampvarb[gdat.thisindxsampbgal[l][a]] + 0.3, '%d' % cnts, color='b', fontsize=13)
    
    if indxevttplot == None:
        plt.figtext(0.76, 0.92, '$C_{back} = %d$' % mean(gdat.thisbackcntsmean[indxenerplot, :]), fontsize=18)
    else:
        plt.figtext(0.76, 0.92, '$C_{back} = %d$' % gdat.thisbackcntsmean[indxenerplot, indxevttplot], fontsize=18)
        
    plt.savefig(path)
    plt.close(figr)

    
def plot_pntsdiff():

    tempindxpntsfull = []
    tempnumbpnts = 10
    tempindxpntsfull.append(range(tempnumbpnts))
    tempsamp = rand(gdat.numbpara)
    tempsamp[gdat.indxsampnumbpnts] = array([tempnumbpnts])
    tempsamp[gdat.indxsampfdfnnorm] = cdfn_logt(array([tempnumbpnts]), minmfdfnnorm, factfdfnnorm)
    tempsamp[gdat.indxsampfdfnslop] = cdfn_atan(array([1.5]), minmfdfnslop, factfdfnslop)
    tempsamp[gdat.indxsamppsfipara] = 0.5
    for c in gdat.indxback:
        tempsamp[gdat.indxsampnormback[c, 0]] = cdfn_logt(array([1.]), minmnormback[c], factnormback[c])
    
    tempsampvarb = retr_sampvarb(gdat, gdat.thisindxpntsfull, drmcsamp[:, 0])
    temppntsflux, temppntscnts, tempmodlflux, tempmodlcnts = retr_maps(gdat, tempindxpntsfull, tempsampvarb)

    pntscnts = tempcnts[0, :, 0] * gdat.expo[0, :, 0] * gdat.apix * gdat.diffener[0]
    isotcnts = isotflux[0, :, 0] * gdat.expo[0, :, 0] * gdat.apix * gdat.diffener[0]
    
    totlcnts0 = isotcnts
    totlcnts1 = pntscnts / 1e6 + isotcnts
    
    nrept = 100
    totlcntsheal0 = zeros((nrept, gdat.numbpixlheal))
    totlcntsheal1 = zeros((nrept, gdat.numbpixlheal))
    for k in range(nrept):
        for n in range(gdat.indxpixlrofi.size):
            totlcntsheal0[k, gdat.indxpixlrofi[n]] = poisson(totlcnts0[n])
            totlcntsheal1[k, gdat.indxpixlrofi[n]] = poisson(totlcnts1[n])
          
    maxmcnts = max(amax(totlcntsheal0), amax(totlcntsheal1))
    gdat.binscnts = linspace(0., maxmcnts, maxmcnts + 2)
    diffcnts = gdat.binscnts[1:] - gdat.binscnts[:-1]
    meancnts = (gdat.binscnts[1:] + gdat.binscnts[:-1]) / 2.
    
    hist0 = empty((nrept, maxmcnts + 1))
    hist1 = empty((nrept, maxmcnts + 1))
    for k in range(nrept):
        hist0[k, :] = histogram(totlcntsheal0[k, gdat.indxpixlrofi], gdat.binscnts)[0].astype(float)
        hist0[k, :] *= 1. / sum(hist0[k, :]) / diffcnts
        hist1[k, :] = histogram(totlcntsheal1[k, gdat.indxpixlrofi], gdat.binscnts)[0].astype(float)
        hist1[k, :] *= 1. / sum(hist1[k, :]) / diffcnts
        
    
    totlcntscart0 = tdpy.util.retr_cart(totlcntsheal0[0, :], minmlgal=gdat.minmlgal, maxmlgal=gdat.maxmlgal, minmbgal=gdat.minmbgal, maxmbgal=gdat.maxmbgal)
    totlcntscart1 = tdpy.util.retr_cart(totlcntsheal1[0, :], minmlgal=gdat.minmlgal, maxmlgal=gdat.maxmlgal, minmbgal=gdat.minmbgal, maxmbgal=gdat.maxmbgal)
    
    fig = plt.figure(figsize=(12, 12))
    axis = figr.add_subplot(221)
    imag = axis.imshow(totlcntscart0, origin='lower', cmap='Reds', extent=gdat.exttrofi)
    plt.colorbar(imag, ax=axis, fraction=0.05)
    
    axis.set_xlabel(gdat.longlabl)
    axis.set_ylabel(gdat.latilabl)
    if gdat.exprtype == 'ferm':
        axis.set_xlim([gdat.maxmlgal, gdat.minmlgal])
        axis.set_ylim([gdat.minmbgal, gdat.maxmbgal])
    else:
        axis.set_xlim(array([gdat.maxmlgal, gdat.minmlgal]) * 3600.)
        axis.set_ylim(array([gdat.minmbgal, gdat.maxmbgal]) * 3600.)
    
    axis.set_title('Isotropic')
    
    axis = figr.add_subplot(222)
    imag = axis.imshow(totlcntscart1, origin='lower', cmap='Reds', extent=gdat.exttrofi)
    plt.colorbar(imag, ax=axis, fraction=0.05)

    axis.set_xlabel(r'$x$ [$^\circ$]')
    axis.set_xlim([gdat.maxmlgal, gdat.minmlgal])
    axis.set_ylim([gdat.minmbgal, gdat.maxmbgal])
    axis.set_title('Isotropic + Unresolved PS')
    
    axis.scatter(tempsampvarb[trueindxsamplgal], tempsampvarb[trueindxsampbgal], s=50, alpha=0.8, marker='x', color='g', linewidth=2)
    
    axis = figr.add_subplot(212)

    tdpy.mcmc.plot_braz(ax, meancnts, hist0,  lcol='lightgreen', alpha=0.3, dcol='green', mcol='darkgreen', labl='Isotropic')
    tdpy.mcmc.plot_braz(ax, meancnts, hist1, lcol='lightblue', alpha=0.3, dcol='blue', mcol='darkblue', labl='Isotropic + Unresolved PS')

    axis.set_title('Count PDF')
    axis.set_xlabel('$k$')
    axis.set_ylabel('d$P$/d$k$')
    axis.set_yscale('log')
    axis.legend()

    plt.savefig(gdat.pathplot + 'pntsdiff.pdf')
    plt.close(figr)
    

def pair_catl(gdat, thisindxpopl, modllgal, modlbgal, modlspec):

    indxmodl = zeros_like(gdat.truelgal[thisindxpopl], dtype=int) - 1
    dir2 = array([modllgal, modlbgal])
    for k in range(gdat.truelgal[thisindxpopl].size):
        dir1 = array([gdat.truelgal[thisindxpopl][k], gdat.truebgal[thisindxpopl][k]])
        dist = angdist(dir1, dir2, lonlat=True)
        indxdist = argmin(dist) 
        if dist[indxdist] < deg2rad(0.5):
            indxmodl[k] = indxdist
    indxtruepntsmiss = where(indxmodl == -1)[0]
    
    return indxmodl, indxtruepntsmiss
     

