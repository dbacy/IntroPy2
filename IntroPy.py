print ('Research on language popularity.')
#LANGUAGE	SHARE OF WEBSITES IN THE TOP 10 MIL.	NATIVE SPEAKERS, MIL.	TOTAL SPEAKERS OF LANGUAGE, MIL.
#English	0.539	378.2	1121
#Russian	0.061	153.9	264.3
#German	0.06	76	132
#Spanish	0.049	442.3	512.9
#French	0.04	76.7	284.9
#Japanese	0.034	128.2	128.3
#Portuguese	0.029	222.7	236.5
# Italian	0.024	64.8	67.8
# Persian	0.02	60	110
# Polish	0.018	39.6	40.3
# Chinese	0.017	908.7	1107
# Danish	0.012	22	28
# Turkish	0.012	78.5	78.9
# Czech	0.01	10.4	10.6

############################################################################################

print(1121 / 7539)
print ((128.3 - 128.2) / 128.3)
print(908.7 / 378.2)


#########################################################################################
english_native = 378.2
russian_native = 153.9
german_native = 76.0
chinese_native = 908.7
top3_total = english_native + russian_native + german_native
print (chinese_native - top3_total )


############################################################################################


japanese_2013 = 0.045
chinese_2013 = 0.043

japanese_2018 = 0.034
chinese_2018 = 0.017

japanese = japanese_2013
chinese = chinese_2013

print(japanese/chinese)

japanese = japanese_2018
chinese = chinese_2018

print(japanese/chinese)

##########################################################################################


russian_web_share = 0.061
total_web = 10000000

russian_websites = russian_web_share * total_web
print(russian_websites)
print(type(russian_websites))
russian_native_millions = 153.9
russian_native = russian_native_millions * 1000000
russian_native_int = int(russian_native)
print(russian_native_int)
print(type(russian_native_int))


############################################################################################


total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_share = 0.017
english_speakers = 1121
english_web_share = 0.539
russian_speakers = 264.3
russian_web_share = 0.061
total_speakers = 7539

chinese_speakers = 1107
english_speakers = 1121
russian_speakers = 264.3

chinese_speakers_share = chinese_speakers / total_speakers
print("Share of people who speak Chinese:", chinese_speakers_share)

english_speakers_share = english_speakers / total_speakers
print("Share of people who speak English:", english_speakers_share)

russian_speakers_share = russian_speakers / total_speakers
print("Share of people who speak Russian:", russian_speakers_share)


##########################################################################################


total_speakers = 7539
chinese_speakers = 1107
english_speakers = 1121
russian_speakers = 264.3

chinese_speakers_share = chinese_speakers / total_speakers
english_speakers_share = english_speakers / total_speakers
russian_speakers_share = russian_speakers / total_speakers
print('Percentage of people who speak Chinese: {:.1%}'.format(chinese_speakers_share))
print('Percentage of people who speak English: {:.1%}'.format(english_speakers_share))
print('Percentage of people who speak Russian: {:.1%}'.format(russian_speakers_share))


#############################################################################################


total_speakers = 7539
chinese_speakers = 1107
english_speakers = 1121
russian_speakers = 264.3

chinese_speakers_share = chinese_speakers / total_speakers
print('--- Chinese ---')
print('Percentage of speakers: {:.1%}'.format(chinese_speakers_share))
print()

english_speakers_share = english_speakers / total_speakers
print('--- English ---')
print('Percentage of speakers: {:.1%}'.format(english_speakers_share))
print()

russian_speakers_share = russian_speakers / total_speakers
print('--- Russian ---')
print('Percentage of speakers: {:.1%}'.format(russian_speakers_share))


###############################################################################################


total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_share = 0.017

english_speakers = 1121
english_web_share = 0.539

russian_speakers = 264.3
russian_web_share = 0.061

chinese_speakers_share = chinese_speakers / total_speakers
chinese_websites = chinese_web_share * total_web
chinese_index = 1000 * chinese_websites / chinese_speakers
print('--- Chinese ---')
print('Percentage of speakers: {:.1%}'.format(chinese_speakers_share))
print('Percentage of websites in the language: {:.1%}'.format(chinese_web_share))
print('Web popularity index: {:.2f}'.format(chinese_index))
print()



english_speakers_share = english_speakers / total_speakers
english_websites = english_web_share * total_web
english_index = 1000 * english_websites / english_speakers
print('--- English ---')
print('Percentage of speakers: {:.1%}'.format(english_speakers_share))
print('Percentage of websites in the language: {:.1%}'.format(english_web_share))
print('Web popularity index: {:.2f}'.format(english_index))
print()




russian_speakers_share = russian_speakers / total_speakers
russian_websites = russian_web_share * total_web
russian_index = 1000 * russian_websites / russian_speakers
print('--- Russian ---')
print('Percentage of speakers: {:.1%}'.format(russian_speakers_share))
print('Percentage of websites in the language: {:.1%}'.format(russian_web_share))
print('Web popularity index: {:.2f}'.format(russian_index))
print()


# --- Chinese ---
# Percentage of speakers: 14.6%
# Percentage of websites in the language: 1.7%
# Web popularity index: 0.15
#
# --- English ---
# Percentage of speakers: 14.8%
# Percentage of websites in the language: 53.9%
# Web popularity index: 4.81
#
# --- Russian ---
# Percentage of speakers: 3.5%
# Percentage of websites in the language: 6.1%
# Web popularity index: 2.31
