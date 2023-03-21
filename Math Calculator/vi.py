def VI_ver():
    print("Bạn muốn tính toán hình học hay hoá học? Chọn [Hình/Hoá] ")
    typeChoice = input("\n=>  ")
    if str(typeChoice) == "Hình":
        VI_ver_hh()
    elif str(typeChoice) == "Hoá":
        VI_ver_h()
def VI_ver_hh():
    print("Bạn muốn tính diện tích hay chu vì hình? [Diện tích/ Chu vi] ")
    ChuVi_DienTich = input("\n=>  ")
    if ChuVi_DienTich == "Diện tích":
        print("Bạn muốn tính diện tích của hình gì?  [Tam giác, Vuông, Chữ nhật, Bình hành, Tam giác đều, Thang] ")
        areaChoice = input("\n=>  ")
        if str(areaChoice) == "Tam giác":
            print("Chiều cao của hình là?")
            height_triang = input("\n=>  ")
            print("Độ dài cạnh của hình là? ")
            width_triang = input("\n=>  ")
            print("Cảnh báo! Bạn phải sử dụng cùng 1 đơn vị đo độ dài!")
            print("Bạn có muốn chọn lại chiều cao và độ dài cạnh? [Có HOẶC Không]")
            Choice = input("\n=>  ")
            if Choice == "Có":
              triang_area()
            elif Choice == "Không":
                print("Bắt đầu tính...\n")
                AREA_RESULT = (int(height_triang) * int(width_triang)) // 2
                print("Kết quả là: ", AREA_RESULT)