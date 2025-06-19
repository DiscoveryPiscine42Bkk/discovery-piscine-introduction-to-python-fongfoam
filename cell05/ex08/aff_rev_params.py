import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรม aff_rev_params.py:
    - แสดงพารามิเตอร์ทั้งหมดในลำดับย้อนกลับ แต่ละพารามิเตอร์ตามด้วยขึ้นบรรทัดใหม่
    - หากมีพารามิเตอร์น้อยกว่าสองตัว (ไม่รวมชื่อสคริปต์) จะแสดง "none"
    """
    actual_params = sys.argv[1:]
    if len(actual_params) < 2:
        print("none")
    else:
        for param in actual_params[::-1]:
            print(param) 
if __name__ == "__main__":
    main()