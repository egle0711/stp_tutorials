import logging

# Setting up the logger
log_file_path = "/home/egleg/uni_test/stp_tutorials/STP_Tutorials/modules/logs/app.log"
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=log_file_path)

# Format sequence in GenBank style
def genbank_format(dna_sequence, block_size=10, blocks_per_row=6):
    try:
        dna_sequence = dna_sequence.upper()
        blocks = [dna_sequence[i:i + block_size] for i in range(0, len(dna_sequence), block_size)]
        position = 1
        formatted_sequence = ''
        
        for i in range(0, len(blocks), blocks_per_row):
            row_blocks = blocks[i:i + blocks_per_row]
            formatted_row = ' '.join(row_blocks)
            formatted_sequence += f"{position: >9} {formatted_row}\n"
            position += block_size * blocks_per_row
            
        logging.info(f"2.1: Formatted sequence in GenBank style:\n{formatted_sequence}")
        print(formatted_sequence)
        return formatted_sequence
        
    except Exception as e:
        logging.error(f"2.1: Error occurred: {e}")
        return None

# Main execution
if __name__ == "__main__":
    sequence = (
        "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC"
        "CTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAA"
        "GAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGG"
        "AACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAA"
        "AGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTT"
        "AGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAA"
        "ACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCA"
        "AAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAA"
        "ACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAAC"
        "CTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTA"
        "TTGCAGTGTGGGAGATCAAG"
    )
    
    try:
        formatted_sequence = genbank_format(sequence)
    except Exception as e:
        logging.error(f"2.1: Error occurred: {e}")
