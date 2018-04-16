class ComparableVersion():

	@classmethod
	def parse_version(self, version):
		self.value = version;

		v_list = list()
		_start_index = 0 
		v_index = 0
		while (v_index<len(version)):
			if v_index == _start_index:
				if version[v_index] is '.' or version[v_index] is "-":
					v_list.append(0)
					v_index += 1
			if version[v_index] is '.' or version[v_index] is "-":
				v_list.append(version[v_index])
				v_index += 1
				continue
			# checks if consecutive characters are also digits.
			# If so, it takes series of digit into account
			if version[v_index].isdigit():
				in_string = version[v_index : v_index + 1]
				length_numerical = 1
				while True:
					if(v_index+length_numerical >= len(version)):
						break
					if version[v_index + length_numerical].isdigit():
						in_string += in_string + str(version[v_index + length_numerical])
						v_index += length_numerical
						length_numerical += 1
					else:
						break
				v_list.append(int(in_string))
			else:
				in_string = version[v_index : v_index + 1]
				length_string = 1
				while True:
					if(v_index+length_string >= len(version)):
						break
					black_list = ['.', '-']
					if version[v_index + length_string] not in black_list:
						in_string += in_string + str(version[v_index + length_string])
						v_index += length_string
						length_string += 1
					else:
						break
				v_list.append(in_string)

		return v_list
		

if __name__ == "__main__":
	print(ComparableVersion.parse_version("1.0-alpha-1"))

