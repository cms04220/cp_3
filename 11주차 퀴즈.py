def v_resident_registration_number(rrn, mult):
    to = 0

    for i in range(12):
        to += int(rrn[i]) * mult[i]

    remainder = to % 11
    ck_number = 11 - remainder


    if ck_number >= 10:
        ck_number %= 10

    return ck_number

resident_registration = input("주민등록번호를 입력하세요: ")

resident_registration_number = resident_registration.replace('-', '')

multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

ck = v_resident_registration_number(resident_registration_number, multipliers)

if ck == int(resident_registration_number[12]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")