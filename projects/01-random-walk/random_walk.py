import numpy as np
import matplotlib.pyplot as plt

def simulate_random_walk(n_steps: int) -> np.ndarray:
  """
  Simulate a one-dimensional random walk.

  Each step is either +1 or -1 with equal probability.
  """
  steps = np.random.choice([-1, 1]), size=n_steps)
  position = np.cumsum(steps)
  return position
