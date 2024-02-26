import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal_distributions():
    """
    This function plots the PDF and CDF for a standard normal distribution (mean=0, std=1)
    and a normal distribution with a mean of 175 and a standard deviation of 3.
    It also calculates and prints the probability of x <= 1 for the standard normal distribution
    and the probability of x >= mean + 2*std for the N(175, 3) distribution.
    """

    # Parameters for the standard normal distribution
    mu_1, sigma_1 = 0, 1
    # Parameters for the normal distribution with mean 175 and std 3
    mu_2, sigma_2 = 175, 3

    # Create an array of x values for plotting the standard normal distribution
    x_1 = np.linspace(mu_1 - 4 * sigma_1, mu_1 + 4 * sigma_1, 1000)
    # Create an array of x values for plotting the normal distribution N(175, 3)
    x_2 = np.linspace(mu_2 - 4 * sigma_2, mu_2 + 4 * sigma_2, 1000)

    # Calculate the PDF for the standard normal distribution
    pdf_1 = norm.pdf(x_1, mu_1, sigma_1)
    # Calculate the CDF for the standard normal distribution
    cdf_1 = norm.cdf(x_1, mu_1, sigma_1)

    # Calculate the PDF for the normal distribution N(175, 3)
    pdf_2 = norm.pdf(x_2, mu_2, sigma_2)
    # Calculate the CDF for the normal distribution N(175, 3)
    cdf_2 = norm.cdf(x_2, mu_2, sigma_2)

    # Calculate the probabilities for the specific conditions
    prob_x_less_1 = norm.cdf(1, mu_1, sigma_1)  # P(x <= 1) for N(0,1)
    prob_x_greater_mu_plus_2sigma = 1 - norm.cdf(mu_2 + 2 * sigma_2, mu_2, sigma_2)  # P(x >= µ + 2σ) for N(175,3)

    # Create a figure with subplots
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    # Plot the PDF for the standard normal distribution
    ax[0, 0].plot(x_1, pdf_1, label='PDF N(0,1)')
    ax[0, 0].fill_between(x_1, pdf_1, where=(x_1 <= 1), color='skyblue', alpha=0.5)
    ax[0, 0].legend()

    # Plot the CDF for the standard normal distribution
    ax[1, 0].plot(x_1, cdf_1, label='CDF N(0,1)')
    ax[1, 0].scatter(1, norm.cdf(1, mu_1, sigma_1), color='red')  # Mark the point for x=1
    ax[1, 0].legend()

    # Plot the PDF for the normal distribution N(175, 3)
    ax[0, 1].plot(x_2, pdf_2, label='PDF N(175,3)')
    ax[0, 1].fill_between(x_2, pdf_2, where=(x_2 >= mu_2 + 2 * sigma_2), color='skyblue', alpha=0.5)
    ax[0, 1].legend()

    # Plot the CDF for the normal distribution N(175, 3)
    ax[1, 1].plot(x_2, cdf_2, label='CDF N(175,3)')
    ax[1, 1].scatter(mu_2 + 2 * sigma_2, norm.cdf(mu_2 + 2 * sigma_2, mu_2, sigma_2),
                     color='red')  # Mark the point for x=µ+2σ
    ax[1, 1].legend()

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plots
    plt.show()

    # Print the calculated probabilities
    print(f'P(x <= 1) for N(0,1): {prob_x_less_1:.4f}')
    print(f'P(x >= µ + 2σ) for N(175,3): {prob_x_greater_mu_plus_2sigma:.4f}')
    
