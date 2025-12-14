import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#INPUT CONDITIONS
#Reaction scheme: aA + bB -> cC
stoic_A = 1 #Stoichiometric coefficient of A
M_A = 28 #kg/kmol Molar mass of species A
stoic_B = 3 #Stoichiometric coefficient of B
M_B = 2 #kg/kmol Molar mass of species B
stoic_C = 2 #Stoichiometric coefficient of C
M_C = 17 #kg/kmol Molar mass of species A

#Stream A
m_A = 1 #kg/s
n_A = m_A / M_A #kmol/s Molar flow rate of species A
c_A = 10 #Cost of species A in £/kg

#Stream B
m_B = 1 #kg/s
n_B = m_B / M_B #Molar flow rate of species B
c_B = 15 #Cost of species B in £/kg

#OUTPUT CONDITIONS
#Total
m_tot_in = m_A + m_B
n_tot_in = n_A + n_B
c_tot_in = c_A * m_A + c_B * m_B

#Output
print("Inlet mass flow rate = ", m_tot_in, " kg/s")
print("Inlet molar flow rate = ", n_tot_in, " kmol/s")
print("Inlet costs = £", c_tot_in, "/s")