beatles_container1 = [('Paul McCartney', 'bass guitar'), 
                      ('John Lennon', 'rhythm guitar'), 
                      ('George Harrison', 'lead guitar'), 
                      ('Ringo Starr', 'drums')] 

beatles_container2 = {'Paul McCartney': 'bass guitar',
                      'John Lennon': 'rhythm guitar',
                      'George Harrison': 'lead guitar',
                      'Ringo Starr': 'drums'}

print(beatles_container2['Ringo Starr'])



def beatle_lookup(name):
    '''Takes a name from The Beatles as input and returns the instrument played by that person in The Beatles. If a name of '''
    beatles_container2 = {'Paul McCartney': 'bass guitar',
                      'John Lennon': 'rhythm guitar',
                      'George Harrison': 'lead guitar',
                      'Ringo Starr': 'drums'}
    
    beatle_names = list(beatles_container2.keys())
    

    if name not in beatles_container2:
        return f"ERROR. Name '{name}' not found. Available names: {beatle_names}"
    else:
        return beatles_container2[name]
    

print(beatle_lookup('John Lennon'))
print(beatle_lookup('Mick Jagger'))
