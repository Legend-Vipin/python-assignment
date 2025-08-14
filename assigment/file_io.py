# file_io.py
# Examples of File Input and Output operations in Python

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Content written to {filename}")

def read_from_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    print(f"Content read from {filename}:")
    print(data)

if __name__ == "__main__":
    filename = "example.txt"
    content = "Hello, this is a sample text file.\nThis demonstrates file I/O in Python."
    
    write_to_file(filename, content)
    read_from_file(filename)
