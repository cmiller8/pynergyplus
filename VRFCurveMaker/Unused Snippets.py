__author__ = 'claytonmiller'

#pbestEIR = leastsq(residuals,p0,args=(npPowerRatio,npIWB,npODB))
#bestparamsCAPFT = pbestCAPFT[0]
#bestparamsEIR = pbestEIR[0]
#cov_x = pbestCAPFT[1]

#print bestparamsCAPFT
#print bestparamsEIR

#print p
#print(infodict['fvec'])



#bestparamsCAPFT = pbestCAPFT[0]
#bestparamsEIR = pbestEIR[0]
#cov_x = pbestCAPFT[1]
#guessfit = CAPFT(npIWB,npODB,p0)
#
#datafit = CAPFT(npIWB,npODB,bestparams)
#plot(datafit)
#title('Curve-fitting example')
#grid(True)
#show()


  #    # Calculate Chi-squared
#    chisq = sum(((y_data-func(x_data,*p))/y_sigma)**2)
#    print "\nEstimated parameters and uncertainties (with initial guesses)"
#    for i in range(len(p)) :
#        print ("   p[%d] = %10.5f +/- %10.5f      (%10.5f)"
#                   %(i,p[i],cov[i,i]**0.5*max(1,numpy.sqrt(chisq/dof)),
#                       p_guess[i]))
#
#    print "Chi-Squared/dof = %10.5f, CDF = %10.5f%%"\
#        %(chisq/dof, 100.*float(scipy.special.chdtrc(dof,chisq)))
#    if chisq > dof :
#        print "Because Chi-squared > dof, the parameter uncertainty"
#        print "      estimates have been scaled up by Chi-squared/dof."
except TypeError:
    print "**** BAD FIT ****"
    print "Parameters were: ",p
    # Calculate Chi-squared for current parameters
    chisq = sum(((y_data-func(x_data,*p))/y_sigma)**2)
    print "Chi-Squared/dof for these parameter values = %10.5f, CDF = %10.5f%%"\
        %(chisq/dof, 100.*float(scipy.special.chdtrc(dof,chisq)))
    print "Uncertainties not calculated."
    print
    print "Try a different initial guess for the fit parameters."
    print "Or if these parameters appear close to a good fit, try giving"
    print "    the fitting program more time by increasing the value of maxfev."
    chisq = None