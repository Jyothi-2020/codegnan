'''
Regular Expression (RegEx)
-->RegEx is a sequence of chart that form a searching pattern.
-->This can be used to check if a string contain the specified search pattern
-->python has a built_in pacakage called 're' which can be ued to work with RegEx..
Functions in re
----------------
1.Findall
2.search
3.fullmatch

Metacharacters
---------------

[]-->a-z,A-Z,0-9 and specified sequence
. ->here each dot is one char
^-->This look for the,string is staring with specified sequence or not.
$-->This look for the,string is ending with specified sequence or not.
*-->zero or more
?-->zero or one
+-->one or more
{}-->

Special sequence
----------------
\S-->no space
\s-->only spaces
\D-->non_digits
\d-->only-digits
\w-->matches any word char(letters,digits,underscore)
\W-->non-words


any="C is a foundational, general-purpose programming language created in 1972 by Dennis Ritchie at Bell Labs."
import re
print(re.findall('[a]',any))
print(re.search('[a]',any))
print(re.findall('[a-mA-z]',any))
print(re.findall('[0-9]',any))
print(re.findall('[ogl]',any))
print(re.findall('p.r.o.e',any))
print(re.search('p.r.o.e',any))
print(re.findall('^C is a',any))
print(re.search('^C is a',any))
print(re.findall('^Bell',any))

so=" general-purpose programming language "
print(re.findall("launguage$",so))

so=" general-purpose programming language "
print(re.findall("g.neral*",so))


so=" general-purpose programming language "
print(re.findall("p.?rpose*",so))


so=" general-purpose programming language "
print(re.findall("g.+eral*",so))

so=" general-purpose programming language "
print(re.findall("p.*",so))

so=" python is a fundamental"
print(re.findall("p.+n*",so))

so=" python is a fundamental"
print(re.findall("p.{10}",so))'''

import re
so=" python is a fundamental"
print(re.findall("\S",so))
print(re.findall("\s",so))
print(re.findall("\D",so))
print(re.findall("\d",so))
print(re.findall("\W",so))
print(re.findall("\w",so))


import re
mobile=input("enter 10 digit mobile num:")
how=re.fullmatch('[6-9][0-9]{9}',mobile)
if how:
    print(f"{mobile} this is india number")
else:
    print(f"{mobile} this is not india number")
    
    
    
    
    
    
    

















