import logging

# Setting up the logger
log_file_path = "/home/egleg/uni_test/stp_tutorials/STP_Tutorials/modules/logs/app.log"
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_file_path)

# Find the complement for a given sequence
def get_complement(seq):
    complement_dict = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return "".join(complement_dict.get(base, base) for base in seq.upper())

# Reverse the complemented sequence
def reverse_string(seq):
    return seq[::-1]

# Main execution
if __name__ == "__main__":
    sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    
    try:
        complemented_seq = get_complement(sequence)
        output = reverse_string(complemented_seq)
        logging.info(output)
    except Exception as e:
        logging.error(f"Error occurred: {e}")


