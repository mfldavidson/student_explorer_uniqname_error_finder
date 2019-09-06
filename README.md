# As of 9/6/19 this repository has been archived and instead lives on in [University of Michigan ITS Teaching & Learning](https://github.com/tl-its-umich-edu/student_explorer_cohort_verification).

# Uniqname Error Finder for Student Explorer application
In [Student Explorer](https://github.com/tl-its-umich-edu/student_explorer/), if a cohort is created with a student uniqname that doesn't match to a student in edwprod.world CNLYR002 DM_STDNT table, the way this manifests in the application is that the advisor sees a student in their "My Students" view named "Not Happened Yet". This program, se_uniq_error_finder.py, was created in order to figure out which uniqname(s) are throwing the error so that you can go back to the advisor to let them know which uniqnames caused the error and get the correct uniqname(s). Run this program by following these instructions for each cohort that needs to be investigated. Steps 1-4 only need to be followed the first time you run the program. After the first time, simply activate your virtual environment and proceed to step 5.

1. Clone this repo to your computer by navigating to the directory/folder where you want it and entering `git clone https://github.com/mfldavidson/student_explorer_uniqname_error_finder.git` in your command line.

2. Create a virtual environment (`python3 -m venv whateveryouwanttonameit`) wherever you keep your virtual environments.

3. Activate the virtual environment (`source whateveryounamedthevirtualenv/bin/activate` if you are on a Mac, or `source whateveryounamedthevirtualenv/Scripts/activate` if you are on a PC).

4. Install all necessary libraries by navigating to the repo and then running the command `pip install -r requirements.txt`

5. Navigate to the Student Explorer Cohort Management page at https://studentexplorer.ai.umich.edu/manage/cohorts/, find the affected cohort, and click on its Code hyperlink. Click the download button to download the cohort data to an XLS file.

6. Change the name of the downloaded CSV file to `cohort.csv` and put it in the same directory/folder as se_uniq_error_finder. You should now have 3 files--`se_uniq_error_finder.py`, `students.htm`, and `cohort.csv`.

7. Navigate to the cohort view (`https://studentexplorer.ai.umich.edu/cohorts/<cohort code>/` - this can easily be done by removing "manage/" and "members/" from the URL when you are on the cohort management page where you downloaded the XLS file). Save the webpage (HTML only, NOT the complete page) as `students.htm` in the repo*. The easiest way to save the htm file is to just use the keyboard shortcut CMD+S for Mac or CTRL+S for Windows.

8. While still inside the repo (and ensuring your virtual environment is activated), run the command `python se_uniq_error_finder.py`.

9. The program should print out one or more uniqnames in the command line. These are the uniqnames that caused the error. It may be worth checking the uniqnames in M-Community to ensure they are invalid uniqnames. If they are invalid, go back to the advisor and let them know which uniqnames are invalid so they can get you the right ones. If the uniqnames do show up in M-Community, discuss with Information Quest why the DM_STDNT table may be missing these students. It is sometimes the case that the student is a real student but they have never registered for any term-bound courses, which means they would never be in Student Explorer.

*Note that the gitignore file will ignore any .htm and .xls files so that this confidential student data is ignored.
