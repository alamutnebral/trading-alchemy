import numpy as np

class Misc:

	def __init__(self, data):
		self.data = data

	def ema_array(self, n):
		amount_of_periods = len(self.data)
		alpha = 2.0 / (n + 1)
		emas = np.zeros(amount_of_periods)
		emas[0] = self.data[0]
		for t in range(1, amount_of_periods):
			emas[t] = alpha * self.data[t] + (1.0 - alpha) * emas[t-1]
		return emas


	def ema1_ema2_cross(self, ema_fast, ema_slow):
		n = len(ema_fast)
		crossings = {}
		for t in range(n - 1):
			d1 = ema_fast[t] - ema_slow[t]
			d2 = ema_fast[t + 1] - ema_slow[t + 1]
			if (d1 < 0) and (d2 > 0):
				crossings[t] = True
			if (d1 > 0) and (d2 < 0):
				crossings[t] = False
		return crossings