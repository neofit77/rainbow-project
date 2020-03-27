Rainbow-project

Project objective is to generate 14,000 random numbers that meet specific parameters. 
Numbers are generated using python script (numpy and csv libraries).

Parameters:
1. Random numbers should fit into a table with 2,000 rows and 7 columns. Preferable  in an Excel Sheet . No two rows can have the same set of seven numbers
2. Random numbers must be from 1 to 50
3. Numbers are arranged in ascending order from left to right, with the smallest number on the row on the extreme left column and largest number on the extreme right column
4. The sum of the seven numbers in each row must be between 138 and 210 (both numbers included)
5. The mean of the seven numbers in each row must be between 20 and 30 (Both numbers included)
6. Difference between minimum number and maximum number in a row should be between 30 and 44 (Both numbers included)
7. The 7th root of the product of all 7 numbers . Such that AxBxCxDxExFxG=  KKK, therefore 7√KKK =KKK^(1/7). The 7th root of each row must be  between 10.54 and 25.18 (these numbers are included)
8. The standard deviation of the seven numbers in each row, must be between 11.0001 and 16.0001  (these numbers are included)
9. We cannot repeat same number in the same row
10. The value of the each number in a colums is represented in probabilityDistribution.csv (
    - for column 'A' rows 1-14 in probabilityDistribution.csv, 
    - for column 'B' rows 15-36 in probabilityDistribution.csv, 
    - for column 'C' rows 37-65 in probabilityDistribution.csv,
    - for column 'D' rows 66-92 in probabilityDistribution.csv, 
    - for column 'E' rows 93-118 in probabilityDistribution.csv, 
    - for column 'F' rows 119-140 in probabilityDistribution.csv, 
    - for column 'G' rows 141-155 in probabilityDistribution.csv
 
 A detailed description of the project is in the file 'The Rainbow Project.pptx'
 Using pyinstaller I made executable files for windows (/build/data/data.exe) and linux (/dist/data / data). 
 The Result.csv file is an example of an output file
 
 Run program:
 - Windows click on data.exe in /build/data
 - Linux run terminal, go to /dist/data folder and then run command ./data
 - Any OS - in terminal, go to folder with data.py file and then run command python data.py
 
