import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรม scan_it.py:
    - รับสองพารามิเตอร์: คำหลัก (keyword) และสตริงที่จะค้นหา (search_string)
    - แสดงจำนวนครั้งที่คำหลักปรากฏในสตริง
    - หากจำนวนพารามิเตอร์ไม่เท่ากับ 2 หรือไม่พบคำหลัก จะแสดง "none"
    """
    if len(sys.argv) != 3:
        print("none")
        return
    keyword = sys.argv[1]
    search_string = sys.argv[2]
    count = search_string.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)
if __name__ == "__main__":
    main()