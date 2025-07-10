import numpy as np


def floatConvertible(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



def getAvgSentiment(sentimentScores: float) -> float:
    avg = np.mean(sentimentScores)
    return avg

