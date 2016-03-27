__author__ = 'chrismurphy'


def find_substring(str_ing):
    vowel = ["A", "E", "I", "O", "U"]
    Stuart = 0
    Kevin = 0

    for x in range(0,len(str_ing)):

        if str_ing[x] in vowel:
            Kevin += (len(str_ing)-x)
        else:
            Stuart += (len(str_ing)-x)
    if(Stuart>Kevin):
        print "Stuart "+str(Stuart)
    if(Stuart<Kevin):
        print "Kevin "+str(Kevin)
    if(Stuart==Kevin):
        print "Draw"




def main():
    S = raw_input("")

    find_substring(S.upper())


main()
