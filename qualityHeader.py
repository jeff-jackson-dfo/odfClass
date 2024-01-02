import misc_functions


class QualityHeader:
    def __init__(self):
        self.QualityDate = None
        self.QualityTests = list()
        self.QualityComments = list()

    def get_quality_date(self):
        print("Getting the Quality Date ...")
        return self.QualityDate

    def set_quality_date(self, odf, quality_date):
        nh = len(odf.HistoryHeader)
        odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: QUALITY_DATE for this ODF object has been "
                                                 "modified from '" +
                                                 misc_functions.check_datetime(self.QualityDate) + "' to '" +
                                                 quality_date + "'.")
        self.QualityDate = quality_date
        return odf

    def get_quality_tests(self):
        print("Getting the Quality Tests ...")
        return self.QualityTests

    def set_quality_tests(self, odf, quality_test, test_number):
        nh = len(odf.HistoryHeader)
        tn = test_number - 1
        odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Comment [" + str(test_number) + "] in " +
                                                 "QUALITY_TESTS for this ODF object has been modified from '" +
                                                 misc_functions.check_string(self.QualityTests[tn]) + "' to '" +
                                                 quality_test + "'.")
        self.QualityTests[tn] = quality_test
        return odf

    def get_quality_comments(self):
        print("Getting the Quality Comments ...")
        return self.QualityComments

    def set_quality_comments(self, odf, quality_comment, comment_number):
        nh = len(odf.HistoryHeader)
        qn = comment_number - 1
        odf.HistoryHeader[nh - 1].Process.append("QUALITY_HEADER Update: Comment [" + str(comment_number) + "] in " +
                                                 "QUALITY_COMMENTS for this ODF object has been modified from '" +
                                                 misc_functions.check_string(self.QualityComments[qn]) + "' to '" +
                                                 quality_comment + "'.")
        self.QualityComments[qn] = quality_comment
        return odf

    def print_header(self):
        print("QUALITY_HEADER")
        print("  QUALITY_DATE = '" + misc_functions.check_string(self.QualityDate) + "'")
        for quality_test in self.QualityTests:
            print("  QUALITY_TESTS = '" + quality_test)
        for quality_comment in self.QualityComments:
            print("  QUALITY_COMMENTS = '" + quality_comment)
