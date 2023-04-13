import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp



chat_id = 561049466

def solution(sample: np.ndarray) -> bool:
    _, p_v = ttest_1samp(sample, 300)
    return p_v < 0.04
