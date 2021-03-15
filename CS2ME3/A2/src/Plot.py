## @file Plot.py
#  @author Kyle Carnrite
#  @brief
#  @date February 15th, 2021
#  @details

import matplotlib.pyplot as plt 

    ## @brief Plots x vs t, y vs t, and y vs x 
    #  @details Assumes arguments provided are correct type
def plot(w, t):
    if not (len(w) == len(t)):
        raise ValueError

    #Get x:
    x = []
    for i in range(len(w)):
        x.append(w[i][0])

    # Get y:
    y = []
    for i in range(len(w)):
        y.append(w[i][1])

    fig, axs = plt.subplots(3)
    axs[0].plot(t, x)
    axs[1].plot(t, y)
    axs[2].plot(x, y)

    plt.show()
