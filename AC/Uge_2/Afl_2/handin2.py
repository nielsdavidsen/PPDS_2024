beatles_container1 = [("Paul McCartney", "bass guitar"), ("John Lennon", "rhythm guitar"), ("George Harrison", "lead guitar"), ("Ringo Starr", "drums")]

beatles_container2 = {beatles_container1[0][0]: beatles_container1[0][1], beatles_container1[1][0]: beatles_container1[1][1], beatles_container1[2][0]: beatles_container1[2][1], beatles_container1[3][0]: beatles_container1[3][1]}


def beatle_lookup(name):

    beatles_container1 = (("Paul McCartney", "bass guitar"), ("John Lennon", "rhythm guitar"), ("George Harrison", "lead guitar"), ("Ringo Starr", "drums"))

    beatles_container2 = {beatles_container1[0][0]: beatles_container1[0][1], beatles_container1[1][0]: beatles_container1[1][1], beatles_container1[2][0]: beatles_container1[2][1], beatles_container1[3][0]: beatles_container1[3][1]}

    if name not in beatles_container2:

        return f"ERROR. Name '{name}' not found. Available names: {list(beatles_container2.keys())}"

    else:

        return beatles_container2[name]



print(beatle_lookup("John Lennon"))
print(beatle_lookup("Mick Jagger"))