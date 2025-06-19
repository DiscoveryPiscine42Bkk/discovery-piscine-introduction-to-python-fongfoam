def filter_transform_and_unique_array(original_array):
    """
    สร้างอาร์เรย์ใหม่โดยการเพิ่ม 2 ให้กับแต่ละองค์ประกอบของอาร์เรย์เดิม,
    กรองเฉพาะตัวเลขที่มีค่ามากกว่า 5, และไม่แสดงเลขซ้ำกัน
    """
    # ใช้ set เพื่อเก็บตัวเลขที่ไม่ซ้ำกัน
    # set เป็นโครงสร้างข้อมูลที่เก็บได้แค่ค่าที่ไม่ซ้ำกันเท่านั้น
    unique_transformed_numbers = set()
    
    for number in original_array:
        transformed_number = number + 2
        # ตรวจสอบว่าตัวเลขที่แปลงแล้วมีค่ามากกว่า 5 หรือไม่
        if transformed_number > 5:
            unique_transformed_numbers.add(transformed_number) # เพิ่มเข้า set

    # แปลง set กลับไปเป็น list เพื่อให้ได้รูปแบบที่ต้องการ
    # หรือจะส่งคืนเป็น set เลยก็ได้ขึ้นอยู่กับการใช้งาน
    return unique_transformed_numbers

# กำหนดอาร์เรย์เริ่มต้น (Original Array)
original_numbers = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างอาร์เรย์ใหม่โดยการเรียกใช้ฟังก์ชันและกรองค่าพร้อมกำจัดเลขซ้ำ
new_numbers_set = filter_transform_and_unique_array(original_numbers)

# แสดงผลลัพธ์
print(f"Original array: {original_numbers}")
print(f"New array: {new_numbers_set}")