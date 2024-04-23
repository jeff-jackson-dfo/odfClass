import odfUtils


class QualityHeader:
    """
    A class to represent a Quality Header in an ODF object.

    Attributes:
    -----------
    _quality_date : string
        the date time when the Quality Header was added to the ODF object
    _quality_tests : list of strings
        list of quality control tests run on the ODF object's data
    _quality_comments : list of strings
        list of comments regarding the quality control carried out on the ODF object's data

    Methods:
    -------
    __init__ :
        initialize a QualityHeader class object
    get_quality_date : string
    set_quality_date : None
    get_quality_tests : list of strings
    set_quality_tests : None
    add_quality_tests : None
    get_quality_comments : list of strings
    set_quality_comments : None
    add_quality_comments : None

    """

    def __init__(self):
        self._quality_date = None
        self._quality_tests = []
        self._quality_comments = []

    def get_quality_date(self):
        return self._quality_date

    def set_quality_date(self, quality_date: str) -> None:
        self._quality_date = quality_date

    def get_quality_tests(self):
        return self._quality_tests

    def set_quality_tests(self, quality_test: str, test_number: int = 0) -> None:
        number_of_tests = len(self.get_quality_tests())
        if test_number == 0 and number_of_tests >= 0:
            self._quality_tests.append(quality_test)
        elif test_number <= number_of_tests and number_of_tests > 0:
            self._quality_tests[test_number] = quality_test
        else:
            raise ValueError("The 'quality_test' number does not match the number of QUALITY_TESTS lines.")

    def get_quality_comments(self):
        return self._quality_comments

    def set_quality_comments(self, quality_comment: str, comment_number: int = 0) -> None:
        number_of_comments = len(self.get_quality_comments())
        if comment_number == 0 and number_of_comments >= 0:
            self._quality_comments.append(quality_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self._quality_comments[comment_number] = quality_comment
        else:
            raise ValueError("The 'quality_comment' number does not match the number of QUALITY_COMMENTS lines.")

    def populate_object(self, quality_fields: list):
        for header_line in quality_fields:
            tokens = header_line.split('=', maxsplit=1)
            quality_dict = odfUtils.list_to_dict(tokens)
            for key, value in quality_dict.items():
                key = key.strip()
                value = value.strip()
                match key:
                    case 'QUALITY_DATE':
                        self.set_quality_date(value)
                    case 'QUALITY_TESTS':
                        self.set_quality_tests(value)
                    case 'QUALITY_COMMENTS':
                        self.set_quality_comments(value)

    def print_object(self) -> str:
        quality_header_output = "QUALITY_HEADER\n"
        quality_header_output += f"  QUALITY_DATE = {odfUtils.check_string(self.get_quality_date())}\n"
        for quality_test in self.get_quality_tests():
            quality_header_output += f"  QUALITY_TESTS = {quality_test}\n"
        for quality_comment in self.get_quality_comments():
            quality_header_output += f"  QUALITY_COMMENTS = {quality_comment}\n"
        return quality_header_output
