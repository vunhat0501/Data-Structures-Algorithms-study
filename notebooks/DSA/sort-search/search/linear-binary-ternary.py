class Student:
    #* Khoi tao class
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
    
    #** hien thi thong tin
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Score: {self.score}"

def linear_search(students, score_to_find):
    for student in students:
        if student.score == score_to_find:
            return student
    return None

def binary_search(students, score_to_find):
    low = 0
    high = len(students) - 1
    
    while low <= high:
        mid = (low + high) // 2

    #* kiem tra xem gia tri can tim co nam o giua hay khong
    if students[mid].score == score_to_find:
        return students[mid]
    
    #* neu gia tri can tim lon hon gia tri o giua
    #* bo qua mang ben trai vaf nguoc lai
    elif students[mid].score < score_to_find:
        low = mid + 1
    else:
        high = mid - 1
    
    return None

def ternary_search(students, score_to_find):
    low = 0
    high = len(students) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
    if students[mid1].score == score_to_find:
        return students[mid1]
    if students[mid2].score == score_to_find:
        return students[mid2]
    
    if score_to_find < students[mid1].score:
        high = mid1 - 1
    elif score_to_find > students[mid2].score:
        low = mid2 + 1
    else:
        low = mid1 + 1
        high = mid2 - 1
    
    return None

def create_student_list():
    students = []
    num_students = int(input("Nhap so luong sinh vien: "))
    
    for i in range(num_students):
        print(f"Nhap thong tin sinh vien thu {i + 1}: ")
        id = float(input("ID: "))
        name = input("Name: ")
        score = float(input("Score: "))
        students.append(Student(id, name, score))
        
    return students

if __name__ == "__main__":
    students = create_student_list()
    sorted_students = sorted(students, key=lambda s: s.score)
    x=float(input("Nhap diem can tim: "))
    
    result_linear = linear_search(students, x)
    if result_linear:
        print(f"Sinh vien co diem bang tim kiem tuyen tinh {x} la: {result_linear}")
    else:
        print(f"Khong tim thay sinh vien co diem {x}")
        
    result_binary = binary_search(students, x)
    
    if result_binary:
        print(f"Sinh vien co diem bang tim kiem nhi phan {x} la: {result_binary}")
    else:
        print(f"Khong tim thay sinh vien co diem {x}")
        
    result_ternary = ternary_search(students, x)
    if result_ternary:
        print(f"Sinh vien co diem bang tim kiem tam phan {x} la: {result_ternary}")
    else:
        print(f"Khong tim thay sinh vien co diem {x}")