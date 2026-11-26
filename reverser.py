def reverse_words(text: str) -> str:
    """กลับลำดับคำในข้อความ โดยตัดช่องว่างส่วนเกินออก"""
    words = text.split()
    return " ".join(words[::-1])


# ส่วนทดสอบฟังก์ชัน (ลบออกได้หากไม่ต้องการ)
if __name__ == "__main__":
    print(reverse_words("hello first year"))  # ผลลัพธ์: year first hello
    print(reverse_words("a  b"))              # ผลลัพธ์: b a