# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self,week_number:int, constructor:list):
        self.week_number=week_number
        self.constructor = constructor

    def number_of_hits(self,numbers:list):
        return len([number  for number in numbers if number in self.constructor])

    def hits_in_place(self, numbers):
        return [number if number in self.constructor else -1 for number in numbers]

if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))
