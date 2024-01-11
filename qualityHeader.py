import odfUtils


class QualityHeader:
    """
    A class to represent a Quality Header in an ODF object.

    Attributes:
    -----------
    QualityDate : string
        the date time when the Quality Header was added to the ODF object
    QualityTests : list of strings
        list of quality control tests run on the ODF object's data
    QualityTests : list of strings
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
        self.QualityDate = None
        self.QualityTests = list()
        self.QualityComments = list()

    def get_quality_date(self):
        return self.QualityDate

    def set_quality_date(self, quality_date: str):
        self.QualityDate = quality_date
        return self

    def get_quality_tests(self):
        return self.QualityTests

    def set_quality_tests(self, quality_test: str, test_number: int):
        number_of_tests = len(self.QualityTests)
        if test_number == 0 and number_of_tests >= 0:
            self.QualityTests.append(quality_test)
        elif test_number <= number_of_tests and number_of_tests > 0:
            self.QualityTests[test_number] = quality_test
        else:
            raise ValueError("The 'quality_test' number does not match the number of QUALITY_TESTS lines.")
        return self

    def add_quality_tests(self, quality_test: str):
        self.QualityTests.append(quality_test)
        return self

    def get_quality_comments(self):
        return self.QualityComments

    def set_quality_comments(self, quality_comment: str, comment_number: int = 0):
        number_of_comments = len(self.QualityComments)
        if comment_number == 0 and number_of_comments >= 0:
            self.QualityComments.append(quality_comment)
        elif comment_number <= number_of_comments and number_of_comments > 0:
            self.QualityComments[comment_number] = quality_comment
        else:
            raise ValueError("The 'quality_comment' number does not match the number of QUALITY_COMMENTS lines.")
        return self

    def add_quality_comments(self, quality_comment):
        self.QualityComments.append(quality_comment)
        return self

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
                        self.add_quality_tests(value)
                    case 'QUALITY_COMMENTS':
                        self.add_quality_comments(value)

    def print_object(self) -> str:
        quality_header_output = "QUALITY_HEADER\n"
        quality_header_output += f"  QUALITY_DATE = {odfUtils.check_string(self.QualityDate)}\n"
        for quality_test in self.QualityTests:
            quality_header_output += f"  QUALITY_TESTS = {quality_test}\n"
        for quality_comment in self.QualityComments:
            quality_header_output += f"  QUALITY_COMMENTS = {quality_comment}\n"
        return quality_header_output
