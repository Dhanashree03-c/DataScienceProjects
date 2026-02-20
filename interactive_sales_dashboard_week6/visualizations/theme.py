"""
Contains global styling configuration for Seaborn and plotly.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def set_seaborn_theme():
    sns.set_theme(
        style = "whitegrid",
        palette = "deep",  #Professional, balanced color scheme
        font_scale = 1.1
    )
    
    #ensures all plots maintain consistent dimensions
    plt.rcParams["figure.figsize"] = (10, 6)