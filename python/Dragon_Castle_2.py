import random

exitChoice = " "

while exitChoice != "Thoát":

    print("Bạn đang ở trong một căn phòng tối nằm trong một lâu đài bí hiểm.")

    print("Có bốn cánh cửa trước mặt bạn. Hãy chọn 1 cánh cửa để thám hiểm")

    playerChoice = input("Hãy chọn 1,2,3 hoặc 4.")

    if playerChoice == "1":

        print("Bạn đã thắng cuộc. Trò chơi kết thúc!")

    elif playerChoice == "2":

        print("Yêu tinh đã nuốt chửng bạn, bạn đã thua!")

    elif playerChoice == "3":

        print("Bạn bước vào căn phòng và thấy một con rồng đang ngủ.")

        print("Bạn có thể:")

        print("1) Ăn trộm vàng của rồng")

        print("2) Thử đi qua con rồng để tới cửa ra")

        dragonChoice = input("Điền 1 hoặc 2.\n")

        if dragonChoice == "1":

            print("Con rồng thức giấc và nuốt chửng bạn luôn. Ái chà chà ngon quá!")

            print("Bạn đã thua, trò chơi kết thúc!")

        elif dragonChoice == "2":

            print("Bạn rón rén đi vòng qua rông và thoát khỏi toà lâu đài. Xin chào ánh mặt trời!")

            print("Bạn đã thắng cuộc. Trò chơi kết thúc!")

        else:

            print("Xin lỗi, bạn đã không chọn 1 hoặc 2.")

    elif playerChoice == "4":

        print("Căn phòng bạn nước vào có một con nhân sư")

        print("Nhân sư bắt bạn phải đoán được con số nó đang nghĩ đến, số đó nằm trong khoảng từ 1 đến 10.")

        number = input("Bạn chọn số nào? ")

        if number == random.randint(1, 10):

            print("Nhân sư gầm lên đầy thất vọng, bạn đã đoán đúng.")

            print("Nhân sư phải thả bạn đi"
           )

            print("Bạn đã chiến thắng, trò chơi kết thúc!")

        else:

            print("Nhân sư nói đáp án của bạn không chính xác.")

            print("Bạn trở thành tù nhân của nó mãi mãi.")

            print("Bạn đã thua, trò chơi kết thúc")

    else:
            print("Xin lỗi, bạn đã không chọn 1,2,3 hoặc 4.")
            exitChoice = input("Ấn ENTER để chơi lại. Gõ THOÁT để đóng trò chơi.") 