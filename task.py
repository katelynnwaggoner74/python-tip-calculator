print("Welcome try my tip calculator!")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to leave? 10 12 15 "))
people = int(input("How many people are spitting the bill? "))
tip_percent = tip / 100
total_tip= bill * tip_percent
total_bill = total_tip + bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount:.2f}")


