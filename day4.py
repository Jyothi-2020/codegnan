'''
CONCATINATION
-------------
-->the(+) for int and can add, but for the other data types it will act as concatinating the data type


a=90
b=8
print(a+b)
any_="python"
so="is a launaguge"
print(any_+so)
an=[1,2]
am=[3,4]
print(an+am)

TUPLE
------
-->collection of different data types seperated by commas,represented in () and immutable

METHODS
-------
COUNT()
-------
---->this used to count the particular item in he tuple

syntax-->variable_name.count(item)


some=(1,"python",[1,2],(3,4))
print(some.count("python"))


INDEX()
------
--->used to find out the the index position of the item,and only gives the first occurance

some=(1,[1,2],(3,4),"python")
print(some.index("python"))

some=(2,[7,8],(90,7),"java","pandas")
print(some.index("java"))


DICTIONARY
----------
--->Dict is a key :value pair , key and value is seperated by : and pair is seperated by comma

eg:

jyothi_details={"name":"jyothi",
                1:2,
                (1,2):[3,4]}
print(type(jyothi_details))


KEYS()
------
used to get keys from

syntax-->dict.keys()

jyothi_details={"name":"jyothi",
                "age" :24,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}
print(jyothi_details.keys())


VALUES()
--------

jyothi_details={"name":"jyothi",
                "age" :24,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}
print(jyothi_details.values())

ITEMS()
-------
-->uesd to get key and value together

syntax-->dict.items()

jyothi_details={"name":"jyothi",
                "age" :24,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}
print(jyothi_details.items())



jyothi_details={"name":"jyothi",
                "age" :24,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}
print(jyothi_details.items())
print(jyothi_details["age"])

UPDATE()
--------
-->used to add a new key :value pair into dict

synatx-->dict.update({key:value})


jyothi_details={"name":"jyothi",
                "age" :24,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}

jyothi_details .update({"Aadhar":"967542345087"})
jyothi_details['name']="kotyada"
print(jyothi_details["age"])



jyothi_details={"name":"jyothi",
                "age" :24,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}

jyothi_details .update({"Aadhar":"967542345087"})
jyothi_details['name']="kotyada"
print(jyothi_details)



CLEAR()
-------
-->used to remove all the items in the dict

jyothi_details={"name":"jyothi",
                "age" :24,
                "mobN":"123456789",
                "pan" :"KPXPB2072H"}
jyothi_details.clear()
print(jyothi_details)

'''







































