import re
re.compile(r'a*bbc+')

# I see the cat
# A cat see the rat

prefix = 0x
number = 0-9
letter = A-F
char   = number | letter
repeated_char = <char> | <char><repeated_char>
string = <prefix><repeated_char>

            <e2>
        <e3> * <e2>
        <e3> * <e3>
        <e3> * (<e1>)
        <e3> * (<e2> + <e1>)
        <e3> * (<e3> + <e2>)
        <e3> * (<e3> + <e3>)

4 + (3 * 5)
