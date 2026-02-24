import re
import numpy as np
import pandas as pd

ANSWER_KEY = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")


def open_file():
    """Task 1: Yêu cầu người dùng nhập tên file và mở file với exception handling."""
    while True:
        filename_input = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        filename = filename_input.strip() + ".txt"
        try:
            f = open(filename, "r")
            print(f"Successfully opened {filename}")
            return f, filename_input.strip()
        except FileNotFoundError:
            print("File cannot be found.")


def is_valid_student_id(student_id):
    """Kiểm tra định dạng ID sinh viên: 'N' theo sau bởi đúng 8 chữ số."""
    return bool(re.fullmatch(r'N\d{8}', student_id))


def analyze_file(file):
    """
    Task 2: Phân tích từng dòng trong file, kiểm tra tính hợp lệ.
    Trả về danh sách các dòng hợp lệ.
    """
    print("\n**** ANALYZING ****")
    lines = file.read().splitlines()
    valid_lines = []
    invalid_count = 0
    has_error = False

    for line in lines:
        if not line.strip():
            continue  # Bỏ qua dòng trống

        values = line.split(",")

        # Kiểm tra số lượng giá trị (phải đúng 26: 1 ID + 25 câu trả lời)
        if len(values) != 26:
            print(f"Invalid line of data: does not contain exactly 26 values:")
            print(line)
            invalid_count += 1
            has_error = True
            continue

        # Kiểm tra định dạng ID sinh viên
        if not is_valid_student_id(values[0]):
            print(f"Invalid line of data: N# is invalid")
            print(line)
            invalid_count += 1
            has_error = True
            continue

        valid_lines.append(values)

    if not has_error:
        print("No errors found!")

    return valid_lines, invalid_count


def grade_student(answers):
    """Chấm điểm một học sinh dựa trên answer key."""
    score = 0
    for student_ans, correct_ans in zip(answers, ANSWER_KEY):
        if student_ans.strip() == "":
            score += 0       
        elif student_ans.strip() == correct_ans:
            score += 4      
        else:
            score -= 1      
    return score


def calculate_statistics(scores):
    """
    Task 3: Tính các thống kê: trung bình, cao nhất, thấp nhất, miền giá trị, trung vị.
    """
    scores_array = np.array(scores)
    mean_score = np.mean(scores_array)
    highest = np.max(scores_array)
    lowest = np.min(scores_array)
    score_range = highest - lowest
    median = np.median(scores_array)

    return mean_score, highest, lowest, score_range, median


def print_report(valid_count, invalid_count, scores):
    """In báo cáo kết quả."""
    print("\n**** REPORT ****")
    print(f"Total valid lines of data: {valid_count}")
    print(f"Total invalid lines of data: {invalid_count}")

    if scores:
        mean_score, highest, lowest, score_range, median = calculate_statistics(scores)
        print(f"Mean (average) score: {mean_score:.2f}")
        print(f"Highest score: {int(highest)}")
        print(f"Lowest score: {int(lowest)}")
        print(f"Range of scores: {int(score_range)}")
        print(f"Median score: {int(median)}")


def write_results(filename_base, student_scores):
    """
    Task 4: Ghi kết quả vào file <filename_base>_grades.txt.
    """
    output_filename = f"{filename_base}_grades.txt"
    df = pd.DataFrame(student_scores, columns=["StudentID", "Score"])
    # Ghi file không có header và index, phân cách bằng dấu phẩy
    df.to_csv(output_filename, index=False, header=False)
    print(f"\nResults saved to {output_filename}")


def main():
    # Task 1: Mở file
    file, filename_base = open_file()

    # Task 2: Phân tích file
    valid_lines, invalid_count = analyze_file(file)
    file.close()

    # Task 3: Chấm điểm
    scores = []
    student_scores = []

    for values in valid_lines:
        student_id = values[0]
        answers = values[1:]  # 25 câu trả lời
        score = grade_student(answers)
        scores.append(score)
        student_scores.append((student_id, score))

    # In báo cáo
    print_report(len(valid_lines), invalid_count, scores)

    # Task 4: Ghi kết quả ra file
    if student_scores:
        write_results(filename_base, student_scores)


if __name__ == "__main__":

    main()
