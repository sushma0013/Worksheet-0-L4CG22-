def generate_permutations(s):

    if len(s) == 1:
        return [s]

 
    permutations = []
    for i, char in enumerate(s):
     
        remaining_chars = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining_chars):
            permutations.append(char + perm)

    return permutations


print(generate_permutations("abc"))


        
