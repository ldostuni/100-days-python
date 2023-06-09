name1 = input("What's your name? ")
name2 = input("What's your lover's name? ")

name1l = name1.lower()
name2l = name2.lower()

occ_e = name1l.count("e") + name2l.count("e")
occ_l = name1l.count("l") + name2l.count("l")
occ_o = name1l.count("o") + name2l.count("o")
occ_r = name1l.count("r") + name2l.count("r")
occ_t = name1l.count("t") + name2l.count("t")
occ_u = name1l.count("u") + name2l.count("u")
occ_v = name1l.count("v") + name2l.count("v")

d1 = occ_t + occ_r + occ_u + occ_e
d2 = occ_l + occ_o + occ_v + occ_e

num = str(d1) + str(d2)

print(f"Your love percentage is {num}%")