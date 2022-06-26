def disemvowel(string_):

    my_str = ''
    chars = set('aeiouAEIOU')

    for c in string_:
        if c not in chars:
            my_str += c
    print(my_str)
    return my_str


if __name__ == '__main__':
    # assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
    # assert disemvowel("No offense but, Your writing is among the worst I've ever read") ==\
    #        "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"
    assert disemvowel("What are you, a communist?") == 'Wht r y,  cmmnst?'
    # assert disemvowel('&> t(oOk,IUG E{XAgJupl]VH,Mom@P#i.uInc I<%  cmurleuEE [a'): '&> t(k,G {XgJpl]VH,Mm@P#.nc <% cmrl [') == '&> t(k,G {XgJpl]VH,Mm@P#.nc <%  cmrl ['
    # assert disemvowel(" HdmOy=ax$O(/ uie>RUeAo PTa qb!j'oqoai][VuDWMeAUEEZ"): "Hdmy=x$(/ >R PT qb!j'q][VDWMZ" == " Hdmy=x$(/ >R PT qb!j'q][VDWMZ"
