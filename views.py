import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import tools
import strats

class Views:

	def __init__(self, t):
		self.t = t

	def MACD_view(self, prices):
		misc = tools.Misc(prices)
		ema_fast = misc.ema_array(13)
		ema_slow = misc.ema_array(26)
		ema_crossings = misc.ema1_ema2_cross(ema_fast, ema_slow)

		fig = plt.figure()
		ax = fig.add_subplot(111)
		self.t = self.t/(60 * 24) #60m * 24h -> days
		plt.plot(self.t, prices, color='green', label='Price')
		plt.plot(self.t, ema_fast, color='blue', label='EMA_FAST')
		plt.plot(self.t, ema_slow, color='yellow', label='EMA_SLOW')
		"""
		for timestamp in ema_crossings:
			time = timestamp / 6
			if (ema_crossings[timestamp] == True):
				plt.text(time, prices[timestamp], 'b', color='green', fontsize=16)
			else:
				plt.text(time, prices[timestamp], 's', color='red', fontsize=16)
		"""
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())
		plt.legend()
		plt.show()
		#print(strats.Strats(fiat=1000, fee=1.0).ema_cross_strategy(self.prices, 1, 2))


	def candles_view(self, open, high, low, close, volume, hours):
		fig = plt.figure()
		ax = fig.add_subplot(111)
		k = 24/hours

		r_width = 0.8 / k
		periods = range(len(open))
		for timestamp in periods:
			r_height = abs(open[timestamp] - close[timestamp]) + 0.1
			r_x = timestamp/k - r_width/2.0
			r_y = min(open[timestamp], close[timestamp])
			if (open[timestamp] > close[timestamp]):
				ax.add_patch(patches.Rectangle((r_x, r_y), r_width, r_height, facecolor='r'))
				plt.plot([timestamp/k, timestamp/k], [low[timestamp], high[timestamp]], 'r')
			else:
				ax.add_patch(patches.Rectangle((r_x, r_y), r_width, r_height, facecolor='g'))
				plt.plot([timestamp/k, timestamp/k], [low[timestamp], high[timestamp]], 'g')

		#plt.plot(self.t, high)
		#line = matplotlib.lines.Line2D([10, 5000], [10, 6000])
		#ax.add_line(line)
		#plt.plot([10, 10], [5000, 6000])
		#plt.legend()
		mng = plt.get_current_fig_manager()
		mng.resize(*mng.window.maxsize())
		plt.show()