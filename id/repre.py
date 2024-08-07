import sys

def get_args():
    # Assuming arguments are passed via command-line
    if len(sys.argv) > 1:
        # Return all command-line arguments excluding the script name (sys.argv[0])
        return sys.argv[1:]
    else:
        # Return default arguments or an empty list if no arguments are provided
        return []

# Example usage:
arguments = get_args()
print("Arguments provided:", arguments)
