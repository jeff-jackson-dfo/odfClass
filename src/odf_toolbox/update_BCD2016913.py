import glob
import os

# Add path to project 'c:/dev/pythonProjects/odfClass/src/odf_toolbox' to Windows variable PYTHONPATH.
import odfHeader
import odfUtils

os.chdir("C:\\DEV\\EdHorne\\CTD\\Backlog\\bdor_2016_aug2017\\ODF\\")
path_to_orig = os.getcwd()
if not os.path.isdir(path_to_orig + '\\Update_Metadata'):
    os.mkdir('Update_Metadata')
path_to_revised = path_to_orig + '\\Update_Metadata'

# Change to folder containing files to be modified
os.chdir(path_to_orig)

# Find all ODF files in the current directory.
files = glob.glob('*.ODF')

# Query the user for his/her name so he/she may be identified in the
# history header as the responsible data quality control person.
user = input('Please enter the name of the analyst performing this data processing: ')
# user = 'Jeff Jackson'

# Loop through the list of ODF files and process both the DN and UP files.
# Iterate through the list of input files.
for file_name in files:

    print()
    print('#######################################################################')
    print('Processing ' + file_name)
    print('#######################################################################')
    print()

    odf = odfHeader.OdfHeader()

    # Clear the log prior to processing the next ODF file.
    odfUtils.list_handler.log_records.clear()

    # Read the ODF file
    odf.read_odf(file_name)

    # Add a new History Header to record the modifications that are made.
    odf.add_history()
    odf.history_headers[-1].set_creation_date(f"'{odfUtils.get_current_date_time()}'")
    history_comment = f'{user} made the following modifications to this file:'
    odf.add_to_history(history_comment)

    # Update Cruise_Header
    odf.cruise_header.set_cruise_number('BCD2016913')
    odf.cruise_header.set_organization('DFO BIO')
    odf.cruise_header.set_chief_scientist('Bruce Hatcher')
    odf.cruise_header.set_start_date('01-JAN-2016 00:00:00.00')
    odf.cruise_header.set_end_date('31-DEC-2016 00:00:00.00')
    odf.cruise_header.set_platform('EXOCET')
    odf.cruise_header.set_area_of_operation('Bras Dor Lake')
    odf.cruise_header.set_cruise_name('Bras Dor Lake')
    # odf.cruise_header.set_cruise_description('')

    # Make sure that the event numbers are 3-digit strings.
    strEvent = odf.event_header.get_event_number()
    strEvent = strEvent.strip("\' ")
    intEvent = int(strEvent)
    if len(strEvent) < 3:
        odf.event_header.set_event_number(f"{intEvent:03}")

    # Add history comments to document that the Slope and Offset values for the primary and secondary conductivity
    # channels were updated from their original acquisition values prior to reprocessing the CTD data files.
    # odf.add_to_history(
    #     'The primary conductivity (3561) and temperature (5081) sensors (pair 1) were replaced with sensors'
    #     ' (1874) and (2303) (pair 2) after the CTD collided with the bottom prior to event 136.')
    # odf.add_to_history('The primary conductivity [3561] calibration coefficient "Offset" was changed from its original '
    #                    'value [0.0] to [-0.00066] for sensor pair 1.')
    # odf.add_to_history('The primary conductivity [3561] calibration coefficient "Slope" was changed from its original '
    #                    'value [1.0] to [1.000039] for sensor pair 1.')
    # odf.add_to_history('The primary conductivity [1874] calibration coefficient "Offset" remained unchanged from its '
    #                    'original value [0.0] to [0.00048] for sensor pair 2.')
    # odf.add_to_history('The primary conductivity [1874] calibration coefficient "Slope" remained unchanged from its '
    #                    'original value [1.0] to [1.000016] for sensor pair 2.')
    # odf.add_to_history('The secondary conductivity [3562] calibration coefficient "Offset" was changed from its '
    #                    'original value [0.0] to [-0.00132].')
    # odf.add_to_history('The secondary conductivity [3562] calibration coefficient "Slope" was changed from its '
    #                    'original value [1.0] to [1.000272].')

    # Add history comments to document that the Soc values for the primary and secondary oxygen channels were updated
    # from their original acquisition values prior to reprocessing the CTD data files.
    # odf.add_to_history('The primary oxygen [0133] calibration coefficient "Soc" was changed from its original value '
    #                    'of [0.3903] to [0.4054].')
    # odf.add_to_history('The secondary oxygen [1588] calibration coefficient "Soc" was changed from its original value '
    #                    'of [0.5347] to [0.4523].')

    # Access the log records stored in the custom handler and add the logged changes to the History_Header.
    log_records = odfUtils.list_handler.log_records
    for record in log_records:
        odf.add_to_history(record)

    # Update the Record_Header and other headers to revise the metadata after modifications have been performed.
    odf.update_odf()

    odf_file_text = odf.print_object(file_version=2)
    print(odf_file_text)

    os.chdir(path_to_revised)

    # Output a new version of the ODF file using the proper file name.
    out_file = odf.generate_file_spec() + '.ODF'
    print(os.getcwd() + "\\" + out_file)
    file1 = open(out_file, "w")
    file1.write(odf_file_text)
    file1.close()

    os.chdir(path_to_orig)

os.chdir(path_to_orig)

# Run the following script on the MATLAB command line once the update script has finished. It creates new files with the
# quality flag fields after running the files through the GTSPP quality control checks.
# add_qfs_to_odf('*.ODF', 'C:\DEV\Data\2014\HUD2014030\CTD\DATASHOP_PROCESSING\Step_3_Update_Metadata',
# 'C:\DEV\Data\2014\HUD2014030\CTD\DATASHOP_PROCESSING\Step_4_Run_Automated_Checks', false, false)
