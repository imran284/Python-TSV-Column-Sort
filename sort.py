def extract_sort_last_column(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        
    # remove header
    if lines[0].startswith("#"):
        lines = lines[1:]
        
    # extract last column
    last_column = [line.strip().split("\t")[-1] for line in lines]
    
    # sort values
    last_column.sort()
    
    # print values
    for value in last_column:
        print(value)
        
if __name__ == "__main__":
    file_path = input("Enter the path to the TSV file: ")
    extract_sort_last_column(file_path)
