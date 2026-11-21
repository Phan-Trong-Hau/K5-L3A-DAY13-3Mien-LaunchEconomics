# Báo cáo nhóm

## 1. Thông tin nhóm

- Nhóm 3Mien, lớp L3A.
- Thành viên và phân công theo checkpoint được ghi trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí và rủi ro của trợ lý hoàn phí LogiX-VN để quyết định có nên chạy pilot Gate 2a cho yêu cầu nội địa và hàng nặng. Phân tích dùng 1.200 yêu cầu trong dữ liệu lab, hai bộ nhãn lỗi độc lập và kế hoạch thử nghiệm có đối chứng.

## 3. Giải pháp

| Nhiệm vụ | Cách làm và bằng chứng |
| --- | --- |
| A · Chi phí | Cộng token và tool trên mọi lần chạy, kể cả lần lỗi, rồi cộng chi phí xem lại và làm lại trước khi chia cho số yêu cầu thành công. Tách theo loại yêu cầu và tính thêm chi phí cố định cho phạm vi pilot. [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Đổi từng đầu vào, thử kịch bản kết hợp và tính cả chi phí nhân viên xử lý thay ở giới hạn 1–3 lần chạy. [Bảng độ nhạy](bang_chi_phi.md#b1--đổi-từng-yếu-tố) |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca, xử lý ca lệch nhãn và đề xuất cách phát hiện, khắc phục cho năm loại lỗi. [Bảng lỗi](bang_loi.md) |
| D · Pilot | Chia ngẫu nhiên theo nhân viên, phân tầng theo depot, dùng đối chứng đồng thời và đặt trước ba luật dừng. [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và rủi ro | Tính thử ba chỉ số, đặc tả các event có `trace_id` và đưa kết quả độ nhạy vào quyết định pilot. [Chỉ số và rủi ro](chi_so.md) · [Hồ sơ launch v0](ho_so_launch_v0.md) |

## 4. Kết quả

- Chi phí cơ sở là **4.472 đ/việc thành công** (simulated) trên 978 việc thành công. Giới hạn hai lần chạy cho tổng chi phí hệ thống thấp nhất trong ba kịch bản, **6.901.220 đ/1.200 yêu cầu** (simulated).
- Chỉ số chính, tỷ lệ sửa hoặc bỏ gợi ý trong số yêu cầu được xem lại và tỷ lệ mở lại trong 7 ngày lần lượt là **82,83%**, **27,12%** và **4,25%** trong dữ liệu chạy thử. Hai bộ nhãn lỗi đồng thuận **19/20 ca (95%)**.
- Hồ sơ đề xuất **Go có điều kiện** cho pilot nội địa và hàng nặng. Repo hiện chưa có kết quả hội đồng duyệt chéo dành cho nhóm.

## 5. Khó khăn và cách xử lý

Với 20 nhân viên mỗi nhóm và ICC 0,02, mức cỡ mẫu hiệu dụng tối đa là 1.000 mỗi nhóm, dưới mức khoảng 1.250 cần để phát hiện chênh lệch 5 điểm phần trăm. Kế hoạch chuyển sang mức 6 điểm và đặt mục tiêu ít nhất 299 yêu cầu đủ điều kiện mỗi nhân viên. Với lỗi gắn nhãn, hai người giữ bộ nhãn ban đầu và ghi quy tắc phân biệt cho ca 13 sau khi đối chiếu.

## 6. Tổng hợp đóng góp

- **Phan Trọng Hâu:** Code A–B, rủi ro kinh tế E2 và tổng hợp hai hồ sơ.
- **Ngô Đức Thịnh:** Bảng chi phí, tính cỡ mẫu D1 và kế hoạch pilot.
- **Bùi Gia Huy:** Gắn nhãn, tổng hợp bảng lỗi và đặc tả chỉ số, event.
- **Vũ Quang Thái:** Gắn nhãn độc lập và đối chiếu kết quả CP3 cùng Huy.

## 7. Hạn chế và hướng cải thiện

Dữ liệu chạy thử thiếu nhóm đối chứng để ước lượng tác động của trợ lý. Chi phí nhân công hiện dựa trên số phút giả lập. Pilot cần đo phút xem lại và làm lại thực tế, theo dõi tỷ lệ mở lại và đối soát sổ cái. Nếu mọi gợi ý hợp lệ đều phải xem lại và làm lại mất 15,3 phút/ca, chi phí mô hình lên **12.415 đ/việc thành công** (simulated), vượt mốc 12.000 đ của nhân viên tự làm.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức của lab](../../docs/du_lieu_va_cong_thuc.md)
- [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- [Script tái lập kết quả](../../src/lab13.py)
