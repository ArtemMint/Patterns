class Number:

    def __init__(self):
        self.value = 1.89

    def get(self):
        return self.value

class String:

    def __init__(self):
        self.value = '123'

    def get(self):
        return self.value

class NumberToStringAdapter(Number):

    def get(self):
        return str(super().get())

def main():
    number = Number()
    string = String()
    num_to_str = NumberToStringAdapter()

    print('Return:' + string.get())
    #print('Return:' + number.get())
    print('Return:' + num_to_str.get())

if __name__ == '__main__':
    main()