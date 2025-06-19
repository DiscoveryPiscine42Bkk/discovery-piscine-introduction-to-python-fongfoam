import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรมสำหรับนับจำนวนพารามิเตอร์
    """
    # sys.argv คือ list ที่เก็บพารามิเตอร์ทั้งหมดที่ส่งเข้ามา
    # โดยที่ sys.argv[0] คือชื่อไฟล์ของสคริปต์เอง
    # ดังนั้น จำนวนพารามิเตอร์จริงคือ len(sys.argv) - 1
    num_parameters = len(sys.argv) - 1
    
    print(f"Number of parameters: {num_parameters}.")

if __name__ == "__main__":
    main()