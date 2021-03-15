# Please replace the values below with your UK bra size and the store you're buying from
band_size = 32 # whole even number between 28-40
cup_size = 'J' # letter(s) in quotation marks between A-L
store_name = 'Breakout Bras' # 'Breakout Bras' or 'Comexim' 

########################################################################
########################################################################
#### You can ignore everything below here, it's just messy code lol ####
########################################################################
########################################################################

# Packages
import pandas as pd
import numpy as np
import math

def estimate_comexim_size(band_size: int, cup_size: str, store_name: str):
    cup_number = uk_cup_reference.loc[cup_size].values[0]
    cup_cm = cup_number * 2.54  # centimeters
    new_cup_number = cup_cm / 2
    #####
    if new_cup_number - math.floor(new_cup_number) < 0.2:
        est_cup_number = [math.floor(new_cup_number)]
    elif new_cup_number - math.floor(new_cup_number) > 0.8:
        est_cup_number = [math.ceil(new_cup_number)]
    else:
        est_cup_number = [math.floor(new_cup_number),math.ceil(new_cup_number)]
    #####
    if store_name == 'Breakout Bras':
        est_cup_sizes = np.squeeze(uk_cup_reference_rev.loc[est_cup_number])
    elif store_name == 'Comexim':
        est_cup_sizes = np.squeeze(pl_cup_reference_rev.loc[est_cup_number])
        band_size = pl_band_reference.loc[band_size].values[0]
    else:
        print('Please enter a valid store name in quotes (\"Breakout Bras\" or \"Comexim\")')
    #####
    if len(est_cup_sizes) == 1:
        print('Your estimated Comexim size from {} is {}.'.format(store_name,str(band_size) + est_cup_sizes[0]))
    else:
        print('Your estimated Comexim size from {} is {}/{}.'.format(store_name,str(band_size) + est_cup_sizes.values[0],est_cup_sizes.values[1]))

# Conversions       
uk_cup_letters = np.array(['A','B','C','D','DD','E','F','FF','G','GG','H','HH','J','JJ','K','KK','L'])
pl_cup_letters = np.array(['A','B','C','D','E','F','G','H','HH','J','K','L','M','N','O','P','Q'])
cup_numbers = np.array([i + 1 for i in range(len(uk_cup_letters))])
uk_band_sizes = np.array([b*2 for b in range(14,21)])
pl_band_sizes = np.array([b*5 for b in range(12,19)])
uk_cup_reference = pd.DataFrame(index=uk_cup_letters.T,data=cup_numbers.T,columns=['cup_number'])
uk_cup_reference_rev = pd.DataFrame(index=cup_numbers.T,data=uk_cup_letters.T,columns=['cup_letter'])
pl_cup_reference_rev = pd.DataFrame(index=cup_numbers.T,data=pl_cup_letters.T,columns=['pl_cup_letter'])
pl_band_reference = pd.DataFrame(index=uk_band_sizes.T,data=pl_band_sizes.T,columns=['pl_band_sizes'])

# Calculate bra size
estimate_comexim_size(band_size,cup_size,store_name)
