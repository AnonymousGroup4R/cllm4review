import hashlib

def apply_sha1_hash(input_seq):
    # Apply SHA-1 hash for each string in the list
    output_seq = []
    for s in input_seq:
        hash_object = hashlib.sha1(s.encode())
        hashed_string = hash_object.hexdigest()
        output_seq.append(hashed_string)
    
    return output_seq

# Example usage
seq_a = ["Hello", "Python", "SHA-1 Hash"]
seq_b = apply_sha1_hash(seq_a)
print(seq_b)