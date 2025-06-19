#!/usr/bin/env python3
import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรม:
    - ตรวจสอบจำนวนพารามิเตอร์
    - ถ้าเป็น 1 พารามิเตอร์ จะแปลงสตริงนั้นเป็นตัวพิมพ์ใหญ่แล้วแสดงผล
    - ถ้าจำนวนพารามิเตอร์ไม่ใช่ 1 จะแสดง "none"
    """
    num_parameters = len(sys.argv) - 1
    if num_parameters == 1:
        input_string = sys.argv[1]
        uppercase_string = input_string.upper()
        print(uppercase_string)
    else:
        print("none")
if __name__ == "__main__":
    main()