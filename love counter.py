f_name = input("Man, input your name: ").lower()
s_name = input("Woman, input your name: ").lower()
f_val = 0
s_val = 0

f_count = f_name.count("t") + f_name.count("r") + \
    f_name.count("u") + f_name.count("e")
s_count = s_name.count("t") + s_name.count("r") + \
    s_name.count("u") + s_name.count("e")


fs_count = f_name.count("l") + f_name.count("o") + \
    f_name.count("v") + f_name.count("e")
ss_count = s_name.count("l") + s_name.count("o") + \
    s_name.count("v") + s_name.count("e")


print(
    f"The percentage that you two are soulmates is {f_count + s_count}{fs_count + ss_count}%")


# for i in f_name:
#     if i == "t" or  i == "r" or i == "u" or i == "e":
#         f_val += 1

# for i in s_name:
#     if i == "t" or  i == "r" or i == "u" or i == "e":
#         f_val += 1

# for i in f_name:
#     if i == "l" or  i == "o" or i == "v" or i == "e":
#         s_val += 1

# for i in s_name:
#     if i == "l" or  i == "o" or i == "v" or i == "e":
#         s_val += 1


#print(f"The percentage that you two are soulmates is {f_val}{s_val}%")
