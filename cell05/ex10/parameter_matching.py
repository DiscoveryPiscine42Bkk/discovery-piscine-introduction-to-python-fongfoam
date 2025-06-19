import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรม parameter_matching.py:
    - ตรวจสอบจำนวนพารามิเตอร์ที่ได้รับ
    - หากมี 1 พารามิเตอร์ จะให้ผู้ใช้ป้อนคำและเปรียบเทียบกับพารามิเตอร์ที่ส่งมา
    - หากจำนวนพารามิเตอร์ไม่ใช่ 1 จะแสดง "none"
    """
    if len(sys.argv) == 2:
        expected_parameter = sys.argv[1]
        user_input = input("What was the parameter? ")
        if user_input == expected_parameter:
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")
if __name__ == "__main__":
    main()