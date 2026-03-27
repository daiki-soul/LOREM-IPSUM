#GROUP 3 CASE STUDY BILLING SYSTEM

#WATER RATES
WATER_TIERS = [
    (10, 29.00),
    (20, 47.57),                 #RATES RESEARCHED FROM OFFICIAL PHILIPPINES UTILITY BILLS RATES!
    (30, 58.30),
    (float('inf'), 65.62),
]
WATER_SEWERAGE_RATE = 0.50
WATER_ENV_CHARGE = 2.00
WATER_VAT_RATE = 0.12

#ELECTRICITY RATES
ELEC_RATE_PER_KWH = 10.95
ELEC_DISTRIBUTION = 0.175
ELEC_TRANSMISSION = 0.101
ELEC_SYSTEM_LOSS = 0.057
ELEC_TAXES = 0.117
ELEC_LIFELINE_LIMIT = 100
ELEC_LIFELINE_DISC = 0.05

session_records = []
total_bills_issued = 0
total_revenue = 0.0

print("="*56)
print("     PHILIPPINE UTILITY BILLING SYSTEM")
print("     Water (Maynilad/Manila Water) | Electric (Meralco)")
print("="*56)

#THE LOOP OFFICAILLY STARTS HERE
while True:
    print("\n  Select Utility Type:")
    print("  [1] Water Billing")
    print("  [2] Electric Billing")
    print("  [3] Session Summary")
    print("  [0] Exit")
    print("-"*56)

    choice = input("  Enter choice: ").strip()
    if choice == "0":
        break

    if choice not in ["1", "2", "3"]:
        print("  Invalid choice. Try again.")
        continue

    if choice == "3":
        if len(session_records) == 0:
            print("  No billing records yet.")
        else:
            print("="*56)
            print("             SESSION SUMMARY")
            print("="*56)
            for i, rec in enumerate(session_records, 1):
                util_label = "WATER" if rec["type"] == "water" else "ELEC "
                print(f"  {i:2d}. [{util_label}] {rec['name']:<25} PHP {rec['total']:10.2f}")
            print("="*56)
            print(f"  Total Bills Issued : {total_bills_issued}")
            print(f"  Total Revenue      : PHP {total_revenue:.2f}")
            print("="*56)
        continue

    #CUSTOMER INFO
    #PUT TRY/EXCEPT HERE TY
    try:
        name = input("  Account Name     : ").strip().title()
        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain letters only!")
        account_no = input("  Account No.      : ").strip()
        if not account_no.isdigit():
            raise ValueError("Account number must contain digits only!")
    except ValueError as e:
        print(f"  Input Error: {e}")
        continue

    #METER READINGS
    unit = "cubic. per.m." if choice == "1" else "kWh"
    try:
        prev_read = float(input(f"  Previous Reading ({unit}): "))
        curr_read = float(input(f"  Current Reading ({unit}): "))
        if prev_read < 0 or curr_read < 0 or curr_read < prev_read:
            raise ValueError("Readings cannot be negative and current >= previous.")
        consumption = curr_read - prev_read
        if consumption == 0:
            print("  Consumption is 0. No bill to generate.")
            continue
    except ValueError as e:
        print(f"  Reading Error: {e}")
        continue

    #WATER BILL CALCULATIONS
    if choice == "1":
        remaining = consumption
        basic_charge = 0
        prev_limit = 0
        for limit, rate in WATER_TIERS:
            if remaining <= 0:
                break
            tier_usage = min(remaining, limit - prev_limit)
            basic_charge += tier_usage * rate
            remaining -= tier_usage
            prev_limit = limit

        sewerage = round(basic_charge * WATER_SEWERAGE_RATE, 2)
        env_charge = WATER_ENV_CHARGE
        subtotal = round(basic_charge + sewerage + env_charge, 2)
        vat = round(subtotal * WATER_VAT_RATE, 2)
        total = round(subtotal + vat, 2)


        #RESIBO WATER
        print("="*56)
        print("          WATER UTILITY BILLING STATEMENT")
        print("="*56)
        print(f"  Account Name    : {name.upper()}")
        print(f"  Account No.     : {account_no}")
        print("-"*56)
        print(f"  Previous Reading: {prev_read:>10.0f} cu.m.")
        print(f"  Current Reading : {curr_read:>10.0f} cu.m.")
        print(f"  Consumption     : {consumption:>10.0f} cu.m.")
        print("-"*56)
        print("  CHARGES BREAKDOWN:")
        print(f"  Basic Water Charge  : PHP {basic_charge:10.2f}")
        print(f"  Sewerage Charge(50%): PHP {sewerage:10.2f}")
        print(f"  Environmental Charge: PHP {env_charge:10.2f}")
        print(f"  VAT (12%)           : PHP {vat:10.2f}")
        print("-"*56)
        print(f"  TOTAL AMOUNT DUE    : PHP {total:10.2f}")
        print("="*56)

    #ELECTRICITY CALCULATIONS
    else:
        generation = round(consumption * ELEC_RATE_PER_KWH, 2)
        distribution = round(generation * ELEC_DISTRIBUTION, 2)
        transmission = round(generation * ELEC_TRANSMISSION, 2)
        system_loss = round(generation * ELEC_SYSTEM_LOSS, 2)
        subtotal = round(generation + distribution + transmission + system_loss, 2)
        taxes = round(subtotal * ELEC_TAXES, 2)
        total = round(subtotal + taxes, 2)
        discount = 0
        if consumption <= ELEC_LIFELINE_LIMIT:
            discount = round(total * ELEC_LIFELINE_DISC, 2)
            total = round(total - discount, 2)

        #RESIBO KURYENTE
        print("="*56)
        print("        ELECTRIC UTILITY BILLING STATEMENT")
        print("="*56)
        print(f"  Account Name    : {name.upper()}")
        print(f"  Account No.     : {account_no}")
        print("-"*56)
        print(f"  Previous Reading: {prev_read:>10.0f} kWh")
        print(f"  Current Reading : {curr_read:>10.0f} kWh")
        print(f"  Consumption     : {consumption:>10.0f} kWh")
        if consumption <= ELEC_LIFELINE_LIMIT:
            print("  ** LIFELINE CUSTOMER — 5% discount applied **")
        print("-"*56)
        print("  CHARGES BREAKDOWN:")
        print(f"  Generation Charge   : PHP {generation:10.2f}")
        print(f"  Distribution (17.5%): PHP {distribution:10.2f}")
        print(f"  Transmission (10.1%): PHP {transmission:10.2f}")
        print(f"  System Loss + FIT   : PHP {system_loss:10.2f}")
        print(f"  Taxes (VAT + others): PHP {taxes:10.2f}")
        if discount > 0:
            print(f"  Lifeline Discount   : PHP {discount:10.2f}  (-)")
        print("-"*56)
        print(f"  TOTAL AMOUNT DUE    : PHP {total:10.2f}")
        print("="*56)

    #PAYMENT
    try:
        payment = float(input("  Enter payment amount (PHP): "))
        if payment <= 0:
            raise ValueError("Payment must be positive.")
    except ValueError as e:
        print(f"  Payment Error: {e}. Skipping payment.")
        continue

    if payment >= total:
        print(f"  Payment accepted! Amount Paid: PHP {payment:.2f}")
        print(f"  Change: PHP {round(payment - total,2):.2f}")
    else:
        print(f"  Insufficient payment! Balance Due: PHP {round(total - payment,2):.2f}")

    total_bills_issued += 1
    total_revenue += total
    util_type = "water" if choice == "1" else "electric"
    session_records.append({"type": util_type, "name": name, "total": total})

    again = input("  Process another bill? (yes/no): ").strip().lower()
    if again == "no":
        break

#FINAL RESIBO
print("="*56)
print("THANK YOU FOR USING THE UTILITY BILLING SYSTEM.".upper())
print("="*56)
print(f"  Total Bills Issued  : {total_bills_issued}")
print(f"  Total Revenue       : PHP {total_revenue:.2f}")
water_count = sum(1 for r in session_records if r["type"]=="water")
elec_count = total_bills_issued - water_count
print(f"  Water Bills Issued  : {water_count}")
print(f"  Electric Bills Issued: {elec_count}")
if total_bills_issued == 0:
    print("  No transactions processed this session.")
elif total_bills_issued <= 5:
    print("  Low volume session.")
else:
    print("  High volume session. Great work!")
print("="*56)











#test