""" Numpy Wrapper Utility module """
import numpy
import functools
import PIL
from skimage import io
import matplotlib.pyplot as plt


class ArrayWrapper:
    """Wrapp numpy 1-d array functionality class"""

    @staticmethod
    def create_array(array_size: int, integer_value: int) -> numpy.ndarray:
        """
        Create and Return an array according to the provided integer value:

        if -1 is provided,
            each integer should be generated as random numbers in the range of 0-1
            and be different from each other (look for methods located inside np.random)

        example:
            create_array(0)
            array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
            array([ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])
            array([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.])
            array([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.])
            create_array(1)

        :param array_size: the amount of elements in the array
        :param integer_value: desired value for each item of the array
        :return: an array of integers where every integer value is set to the provided integer value
        """
        if integer_value == -1:
            return numpy.random.rand(1, array_size)
        return numpy.linspace(integer_value, integer_value, array_size)

    @staticmethod
    def create_array_from_range(start_index, end_index, step=None):
        """
        Create and Return an array from start index till the end index with step delta between each two values
        if no step provided, delta should be equal to one
        example:
            create_array_from_range(10,51)
            array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                   44, 45, 46, 47, 48, 49, 50, 51])

            create_array_from_range(10,51,2)
            array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                   44, 45, 46, 47, 48, 49, 50, 51])

        :param start_index:
        :param end_index:
        :param step:
        :return: an array of integers starting from the start index until the end index included!
        the delta between to adjacent integers should be equal to the step size
        """

        return numpy.arange(start=start_index, stop=end_index, step=step)

    @staticmethod
    def reshape_if_possible(array: numpy.ndarray, new_shape: tuple) -> (numpy.ndarray, None):
        """
        Return a reshaped array according to the provided new shape if possible
        if not possible, return None
        :param array:
        :param new_shape:
        :return:
        """
        if array.size == functools.reduce(lambda x, y: x * y, new_shape):
            return array.reshape(new_shape)


class MatrixWrapper:

    def __init__(self, matrix: numpy.ndarray):
        """
        :param matrix:
        """
        self._matrix = matrix

    def get_only_positive_numbers(self):
        """
        Return the matrix with only positive values
        :return:the matrix with only positive values
        """
        return self._matrix[self._matrix >= 0]

    def get_negatives(self):
        """
        :return:the matrix with only negative values
        """
        return self._matrix[self._matrix < 0]

    def increase_values_by(self, integer_value):
        """
        Increase all values of the metrics by the provided integer value
        :param integer_value:
        :return:the matrix with all new values
        """
        return self._matrix + integer_value

    def get_column(self, column_index) -> numpy.ndarray:
        """
        Get column by index
        if the original metrix was
        array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
        and we call my_instance.get_column(column_index), the result should be:
        array([1, 4, 7])
        :return: arry of the number in specific columns
        """
        if self._matrix.shape[1] < column_index:
            print("You have exceeded the number of columns")
        else:
            return self._matrix[:, [column_index]]

    def get_row(self, row_index):
        """
        Get row by index
        :return:arry of the number in specific row
        """
        if self._matrix.shape[0] < row_index:
            print("You have exceeded the number of row")
        else:
            return self._matrix[[row_index], :]


class ImageProcessingWrapper:
    """
    In order to solve this exercise use matplot lib imread
    you can also use imshow for your own testing - don't forget to remove this before submitting the assignment
    """

    """
           Get an image path and return a numpy array representing one of the colors channel according to the
           provided arguments

           :param image_path: path to a local image
           :param color_flag: should be either 'R' 'G' or 'B', anything else will cause the function to return a
           None object
           :return: numpy.ndarray object representing the picture color channel (can be Red, Green or Blue)
           """

    @staticmethod
    def get_channel_by_color(image_path: str, color_flag: str) -> numpy.ndarray:
        picture = numpy.array(PIL.Image.open(image_path))
        img = picture.copy()
        if color_flag == 'G':
            img[:, :, (0, 2)] = 0  # reset the Other color
        elif color_flag == 'B':
            img[:, :, (0, 1)] = 0  # reset the Other color
        elif color_flag == 'R':
            img[:, :, (1, 2)] = 0  # reset the Other color
        return img

    """
            Get an image path and return a numpy array representing the image inverted upside down
            :param image_path: path to a local image
            :return: numpy.ndarray object representing the picture color channel (can be Red, Green or Blue)
            """

    @staticmethod
    def get_flipped_image_horizontally(image_path: str) -> numpy.ndarray:
        img = PIL.Image.open(image_path)
        return numpy.asarray(img.rotate(180))

    """
            Get an image path and return a numpy array representing the image where every color channel is swapped
            according to the swipe dict items
            for example:
            if swipe_dict == {'R': 'G'}:
                swipe the red channel with the green channel
            if swipe_dict == {'G': 'B', 'B': 'R'}
                swipe the blue channel with the red channel and the green channel with the blue channel

            if swipe dict is greater that 2 swipes, the function will return None
            the swipes should be executed according to the original image array
            :param image_path:
            :param swipe_dict:
            :return: arry of img whit swiped color
            """

    @staticmethod
    def get_swiped_color_channels(image_path: str, swipe_dict: dict):
        img = plt.imread(image_path)
        if len(swipe_dict) > 2:
            return None
        if len(swipe_dict) < 1:  # no change
            return numpy.asarray(img)
        # 1 or 2 swiped:
        order = {'R': 0, 'G': 1, 'B': 2}
        for element in swipe_dict.keys():  # change the val of the current key
            temp = order[element]
            order[element] = order[swipe_dict[element]]
            order[swipe_dict[element]] = temp
        new_order = []
        for index in order.values():  # fill the list in the index whit good order
            new_order.append(index)
        new_img = img[:, :, new_order]  # cheing the color according the order in the list
        return numpy.asarray(new_img)

    # Interview Question
    # Implement the following:
    # String Patterns
    # write a function that will receive two strings: src_str, dst_str
    # if there is a consistent mapping between both strings the function will return True
    # otherwise the function will return False
    # don't forget to add documentation
    # example usage:
    # mapped_strings(src_str="aba", dst_str="abc") -> return False
    # mapped_strings(src_str='tatsy', dst_str='pepbi') -> return True
    # make the solution as efficient as possible


def mapped_strings(src_str: str, dst_str: str) -> bool:
    # TODO: implement this
    src_dic = {}
    dst_dic = {}
    for i in range(len(src_str)):
        if src_str[i] in src_dic.keys():
            if src_dic[src_str[i]] != dst_str[i]:  # wrong char
                return False
        else:  # add new char key to the dict
            src_dic[src_str[i]] = dst_str[i]

        if dst_str[i] in dst_dic.keys():
            if dst_dic[dst_str[i]] != src_str[i]:  # wrong char
                return False
        else:
            dst_dic[dst_str[i]] = src_str[i]  # add new char key to the dict
    return True  # if not return yet False - return True
