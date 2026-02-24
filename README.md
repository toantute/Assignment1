# Test Grade Calculator

Chương trình Python tính toán và phân tích điểm thi cho nhiều lớp học.

## Yêu cầu

- Python 3.x
- pandas
- numpy

Cài đặt thư viện nếu chưa có:
```bash
pip install pandas numpy
```

## Cách chạy

1. Đảm bảo file dữ liệu (ví dụ: `class1.txt`, `class2.txt`) nằm **cùng thư mục** với file chương trình.

2. Chạy chương trình:
```bash
python lastname_firstname_grade_the_exams.py
```

3. Nhập tên file khi được hỏi (không cần đuôi `.txt`):
```
Enter a class file to grade (i.e. class1 for class1.txt): class1
```

4. Nếu file không tồn tại, chương trình sẽ thông báo lỗi và yêu cầu nhập lại.

## Định dạng file đầu vào

Mỗi dòng trong file có định dạng:
```
N12345678,B,A,D,D,C,...
```
- Giá trị đầu tiên: ID sinh viên (ký tự `N` + 8 chữ số)
- 25 giá trị tiếp theo: câu trả lời (A/B/C/D hoặc trống nếu bỏ qua)

## Kết quả đầu ra

- In báo cáo ra màn hình: số dòng hợp lệ/không hợp lệ, điểm trung bình, cao nhất, thấp nhất, miền giá trị, trung vị.
- Tạo file `<tên_file>_grades.txt` chứa ID và điểm của từng học sinh.

## Cách tính điểm

| Trường hợp       | Điểm |
|------------------|------|
| Trả lời đúng     | +4   |
| Bỏ qua câu hỏi  |  0   |
| Trả lời sai      | -1   |

## Ví dụ

```
Enter a class file to grade (i.e. class1 for class1.txt): class1
Successfully opened class1.txt

**** ANALYZING ****
No errors found!

**** REPORT ****
Total valid lines of data: 20
Total invalid lines of data: 0
Mean (average) score: 75.60
Highest score: 91
Lowest score: 59
Range of scores: 32
Median score: 73

Results saved to class1_grades.txt
```
