import logging

# Set up logging
log_file_path = "/home/egleg/uni_test/stp_tutorials/STP_Tutorials/modules/logs/app.log"

logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

codon_dict = {
    "AAA": "K", "AAC": "N", "AAG": "K", "AAU": "N",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
    "AGA": "R", "AGC": "S", "AGG": "R", "AGU": "S",
    "AUA": "I", "AUC": "I", "AUG": "M", "AUU": "I",

    "CAA": "Q", "CAC": "H", "CAG": "Q", "CAU": "H",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
    "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",

    "GAA": "E", "GAC": "D", "GAG": "E", "GAU": "D",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGU": "G",
    "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",

    "UAA": "*", "UAC": "Y", "UAG": "*", "UAU": "Y",
    "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
    "UGA": "*", "UGC": "C", "UGG": "W", "UGU": "C",
    "UUA": "L", "UUC": "F", "UUG": "L", "UUU": "F"
}


def dna_to_rna(dna_seq):
    """Convert DNA sequence to RNA by replacing T with U."""
    return dna_seq.replace('T', 'U')

def split_into_codons(seq, chunk_size=3):
    """Split the sequence into codons and log the chunking."""
    return [seq[i:i+chunk_size] for i in range(0, len(seq), chunk_size)]

def translate_codons(codons):
    """Translate a list of codons into their respective amino acids."""
    return ''.join([codon_dict.get(codon, '?') for codon in codons])

def Translate(input_seq):
    rna_seq = dna_to_rna(input_seq)
    codons = split_into_codons(rna_seq)  # default chunk size is 3, but you can adjust it
    return translate_codons(codons)

def main():
    try:
        input_seq = 'ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAA'
        logging.info('2.2: ' + Translate(input_seq))
    except Exception as e:
        logging.error(f"2.2: An error occurred: {e}")

if __name__ == "__main__":
    main()