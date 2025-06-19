import sys
def main():
    """
    ฟังก์ชันหลักของโปรแกรม append_it.py:
    - แสดงพารามิเตอร์แต่ละตัวที่ต่อท้ายด้วย "ism"
    - ข้ามพารามิเตอร์ที่ลงท้ายด้วย "ism" อยู่แล้ว
    - หากไม่มีพารามิเตอร์ จะแสดง "none"
    """
    actual_params = sys.argv[1:]
    if not actual_params:
        print("none")
        return
    for param in actual_params:
        if not param.endswith("ism"):
            print(f"{param}ism")
if __name__ == "__main__":
    main()