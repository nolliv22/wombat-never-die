"""
Mouvement dans un champ de pesanteur uniforme avec frottement fluide
proportionnel à la vitesse : résolution de
d^2r/dt^2 + 1/tau*dr/dt = g
en décomposant en un système de quatre équations du premier ordre
dx/dt = vx
dz/dt = vz
dvx/dt = -vx/tau
dvz/dt = -vz/tau + g
"""


from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


plt.close()

# Paramètres
tau = 1        # Temps caractéristique
g = 9.8        # Champ de pesanteur
a = 1/4        # Coefficient de frottements fluides

def deriv(syst, t):
    x = syst[0]
    z = syst[1]
    vx = syst[2]
    vz = syst[3]
    dxdt = vx
    dzdt = vz
    dvxdt = -vx/tau
    dvzdt = -vz/tau - g
    return [dxdt,dzdt,dvxdt,dvzdt]

def deriv1(syst, t):
    x1 = syst[0]
    z1 = syst[1]
    vx1 = syst[2]
    vz1 = syst[3]
    dx1dt = vx1
    dz1dt = vz1
    dvx1dt = 0
    dvz1dt = - g
    return [dx1dt,dz1dt,dvx1dt,dvz1dt]

def deriv2(syst, t):
    x2 = syst[0]
    z2 = syst[1]
    vx2 = syst[2]
    vz2 = syst[3]
    dx2dt = vx2
    dz2dt = vz2
    dvx2dt = - a*vx2*np.sqrt(vx2**2+vz2**2)
    dvz2dt = - a*vz2*np.sqrt(vx2**2+vz2**2) - g
    return [dx2dt,dz2dt,dvx2dt,dvz2dt]

# Paramètres d'intégration
t0 = 0                          # Instant de début d'intégration
tf = 50                         # Instant de fin d'intégration
nbPas = 1000                    # Nombre de pas d'intégration
t = np.linspace(t0,tf,nbPas)    # Liste des instants

# Conditions initiales et résolution
x0 = 0
z0 = 0
vx0 = 3
vz0 = 3
ci = np.array([x0,z0,vx0,vz0])
sols = odeint(deriv,ci,t)       # Résolution numérique
sols1 = odeint(deriv1,ci,t)       # Résolution numérique
sols2 = odeint(deriv2,ci,t)       # Résolution numérique

# Obtention des solutions
x = sols[:,0]
z = sols[:,1]
vx = sols[:,2]
vz = sols[:,3]
x1 = sols1[:,0]
z1 = sols1[:,1]
vx1 = sols1[:,2]
vz1 = sols1[:,3]
x2 = sols2[:,0]
z2 = sols2[:,1]
vx2 = sols2[:,2]
vz2 = sols2[:,3]

# Figure
taillePolice = 18
xf=x0+vx0*tau
vzf=-g*tau
fig=plt.figure()
taille = 0.99
fig.subplots_adjust(right=taille,left=1-taille,
                    top=taille,bottom=1-taille,
                    wspace=1.01-taille,hspace=1.01-taille)    # Taille du graphe tracé


# x(t)
fig1=plt.subplot(231)
plt.plot(t,x,t,x1,t,x2)
abstexteordxt = -0.5
ordtexteabsxt = -0.4                                   # Position du texte le long de l'axe des abcisses
plt.text(abstexteordxt,ordtexteabsxt,                  # Origine
         '$0$', fontsize=taillePolice)

