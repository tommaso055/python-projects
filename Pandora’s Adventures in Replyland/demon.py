class Demon:
	def __init__(self, number, Sc, Tr, Sr, Na, *args):
		self.number = int(number)
		self.stamina_consumed = int(Sc)
		self.turns_before_stamina_restoring = int(Tr)
		self.stamina_resotored = int(Sr)
		self.artifacts_number = int(Na)
		self.artifacts_list = map(int, args)
