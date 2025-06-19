import sys

def main():
    """
    ฟังก์ชันหลักของโปรแกรม string_are_arrays.py:
    - รับสตริงหนึ่งตัวเป็นพารามิเตอร์
    - แสดง 'z' สำหรับทุกการปรากฏของตัวอักษร 'z' (ตัวพิมพ์เล็ก) ในสตริงนั้น
    - หากจำนวนพารามิเตอร์ไม่เท่ากับ 1 หรือไม่พบตัวอักษร 'z' จะแสดง "none"
    """
    if len(sys.argv) != 2:
        print("none")
        return
    search_string = sys.argv[1]
    z_count = 0
    for char in search_string:
        if char == 'z':
            print("z") 
            z_count += 1
    if z_count == 0:
        print("none")
if __name__ == "__main__":
    main()