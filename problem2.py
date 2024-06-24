#WAP to input side of a square & print its area.

def calculate_area_of_square(side_length):
    return side_length ** 2

if __name__ == "__main__":
    
    side_length = float(input('Enter the side value: '))
    
    area = calculate_area_of_square(side_length)
    
    print(f"The are of square is: {area}")