words = input("Enter your words: ").split()
final_str = f"!{words[1]} ! {words[0]}!"
print(f"!{words[1]} ! {words[0]}!")
print("!"+words[1]+" ! "+words[0]+"!")
print("!{} ! {}!".format(words[1], words[0]))
print("!%s ! %s!" % (words[1], words[0]))
print(f"{final_str}")
print("{}".format(final_str))
print(final_str)
print("%s" % final_str)
