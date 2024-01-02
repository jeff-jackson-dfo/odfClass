import misc_functions


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
        print("Getting the Quality Date ...")
        return self.QualityDate

    def set_quality_date(self, odf, quality_date):
        nh = len(odf.HistoryHeader)
        if self.QualityDate is None:
            quality_date = misc_functions.get_current_date_time()
        odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: QUALITY_DATE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_datetime(self.QualityDate) + "' to '" +
                                                 quality_date + "'")
        self.QualityDate = quality_date
        return odf

    def get_quality_tests(self):
        print("Getting the Quality Tests ...")
        return self.QualityTests

    def set_quality_tests(self, odf, quality_test, test_number):
        nh = len(odf.HistoryHeader)
        ntests = len(self.QualityTests)
        if test_number <= 0 or test_number > ntests + 1:
            raise Exception("Input argument 'test_number' is outside the number of Quality Test lines.")
        elif test_number == 1:
            tn = 0
            odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(test_number) + "] in " +
                                                     "QUALITY_TESTS for this ODF object has been modified from ''" +
                                                     " to '" + quality_test + "'")
            self.QualityTests.append(quality_test)
        elif test_number > ntests + 1:
            tn = test_number - 1
            odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(test_number) + "] in " +
                                                     "QUALITY_TESTS for this ODF object has been modified from '" +
                                                     misc_functions.check_string(self.QualityTests[tn]) + "' to '" +
                                                     quality_test + "'")
            self.QualityTests[tn] = quality_test
        else:
            tn = test_number - 1
            odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(test_number) + "] in " +
                                                     "QUALITY_TESTS for this ODF object has been modified from '" +
                                                     misc_functions.check_string(self.QualityTests[tn]) + "' to '" +
                                                     quality_test + "'")
            self.QualityTests[tn] = quality_test
        return odf

    def add_quality_tests(self, odf, quality_test):
        nh = len(odf.HistoryHeader)
        ntests = len(self.QualityTests)
        odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(ntests + 1) + "] in " +
                                                 "QUALITY_TESTS for this ODF object was added " +
                                                 "with following text: '" + quality_test + "'")
        self.QualityTests.append(quality_test)
        return odf

    def get_quality_comments(self):
        print("Getting the Quality Comments ...")
        return self.QualityComments

    def set_quality_comments(self, odf, quality_comment, comment_number):
        nh = len(odf.HistoryHeader)
        ncomments = len(self.QualityComments)
        if comment_number <= 0 or comment_number > ncomments + 1:
            raise Exception("Input argument 'comment_number' is outside the number of Quality Test lines.")
        elif comment_number == 1:
            tn = 0
            odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(comment_number) + "] in " +
                                                     "QUALITY_COMMENTS for this ODF object has been modified from ''" +
                                                     " to '" + quality_comment + "'")
            self.QualityComments.append(quality_comment)
        elif comment_number > ncomments + 1:
            tn = comment_number - 1
            odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(comment_number) + "] in " +
                                                     "QUALITY_COMMENTS for this ODF object has been modified from '" +
                                                     misc_functions.check_string(self.QualityComments[tn]) + "' to '" +
                                                     quality_comment + "'")
            self.QualityComments[tn] = quality_comment
        else:
            tn = comment_number - 1
            odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(comment_number) + "] in " +
                                                     "QUALITY_COMMENTS for this ODF object has been modified from '" +
                                                     misc_functions.check_string(self.QualityComments[tn]) + "' to '" +
                                                     quality_comment + "'")
            self.QualityComments[tn] = quality_comment
        return odf

    def add_quality_comments(self, odf, quality_comment):
        nh = len(odf.HistoryHeader)
        ncomments = len(self.QualityComments)
        odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Line [" + str(ncomments + 1) + "] in " +
                                                 "QUALITY_COMMENTS for this ODF object was added " +
                                                 "with following text: '" + quality_comment + "'")
        self.QualityComments.append(quality_comment)
        return odf

    def print_header(self):
        print("QUALITY_HEADER")
        print("  QUALITY_DATE = '" + misc_functions.check_string(self.QualityDate) + "'")
        for quality_test in self.QualityTests:
            print("  QUALITY_TESTS = '" + quality_test + "'")
        for quality_comment in self.QualityComments:
            print("  QUALITY_COMMENTS = '" + quality_comment + "'")
