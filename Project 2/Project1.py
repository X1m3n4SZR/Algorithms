import itertools

def parse_set(line):
    # Example line: "A = {1, 2, 3}"
    start = line.find('{') + 1
    end = line.find('}')
    elements = line[start:end].split(',')
    return set(e.strip() for e in elements if e.strip())

def power_set(s):
    # Returns the power set as a list of sets
    ps = []
    for r in range(len(s) + 1):
        for combo in itertools.combinations(s, r):
            ps.append(set(combo))
    return ps

def format_set(s):
    return '{' + ', '.join(str(x) for x in sorted(s)) + '}'

def format_power_set(ps):
    return '{' + ', '.join(format_set(subset) for subset in ps) + '}'

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    # Read input sets from file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    A = parse_set(lines[0])
    B = parse_set(lines[1])

    # Perform set operations
    union = A | B
    intersection = A & B
    cartesian = {(a, b) for a in A for b in B}
    sym_diff = A ^ B
    pset = power_set(A)

    # Prepare output
    results = []
    results.append(f"A ∪ B = {format_set(union)}")
    results.append(f"A ∩ B = {format_set(intersection)}")
    results.append(f"A × B = {cartesian}")
    results.append(f"A ⊕ B = {format_set(sym_diff)}")
    results.append(f"𝒫(A) = {format_power_set(pset)}")

    output_text = '\n'.join(results)

    # Print to console
    print(output_text)

    # Write to file
    with open(output_file, 'w') as f:
        f.write(output_text)

if __name__ == "__main__":
    main()
