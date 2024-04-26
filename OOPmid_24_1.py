import streamlit as st
import pandas as pd

exam_title = "2024 Spring Objective Oriented Programming"
fname = "OOP_Midterm_Grading.xlsx"
solution_1 = '''Solution
1. (10p - 2p each) \n
(a) T \n
(b) F \n
(c) F \n
(d) T \n
(e) T \n
'''

solution_2 = '''
2. (10p - 2p each) \n
(a) Compile \n 
(b) Garbage \n
(c) Object \n
(d) Polymorphism \n
'''

solution_3 = '''
3. (15p) \n
(a) - 3p \n
Integrated Development Environment \n
(b) - 6p (2p each) \n
char, short (2 bytes) / int, float (4 bytes) / double,long (8 bytes) \n
(c) - 6p (2p each) \n
17ff 1755 144 \n
'''

solution_4 = '''
4. (7p) \n
(a) - 3p \n
It serves as a fallback option. It executes when none of the preceding case labels match the value of the expression being evaluated \n
(b) - 4p \n
200 \n
'''

solution_5_1 = '''
5. (11P) 
'''

code_5 = '''
import java.util.Scanner;

public class Summations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a positive integer n: ");
        int n = scanner.nextInt();
        if (n <= 0) {
            System.out.println("The input is wrong");
            return;
        }

        int sumA = 0;
        for (int i = 1; i <= n; i++) {
            sumA += i * i;
        }

        int sumB = 0;
        int k = 1;
        while (k <= n) {
            if (k % 10 != 4) {
                sumB += k;
            }
            k++;
        }
        System.out.println("A = " + sumA);
        System.out.println("B = " + sumB);
    }
}
'''

solution_5_2 = '''

for statement - 4p \n
(while, if) - 4p \n
Input - 3p \n
'''

solution_6_1 = '''
6. (10p)
'''

code_6 = '''
import java.util.Scanner;
public class NumberPattern {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int numRows = scanner.nextInt();
        int[][] numbers = new int[numRows][];

        // Store the computed values
        for (int i = 0; i < numRows; i++) {
            numbers[i] = new int[i + 1]; // Initialize the row with exact number of elements
            numbers[i][0] = 1; // Set the first element of each row
            for (int j = 1; j < numbers[i].length; j++) { // Compute values in the row
                if (j == 1) {
                    numbers[i][j] = 2 * numbers[i - 1][j - 1] + numbers[i - 1][j];
                } else {
                    numbers[i][j] = 2 * numbers[i - 1][j - 1] + numbers[i][1][j - 1];
                }
            }
        }

        // Printing the numbers as per the computed matrix
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numbers[i].length; j++) {
                System.out.print(numbers[i][j] + " ");
            }
            System.out.println();
        }
        
        scanner.close();
    }
}
'''

solution_6_2 ='''

Input part - 2p \n
Algorithm, output part - 8p \n
'''

solution_7 = '''
7. (8p - 2p each) \n
(a) - (4) \n
(b) - (3) \n
(c) - (2) \n
(d) - (1) \n
'''

solution_8 = '''
8. (9p - 3p each) \n
(1) try \n
(2) number < min(As an alternative, 1) || number > max(As an alternative, 100) \n
(3) catch \n
'''
solution_9 = '''
9.
(a) - 3p \n
2 4 6 8 10 \n

(b) - 7p \n
The error arises because the class AccessEx is attempting to access private members "b" of the Sample class,  \n
which are not accessible outside of the Sample class itself. There can be two possible ways to fix these errors. \n

Solution: \n
1. Make b accessible: We can change the access modifier of b from private to either public or protected, depending on your design requirements. \n
2. Provide a public method to access b: We can create a public method within the Sample class to set the value of b. \n

Explain the Error correctly - 4p \n
Right solution - 3p \n
'''
solution_10_1 = '''
10. 
'''

code_10 ='''
import java.util.Scanner;

class Circle {
    private double radius;
    private double centerX;
    private double centerY;

    public Circle(double radius, double centerX, double centerY) {
        this.radius = radius;
        this.centerX = centerX;
        this.centerY = centerY;
    }

    public boolean hasIntersection(Circle other) {
        double distanceBetweenCenters = calculateDistance(centerX, centerY, other.centerX, other.centerY);
        return distanceBetweenCenters < radius + other.radius;
    }

    private double calculateDistance(double x1, double y1, double x2, double y2) {
        return Math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));
    }
}
public class CircleIntersectionChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the radius and coordinates of the first and second circle:");
        double radius1 = scanner.nextDouble();
        double centerX1 = scanner.nextDouble();
        double centerY1 = scanner.nextDouble();
        double radius2 = scanner.nextDouble();
        double centerX2 = scanner.nextDouble();
        double centerY2 = scanner.nextDouble();
        Circle circle1 = new Circle(radius1, centerX1, centerY1);
        Circle circle2 = new Circle(radius2, centerX2, centerY2);

        if (circle1.hasIntersection(circle2)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        
        scanner.close();
    }
}
'''

solution_10_2 = '''

Circle Class - 6p \n
Main Program - 6p \n

However, If your code has problem with the output, your lose 3 point \n
'''

# Setup Title & Wide layout
st.set_page_config(page_title=exam_title, layout="wide")
st.markdown(
    """
    <style>
    textarea {
        font-size: 2rem !important;
    }
    input {
        font-size:1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Load the Excel data
df = pd.read_excel(fname)

def get_student_data(student_id):
    """
    Fetch the data for a given student ID from the Excel file.
    
    Args:
    - student_id (int): The ID of the student.
    
    Returns:
    - pd.DataFrame or None: The data for the student if found, otherwise None.
    """
    student_data = df[df["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None

# Streamlit app layout and logic
st.title(exam_title)

# Get the student ID from the user
student_id = st.text_input("Enter your email", value='hwanheelee@cau.ac.kr')

# When the user provides a student ID, fetch and display the data
if student_id:
    data = get_student_data(student_id)
    
    if data is not None:
        to_show = data.set_index("e-mail")
        st.write("E-mail: ", to_show.index[0])
        s = to_show.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
        st.dataframe(s, hide_index=True)
    else:
        st.write(f"No data found for email: {student_id}")
        
st.write(solution_1)  
st.markdown("""---""")
st.write(solution_2)  
st.markdown("""---""")
st.write(solution_3)  
st.markdown("""---""")
st.write(solution_4)  
st.markdown("""---""")
st.write(solution_5_1)  
st.code(code_5, language='java')
st.write(solution_5_2)  
st.markdown("""---""")
st.write(solution_6_1)  
st.code(code_6, language='java')
st.write(solution_6_2)  
st.markdown("""---""")
st.write(solution_7) 
st.markdown("""---""")
st.write(solution_8) 
st.markdown("""---""")
st.write(solution_9) 
st.markdown("""---""")
st.write(solution_10_1) 
st.code(code_10, language='java')
st.write(solution_10_2)  
        
