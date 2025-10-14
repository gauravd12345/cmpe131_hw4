from cacti import cacti_number

def main():
    plot = [ [1, 0, 1, 0, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0] ]
    
    print(cacti_number(plot))

    plot = [ [0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 0, 1] ]
    
    print(cacti_number(plot))

main()