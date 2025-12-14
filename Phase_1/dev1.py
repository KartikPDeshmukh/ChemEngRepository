import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#INPUT CONDITIONS
#Reaction scheme: aA + bB -> cC; assumed to be Haber Process
stoic_A = 1 #Stoichiometric coefficient of A
M_A = 28 #kg/kmol Molar mass of species A; assumed to be Nitrogen
stoic_B = 3 #Stoichiometric coefficient of B
M_B = 2 #kg/kmol Molar mass of species B; assumed to be Hydrogen
stoic_C = 2 #Stoichiometric coefficient of C
M_C = 17 #kg/kmol Molar mass of species C; assumed to be Ammonia
yield_CA = 1 #Yield of C from A being the limiting species. 
#Of the reactant that did react, how much of that ended up as the desired product? 
#This would be 100% as only C is produced
X_A = 0.9 #Coversion of A
N_units = 1 #Number of reactors or functional units

#Stream A
m_A_in = 1 #kg/s
n_A_in = m_A_in / M_A #kmol/s Molar flow rate of species A
#c_A_in = 10 #Cost of species A in £/kg

#Stream B
m_B_in = 1 #kg/s
n_B_in = m_B_in / M_B #Molar flow rate of species B
#c_B_in = 15 #Cost of species B in £/kg

#OUTPUT CONDITIONS
#Total
m_tot_in = m_A_in + m_B_in
n_tot_in = n_A_in + n_B_in
#c_tot_in = c_A_in * m_A_in + c_B_in * m_B_in

#Reaction calculations
n_C_out = (stoic_C / stoic_A) * yield_CA * X_A * n_A_in
m_C_out = M_C * n_C_out
n_A_out = n_A_in * (1 - X_A)
m_A_out = M_A * n_A_out
n_B_out = n_B_in - (stoic_B / stoic_A) * yield_CA * n_A_in * X_A
m_B_out = M_B * n_B_out

#Output
#print("Inlet mass flow rate = ", m_tot_in, " kg/s")
#print("Inlet molar flow rate = ", n_tot_in, " kmol/s")
#print("Inlet costs = £", c_tot_in, "/s")
print("Outflow of C =", n_C_out, "kmol/s")
print("Outflow of B =", n_B_out, "kmol/s")
print("Outflow of A =", n_A_out, "kmol/s")

print("Outflow of C =", m_C_out, "kg/s")
print("Outflow of B =", m_B_out, "kg/s")
print("Outflow of A =", m_A_out, "kg/s")

#OPEX and CAPEX
#CAPEX estimation based on Bridgwater's (IChemE) correlation
Q = m_tot_in * 3600 * 24 * 365 / 1000  #Annual plant capacity in te/y
if Q < 60000:
    C = 150000 * N_units * (Q / X_A)**0.30
else:
    C = 170 * N_units * (Q / X_A)**0.675
print(C)
