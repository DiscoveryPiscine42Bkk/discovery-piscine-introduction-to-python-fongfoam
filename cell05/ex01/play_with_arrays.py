def transform_array(original_array):
    """
    สร้างอาร์เรย์ใหม่โดยการเพิ่ม 2 ให้กับแต่ละองค์ประกอบของอาร์เรย์เดิม
    """
    new_array = []
    for number in original_array:
        new_array.append(number + 2)
    return new_array

# กำหนดอาร์เรย์เริ่มต้น (Original Array)
original_numbers = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างอาร์เรย์ใหม่โดยการเรียกใช้ฟังก์ชัน
new_numbers = transform_array(original_numbers)

# แสดงผลลัพธ์
print(f"Original array: {original_numbers}")
print(f"New array: {new_numbers}")