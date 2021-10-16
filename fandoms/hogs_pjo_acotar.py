from collections import Counter
from statistics import mode

pjo = []
m_pjo = []
acotar = []
hogwarts = []

print("Welcome to the Fandom Quiz! Feature BookTok books!")
print(
    """
Question One: What is your favorite season:
    1. Spring
    2. Summer
    3. Autumn
    4. Winter
"""
)
q1 = int(input("1, 2, 3, or 4: "))
if q1 == 1:
    pjo.append('Demeter')
    m_pjo.append('Iris')
    m_pjo.append('Hebe')
    acotar.append('Dawn')
    acotar.append('slytherin')
    hogwarts.append('Hufflpuff')
if q1 == 2:
    pjo.append('Dionyses')
    pjo.append('Poseidon')
    pjo.append('Apollo')
    m_pjo.append('Nyche')
    acotar.append('Day')
    acotar.append('Summer')
    hogwarts.append('Gryffindor')
if q1 == 3:
    m_pjo.append('Artemis')
    pjo.append('Poseidon')
    pjo.append('Apollo')
    pjo.append('Athena')
    acotar.append('Day')
    acotar.append('qu')
    hogwarts.append('Gryffindor')
    hogwarts.append('Ravenclaw')
if q1 == 4:
    m_pjo.append('Hades')
    m_pjo.append('Artemis')
    acotar.append('Night')
    acotar.append('Winter')
    hogwarts.append('Ravenclaw')
    hogwarts.append('slytherin')
else:
    print("Please select a proper number.")
print(
    """Question Two: What time of day do you feel most alive?
      1. Dawn
      2. Morning
      3. Noon
      4. Afternoon
      5. Evening"
      6. Nightfall
      7. Midnight
""")
q2 = int(input("1, 2, 3, 4, 5, 6, or 7: "))
if q2 == 1:
    pjo.append("Zues")
    pjo.append('Apollo')
    pjo.append('Ares')
    pjo.append('Hermes')
    m_pjo.append('Nyche')
    m_pjo.append('Tyche')
    acotar.append('Dawn')
    acotar.append('slytherin')
    hogwarts.append('Hufflpuff')
if q2 == 2:
    pjo.append('Zues')
    pjo.append('Apollo')
    pjo.append('Ares')
    pjo.append('Hermes')
    m_pjo.append('Nyche')
    m_pjo.append('Tyche')
    acotar.append('Dawn')
    acotar.append('Summer')
    hogwarts.append('slytherin')
    hogwarts.append('Gryffindor')
if q2 == 3:
    pjo.append('Demeter')
    pjo.append('Ares')
    pjo.append('Heaphestus')
    pjo.append('Aphrodite')
    m_pjo.append('Iris')
    m_pjo.append('Nemisis')
    acotar.append('Day')
    acotar.append('spring')
    hogwarts.append('Hufflpuff')
if q2 == 4:
    pjo.append('Aphrodite')
    pjo.append('Hermes')
    pjo.append('Dionyses')
    m_pjo.append('Hypnos')
    m_pjo.append('Tyche')
    acotar.append('Day')
    acotar.append('Summer')
    hogwarts.append('slytherin')
if q2 == 5:
    pjo.append('Aphrodite')
    pjo.append('Heaphestus')
    pjo.append('Dionyses')
    pjo.append('Hermes')
    acotar.append('Night')
    acotar.append('Autumn')
    hogwarts.append('Ravenclaw')
if q2 == 6:
    m_pjo.append('Hades')
    m_pjo.append('Hypnos')
    m_pjo.append('Hecate')
    m_pjo.append('Artemis')
    acotar.append('Night')
    acotar.append('Autumn')
    hogwarts.append('Ravenclaw')
if q2 == 6:
    m_pjo.append('Hades')
    m_pjo.append('Hypnos')
    m_pjo.append('Hecate')
    m_pjo.append('Artemis')
    m_pjo.append('Artemis')
    acotar.append('Night')
    acotar.append('Autumn')
    hogwarts.append('Ravenclaw')
if q2 == 7:
    m_pjo.append('Hades')
    m_pjo.append('Hades')
    m_pjo.append('Hypnos')
    m_pjo.append('Hecate')
    m_pjo.append('Hecate')
    m_pjo.append('Artemis')
    m_pjo.append('Artemis')
    acotar.append('Night')
    acotar.append('Night')
    acotar.append('Night')
    acotar.append('Winter')
    hogwarts.append('Ravenclaw')
    hogwarts.append('slytherin')

else:
    print("Please select a proper number.")

pjo_temp = [wrd for sub in pjo for wrd in sub.split()]
pjo_res = mode(pjo_temp)
m_pjo_temp = [wrd for sub in m_pjo for wrd in sub.split()]
m_pjo_res = mode(m_pjo_temp)
court_temp = [wrd for sub in acotar for wrd in sub.split()]
court_res = mode(court_temp)
house_temp = [wrd for sub in hogwarts for wrd in sub.split()]
house_res = mode(house_temp)

print('Your godly parent is:', pjo_res)
print('Your minor godly parent is:', m_pjo_res)
print('Your court is: the', court_res, 'Court')
print('Your Hogwarts house is:', house_res)
