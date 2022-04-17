"""
Mouvement d'un pendule simpe : résolution en décomposant en
un système de deux équations du premier ordre
dtheta/dt = w
dw/dt = - g/l*sin(theta)
"""


from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
g = 9.8         # Champ de pesanteur
l = 1           # Longueur

def deriv(syst, t):
    theta = syst[0]
    w = syst[1]
    dthetadt = w
    dwdt = - g/l*np.sin(theta)
    return [dthetadt,dwdt]

# Paramètres d'intégration
t0 = 0                          # Instant de début d'intégration
tf = 50                         # Instant de fin d'intégration
nbPas = 1000                    # Nombre de pas d'intégration
t = np.linspace(t0,tf,nbPas)    # Liste des instants

# Conditions initiales et résolution
theta0 = 2.5
w0 = 1
ci = np.array([theta0,w0])
sols = odeint(deriv,ci,t)       # Résolution numérique

# Obtention des solutions
theta = sols[:,0]
w = sols[:,1]

# Figure
tau = tf/3
thetamax = np.max(theta)
wmax = np.max(w)
facteur = 5                                             # Facteur de décalage du texte                                        
taillePolice = 18
fig=plt.figure()
taille = 0.99
fig.subplots_adjust(right=taille,
                    left=1-taille,
                    top=taille,
                    bottom=1-taille,
                    wspace=1.01-taille,
                    hspace=1.01-taille)                 # Taille du graphe tracé


# theta(t)
fig1=plt.subplot(231)
plt.plot(t,theta)
abstexteordthetat = -0.5
ordtexteabsthetat = -thetamax/facteur                   # Position du texte le long de l'axe des abcisses
plt.text(abstexteordthetat,ordtexteabsthetat,           # Origine
         '$0$', fontsize=taillePolice)

# Abscisse theta(t)
absthetatmin = -1                                       # Limite à gauche
absthetatmax = 5                                        # Limite à droite
plt.xlim(absthetatmin,absthetatmax)                     # Limites
plt.annotate('',(absthetatmax,0),(absthetatmin,0),      # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(absthetatmax+abstexteordthetat,                # Label
         ordtexteabsthetat,
         '$t$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs

# Ordonnée theta(t)
ordthetatmin = -1.2*thetamax                                # Limite en bas
ordthetatmax = 1.2*thetamax                                 # Limite en haut
plt.ylim(ordthetatmin,ordthetatmax)                     # Limites
plt.annotate('',(0,ordthetatmax),(0,ordthetatmin),      # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordthetat,                             # Label
         ordthetatmax+ordtexteabsthetat,
         r'$\theta$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs
plt.text(abstexteordthetat-0.2,                         # Position initiale
         theta0+ordtexteabsthetat+0.5,
         r'$\theta_0$',fontsize=taillePolice)
         
# w(t)
fig1=plt.subplot(232)
plt.plot(t,w)
abstexteordwt = -0.4                                    # Position du texte le long de l'axe des ordonnées
ordtexteabswt = -wmax/facteur                           # Position du texte le long de l'axe des abcisses
plt.text(abstexteordwt,ordtexteabswt,                   # Origine
         '$0$', fontsize=taillePolice)

# Abscisse w(t)
abswtmin = -1                                           # Limite à gauche
abswtmax = 5                                            # Limite à droite
plt.xlim(abswtmin,abswtmax)                             # Limites
plt.annotate('',(abswtmax,0),(abswtmin,0),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abswtmax+abstexteordwt,ordtexteabswt,          # Label
         '$t$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs

# Ordonnée w(t)
ordwtmin = -1.2*wmax                                        # Limite en bas
ordwtmax = 1.2*wmax                                         # Limite en haut
plt.ylim(ordwtmin,ordwtmax)                             # Limites
plt.annotate('',(0,ordwtmax),(0,ordwtmin),              # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordwt,ordwtmax+ordtexteabswt,          # Label
         r'$\dot{\theta}$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs
plt.text(abstexteordwt-0.2,w0-0.1,                      # Vitesse initiale
         r'$\dot{\theta}_0$',fontsize=taillePolice)
         
# w(theta)
fig1=plt.subplot(233)
plt.plot(theta,w)
abstexteordwtheta = -thetamax/facteur                   # Position du texte le long de l'axe des ordonnées
ordtexteabswtheta = -wmax/facteur                       # Position du texte le long de l'axe des abcisses
plt.text(abstexteordwtheta,ordtexteabswtheta,           # Origine
         '$0$', fontsize=taillePolice)

# Abscisse w(theta)
abswthetamin = -1.2*thetamax                                # Limite à gauche
abswthetamax = 1.2*thetamax                                 # Limite à droite
plt.xlim(abswthetamin,abswthetamax)                     # Limites
plt.annotate('',(abswthetamax,0),(abswthetamin,0),      # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abswthetamax+abstexteordwtheta,                # Label
         ordtexteabswtheta,
         r'$\theta$', fontsize=taillePolice)
plt.xticks([])                                          # Effacement des valeurs
         
# Ordonnée w(theta)
ordwthetamin = -1.2*wmax                                    # Limite en bas
ordwthetamax = 1.2*wmax                                     # Limite en haut
plt.ylim(ordwthetamin,ordwthetamax)                     # Limites
plt.annotate('',(0,ordwthetamax),(0,ordwthetamin),      # Axe
             arrowprops=dict(arrowstyle='->'))
plt.text(abstexteordwtheta,                             # Label
         ordwthetamax+ordtexteabswtheta,
         r'$\dot{\theta}$',fontsize=taillePolice)
plt.yticks([])                                          # Effacement des valeurs

# Orientation trajectoire de phase w(theta)
tfleche1=tau
plt.annotate('',(theta[tfleche1+1],w[tfleche1+1]),
             (theta[tfleche1],w[tfleche1]),
             arrowprops=dict(arrowstyle='->',
                             color='b',
                             mutation_scale=1.4*taillePolice))
             
#Affichage des graphiques
plt.show()
