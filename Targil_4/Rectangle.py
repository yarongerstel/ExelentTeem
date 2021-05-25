import random


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return f'({self._x},{self._y})'


class Rectangle:

    def __init__(self, start_point=(0, 1), end_point=(1, 0)):
        # בודק אם הנקודות שהוכנסו הוכנסו בצורה הגיונית.
        # *המחלקה עובדת על ערך מוחלט ולכן היה עובד גם הפוך, אבל עדיין מונע להמשיך אם הוכנס ערכים לא נכונים
        while start_point[0] >= end_point[0] or start_point[1] <= end_point[1]:
            print("Error! the point not in the right order! the Rectangle don't was build")
            start_point = input("input the start_point:\t like:0, 0\t:")
            end_point = input("input the end_point:\t like:0, 0\t:")
            start_point = (start_point[0], start_point[-1])
            end_point = (end_point[0], end_point[-1])
        else:
            p = Point(start_point[0], start_point[1])
            p2 = Point(end_point[0],end_point[1])
            self._start_point = p
            self._end_point = p2

    def get_width(self):
        if abs(self._start_point.get_x()) >= abs(self._end_point.get_x()):
            return self._start_point.get_x() - self._end_point.get_x()
        else:
            return self._end_point.get_x() - self._start_point.get_x()

    def get_height(self):
        if abs(self._start_point.get_y()) >= abs(self._end_point.get_y()):
            return self._start_point.get_y() - self._end_point.get_y()
        else:
            return self._end_point.get_y() - self._start_point.get_y()

    def get_surface(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return self.get_width() * 2 + self.get_height() * 2

    def randomize_start_point(self):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        p = Point(x, y)
        self._start_point = p

    def randomize_end_point(self):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        p = Point(x, y)
        self._end_point = p

    def __str__(self):
        return f'### Rectangle ###\n' \
               f'My Width:{self.get_width()}\n' \
               f'My Height:{self.get_height()}\n' \
               f'My Surface:{self.get_surface()}\n' \
               f'My Perimeter:{self.get_perimeter()}\n'

    @staticmethod
    def filter_by_size(lis, surface):
        new_list = []
        for i in lis:
            if i.get_surface() >= surface:
                new_list.append(i)
        return new_list

    @staticmethod
    def filter_by_perimeter(lis, perimeter):
        new_list = []
        for i in lis:
            if i.get_surface() >= perimeter:
                new_list.append(i)
        return new_list

    @classmethod
    def rand_rects(cls):
        num = random.randint(1, 50)
        lis = []
        for i in range(num):
            temp = Rectangle()
            temp.randomize_start_point()
            temp.randomize_end_point()
            # בודק אם הנקודות שהוכנסו הוכנסו בצורה הגיונית.
            if temp._start_point.get_x() < temp._end_point.get_x() or\
                    temp._start_point.get_y() > temp._end_point.get_y():
                lis.append(temp)
        lis = Rectangle.filter_by_perimeter(lis, 30)
        lis = Rectangle.filter_by_size(lis, 900)
        for i in lis:
            print(i)


def main():
    Rectangle.rand_rects()


if __name__ == main():
    main()
