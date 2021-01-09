import matplotlib.pyplot as plt
import numpy as np

def exponential_distribution_pdf(lamda: float, x: np.ndarray):
    return np.multiply(lamda, np.exp(-lamda * x))

def exponential_distribution_cdf(lamda: float, x: np.ndarray):
    return 1 - np.exp(np.multiply(-lamda, x))

def generate_exponential_samples(lamda: float, r: np.ndarray):
    samples = -np.log(r) / lamda
    return samples

def plot_figure(info: dict, x: np.ndarray, y: np.ndarray):
    plot = plt.figure(info["iter"])
    for i in range(3):
        lam = info["lamda"][i,0]
        label = info["label"] + str(lam)
        plt.plot(x, y[i,:], label=label)
    plt.ylabel("Probability Density")
    plt.xlabel("x")
    plt.title(info["title"])
    plt.grid(True)
    plt.legend()

if __name__ == "__main__":
    lamda = np.array([[0.5], [1.0], [1.5]])
    r = np.random.uniform(0.0, 1.0, (1, 50))
    values = np.linspace(0, 2*np.pi, 50)
    exponential_samples = generate_exponential_samples(lamda, r)
    np.save("generated_samples/exponential_samples", exponential_samples)
    print(f"Saved!\nExponential samples shape:\n {exponential_samples.shape}")
    exponential_pdf_values = exponential_distribution_pdf(lamda, values)
    exponential_cdf_values = exponential_distribution_cdf(lamda, values)

    info_pdf = {
        "iter": 1,
        "lamda": lamda,
        "label": "f_X(x) λ = ",
        "title": "Probability Density Functions"
    }

    info_cdf = {
        "iter": 2,
        "lamda": lamda,
        "label": "F_X(x) λ = ",
        "title": "Cumulative Distribution Functions"
    }

    plot_figure(info_pdf, values, exponential_pdf_values)
    plot_figure(info_cdf, values, exponential_cdf_values)
    plt.show()