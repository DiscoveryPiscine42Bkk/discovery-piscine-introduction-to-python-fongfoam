import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรม count_it.py:
    - แสดงจำนวนพารามิเตอร์ที่รับเข้ามา
    - แสดงแต่ละพารามิเตอร์และความยาวของพารามิเตอร์นั้น
    - หากไม่มีพารามิเตอร์ใดๆ จะแสดง "none"
    """
    actual_params = sys.argv[1:]
    if not actual_params:
        print("none")
    else:
        print(f"parameters: {len(actual_params)}")
        for param in actual_params:
            print(f"{param}: {len(param)}")
if __name__ == "__main__":
    main()