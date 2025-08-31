#Christopher Rhyan Poole
#CIS 261
#Rectangle


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return (self.height * self.width)

    def print_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("* " * self.width)
            else:
                print("* " + "  " * (self.width - 2) + "* ")

def main():
    print("Rectangle Calculator")
    while True:
        height = int(input("Height: "))
        width = int(input("Width: "))

        rect = Rectangle(height, width)

        print("Perimeter:", rect.get_perimeter())
        print("Area:", rect.get_area())
        rect.print_rectangle()

        cont = input("Continue? (y/n): ").lower()
        if cont != "y":
            break

if __name__ == "__main__":
    main()