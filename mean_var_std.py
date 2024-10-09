import numpy as np

def calculate(list):
    if len(list) == 9:
        l = np.reshape(list, (3,3))
        # mean = np.array([np.mean(l, axis = 0), np.mean(l, axis = 1), np.mean(l)])
        # variance = np.array([np.var(l, axis = 0), np.var(l, axis = 1), np.var(l)])
        # std = np.array([np.std(l, axis = 0), np.std(l, axis = 1), np.std(l)])
        # max_val = np.array([np.max(l, axis = 0), np.max(l, axis = 1), np.max(l)])
        # min_val = np.array([np.min(l, axis = 0), np.min(l, axis = 1), np.min(l)])
        # sum_val = np.array([np.sum(l, axis = 0), np.sum(l, axis = 1), np.sum(l)])

        calculations = {
            'mean': [np.mean(l, axis = 0).tolist(), np.mean(l, axis = 1).tolist(), np.mean(l).tolist()],
            'variance': [np.var(l, axis = 0).tolist(), np.var(l, axis = 1).tolist(), np.var(l).tolist()],
            'standard deviation': [np.std(l, axis = 0).tolist(), np.std(l, axis = 1).tolist(), np.std(l).tolist()],
            'max': [np.max(l, axis = 0).tolist(), np.max(l, axis = 1).tolist(), np.max(l).tolist()],
            'min': [np.min(l, axis = 0).tolist(), np.min(l, axis = 1).tolist(), np.min(l).tolist()],
            'sum': [np.sum(l, axis = 0).tolist(), np.sum(l, axis = 1).tolist(), np.sum(l).tolist()]
        }

        return calculations
    else:
        raise ValueError('List must contain nine numbers.')