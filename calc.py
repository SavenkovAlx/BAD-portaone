class Calculation():
    def __init__(self, arr=[]):
        self.numbers = arr
        self.length = len(self.numbers)

    def max_number(self):
        num = self.numbers[0]
        for i in self.numbers:
            if num < i:
                num = i
        return num

    def min_number(self):
        num = self.numbers[0]
        for i in self.numbers:
            if num > i:
                num = i
        return num

    def median(self):
        sort_num = sorted(self.numbers)
        if self.length % 2 != 0:
            return round(sort_num[self.length//2], 1)
        else:
            return round((sort_num[self.length//2] + sort_num[self.length//2 - 1]) * 0.5, 1)

    def average(self):
        sum = 0
        for i in self.numbers:
            sum += i
        return round(sum / self.length, 1)

    def ascending_sequence(self):
        new_list = [self.numbers[0], ]
        temporary_list = [self.numbers[0], ]
        current_num = self.numbers[0]
        for i in self.numbers[1:]:
            if i > current_num:
                temporary_list.append(i)
                current_num = i
            else:
                if len(temporary_list) > len(new_list):
                    new_list = [x for x in temporary_list]
                current_num = i
                temporary_list = [current_num, ]
        return new_list

    def descending_sequence(self):
        new_list = [self.numbers[0], ]
        temporary_list = [self.numbers[0], ]
        current_num = self.numbers[0]
        for i in self.numbers[1:]:
            if i < current_num:
                temporary_list.append(i)
                current_num = i
            else:
                if len(temporary_list) > len(new_list):
                    new_list = [x for x in temporary_list]
                current_num = i
                temporary_list = [current_num, ]
        return new_list
