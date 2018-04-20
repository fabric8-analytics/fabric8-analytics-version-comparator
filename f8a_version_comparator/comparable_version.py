# class ComparableVersion():

# 	@classmethod
# 	def parse_version(self, version):
# 		self.value = version;

# 		v_list = list()
# 		_start_index = 0 

# 		v_index = 0

# 		qualifiers = ["alpha", "beta", "milestone", "rc", "snapshot", "", "sp"]
# 		short_qualifiers = { "a" : "alpha", "b" : "beta", "m" : "milestone"}
# 		aliases = {
#                "ga" : "",
#                "final" : "",
#                "cr" : "rc"
#    		 }
# 		while (v_index<len(version)):
# 			if version[v_index] is '.' or version[v_index] is "-":
# 				if v_index == _start_index:
# 					v_list.append(0)
# 				v_list.append(version[v_index])
# 				v_index += 1
# 			# checks if consecutive characters are also digits.
# 			# If so, it takes series of digit into account
# 			if version[v_index].isdigit():

# 				in_string = version[v_index : v_index + 1]
# 				length_numerical = 1
# 				while True:
# 					if(v_index+length_numerical >= len(version)):
# 						break
# 					if version[v_index + length_numerical].isdigit():
# 						in_string += str(version[v_index + length_numerical])
						
# 						length_numerical += 1
# 					else:
# 						break
# 				v_index += length_numerical	
# 				v_list.append(int(in_string))
# 			else:
# 				in_string = version[v_index : v_index + 1]
# 				length_string = 1
# 				while True:
# 					if(v_index+length_string >= len(version)):
# 						break
# 					black_list = ['.', '-']
# 					if version[v_index + length_string] not in black_list:
# 						if version[v_index] in short_qualifiers.keys():
# 							if (v_index + 1) < len(version):
# 								version[v_index + 1].isdigit()

# 						in_string += str(version[v_index + length_string])
# 						length_string += 1
# 					else:
# 						break
# 				if in_string in qualifiers:
# 					v_list.append(in_string)
# 				else:
# 					str_index = 0
# 					import pdb
# 					pdb.set_trace()
# 					while str_index < len(in_string):
# 						if in_string[str_index].isdigit():
# 							v_list.append(int(in_string[str_index]))
# 						else:
# 							parse_char = str(in_string[str_index])
# 							if parse_char in short_qualifiers.keys():
# 								v_list.append(short_qualifiers.get(parse_char))
# 							else:
# 								v_list.append(parse_char)
# 						str_index +=1
# 					v_index += length_string
# 		return v_list
		

# def equalize_str_lengths(v1, v2):

# 	flag = False
# 	if len(v1) > len(v2):
# 		diff_index = len(v2)
# 		max_len = len(v1)
# 		flag = True
# 	else:
# 		diff_index = len(v1)
# 		max_len = len(v2)

# 	while diff_index < max_len:
# 		if flag:
# 			diff_value = v1[diff_index]
# 			if v1[diff_index] == '.' or v1[diff_index] == "-":
# 				v2.append(diff_value)
# 			else:
# 				v2.append("")
# 		else:
# 			diff_value = v2[diff_index]
# 			if v2[diff_index] == '.' or v2[diff_index] == "-":
# 				v1.append(diff_value)
# 			else:
# 				v1.append("")

# 		diff_index += 1

# def compare_string(s1, s2):
# 	qualifiers = ["alpha", "beta", "milestone", "rc", "snapshot", "", "sp"]
# 	aliases = {
#                "ga" : "",
#                "final" : "",
#                "cr" : "rc"
#     		}
#     if s1 in aliases:
#         s1 = aliases.get(s1)

#     if s1 in qualifiers and s2 in qualifiers:
#     	if qualifiers.index(s1) > qualifiers.index(s2):
#     		return -1
#     	elif qualifiers.index(s1) < qualifiers.index(s2):
#     		return 1
#     	else:
#     		return 0

# def compare_item(v1, v2):

#     _loop_index = 0
#     while _loop_index < len(v1):
#     	v1_item = v1[_loop_index]
#     	v2_item = v2[_loop_index]
#     	if isinstance(v1_item, int) and isinstance(v2_item, int):
#     		if v1_item < v2_item:
#     			return 1
#     		elif v1_item > v2_item:
#     			return -1
#     	if isinstance(v1_item, int) and isinstance(v2_item, str):
#     		return -1
#     	if isinstance(v1_item, str) and isinstance(v2_item, int):
#     		return 1
#     	if isinstance(v1_item, str) and isinstance(v2_item, str):
#     		str_comp =  compare_string_item(v1_item, v2_item) 
#     		if str_comp is not 0:
#     			return str_comp


# if __name__ == "__main__":
# 	v1 = ComparableVersion.parse_version("1.1a123")
# 	v2 = ComparableVersion.parse_version("1.alpha")
# 	print(v1)
# 	print(v2)
# 	# if len(v1) != len(v2):
# 	# 	equalize_str_lengths(v1,v2)
# 	# item_dict = { "1.11.1" : v1 , "1" : v2}

