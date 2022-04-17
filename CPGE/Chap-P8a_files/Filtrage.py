# -*- coding: utf-8 -*-
"""
Published: january 2020

@author: Tuch from D.Jurine
"""
#! /usr/bin/env python
import os
os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin'
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import rc
from scipy import signal
from scipy import fftpack
from random import gauss

##################################
# Utilisation de Latex
# Annoter sauf pour sortie definitive car ca ralentit
##################################
plt.rcParams['text.usetex']=True
#matplotlib.rc('text', usetex=True)
#rc('text', usetex=True)
plt.rcParams['text.latex.unicode']=True
plt.rcParams['font.family'] = 'serif'   # par défaut la police sera Computer modern
##################################
# Cosmétique
##################################
plt.rcParams['font.serif'] = 'Computer Modern Serif'   # par défaut la police sera Computer modern
plt.rcParams['mathtext.fontset'] = 'cm' # police Computer modern pour les expressions mathématiques
plt.rcParams['axes.labelsize'] = 1.2*plt.rcParams['font.size']
plt.rcParams['axes.titlesize'] = 1.2*plt.rcParams['font.size']
plt.rcParams['legend.fontsize'] = plt.rcParams['font.size']
plt.rcParams['xtick.labelsize'] = plt.rcParams['font.size']
plt.rcParams['ytick.labelsize'] = plt.rcParams['font.size']
plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.loc'] = 'upper right'
plt.rcParams['figure.figsize'] = (7, 9)
plt.rcParams['font.size'] = 10


####################################    
# Variables globales utiles
#################################### 
j=complex(0,1)
pi=np.pi

####################################    
# Bibliothèque de signaux
#################################### 
def creneau(t):
    #signal créneau de frequence f
    return np.sign(np.sin(2*pi*f*t))

def triangle(t):
    # signal triangulaire de frequence f
    T=1/f
    triangle=1+40/T*(np.abs(t-T*np.floor(t/T)-T/2)-T/4)
    return triangle

def sinus(t):
    return np.sin(2*pi*f*t)

def sinus1(t):
    somme=2*np.sin(2*pi*f1*t)+np.sin(2*pi*f2*t)
    return somme
    
def bruitBlanc(t):
    x = np.zeros(len(t))
    for i in range(len(t)):
        x[i] = gauss(0,0.5)
    return x

def sinusBruit(t):
    x = np.zeros(len(t))
    for i in range(len(t)):
        x[i] = np.sin(2*pi*f*t[i])+gauss(0,0.5)
    return x

def creneauBruit(t):
    x = np.zeros(len(t))
    for i in range(len(t)):
        x[i] = np.sign(np.sin(2*pi*f*t[i]))+gauss(0,0.5)
    return x

def triangleBruit(t):
    T=1/f
    x = np.zeros(len(t))
    for i in range(len(t)):
        x[i] = 4/T*(np.abs(t[i]-T*np.floor(t[i]/T)-T/2)-T/4)+gauss(0,0.5)
    return x

####################################    
# bibliothèque de fonctions de transfert
####################################       
def Hsuiveur():
    return np.array([1.0]),np.array([1.0])

def H1passebas(fc):
    omega_c = 2.0*pi*fc
    # Coefficient du denominateur
    a = np.array( [1.0/(omega_c) , 1.0 ])
    # Coefficient du numerateur
    b=np.array([1.0])
    return b,a

def H1passehaut(fc):
    omega_c = 2.0*pi*fc
    # Coefficient du denominateur
    a = np.array( [1.0/(omega_c) , 1.0 ])
    # Coefficient du numerateur
    b=np.array([0.5/(omega_c),0.0])
    return b,a

def H2passebas(f0,Q):
    omega_0 = 2.0*pi*f0
    # Coefficient du denominateur
    a = np.array( [ 1.0/omega_0**2 , 1.0/(Q*omega_0) , 1.0 ])
    # Coefficient du numerateur
    b=np.array([1.0])
    return b,a

def H2passebande(f0,Q):
    omega_0 = 2.0*pi*f0
    # Coefficient du denominateur
    a = np.array( [ 1.0/omega_0**2 , 1.0/(Q*omega_0) , 1.0 ])
    # Coefficient du numerateur
    b= np.array( [ 0 , 1.0/(Q*omega_0) , 0 ])
    return b,a
    
def H2passehaut(f0,Q):
    omega_0 = 2.0*pi*f0
    # Coefficient du denominateur
    a = np.array( [ 1.0/omega_0**2 , 1.0/(Q*omega_0) , 1.0 ])
    # Coefficient du numerateur
    b= np.array( [  1.0/omega_0**2 , 0, 0])
    return b,a

