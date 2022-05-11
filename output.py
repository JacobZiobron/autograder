import xlsxwriter
from finalExamTests import *
import globals
# set_column(first_col, last_col, width, cell_format, options)

#Function to print out the worksheet
def initialize():
    # The name of the outputted excel file
    workbook = xlsxwriter.Workbook("FinalProject.xlsx")
    worksheet = workbook.add_worksheet()

    # Bold Format
    bold = workbook.add_format({'bold': True})
    bold.set_text_wrap()
    bold.set_border()

    # Regular Cell Formatting
    cell_format = workbook.add_format()
    cell_format.set_text_wrap()
    cell_format.set_border()


    worksheet.set_column(0,0,120)
    worksheet.set_column(3,3,40)


    def fileText(worksheet, bold, cell_format):
        worksheet.write(0, 0, "Final Project: Data Analysis Program", bold)
        worksheet.write(1,0, "Name:", bold)
        worksheet.write(3,0, 
        """
        Proficiency Scale\n

        0 = Action item missed. \n
        1 = An incomplete or entirely incorrect answer is given. This would apply if the program or parts of the program do not compile, do not run or produce errors.\n
        2 = An answer is given but there are issues including not meeting the specifications and producing multiple incorrect results. This would apply if the program or parts of the program produce multiple incorrect results.\n
        3 = A complete answer is given but it does not meet all the specifications. This would apply if the program or parts of the program run without any errors but sometimes produce incorrect results.\n
        4 = A complete and correct answer is given meeting all the specifications. This would apply if the program or parts of the program run without any errors and always produce expected results.\n

        """, cell_format)

        worksheet.write(4, 1, "Earned Points", bold)
        worksheet.write(4, 2, "Possible Points", bold)
        worksheet.write(4, 3, "Comments", bold)
        worksheet.write(5, 0, "Part II: Data Analysis Program", bold)

        worksheet.write(6,0,
        """
        You should use comments (#) in your program to design your program and include the following:
        - Your name, course name and semester, title of this assignment, and date.
        - The title and description of the program.
        - Your general solution for this program.
        - Pseudocode (i.e., the steps needed to perform tasks and write your informal code for the program).
        """
        , cell_format)

        worksheet.write(7,0,
        """
        A. Setting Up And Providing A List Of Options To User
        It outputs: 
        - The name of your topic
        - One of your data-driven questions 
        - A welcome message 
        - Provide the user with eight options to choose from and wait until the user enters a valid choice
        - If the user enters input that does not contain only digits, then the program should output: You did not enter input with only digits! Try again.
        - If the user enters input that is outside of the range of options, then the program should output: You did not enter a valid choice. Chose any option from 1 to 8.
        """
        , cell_format)

        worksheet.write(8,0,
        """
        A. Setting Up And Providing A List Of Options To User 
        Correctly define and call ALL of the required functions:
        - main: This function set ups the program and manages calls to other functions defined to handle the eight options. 
        - welcome_msg: This function outputs the name of your topic, data-driven questions and a welcome message to your data analysis program.
        - get_choice: This function outputs the list of eight choices for the main menu and calls the check_choice function passing it 1 as the minimum and 8 as the maximum to obtain a valid input from the user.
        - check_choice - This function asks the user for their choice and then checks that the user's input is a valid digit between the minimum and maximum arguments passed to it.
        """
        , cell_format)

        worksheet.write(9,0,
        """
        B. Overview Of Your Topic And Data Set
        It outputs: 
        - An overview of your topic and data set
        """
        , cell_format)

        worksheet.write(10,0,
        """
        B. Overview Of Your Topic And Data Set
        Correctly define and call ALL of the required functions:
        - overview: This function outputs an overview of your topic and data set. It is called in the main function when the user chooses option 1 from the main menu.
        """
        , cell_format)

        worksheet.write(11,0,
        """
        C. Data-Driven Question And Prediction 
        It outputs: 
        - Data-driven questions and predictions that made about topic and data set 
        """
        , cell_format)

        worksheet.write(12,0,
        """
        C. Data-Driven Question And Prediction 
        Correctly define and call ALL of the required functions:
        - dq: This function outputs your data-driven questions and predictions about your topic. It is called in the main function when the user chooses option 2 from the main menu.
        """
        , cell_format)

        worksheet.write(13,0,
        """
        "D. Basic Data Statistics  
        - Provide the user with a new set of numbered options to choose from with basic data statistics calculated on your topic.
        - Waits until the user enters a valid choice.
        - If the user enters input that does not contain only digits, then the program should output: You did not enter input with only digits! Try again.
        - If the user enters input that is outside of the range of options, then the program should output: You did not enter a valid choice. Chose any option from [min] to [max].
        - If the user enters valid input and chooses one of the numbered options in this new menu, then the program should output the appropriate data statistics.
        - Its last option will allow the user to return to the main menu with the eight options.
        """
        , cell_format)

        worksheet.write(14,0,
        """
        D. Basic Data Statistics 
        Correctly define and call ALL of the required functions:
        - basic_stats: This function provides the user with another set of options computing basic data statistics on your topic from. It should call the check_choice function passing it the minimum and maximum numbered options for its set of options to obtain a valid input from the user. Once it is returned the valid choice from the check_choice function, it then calls the appropriate function to output the data statistic chosen by the user. This function is called in the main function when the user chooses option 3 from the main menu.
        - option1: This function outputs appropriate data and calculations for this option.
        - option2: This function outputs appropriate data and calculations for this option.
        - option3: This function outputs appropriate data and calculations for this option.
        - option4: This function outputs appropriate data and calculations for this option.
        """
        , cell_format)

        worksheet.write(15,0,
        """
        E. Simple Visualizations 
        - Provide the user with a new set of numbered options to choose from with simple visualizations on your topic created.
        - Waits until the user enters a valid choice.
        - If the user enters input that does not contain only digits, then the program should output: You did not enter input with only digits! Try again.
        - If the user enters input that is outside of the range of options, then the program should output: You did not enter a valid choice. Chose any option from [min] to [max].
        - If the user enters valid input and chooses one of the numbered options in this new menu, then the program should output the appropriate visualization.
        - Its last option will allow the user to return to the main menu with the eight options.
        """
        , cell_format)

        worksheet.write(16,0,
        """
        E. Simple Visualizations   
        Correctly define and call ALL of the required functions:
        - simple_visualizations: This function provides the user with another set of options outputting simple visualizations on your topic. It should call the check_choice function passing it the minimum and maximum numbered options for its set of options to obtain a valid input from the user. Once it is returned the valid choice from the check_choice function, it then calls the appropriate function that outputs the visualization chosen by the user. This function is called in the main function when the user chooses option 4 from the main menu.
        - scatter_visual: This function creates and outputs a scatter chart based on the lists of x and y coordinates it receives as arguments.
        - line_visual: This function creates and outputs a line chart based on the lists of x and y coordinates it receives as arguments. 
        - bar_visual: This function creates and outputs a bar chart based on the lists of x-coordinates of each bar’s left edge and heights of each bar along y-axis it receives as arguments.
        - pie_visual: This function creates and outputs a pie chart based on the lists of values and slice labels it receives as an argument.
        - minimum_val: This function finds the minimum value in a list that it receives as an argument.
        - maximum_val: This function finds the maximum value in a list.
        - average_val: This function finds the average value of a list that it receives as an argument.
        """
        , cell_format)

        worksheet.write(17,0,
        """
        F. Survey Analysis  
        - When the user chooses the fifth option (Survey Analysis) OR the seventh option (Findings and Observations) for the FIRST time in your program, then it must clean your survey responses and output any errors it found.
        - Your Google Forms survey is only be processed and cleaned ONCE meaning that it will only run when the fifth or seventh option have been chosen for the first time.
        - Provide the user with a new set of numbered options to choose from with your basic data statistic, histogram and pie chart created from your Google Forms survey responses on your topic.
        - Waits until the user enters a valid choice.
        - If the user enters input that does not contain only digits, then the program should output: You did not enter input with only digits! Try again.
        - If the user enters input that is outside of the range of options, then the program should output: You did not enter a valid choice. Chose any option from [min] to [max].
        - If the user enters valid input and chooses one of the numbered options in this new menu, then the program should output the appropriate visualization and data statistic.
        - Its last option will allow the user to return to the main menu with the eight options.
        """
        , cell_format)

        worksheet.write(18,0,
        """
        F. Survey Analysis   
        Correctly define and call ALL of the required functions:
        - read_csv: This function opens/reads the survey responses CSV file and checks/cleans invalid data entries in each row of the CSV file. It is called in the main function when the user chooses option 5 OR option 7 from the main menu for the FIRST TIME.
        - survey_analysis: This function provides the user with another set of options outputting histogram(s), data computations and pie chart(s) created from your Google Forms survey responses. It should call the check_choice function passing it the minimum and maximum numbered options for its set of options to obtain a valid input from the user. Once it is returned the valid choice from the check_choice function, it then calls the appropriate function that outputs the data statistics or visualization chosen by the user. This function is called in the main function when the user chooses option 5 from the main menu after the Google Forms survey has been read and cleaned from the read_csv function.
        - check_age: This function checks if the age contains only digits OR that the first two characters contain only digits (i.e., 21yrs becomes 21) AND if the age is between 0 and 150.
        - check_linear_scale: This function checks if rating contains only digits and if the rating is between the specified scale (i.e., 1 to 5, 1 to 10, etc.).
        - check_multiple_choice: This function checks if the choice for the multiple choice question is not empty and is one of the provided choices for the question.
        - plt_linear_rating: This function plots a histogram with the ratings for your linear scale question.
        - plt_counts: This function plots a pie chart of the counts for each choice in the multiple choice question.
        - compute: This function computes a data statistic using the numpy package (i.e, mean, median, standard deviation) with the ratings for your linear scale question.
        """
        , cell_format)

        worksheet.write(19,0,
        """
        G. Data Set Analysis  
        - When the user chooses the sixth option (Data Set Analysis) OR the seventh option (Findings and Observations) for the FIRST time in your program, then it must clean the DataFrame containing the data from your data set you found online and output any errors it found and resolved.
        - Your DataFrame is only be processed and cleaned ONCE meaning that it will only run when the sixth or seventh option have been chosen for the first time.
        - Provide the user with a new set of numbered options to choose from with each of your pivot tables and visualizations created from your DataFrame containing the data set you found online.
        - Waits until the user enters a valid choice.
        - If the user enters input that does not contain only digits, then the program should output: You did not enter input with only digits! Try again.
        - If the user enters input that is outside of the range of options, then the program should output: You did not enter a valid choice. Chose any option from [min] to [max].
        - If the user enters valid input and chooses one of the numbered options in this new menu, then the program should output the appropriate pivot table or visualization.
        - Its last option will allow the user to return to the main menu with the eight options.
        """
        , cell_format)

        worksheet.write(20,0,
        """
        G. Data Set Analysis     
        Correctly define and call ALL of the required functions:
        - process_df: This function calls the necessary functions to read the data set you found online into a DataFrame and clean it. This function will output the errors in the DataFrame as well as how these errors have been resolved. It is called in the main function when the user chooses option 6 OR option 7 from the main menu for the FIRST TIME. 
        - read_as_dataframe: This function converts data in a CSV file to a Pandas DataFrame.
        - clean_dataframe: After visually inspecting your data set, this function will resolve any data errors that you found in your inspection. You can use any of the techniques to clean data discussed in the lectures and lab such as dropping or filling missing values, dropping duplicate rows, replacing erroneous data values, formatting values, and converting columns to their proper data type.
        - data_analysis: This function provides the user with another set of options outputting pivot tables and visualizations created from your cleaned DataFrame. It should call the check_choice function passing it the minimum and maximum numbered options for its set of options to obtain a valid input from the user. Once it is returned the valid choice from the check_choice function, it then calls the appropriate function that outputs the pivot table or visualization chosen by the user. This function is called in the main function when the user chooses option 6 from the main menu after the DataFrame has been read and cleaned from the process_df function.
        - get_subset: Using your cleaned Pandas DataFrame, you will create filtered subset(s) of it to help narrow it down and perform computations on particular information that will serve as supporting evidence to some of the questions you posed about your topic.
        - groupby_sum_table: This function uses the groupby() method to create a summary table with at least ONE mathematical computation (i.e., mean, sum, etc.) applied that is relevant to the questions you posed about your topic.
        - piv_sum_table: This function uses the pivot_table() method to create a summary table with at least ONE mathematical computation (i.e., mean, sum, etc.) applied that is relevant to the questions you posed about your topic.

        You will use the same functions for each of your visualizations that you created in Assignment 12: Summarizing & Visualizing DataFrames your program. Make sure to pass the value(s) needed to create these visualizations from your data_analysis function as arguments.
        - Create and output a scatter chart that is relevant to the questions you posed about your topic.
        - Create and output a line chart that is relevant to the questions you posed about your topic.
        - Create and output a bar chart that is relevant to the questions you posed about your topic.
        - Create and output any type of chart on at least ONE of your summary tables that is relevant to the questions you posed about your topic.
        - You should create and output at least FOUR charts overall that have been described above.
        - All the charts you create must have appropriate titles, x-axis and y-axis labels, legends, ranges, and style/color schemes.
        """
        , cell_format)

        worksheet.write(21,0,
        """
        H. Findings and Observations 
        - When the user chooses the seventh option (Findings and Observations) for the FIRST time in your program and NEITHER the fifth option (Survey Analysis) OR sixth option (Data Set Analysis) have been chosen by the user yet, then it must clean BOTH the Google Forms survey responses and the DataFrame containing the data from your data set you found online.
        - The seventh option will provide the user with findings and observations to your data-driven questions that MUST be supported with data statistics, pivot tables and visualizations. You must also include descriptions of how these data statistics, pivot tables and visualizations serve as supporting evidence to the data-driven questions.
        """
        , cell_format)

        worksheet.write(22,0,
        """
        H. Findings and Observations     
        Correctly define and call ALL of the required functions:
        - findings: This function outputs the findings and observations to the data-driven questions using data statistics, pivot tables and summary statistics, and visualizations as supporting evidence. It is called in the main function when the user chooses option option 7 from the main menu. 
        """
        , cell_format)

        worksheet.write(23,0,
        """
        I. Quit 
        - The eighth option in your program will allow the user to quit the program to stop it from running.
        """
        , cell_format)

        worksheet.write(24,0,
        """
        Setup the program and manage function to calls to the majority of functions in the main function.
        - Calls a majority of the functions specified above and passes each of these functions the correct number and type of arguments needed.
        """
        , cell_format)

        worksheet.write(25,0,
        """
        Program produces the result that is expected.
        If your program does not run, or runs with errors, you will lose at least half of the possible points.
        """
        , cell_format)

        worksheet.write(26,0,
        """
        Program is readable to other people. This includes well-named variables, use of extra lines to break up sections of code, and placement of comments above code.
        """
        , cell_format)

        worksheet.write(27, 0, "Part III: Updating Your Google Site", bold)

        worksheet.write(28,0,
        """
        A subpage of the fifth page dedicated to your Python programs with:

        A title with a background.
        - This title should be related to your python program and topic.
        - A background image. It does not have to match the ones on your previous pages.

        A description of your Python program.
        - An overview of the Python program you wrote describing what it does and descriptions of each option in your program. 
        - A general solution describing how you designed this program (i.e., algorithm, use of variables, types, arithmetic operators, conditional statements, loops, functions, lists, dictionaries, matplotlib, csv, numpy, pandas, etc.).
        - Expected output of your program (i.e., what is your program supposed to output to the user). 

        Embed the Python program that you wrote for this assignment.
        - Include ALL your code for this program.
        - Include ALL the output that your program produces after it is finished running. 
        - Ensure that your program output is correct and matches the expected output you described above.
        """
        , cell_format)

        worksheet.write(29,0,
        """
        Add a final page (not a subpage!) called Findings and Observations to your Google Site with:

        A title with a background.
        - This title should be called Findings and Observations.
        - A background image. It does not have to match the one on your homepage.

        Findings and observations to the data-driven questions you posed about your topic on your homepage.
        - Include findings and observations to your data-driven questions that MUST be supported with evidence through your data statistics, pivot tables and visualizations.
        - You MUST include descriptions of how these data statistics, pivot tables and visualizations help support your findings and observations to your data-driven questions. 
        """
        , cell_format)

        worksheet.write(30,0,"Submission: URL of Google Site, CSV Files & Python Script", bold)

        worksheet.write(31,0,
        """
        Student includes the URL link to their Google Site. The Google Site must have its privacy permission set (i.e., Anyone with the link can view) so that the grader can use the URL to view it.
        """
        , cell_format)

        worksheet.write(32,0,
        """
        Student submits a Python script attachment with correct name—lastname_final.py where lastname is the student's last name.

        Student submits a CSV file attachment of their Google Forms survey responses with correct name—lastname_survey_.csv where lastname is the student's last name.

        Student submits a CSV file attachment of the data set they found online with correct name—lastname_topic.csv where lastname is the student's last name.
        """
        , cell_format)

        worksheet.write(34,0, "Total", bold)

    fileText(worksheet, bold, cell_format)

    # Gradebook - Earned Points
    worksheet.write(6, 1, sum(globals.points7), cell_format)
    worksheet.write(7, 1, sum(globals.points8), cell_format)
    worksheet.write(8, 1, sum(globals.points9), cell_format)
    worksheet.write(9, 1, sum(globals.points10), cell_format)
    worksheet.write(10, 1, sum(globals.points11), cell_format)
    worksheet.write(11, 1, sum(globals.points12), cell_format)
    worksheet.write(12, 1, sum(globals.points13), cell_format)
    worksheet.write(13, 1, sum(globals.points14), cell_format)
    worksheet.write(14, 1, sum(globals.points15), cell_format)
    worksheet.write(15, 1, sum(globals.points16), cell_format)

    worksheet.write(16, 1, sum(globals.points17), cell_format)
    worksheet.write(17, 1, sum(globals.points18), cell_format)
    worksheet.write(18, 1, sum(globals.points19), cell_format)
    worksheet.write(19, 1, sum(globals.points20), cell_format)
    worksheet.write(20, 1, sum(globals.points21), cell_format)
    worksheet.write(21, 1, sum(globals.points22), cell_format)
    worksheet.write(22, 1, sum(globals.points23), cell_format)
    worksheet.write(23, 1, sum(globals.points24), cell_format)
    worksheet.write(24, 1, sum(globals.points25), cell_format)
    worksheet.write(25, 1, sum(globals.points26), cell_format)
    worksheet.write(26, 1, sum(globals.points27), cell_format)

    worksheet.write(28, 1, sum(globals.points29), cell_format)
    worksheet.write(29, 1, sum(globals.points30), cell_format)

    worksheet.write(31, 1, sum(globals.points32), cell_format)
    worksheet.write(32, 1, sum(globals.points33), cell_format)

    # Formula to add up total points
    worksheet.write('B35', '=SUM(B7:B34)', cell_format)


    # Gradebook - Possible Points
    worksheet.write(6, 2, "4", cell_format)
    worksheet.write(7, 2, "4", cell_format)
    worksheet.write(8, 2, "4", cell_format)
    worksheet.write(9, 2, "4", cell_format)
    worksheet.write(10, 2, "4", cell_format)
    worksheet.write(11, 2, "4", cell_format)
    worksheet.write(12, 2, "4", cell_format)
    worksheet.write(13, 2, "4", cell_format)
    worksheet.write(14, 2, "4", cell_format)
    worksheet.write(15, 2, "4", cell_format)

    worksheet.write(16, 2, "4", cell_format)
    worksheet.write(17, 2, "4", cell_format)
    worksheet.write(18, 2, "4", cell_format)
    worksheet.write(19, 2, "4", cell_format)
    worksheet.write(20, 2, "4", cell_format)
    worksheet.write(21, 2, "4", cell_format)
    worksheet.write(22, 2, "4", cell_format)
    worksheet.write(23, 2, "4", cell_format)
    worksheet.write(24, 2, "4", cell_format)
    worksheet.write(25, 2, "4", cell_format)
    worksheet.write(26, 2, "4", cell_format)

    worksheet.write(28, 2, "4", cell_format)
    worksheet.write(29, 2, "4", cell_format)

    worksheet.write(31, 2, "4", cell_format)
    worksheet.write(32, 2, "4", cell_format)

    worksheet.write(34, 2, "100", cell_format)



    # Gradebook - Comments
    worksheet.write(6, 3, ' '.join(globals.comment7), cell_format)
    worksheet.write(7, 3, ' '.join(globals.comment8), cell_format)
    worksheet.write(8, 3, ' '.join(globals.comment9), cell_format)
    worksheet.write(9, 3, ' '.join(globals.comment10), cell_format)
    worksheet.write(10, 3, ' '.join(globals.comment11), cell_format)
    worksheet.write(11, 3, ' '.join(globals.comment12), cell_format)
    worksheet.write(12, 3, ' '.join(globals.comment13), cell_format)
    worksheet.write(13, 3, ' '.join(globals.comment14), cell_format)
    worksheet.write(14, 3, ' '.join(globals.comment15), cell_format)
    worksheet.write(15, 3, ' '.join(globals.comment16), cell_format)
    worksheet.write(16, 3, ' '.join(globals.comment17), cell_format)
    worksheet.write(17, 3, ' '.join(globals.comment18), cell_format)
    worksheet.write(18, 3, ' '.join(globals.comment19), cell_format)
    worksheet.write(19, 3, ' '.join(globals.comment20), cell_format)
    worksheet.write(20, 3, ' '.join(globals.comment21), cell_format)
    worksheet.write(21, 3, ' '.join(globals.comment22), cell_format)
    worksheet.write(22, 3, ' '.join(globals.comment23), cell_format)
    worksheet.write(23, 3, ' '.join(globals.comment24), cell_format)
    worksheet.write(24, 3, ' '.join(globals.comment25), cell_format)
    worksheet.write(25, 3, ' '.join(globals.comment26), cell_format)
    worksheet.write(25, 3, ' '.join(globals.comment27), cell_format)
    worksheet.write(28, 3, ' '.join(globals.comment29), cell_format)
    worksheet.write(29, 3, ' '.join(globals.comment30), cell_format)
    worksheet.write(31, 3, ' '.join(globals.comment32), cell_format)
    worksheet.write(32, 3, ' '.join(globals.comment33), cell_format)

    fileText(worksheet, bold, cell_format)
    workbook.close()

