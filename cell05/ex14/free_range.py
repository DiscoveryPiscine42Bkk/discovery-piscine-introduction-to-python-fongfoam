import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรม free_range.py:
    - รับพารามิเตอร์สองตัวที่เป็นตัวเลข
    - สร้างและแสดงอาร์เรย์ที่มีค่าทั้งหมดระหว่างสองตัวเลขนั้น (รวมทั้งสองตัวเลข)
    - หากจำนวนพารามิเตอร์ไม่เท่ากับ 2 จะแสดง "none"
    """
    # len(sys.argv) จะเท่ากับ 3
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result_array = list(range(num1, num2 + 1))
        print(result_array)
        
    except ValueError:
        print("none") 

if __name__ == "__main__":
    main()