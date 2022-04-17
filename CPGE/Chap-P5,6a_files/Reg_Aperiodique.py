"""
Oscillateur amorti : résolution de
d^2x/dt^2+omega0/Q*dx/dt+omega0^2*x=omega0^2*xe
en décomposant en un système de deux équations du premier ordre
dx/dt = v
dv/dt = -omega0/Q*v+omega0^2*(xe-x)
"""


from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Paramètres
omega0 = 1        # Pulsation propre
Q = 0.2             # Facteur de qualité
xe = 0.5          # Etat d'équilibre final

def deriv(syst, t):
    x = syst[0]                             # Variable1 x
    v = syst[1]                             # Variable2 v
    dxdt = v                                # Equation différentielle 1
    dvdt = -omega0/Q*v+omega0**2*(xe-x)     # Equation différentielle 2
    return [dxdt,dvdt]                      # Dérivées des variables

# Paramètres d'intégration
t0 = 0                          # Instant de début d'intégration
tf = 50                         # Instant de fin d'intégration
nbPas = 1000                    # Nombre de pas d'intégration
t = np.linspace(t0,tf,nbPas)    # Liste des instants

# Conditions initiales et résolution
x0 = 1                          # Position initiale
v0 = 3                          # Vitesse initiale
ci = np.array([x0,v0])          # Tableau des consitions initiales
sols = odeint(deriv,ci,t)       # Résolution numérique

# Obtention des solutions
x = sols[:, 0]                  #Position
v = sols[:, 1]                  #Vitesse

# Portrait de phase
fig=plt.figure()
plt.plot(x,v)
plt.text(-0.2,-0.3,'$0$', fontsize=16)              # Origine
fig.subplots_adjust(right=1,left=0,top=1,bottom=0)  # Trace le graphe sur tout l'espace disponible

# Abscisse
plt.axhline(color='black')                      # Axe
plt.text(3.8,-0.3,'$u$', fontsize=16)           # Label
plt.xlim(-4,4)                                  # Limites
plt.xticks([])                                  # Effacement des valeurs                                  

# Ordonnée
plt.axvline(color='black')                      # Axe
plt.text(-0.2,3.6,'$\dot{u}$', fontsize=16)     # Label
plt.ylim(-4,4)                                  # Limites
plt.yticks([])                                  # Effacement des valeurs

# Repérage de la position initiale
plt.plot([x0,x0],[0,v0],'k--')                      # Segment
plt.text(x0+0.05,0.1,'$u_0$', fontsize=16)          # Label

# Repérage de la vitesse initiale
plt.plot([0,x0],[v0,v0],'k--')                      # Segment                  
plt.text(-0.3,v0-0.1,'$\dot{u}_0$', fontsize=16)    # Label

# Repérage de l'état d'équilibre
plt.text(xe-0.1,0.1,'$u_\mathrm{e}$', fontsize=16)

#Affichage du graphique
plt.show()