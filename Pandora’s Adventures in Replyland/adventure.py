import demon
from collections import deque
class Adventure:
	def __init__(self, input_file=False , output_file="output.txt"):
		assert input_file, "Provide a file path in order to start an Adventure!"
		self.input_file = input_file
		self.output_file = output_file
		self.demons = []
		self.create_demons()
		self.optimal_path = self.defeat_demons(0, [False*self.number_of_demons], self.initial_stamina, deque([0*self.total_turns]), 0)
		self.create_output_file()

	def create_demons(self):
		# demon: (self, number, Sc, Tr, Sr, Na, *args)
		input_fd = open(self.input_file, "r")
		line = input_fd.readline().strip("\n").split()
		map(int, line)
		self.initial_stamina = line[0]
		self.max_stamina = line[1]
		self.total_turns = line[2]
		self.number_of_demons = line[3]
		for i in range(self.number_of_demons):
			line = input_fd.readline().strip("\n").split()
			self.demons.append(Demon(i, line))
		input_fd.close()


	def defeat_demons(self, current_turn, defeated_demons, current_stamina, stamina_recovery, artifacts_count):
		optimal_path = (0, [])
		if current_turn == self.total_turns: return optimal_path

		current_stamina = min(self.max_stamina, current_stamina + stamina_recovery.popleft())
		for i in range(number_of_demons):
			if not defeated_demons[i] and demons[i].stamins_consumed <= current_stamina:
				defeated_demons_updated = defeated_demons.copy()
				defeated_demons_updated[i] = True
				stamina_recovery_updated = stamina_recovery.copy()
				artifacts_earned = sum(demons[i].artifacts_list[:(self.total_turns - current_turn)])
				stamina_recovery_updated[demons[i].turns_before_stamina_restoring - 1] = demons[i].stamina_restored
				path_continuation = self.defeat_demons( current_turn + 1, defeated_demons_updated, current_stamina - demons[i].stamins_consumed, stamina_recovery_updated, artifacts_count + artifacts_earned)
				if path_continuation[0] + artifacts_earned > optimal_path:
					optimal_path = (path_continuation[0] + artifacts_earned, [i] + path_continuation[1])
		return optimal_path


	def create_output_file(self):
		output_fd = open(self.output_file, "a")
		output_fd.write("\n".join(self.optimal_path))
		input_fd.close()

adventure = Adventure("text_input.txt")