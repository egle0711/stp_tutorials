import logging

# Set up logging
log_file_path = "/home/egleg/uni_test/stp_tutorials/STP_Tutorials/modules/logs/app.log"

logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

def print_sequence_in_blocks(seq, block_size):
    """Divide a sequence into blocks of a given size and join them with spaces."""
    try:
        blocks = [seq[i:i + block_size] for i in range(0, len(seq), block_size)]
        formatted_sequence = ' '.join(blocks)
        logging.info(f"1.4: Formatted sequence: {formatted_sequence}")
        return formatted_sequence
    except Exception as e:
        logging.error(f"1.4: An error occurred: {e}")
        return None

def main():
    try:
        sequence = "aggagtaagcccttgcaactggaaatacacccattg"
        block_size = 3
        formatted_sequence = print_sequence_in_blocks(sequence, block_size)
        print(formatted_sequence)
    except Exception as e:
        logging.error(f"An error occurred in main: {e}")

if __name__ == "__main__":
    main()
