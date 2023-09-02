# 按间距中的绿色按钮以运行脚本。
def receipt():
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill?$ "))
    tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
    people = int(input("how many people to split the bill?"))

    return bill, tip, people


def calculate(bill, tip, people):
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    return final_amount


if __name__ == '__main__':
    bill, tip, people = receipt()
    final_amount = calculate(bill, tip, people)

    print(f"Each person should pay: ${final_amount}")