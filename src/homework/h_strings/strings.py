#get_hamming_distance and get_dna_complement

def get_hamming_distance(dna1, dna2): #string parameter 1 and string parameter 2

    Lan = len(dna1)

    distance = 0 #start with the o position and count up

    for i in range(Lan):
        if dna1[i] != dna2[i]: #if the two chars are not equal, add 1 to distance
            distance += 1

    return distance
    
def get_dna_complement(dna):

    #make each complement reverse
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    reverse_complement = ""

    #use for loop to reverse each index in dna
    for index in range(0, len(dna)):
        base = dna[index]
        reverse_complement += complement[base]

    #reverse sequence
    result_complement = reverse_complement[::-1]

    return result_complement
    
