def display_menu():
    """แสดงเมนูหลักของโปรแกรม"""
    print("\n--- ระบบจัดการงานดูแลสัตว์ในฟาร์ม ---")
    print("1. เพิ่มงานใหม่")
    print("2. ดูงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปงานตามหมวดหมู่")
    print("5. ออกจากโปรแกรม")
    print("-----------------------------------")

def add_task(tasks):
    """เพิ่มงานใหม่เข้าไปในรายการ"""
    print("\n--- เพิ่มงานใหม่ ---")
    task_name = input("ป้อนชื่องาน (เช่น ให้อาหารไก่, ตรวจสุขภาพวัว): ")
    
    # กำหนดหมวดหมู่เริ่มต้น หรือให้ผู้ใช้เลือก
    print("เลือกหมวดหมู่งาน:")
    print("  1. ให้อาหาร")
    print("  2. ทำความสะอาด")
    print("  3. ตรวจสุขภาพ")
    print("  4. อื่นๆ")
    category_choice = input("ป้อนตัวเลขหมวดหมู่: ")

    category = "อื่นๆ" # หมวดหมู่เริ่มต้น
    if category_choice == '1':
        category = "ให้อาหาร"
    elif category_choice == '2':
        category = "ทำความสะอาด"
    elif category_choice == '3':
        category = "ตรวจสุขภาพ"
    
    tasks.append({"name": task_name, "category": category})
    print(f"เพิ่มงาน '{task_name}' (หมวดหมู่: {category}) เรียบร้อยแล้ว!")

def view_tasks(tasks):
    """แสดงรายการงานทั้งหมดที่มี"""
    print("\n--- รายการงานทั้งหมด ---")
    if not tasks:
        print("ยังไม่มีงานในรายการ")
        return

    for i, task in enumerate(tasks):
        print(f"{i + 1}. ชื่อ: {task['name']}, หมวดหมู่: {task['category']}")

def delete_task(tasks):
    """ลบงานออกจากรายการ"""
    print("\n--- ลบงาน ---")
    if not tasks:
        print("ยังไม่มีงานให้ลบ")
        return

    view_tasks(tasks) # แสดงรายการงานเพื่อให้ผู้ใช้เลือก
    try:
        task_index = int(input("ป้อนหมายเลขงานที่ต้องการลบ: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"ลบงาน '{removed_task['name']}' เรียบร้อยแล้ว!")
        else:
            print("หมายเลขงานไม่ถูกต้อง โปรดลองอีกครั้ง")
    except ValueError:
        print("อินพุตไม่ถูกต้อง กรุณาป้อนตัวเลข")

def summarize_tasks(tasks):
    """สรุปจำนวนงานตามหมวดหมู่"""
    print("\n--- สรุปงานตามหมวดหมู่ ---")
    if not tasks:
        print("ยังไม่มีงานให้สรุป")
        return

    category_counts = {}
    for task in tasks:
        category = task['category']
        category_counts[category] = category_counts.get(category, 0) + 1

    for category, count in category_counts.items():
        print(f"  - {category}: {count} งาน")

def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    farm_tasks = [] # รายการสำหรับเก็บงานต่างๆ

    while True:
        display_menu()
        choice = input("กรุณาเลือกเมนู (1-5): ")

        if choice == '1':
            add_task(farm_tasks)
        elif choice == '2':
            view_tasks(farm_tasks)
        elif choice == '3':
            delete_task(farm_tasks)
        elif choice == '4':
            summarize_tasks(farm_tasks)
        elif choice == '5':
            print("ออกจากโปรแกรม ขอบคุณที่ใช้งาน!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง โปรดเลือก 1-5")

if __name__ == "__main__":
    main()