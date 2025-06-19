def filter_and_transform_array(original_array):
    """
    สร้างอาร์เรย์ใหม่โดยการเพิ่ม 2 ให้กับแต่ละองค์ประกอบของอาร์เรย์เดิม
    แล้วกรองเฉพาะตัวเลขที่มีค่ามากกว่า 5 เท่านั้น
    """
    new_array = []
    for number in original_array:
        transformed_number = number + 2
        # ตรวจสอบว่าตัวเลขที่แปลงแล้วมีค่ามากกว่า 5 หรือไม่
        if transformed_number > 5:
            new_array.append(transformed_number)
    return new_array

# กำหนดอาร์เรย์เริ่มต้น (Original Array)
original_numbers = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างอาร์เรย์ใหม่โดยการเรียกใช้ฟังก์ชันและกรองค่า
new_numbers = filter_and_transform_array(original_numbers)

# แสดงผลลัพธ์
print(f"Original array: {original_numbers}")
print(f"New array: {new_numbers}")