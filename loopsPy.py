# NAME	EMOJI	EMOJIXPRESS, MIL.	INSTAGRAM, MIL.	TWITTER, MIL.
# Grinning	image	2.26	1.02	87.3
# Beaming	image	19.1	1.69	150
# ROFL	image	25.6	0.774	0
# Tears of Joy	image	233	7.31	2270
# Winking	image	15.2	2.36	264
# Happy	image	22.7	4.26	565
# Heart Eyes	image	64.6	11.2	834
# Kissing	image	87.5	5.13	432
# Thinking	image	6.81	0.636	0
# Unamused	image	6	0.236	478
# Sunglasses	image	4.72	3.93	198
# Loudly Crying	image	24.7	1.35	654
# Kiss Mark	image	21.7	2.87	98.7
# Two Hearts	image	10	5.69	445
# Heart	image	118	26	1080
# Heart Suit	image	3.31	1.82	697
# Thumbs Up	image	23.1	3.75	227
# Shrugging	image	1.74	0.11	0
# Fire	image	4.5	2.49	150
# Recycle	image	0.0333	0.056	932

twitter = [87.3, 150.0, 0.0, 2270.0, 264.0, 565.0, 834.0, 432.0, 0.0, 478.0]

print('Twitter, mil.')
print('------------')

for element in twitter:
    print(element)

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]

emojixpress_total = 1720

print("Emoji share:")

# create a for loop
for value in emojixpress:
        share = value / emojixpress_total
        print("{:.1%}".format(share))  # input the variable share

print()
print('Total emojis: 1.72 billion')