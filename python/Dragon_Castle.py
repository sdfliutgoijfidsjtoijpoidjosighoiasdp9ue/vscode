print("Bạn đang ở trong một căn phòng tối nằm trong một lâu đài bí hiểm.")
print("Có ba cánh cửa trước mặt bạn. Hãy chọn 1 cánh cửa để thám hiểm")
playerChoice = input("Hãy chọn 1,2 hoặc 3.")
if playerChoice == "1":
    print("Bạn đã thắng cuộc. Trò chơi kết thúc!")
elif playerChoice == "2":
    print("Yêu tinh đã nuốt chửng bạn, bạn đã thua!")
elif playerChoice == "3":
    print("Bạn đã bình rồng ăn thịt. Bạn đã thua!")
else:
    print("Vui lòng chọn 1 số từ 1 đến 3.")
print("Khởi động lại trò chơi để thám hiểm nữa nào!")