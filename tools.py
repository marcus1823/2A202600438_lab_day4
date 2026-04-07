from langchain_core.tools import tool

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}
HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham só:
    - origin: Thành phố khởi hành (VD: 'Hà Nội', 'Đà Nẵng', 'Hồ Chí Minh')
    - destination: Thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    Nếu không tìm thấy tuyến bay, trả về thng báo không có chuyến
    """

    #TODO: Sinh viên tự triển khai
    # - Tra cưứu FLIGHTS_DB với key (origin, destination)
    #- Nếu tìm thấy, định dạng danh sách chuyến bay dễ đọc, bao gốm giá tiền, giờ bay, hãng hàng không, hạng vé
    # - Nếu không tìm thấy, thử tra ngược (destination, origin) để kiểm tra xem có chuyến bay ngược không, nếu có thì trả về thông báo "Không có chuyến bay từ {origin} đến {destination}, nhưng có chuyến bay ngược lại."
    # - Nếu vẫn không tìm thấy, trả về thông báo "Không có chuyến bay từ {origin} đến {destination}."
    #- gợi ý: format giá tiền có dấu chấm phân cách (1.450.000đ)

    # Bắt đầu:
    key = (origin, destination)
    if key in FLIGHTS_DB:
        flights = FLIGHTS_DB[key]
        result = f"Có {len(flights)} chuyến bay từ {origin} đến {destination}:\n"
        for flight in flights:
            price_formatted = f"{flight['price']:,}đ".replace(",", ".")
            result += f"- Hãng: {flight['airline']}, Khởi hành: {flight['departure']}, Đến nơi: {flight['arrival']}, Giá: {price_formatted}, Hạng vé: {flight['class']}\n"
        return result
    else:
        reverse_key = (destination, origin)
        if reverse_key in FLIGHTS_DB:
            return f"Không có chuyến bay từ {origin} đến {destination}, nhưng có chuyến bay ngược lại."
        else:
            return f"Không có chuyến bay từ {origin} đến {destination}."



@tool
def search_hotels(city: str, max_price_per_night: int = 999999999) -> str:
    """
    Tìm kiếm khách sạn trong thành phố, có thể lịc theo giá tối đa mỗi đêm
    Tham số:
    - city: Tên thành phố cần tìm khách sạn (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    - max_price_per_night: Mức giá tối đa cho mỗi đêm (VNĐ) (mặc định là không giới hạn)
    Trả về danh sách phù hợp với tên, số sao, giá tiền, khu vực và đánh giá.
    Nếu không tìm thấy khách sạn nào phù hợp, trả về thông báo không có khách sạn.
    """

    """
    Todo: Sinh viên tự triển khai
    # - Tra cưứu HOTELS_DB[city] để lấy danh sách khách sạn trong thành phố
    # - Lọc danh sách khách sạn theo max_price_per_night
    # - Sắp xếp theo rating giảm dần
    # - Định dạng kết quả trả về dễ đọc, bao gồm tên khách sạn, số sao, giá tiền, khu vực và đánh giá
    # - Nếu không tìm thấy khách sạn nào phù hợp, trả về thông báo "Không có khách sạn nào phù hợp ở {city} với mức giá tối đa {max_price_per_night}đ hoặc giá dưới Y/đêm hãy thử tăng ngân sách "
    """

    if city in HOTELS_DB:
        hotels = HOTELS_DB[city]
        filtered_hotels = [hotel for hotel in hotels if hotel["price_per_night"] <= max_price_per_night]
        sorted_hotels = sorted(filtered_hotels, key=lambda x: x["rating"], reverse=True)

        if sorted_hotels:
            result = f"Có {len(sorted_hotels)} khách sạn phù hợp ở {city} với mức giá tối đa {max_price_per_night}đ:\n"
            for hotel in sorted_hotels:
                price_formatted = f"{hotel['price_per_night']:,}đ".replace(",", ".")
                result += f"- Tên: {hotel['name']}, Số sao: {hotel['stars']}, Giá: {price_formatted}/đêm, Khu vực: {hotel['area']}, Đánh giá: {hotel['rating']}\n"
            return result
        else:
            return f"Không có khách sạn nào phù hợp ở {city} với mức giá tối đa {max_price_per_night}đ hoặc giá dưới {max_price_per_night}đ/đêm hãy thử tăng ngân sách."
    else:
        return f"Không có khách sạn nào phù hợp ở {city}."

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ đi các khoản chi tiêu.
    Tham số:
    - total_budget: Ngân sách tổng ban đầu (VNĐ)
    - expenses: Chuỗi liệt kê các khoản chi tiêu, mỗi khoản cách nhau bằng dấu phẩy, định dạng "Mục tiêu: Số tiền" (VD: "Vé máy bay: 1.450.000đ, Khách sạn: 1.200.000đ")
    Trả về bảng bảng chi tiết các khoản chi tiêu và ngân sách còn lại sau khi trừ đi các khoản chi tiêu.
    Nếu vượt quá ngân sách, trả về thông báo cảnh báo "Ngân sách không đủ, bạn đã vượt quá ngân sách {total_budget}VNĐ."
    """

    #Todo: Sinh viên tự triển khai
    # - Parse chuỗi expenses thành dict {tên: số tiền}
    # - Tính tổng chi phí
    # - Tính tổng số tiền còn lại = total_bugdet - tổng chi phí
    # fornat bảng chi tiết:
    # Bảng chi phí:
    # - Vé máy bay: 1.450.000đ
    # - Khách sạn: 1.200.000đ
    # Tổng chi: 2.650.000đ
    # Ngân sách: 3.350.000đ
    # Còn lại: 700.000đ
    # - Nếu tổng chi phí vượt quá ngân sách, trả về thông báo cảnh báo "Vượt quá ngân sách X đồng, Cần điều chỉnh lại"
    # - Xử lý lỗi: nếu định dạng expenses không đúng, trả về thông báo lỗi rõ ràng "Định dạng chi tiêu không đúng, vui lòng sử dụng định dạng 'Mục tiêu: Số tiền' và cách nhau bằng dấu phẩy."

    try:
        expense_items = expenses.split(",")
        expense_dict = {}
        total_expense = 0

        for item in expense_items:
            name, amount_str = item.split(":")
            name = name.strip()
            amount_str = amount_str.strip().replace(".", "").replace("đ", "")
            amount = int(amount_str)
            expense_dict[name] = amount
            total_expense += amount

        remaining_budget = total_budget - total_expense

        result = "Bảng chi phí:\n"
        for name, amount in expense_dict.items():
            amount_formatted = f"{amount:,}đ".replace(",", ".")
            result += f"- {name}: {amount_formatted}\n"

        total_expense_formatted = f"{total_expense:,}đ".replace(",", ".")
        remaining_budget_formatted = f"{remaining_budget:,}đ".replace(",", ".")

        result += f"Tổng chi: {total_expense_formatted}\n"
        result += f"Ngân sách: {total_budget:,}đ\n"
        result += f"Còn lại: {remaining_budget_formatted}\n"

        if total_expense > total_budget:
            result += f"Vượt quá ngân sách {total_budget:,}đ, Cần điều chỉnh lại."

        return result
    except Exception as e:
        return "Định dạng chi tiêu không đúng, vui lòng sử dụng định dạng 'Mục tiêu: Số tiền' và cách nhau bằng dấu phẩy."