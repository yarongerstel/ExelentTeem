"""
Pandas Assignment

- add proper documentation for each function
- implement all the missing methods
- please follow pep8 conventions https://www.python.org/dev/peps/pep-0008/
"""
import pandas as pd
import typing
import os.path


class SalariesParserError(Exception):
    def __init__(self, message):
        self.message = message


class SalariesParser:

    def __init__(self, csv_file_path):
        try:
            self._csv_file_path = csv_file_path
            self._is_file_exists()
            # TODO: add a block of code that will try to read the provided csv file with pandas
            # wrap the read process with a try-except block
            # except 'pandas.errors.ParserError'
            # if such error occur the __init__ function should fail and raise a custom exception created by you
            # named SalariesParserError
            self._file = pd.read_csv(csv_file_path)
        except pd.errors.ParserError:
            raise SalariesParserError("Oops! Failed to open file")

    # TODO: write a function that will check if the provided file exists
    # if not it will raise an exception of FileNotFound
    def _is_file_exists(self):
        """
        :return: if is file exists return True else:
        :raises: FileNotFound
        """

        if not os.path.exists(self._csv_file_path):
            raise NameError('File Not Found')
        return True

    # TODO: return a dataframe holding the data from the csv file provided in the __init__ function
    def get_as_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self._file)

    # TODO: return a dataframe holding data of first 10 rows
    def get_top(self) -> pd.DataFrame:
        return pd.DataFrame(self._file).head(10)

    # TODO: return the avg of base payment ?
    def get_average_of_base_pay(self) -> float:
        return self._file["BasePay"].dropna().mean()

    # TODO: return the biggest amount of over time payment
    def get_max_over_time_pay(self) -> float:
        return self._file["OvertimePay"].max()

    # TODO: return the job title according to the provided name
    # if an employee with a matching name is not found return 'N/A'
    # the function should be compatible with lower & upper case, meaning looking for edward should return
    # the function should be case sensitive (looking for edward won't produce same results as looking for EDWARD)
    # the returned item should be a series object
    # for example:
    # if the provided name will be equal to: "GARY JIMENEZ"
    # the output of the function will be the following series:
    #   1    CAPTAIN III (POLICE DEPARTMENT)
    #   Name: JobTitle, dtype: object
    def get_job_title_by_name(self, name: str) -> pd.Series:
        return self._file[self._file.EmployeeName == name]['JobTitle']

    # TODO:  get the name of the most expensive employee
    def get_most_expensive_employee(self) -> str:
        return dict(self._file[self._file.TotalPay == self._file.TotalPay.max()].loc[0])["EmployeeName"]

    def get_salaries_by_year_series(self) -> pd.Series:
        # a = self._file[self._file["Year"] > 2010]
        # b = self._file[self._file["Year"] < 2015]
        # return pd.concat([a, b], axis=0)["BasePay"].dropna().mean()
        return self._file.loc[self._file['Year'].isin(range(2011, 2015))].groupby(["Year"]).mean()['BasePay']


# project euler question
# https://projecteuler.net/problem=25
# implement a fibonacci generator function
# the function should yield numbers where last yielded item will be the item with the position of max_index
# for max_index = 12, the last value of the generator should be 12
def fibonacci_generator(max_index: int) -> typing.Generator:
    """

    :param max_index:
    :return: typing.Generator
    """
    a, b, n = 0, 1, 1
    for _ in range(max_index):
        yield n
        n = a + b
        a = b
        b = n


if __name__ == '__main__':
    my_file = r"C:\Users\USER001\PycharmProjects\targil_7\Salaries.csv"
    salaries_parser = SalariesParser(csv_file_path=my_file)
    print(f'Salaries DataFrame: {salaries_parser.get_as_dataframe()}')
    print(f'top 10: {salaries_parser.get_top()}')
    print(f'average base pay: {salaries_parser.get_average_of_base_pay()}\n')
    print(f'max over time pay: {salaries_parser.get_max_over_time_pay()}\n')
    name = 'GARY JIMENEZ'
    print(f'{name} job title: {salaries_parser.get_job_title_by_name(name=name)}\n')
    print(f'most expensive employee:{salaries_parser.get_most_expensive_employee()}\n')
    print(f'salaries aggregated by year: {salaries_parser.get_salaries_by_year_series()}\n')
    for nex in fibonacci_generator(2):
        print(nex)
