import datatable
# import xlrd


class ParameterClass:

    def __init__(self):
        ParameterClass()


if __name__ == '__main__':
    # parameterClass = ParameterClass()
    # print(parameterClass)

    # url = "https://raw.githubusercontent.com/Rdatatable/data.table/master/vignettes/flights14.csv"
    datatable.fread('lookup_file/flights14.csv')

    # df = datatable.fread('lookup_files/gf3defs_sorted.xlsx')
    # print(df)


#         load('gf3def.mat', 'gf3LIST');
#
#         %find
#         corresponding
#         code, set
#         defaults.
#         for i = 1:length(gf3LIST)
#         if strcmpi(code, gf3LIST{i}.code) == 1
#         E.code = gf3LIST
#         {i}.code;
#         E.desc = gf3LIST
#         {i}.desc;
#         E.units = gf3LIST
#         {i}.units;
#         E.fieldwidth = gf3LIST
#         {i}.fieldwidth;
#         E.decimalplaces = gf3LIST
#         {i}.decimalplaces;
#
#     end
#
#
# end
#
# clear
# gf3LIST;