def H2rejecteur(f0,Q):
    omega_0 = 2.0*pi*f0
    # Coefficient du denominateur
    a = np.array( [ 1.0/omega_0**2 , 1.0/(Q*omega_0) , 1.0 ])
    # Coefficient du numerateur
    b= np.array( [ 1.0/omega_0**2 , 1.e-5, 1.0 ])
    return b,a

####################################    
# Procedure de filtrage
####################################   
def filtrage(x,H,f):
    ####################################    
    # Calcul entrée
    ####################################    
    t = np.linspace(0 , 10.0 / f , 16384)
    entree = x(t)
    fft_entree = fftpack.fft(entree)
    frequences = fftpack.fftfreq( len(entree) , t[1]-t[0] )
    ####################################    
    # Calcul sortie
    ####################################    
    b,a=H
    [ fs, H ] = signal.freqs(b,a,2*pi*frequences)
    fft_sortie = H * fft_entree
    zero=0*fft_entree
    sortie = fftpack.ifft(fft_sortie)
    ####################################    
    # Preparation Bode
    ####################################    
    frequence=np.logspace(np.log10(f)-3,np.log10(f)+3,1000)
    [w,qH]=signal.freqs(b,a,2*pi*frequence)
    GdB=20.0*np.log10(np.absolute(qH))

    ####################################    
    # Tracé entrée
    ####################################    
    plt.subplot(3,2,1)
    plt.plot(t , entree,'k-',linewidth=2)
    plt.grid(True, which='major', color='black', linestyle='-', linewidth=0.8)   
    plt.ylabel(u'$e$ (V)')
    plt.xlabel(u'$t$ (s)')
    plt.axis([min(t),max(t),1.2*min(entree),1.2*max(entree)])
    #plt.axis([min(t),max(t),-2.1,2.1])

    plt.subplot(3,2,2)
    plt.semilogx()
    plt.vlines(frequences ,zero,np.absolute(fft_entree)/(len(entree)),'black',linewidth=3)
    plt.legend([u'$e$'])
    plt.grid(True, which='major',color='black', linestyle='-',linewidth=0.8)
    plt.grid(True, which='minor',color='black', linestyle='-',linewidth=0.4)
    plt.axis([f/1000, 1000 * f,0,1.2*max(np.absolute(fft_entree)/(len(entree)))])

##    plt.show()
    
    ####################################    
    # Tracé Bode
    ####################################    
    plt.subplot(3,2,4)
    plt.semilogx()
    plt.plot(frequence,GdB,'k-',linewidth=2)
    plt.axis([f/1000, 1000 * f,min(GdB)-10,max(GdB)+10])
    plt.grid(True, which='major',color='black', linestyle='-',linewidth=0.8)
    plt.grid(True, which='minor',color='black', linestyle='-',linewidth=0.4)
    plt.ylabel(u'$G_{dB}$')

    ####################################    
    # Tracé sortie
    ####################################    
    plt.subplot(3,2,5)
    plt.plot(t , sortie,'r-',linewidth=2)
    plt.axis([min(t),max(t),1.2*min(sortie),1.2*max(sortie)])
    #plt.axis([min(t),max(t),-2.1,2.1])    
    plt.grid(True, which='major', color='black', linestyle='-', linewidth=0.8)
    plt.ylabel(u'$s$ (V)')
    plt.xlabel(u'$t$ (s)')

    plt.subplot(3,2,6)
    plt.semilogx()
    plt.vlines(frequences ,zero,np.absolute(fft_sortie)/(len(entree)),'r',linewidth=3)
    plt.legend([u'$s$'])
    plt.axis([f/1000,1000 * f,0,1.2*max(np.absolute(fft_sortie)/(len(entree)))])
    plt.grid(True, which='major',color='black', linestyle='-',linewidth=0.8)
    plt.grid(True, which='minor',color='black', linestyle='-',linewidth=0.4)
    plt.xlabel(u'$f$ (Hz) (échelle log)')


    plt.show()
    plt.savefig('TestTuch.pdf')

    
####################################    
# Programme principal
#################################### 

plt.close()

####################################    
# Reglages signaux et Bode
# f0, Q pour fonction de transfert
# f pour signal
#################################### 

f0=900.
f=10.
f1=5.
f2=30.
Q=0.71

filtrage(sinus1,H1passehaut(f0),f)

# à annoter si on ne veut pas sauver car ça ralentit
plt.savefig('TestTuch.eps')

# pour savoir si c'est fini
print('OK')
