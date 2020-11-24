def uniq(sequence):
    have = set()
    output_sequence = []
    for elem in sequence:
        if elem not in have:
            output_sequence.append(elem)
            have.add(elem)
    return output_sequence

input_sequence = [5, 2, 3, 5, 6, 2, 11, 2, 9, 100, 1, 100]

output_sequence = uniq(input_sequence)

print('the output is ...')
for elem in output_sequence:
    print(elem)

# output_sequence = [5, 2, 3, 6, 11, 9, 100, 1]

