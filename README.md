# FASTA-Sorter-Utility
FASTA File Sorter
Description
This Python script reads, sorts, and writes FASTA files. It takes an input FASTA file, sorts the sequences by length in descending order, and writes the sorted sequences to an output FASTA file. Each sequence in the output file is formatted with a maximum line length of 80 characters.

Features
Reads FASTA files and extracts sequences.
Sorts sequences by length in descending order.
Formats and writes sequences to an output FASTA file.
Command-line interface for easy usage.
Requirements
Python 3.12.0 or later
Installation
No installation is required. You only need to have Python 3.12.0 or later installed on your system.

Usage
To use the script, run the following command from your terminal:

bash
Copy code
python3 R11896961_assignment_1.py -i <input_file> -o <output_file>
Arguments
-i <input_file>: Path to the input FASTA file.
-o <output_file>: Path to the output FASTA file where sorted sequences will be saved.
Example
bash
Copy code
python3 R11896961_assignment_1.py -i input.fasta -o sorted_output.fasta
Notes
Ensure that the input file exists and the specified output directory is valid.
The output file will be created or overwritten if it already exists.
Sequences in the output file will be wrapped at 80 characters per line.
Author
bhgandha (R11896961)
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Thanks to the contributors and users of the Python community.
