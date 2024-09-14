import argparse
import os

def User_arg():
    parser = argparse.ArgumentParser(description='FASTA Sorter')
    parser.add_argument('-i', type=str, required=True)
    parser.add_argument('-o', type=str, required=True)
    args = parser.parse_args()

    if not os.path.isfile(args.i):
        raise FileNotFoundError("Error: File not found")
    
    output_dir = os.path.dirname(args.o)

    if output_dir and not os.path.isdir(output_dir):
        raise NotADirectoryError("Error: Directory not found")
    
    return args

def Sequence_read(file_path):

    sequences = []

    with open(file_path, 'r') as file:
        header = None
        sequence = ""
        
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    sequences.append((header, sequence))
                header = line
                sequence = ""
            else:
                sequence += line
        
        if header:
            sequences.append((header, sequence))
    
    return sequences

def Sequence_sort(sequences):
    return sorted(sequences, key=lambda x: len(x[1]), reverse=True)

def Sequence_write(file_path, sequences):
    with open(file_path, 'w') as file:
        for header, sequence in sequences:
            file.write(f"{header}\n")
            for i in range(0, len(sequence), 80):
                file.write(f"{sequence[i:i+80]}\n")

def main():
    args = User_arg()
    sequences = Sequence_read(args.i)
    sorted_sequences = Sequence_sort(sequences)
    Sequence_write(args.o, sorted_sequences)
    print("Completed")

if __name__ == "__main__":
    main()
