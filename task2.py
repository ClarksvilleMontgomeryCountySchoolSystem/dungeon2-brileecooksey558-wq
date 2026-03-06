good = r"""            ____
   M.K.'97   , =, ( _________
             | ='  (VvvVvV--'
             |____(
"""
bad = r"""        ,OO.--.
      ,O  //\  '--------.
      O   \O/  .-,-,-,-,-'
      O,  ,O--'
      'O.-O.
 jgs   /<__>\
       \    /
        '. |
         < |
         < |
         <_/
"""
has_key = True
if has_key:
    outcome = "Click: Continue ahead and unlock the door."
    print(good)
else:
    outcome = "Doom: Retrace your steps to find the key."
    print(bad)
print(outcome)