# Abscisse x(t)
absxtmin = -1                                           # Limite à gauche
absxtmax = 5                                            # Limite à droite
plt.xlim(absxtmin,absxtmax)                             # Limites
plt.annotate('',(absxtmax,0),(absxtmin,0),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(absxtmax+abstexteordxt,ordtexteabsxt,      # Label
         '$t$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs

# Ordonnée x(t)
ordxtmin = -0.6                                         # Limite en bas
ordxtmax = 4                                            # Limite en haut
plt.ylim(ordxtmin,ordxtmax)                             # Limites
plt.annotate('',(0,ordxtmax),(0,ordxtmin),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordxt,ordxtmax+ordtexteabsxt+0.1,      # Label
         '$x$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs

# Asymptote x(t)
plt.plot([0,absxtmax],[xf,xf],'k--')
plt.text(abstexteordxt-0.2,xf-0.1,
         '$x_\mathrm{f}$', fontsize=taillePolice)

# Tangente à l'origine x(t)
plt.plot([0,tau],[0,xf],'k--')
plt.plot([tau,tau],[0,xf],'k--')
plt.text(tau-0.2,ordtexteabsxt+0.05,r'$\tau$', fontsize=taillePolice)

# vx(t)
fig1=plt.subplot(232)
plt.plot(t,vx,t,vx1,t,vx2)
abstexteordvxt = -0.5                                   # Position du texte le long de l'axe des ordonnées
ordtexteabsvxt = -0.4                                   # Position du texte le long de l'axe des abcisses
plt.text(abstexteordvxt,ordtexteabsvxt,                 # Origine
         '$0$', fontsize=taillePolice)

# Abscisse vx(t)
absvxtmin = -1                                          # Limite à gauche
absvxtmax = 5                                           # Limite à droite
plt.xlim(absvxtmin,absvxtmax)                           # Limites
plt.annotate('',(absvxtmax,0),(absvxtmin,0),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(absvxtmax+abstexteordvxt,ordtexteabsvxt,       # Label
         '$t$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs

# Ordonnée vx(t)
ordvxtmin = -0.6                                        # Limite en bas
ordvxtmax = 4                                           # Limite en haut
plt.ylim(ordvxtmin,ordvxtmax)                           # Limites
plt.annotate('',(0,ordvxtmax),(0,ordvxtmin),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordvxt,ordvxtmax+ordtexteabsvxt,       # Label
         '$\dot{x}$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs
plt.text(abstexteordvxt-0.2,vx0-0.1,                    # Vitesse initiale
         '$\dot{x}_0$',fontsize=taillePolice)
         
# Tangente à l'origine vx(t)
plt.plot([0,tau],[vx0,0],'k--')
plt.text(tau-0.1,ordtexteabsvxt+0.05,
         r'$\tau$', fontsize=taillePolice)

# vx(x)
fig1=plt.subplot(233)
plt.plot(x,vx,x1,vx1,x2,vx2)
abstexteordvxx = -0.5                                   # Position du texte le long de l'axe des ordonnées
ordtexteabsvxx = -0.4                                   # Position du texte le long de l'axe des abcisses
plt.text(abstexteordvxx,ordtexteabsvxx,                 # Origine
         '$0$', fontsize=taillePolice)

# Abscisse vx(x)
absvxxmin = -1                                          # Limite à gauche
absvxxmax = 5                                           # Limite à droite
plt.xlim(absvxxmin,absvxxmax)                           # Limites
plt.annotate('',(absvxxmax,0),(absvxxmin,0),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(absvxxmax+abstexteordvxx,ordtexteabsvxx,       # Label
         '$x$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs
plt.text(xf-0.2,ordtexteabsvxx,                     # Position finale
         '$x_\mathrm{f}$',fontsize=taillePolice)
         
# Ordonnée vx(x)
ordvxxmin = -0.6                                        # Limite en bas
ordvxxmax = 4                                           # Limite en haut
plt.ylim(ordvxxmin,ordvxxmax)                           # Limites
plt.annotate('',(0,ordvxxmax),(0,ordvxxmin),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordvxx,ordvxxmax+ordtexteabsvxx,       # Label
         '$\dot{x}$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs
plt.text(abstexteordvxx-0.2,vx0-0.1,                    # Vitesse initiale
         '$\dot{x}_0$',fontsize=taillePolice)

# Orientation trajectoire de phase vx(x)
plt.annotate('',(xf/2,vx0/2),(x0,vx0),
             arrowprops=dict(arrowstyle='->',
                             color='b',
                             mutation_scale=1.4*taillePolice))
         
# z(t)
fig1=plt.subplot(234)
plt.plot(t,z,t,z1,t,z2)
abstexteordzt = -0.5
ordtexteabszt = -1.0                                   # Position du texte le long de l'axe des abcisses
plt.text(abstexteordzt,ordtexteabszt,                  # Origine
         '$0$', fontsize=taillePolice)

# Abscisse z(t)
absztmin = -1                                           # Limite à gauche
absztmax = 5                                            # Limite à droite
plt.xlim(absztmin,absztmax)                             # Limites
plt.annotate('',(absztmax,0),(absztmin,0),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(absztmax+abstexteordzt,ordtexteabszt,          # Label
         '$t$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs

# Ordonnée z(t)
ordztmin = -10                                          # Limite en bas
ordztmax = 2                                            # Limite en haut
plt.ylim(ordztmin,ordztmax)                             # Limites
plt.annotate('',(0,ordztmax),(0,ordztmin),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordzt,ordztmax+ordtexteabszt,          # Label
         '$z$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs

# vz(t)
fig1=plt.subplot(235)
plt.plot(t,vz,t,vz1,t,vz2)
abstexteordvzt = -0.5                                   # Position du texte le long de l'axe des ordonnées
ordtexteabsvzt = -1.4                                   # Position du texte le long de l'axe des abcisses
plt.text(abstexteordvzt,ordtexteabsvzt,                 # Origine
         '$0$', fontsize=taillePolice)

# Abscisse vz(t)
absvztmin = -1                                          # Limite à gauche
absvztmax = 5                                           # Limite à droite
plt.xlim(absvztmin,absvztmax)                           # Limites
plt.annotate('',(absvztmax,0),(absvztmin,0),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(absvztmax+abstexteordvzt,ordtexteabsvzt,       # Label
         '$t$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs

# Ordonnée vz(t)
ordvztmin = -11                                         # Limite en bas
ordvztmax = 6                                           # Limite en haut
plt.ylim(ordvztmin,ordvztmax)                           # Limites
plt.annotate('',(0,ordvztmax),(0,ordvztmin),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordvzt,ordvztmax+ordtexteabsvzt,       # Label
         '$\dot{z}$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs
plt.text(abstexteordvzt-0.1,vx0-0.1,                    # Vitesse initiale
         '$\dot{z}_0$',fontsize=taillePolice)
         
# Asymptote vz(t)
plt.plot([0,absvztmax],[vzf,vzf],'k--')
plt.text(abstexteordxt-0.05,vzf-0.2,
         '$\dot{z}_\mathrm{f}$', fontsize=taillePolice)

# Tangente à l'origine vz(t)
plt.plot([0,tau],[vz0,vzf],'k--')
plt.plot([tau,tau],[0,vzf],'k--')
plt.text(tau-0.1,0.5,r'$\tau$', fontsize=taillePolice)

# vz(z)
fig1=plt.subplot(236)
plt.plot(z,vz,z1,vz1,z2,vz2)
abstexteordvzz = -0.8                                     # Position du texte le long de l'axe des ordonnées
ordtexteabsvzz = -1.4                                   # Position du texte le long de l'axe des abcisses
plt.text(abstexteordvzz,ordtexteabsvzz,                 # Origine
         '$0$', fontsize=taillePolice)

# Abscisse vz(z)
absvzzmin = -10                                         # Limite à gauche
absvzzmax = 2                                           # Limite à droite
plt.xlim(absvzzmin,absvzzmax)                           # Limites
plt.annotate('',(absvzzmax,0),(absvzzmin,0),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(absvzzmax+abstexteordvzz,ordtexteabsvzz,       # Label
         '$z$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs
         
# Ordonnée vz(z)
ordvzzmin = -11                                         # Limite en bas
ordvzzmax = 6                                           # Limite en haut
plt.ylim(ordvzzmin,ordvzzmax)                           # Limites
plt.annotate('',(0,ordvzzmax),(0,ordvzzmin),            # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordvzz-0.1,ordvzzmax+ordtexteabsvzz,       # Label
         '$\dot{z}$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs
plt.text(abstexteordvzz-0.4,vx0-0.1,                    # Vitesse initiale
         '$\dot{z}_0$',fontsize=taillePolice)

# Orientation trajectoire de phase vz(z)
tfleche2=30*tau
plt.annotate('',(z[tfleche2+1],vz[tfleche2+1]),
             (z[tfleche2],vz[tfleche2]),
             arrowprops=dict(arrowstyle='->',
                             color='b',
                             mutation_scale=1.4*taillePolice))             
             
# Asymptote vz(z)
plt.plot([absvzzmin,0],[vzf,vzf],'k--')
plt.text(0.1,vzf-0.3,
         '$\dot{z}_\mathrm{f}$', fontsize=taillePolice)             

# Trajectoire z(x)
fig2=plt.figure()
fig2.subplots_adjust(right=taille,left=1-taille,      # Taille du graphe tracé
                    top=taille,bottom=1-taille,
                    wspace=1-taille,hspace=1-taille)    
fig3=plt.subplot(231)
plt.plot(x,z,x1,z1,x2,z2)
abstexteordzx = -0.4
ordtexteabszx = -0.9                                    # Position du texte le long de l'axe des abcisses
plt.text(abstexteordzx+0.1,ordtexteabszx,                   # Origine
         '$0$', fontsize=taillePolice)

# Abscisse z(x)
abszxmin = -0.5                                         # Limite à gauche
abszxmax = xf+1                                       # Limite à droite
plt.xlim(abszxmin,abszxmax)                             # Limites
plt.annotate('',(abszxmax,0),(abszxmin,0),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abszxmax+abstexteordzx,ordtexteabszx,          # Label
         '$x$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs

# Ordonnée z(x)
ordzxmin = -10                                          # Limite en bas
ordzxmax = 2                                            # Limite en haut
plt.ylim(ordzxmin,ordzxmax)                             # Limites
plt.annotate('',(0,ordzxmax),(0,ordzxmin),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordzx,ordzxmax+ordtexteabszx,          # Label
         '$z$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs

# Asymptote vertcale x=xf
plt.plot([xf,xf],[ordzxmin,0],'k--')
plt.text(xf-0.2,0.4,'$x_\mathrm{f}$', fontsize=taillePolice)

# Orientation trajectoire de phase vz(z)
tfleche3=20*tau
plt.annotate('',(x[tfleche3+1],z[tfleche3+1]),
             (x[tfleche3],z[tfleche3]),
             arrowprops=dict(arrowstyle='->',
                             color='b',
                             mutation_scale=1.4*taillePolice))
plt.annotate('',(x1[tfleche3+1],z1[tfleche3+1]),
             (x1[tfleche3],z1[tfleche3]),
             arrowprops=dict(arrowstyle='->',
                             color='g',
                             mutation_scale=1.4*taillePolice))
plt.annotate('',(x2[tfleche3+1],z2[tfleche3+1]),
             (x2[tfleche3],z2[tfleche3]),
             arrowprops=dict(arrowstyle='->',
                             color='r',
                             mutation_scale=1.4*taillePolice))
             
#Affichage des graphiques
plt.show()
