import logging

# Configure logging
logging.basicConfig(filename='/home/egleg/uni_test/stp_tutorials/STP_Tutorials/modules/logs/app.log', level=logging.INFO)

def gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    total_count = len(sequence)
    
    if total_count == 0:
        gc_content_percentage = 0.0  # Handle empty sequences
    else:
        gc_content_percentage = (gc_count / total_count) * 100
        gc_content_percentage = round(gc_content_percentage, 2)  # Round to 2 decimal places

    logging.info(f"The GC content is {gc_content_percentage}%")

sequence = "aggagtaagcccttgcaactggaaatacacccattg"
gc_content(sequence)
