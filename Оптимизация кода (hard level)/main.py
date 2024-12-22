import numpy as np
from scipy.signal import convolve
from memory_profiler import profile

@profile
def compute_baseline(movie, f_noise_sigma, mean_window_size, num_iterations):
    N, M, T = movie.shape
    movie = movie.astype(np.float32)
    flags = np.ones((N, M), dtype = bool)

    w_sizes = np.clip(np.arange(T) + (mean_window_size + 1) // 2, 0, T) \
            - np.clip(np.arange(T) - mean_window_size // 2, 0, T)
    w_sizes = w_sizes.astype(np.float32)
    kernel = np.ones((mean_window_size), dtype = np.float32)[np.newaxis, np.newaxis]

    init = movie.copy()
    for _ in range(num_iterations):
        init[flags] = convolve(movie, kernel, mode = 'same', method = 'fft')[flags] / w_sizes
        np.minimum(init, movie, out = movie)
        
        D = np.sqrt(np.mean((init - movie) ** 2, axis = 2) * T / (T - 1))
        flags &= (D >= f_noise_sigma)
    return init


if __name__ == "__main__":
    np.random.seed(3)
    movie = np.random.random((150, 150, 1000))
    f_noise_sigma = np.random.random((150, 150))
    mean_window_size = 1000
    num_iterations = 10
    movie = compute_baseline(movie, f_noise_sigma, mean_window_size, num_iterations)
    #print(movie)