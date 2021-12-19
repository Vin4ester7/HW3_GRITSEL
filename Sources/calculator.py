class calculator:
    def init(self):
        pass

    def maximum(self, list):
        max = list[0]
        for number in list:
            if number > max:
                max = number
        return max

    def minimum(self, list):

        min = list[0]

        for number in list:
            if number < min:
                min = number
        return min

    def sum_numbers(self, list):

        sum = 0

        for number in list:
            sum += number
        return sum

    def multiplication_numbers(self, list):

        multiplication = 1

        for number in list:
            multiplication *= number
        return multiplication
