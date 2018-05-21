import tools

class Strats:

	def __init__(self, fiat, fee, log=False):
		self.fiat = fiat
		self.fee = fee
		self.log = log

	def ema_cross_strategy(self, prices, fast_period, slow_period):
		fiat = 1000
		balance = 0
		misc = tools.Misc(prices)
		ema_fast = misc.ema_array(fast_period)
		ema_slow = misc.ema_array(slow_period)
		ema_crossings = misc.ema1_ema2_cross(ema_fast, ema_slow)
		filename = "EMA" + str(fast_period) + "EMA" + str(slow_period) + "_4h_100days"
		with open(filename, 'w') as log:
			for timestamp in ema_crossings:
				if (ema_crossings[timestamp] == True):
					balance = (self.fiat / prices[timestamp]) * (1.0 - self.fee / 100.0)
					self.fiat = 0
					status_message = "buy:  day {:<2} price: {:<5}\n".format(int(timestamp/6), int(prices[timestamp]))
					log.write(status_message)
				else:
					self.fiat = (balance * prices[timestamp]) * (1.0 - self.fee / 100.0)
					balance = 0
					status_message = "sell: day {:<2} price: {:<5}".format(int(timestamp/6), int(prices[timestamp]))
					log.write(status_message + " balance: {}\n".format(self.fiat))
		if (fiat > 0):
			return self.fiat
		else:
			return balance * prices[len(prices) - 1]