import logging
from collections import Counter
from itertools import product

# Setting up the logger
log_file_path = "/home/egleg/uni_test/stp_tutorials/STP_Tutorials/modules/logs/app.log"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_file_path)

def count_nucleotides(sequence, n):
    return Counter([sequence[i:i + n] for i in range(len(sequence) - n + 1)])

def generate_possible_nucleotides(n, bases='ACGT'):
    return [''.join(p) for p in product(bases, repeat=n)]

def main():
    sequence = "aggagtaagcccttgcaactggaaatacacccattg"
    sequence = sequence.upper()

    # Single nucleotide count
    single_counts = count_nucleotides(sequence, 1)
    logging.info("Counts for 1-nucleotides:")
    print("Counts for 1-nucleotides:")
    for k, v in sorted(single_counts.items()):
        logging.info(f"{k} {v}")
        print(f"{k.lower()} {v}")

    print()
    logging.info('')

    # Di-nucleotide count
    di_counts = count_nucleotides(sequence, 2)
    logging.info("Counts for 2-nucleotides:")
    print("Counts for 2-nucleotides:")
    for k, v in sorted(di_counts.items()):
        logging.info(f"{k} {v}")
        print(f"{k.lower()} {v}")

    print()
    logging.info('')

    # Tri-nucleotide count
    tri_counts = count_nucleotides(sequence, 3)
    logging.info("Counts for 3-nucleotides:")
    print("Counts for 3-nucleotides:")
    for k, v in sorted(tri_counts.items()):
        logging.info(f"{k} {v}")
        print(f"{k.lower()} {v}")

if __name__ == "__main__":
    main()
