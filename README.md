# Anti-plagiarism
Machine Learning Весна'23

Write an anti-plagiarism program that compares two Python program texts and evaluates their similarity.

To solve this problem, I used the Wagner-Fischer algorithm

![image](https://user-images.githubusercontent.com/83032359/211209946-95e446d2-108c-4d68-97e5-f6d87184193a.png)


# Interface
You need to implement the script compare.py , which accepts a file with a list of document pairs and the path to the output file. The script should compare pairs of documents and write to the output file an assessment of the similarity of program texts.

## Data
plagiat.zip was unpacked and extracted to the same location as compare.py

![image](https://user-images.githubusercontent.com/83032359/211210386-7f7629ab-b596-4e6b-8df2-01c42d3df8e7.png)


### Example of an input file input.txt
![image](https://user-images.githubusercontent.com/83032359/211210521-ff40f662-65ba-490c-b8cb-c7030206c570.png)

### Example of an output file scores.txt
![image](https://user-images.githubusercontent.com/83032359/211210574-1680338d-1939-4f82-87c4-215ea420ea39.png)

### Call via console
![image](https://user-images.githubusercontent.com/83032359/211210776-b0273fe5-83e4-4d5e-91ec-fd1a2a42027c.png)


# Features

• Implementation the console interface via argparse  
•	Using ast to analyze the code  
• Using the re regular expression library  
• The Wagner-Fischer algorithm and normalization were implemented in functions.py
