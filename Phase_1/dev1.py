import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#INPUT CONDITIONS
#Two inlet streams: A and B

#Stream A
m_A = 1 #kg/s
M_A = 10 #kg/kmol Molar mass of species A
n_A = m_A / M_A #kmol/s Molar flow rate of species A
c_A = 10 #Cost of species A in £/kg

#Stream B
m_B = 1 #kg/s
M_B = 20 #kg/kmol Molar mass of species B
n_B = m_B / M_B #Molar flow rate of species B
c_B = 15 #Cost of species B in £/kg

#Total
m_tot_in = m_A + m_B
n_tot_in = n_A + n_B
c_tot_in = c_A * m_A + c_B * m_B

#Output
print("Inlet mass flow rate = ", m_tot_in, " kg/s")
print("Inlet molar flow rate = ", n_tot_in, " kmol/s")
print("Inlet costs = £", c_tot_in, "/s")