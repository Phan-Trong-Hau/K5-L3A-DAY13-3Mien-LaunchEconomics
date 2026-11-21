# Báo cáo nhóm

## 1. Thông tin nhóm

- Nhóm 3Mien, lớp L3A.
- Thành viên và phân công theo checkpoint được ghi trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí và rủi ro của trợ lý hoàn phí LogiX-VN để quyết định có nên chạy pilot Gate 2a cho yêu cầu nội địa và hàng nặng. Phân tích dùng 1.200 yêu cầu trong dữ liệu lab, hai bộ nhãn lỗi độc lập và kế hoạch thử nghiệm có đối chứng.

## 3. Giải pháp

- **A–B:** lập mô hình chi phí, tách loại yêu cầu, tính cố định và độ nhạy; xem [bảng chi phí](bang_chi_phi.md), [code](../../src/lab13.py).
- **C:** Huy và Thái gắn nhãn độc lập 20 ca, đối chiếu và thống nhất ca lệch; lập cách phát hiện, khắc phục cho 5 loại lỗi trong [bảng lỗi](bang_loi.md).
- **D:** đề xuất chia ngẫu nhiên theo nhân viên, có đối chứng, cỡ mẫu, kiểm tra lưu lượng theo nhân viên và 4 luật dừng trong [pilot plan](pilot_plan.yaml).
- **E:** đặc tả chỉ số, event có `trace_id` và rủi ro kinh tế trong [chỉ số](chi_so.md); tổng hợp 7 mục, trạng thái, vai trò và đề xuất trong [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

- Chi phí toàn mẫu: **4.472 đ/việc thành công** (simulated), gấp **16,3 lần** hóa đơn token và tool chia số yêu cầu. Phạm vi `noi_dia` + `hang_nang` có chi phí gồm cố định **4.599 đ/việc** ở 45.000 yêu cầu/tháng (simulated), so với mốc thủ công 12.000 đ.
- Ba yếu tố nhạy nhất: làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% **+23,1%** (simulated). Xem lại 100% có thể lên **12.415 đ/việc** (simulated), vượt mốc thủ công.
- Bảng lỗi: **19/20 = 95%** đồng thuận ban đầu; ca 13 thống nhất **Giới hạn hệ thống**; có khắc phục cho **5/5 loại**.
- Chỉ số toàn mẫu: đóng 24 giờ, không mở lại 7 ngày **82,83%**; sửa/bỏ gợi ý **27,12%**; mở lại **4,25%**. Đây là số liệu lab, chưa chứng minh tác động của trợ lý.
- Pilot đề xuất **20 nhân viên/nhóm**, **299 yêu cầu/người**, tương đương **5.980 yêu cầu/nhóm**, mẫu hiệu dụng **859,20**; MDE 6 điểm phần trăm, power 0,80; giai đoạn phân tích chính **21 ngày** (~570 yêu cầu đủ điều kiện/ngày), ngày quyết định **26/01/2027**.
- **Đề xuất: Go có điều kiện** cho kế hoạch pilot trong phạm vi đã chọn. Trước bật phải kiểm chứng chống hoàn trùng, ghi sổ, event, roster 40 người/12 depot và lưu lượng thực tế 4 tuần theo từng nhân viên; sau đó đo phút thật, kiểm soát an toàn và chi phí theo các cổng của hồ sơ launch.
- **Duyệt chéo: Chờ hội đồng.** Chưa có điểm, quyết định hoặc phản hồi; [phiếu chấm](phieu_cham.md) chỉ hoàn thiện khi nhận hồ sơ nhóm được giao.

## 5. Khó khăn và cách xử lý

Với 20 nhân viên mỗi nhóm và ICC 0,02, mức cỡ mẫu hiệu dụng tối đa là 1.000 mỗi nhóm, dưới mức khoảng 1.250 cần để phát hiện chênh lệch 5 điểm phần trăm. Kế hoạch chuyển sang mức 6 điểm và đặt mục tiêu ít nhất 299 yêu cầu đủ điều kiện mỗi nhân viên. Với lỗi gắn nhãn, hai người giữ bộ nhãn ban đầu và ghi quy tắc phân biệt cho ca 13 sau khi đối chiếu.

## 6. Tổng hợp đóng góp

- **Phan Trọng Hâu:** Code A–B, rủi ro kinh tế E2 và tổng hợp hai hồ sơ.
- **Ngô Đức Thịnh:** Bảng chi phí, tính cỡ mẫu D1 và kế hoạch pilot.
- **Bùi Gia Huy:** Gắn nhãn, tổng hợp bảng lỗi và đặc tả chỉ số, event.
- **Vũ Quang Thái:** Gắn nhãn độc lập và đối chiếu kết quả CP3 cùng Huy.

## 7. Hạn chế và hướng cải thiện

Phút xem lại/làm lại còn giả lập; ngưỡng an toàn và lịch pilot là đề xuất. CSV chỉ có 20 nhân viên tại 6 depot (tải mẫu lệch 39–73 yêu cầu đủ điều kiện/người), chưa chứng minh đủ roster 40 người tại 12 depot và lưu lượng thực tế theo nhân viên. Cần xác nhận nguồn lực và lưu lượng thực tế theo nhân viên (hoặc chốt kéo dài giai đoạn chính trước khi bật), đo phút thật, triển khai event và theo dõi đủ cửa sổ trước kết luận. Thịnh đã chạy lại kiểm tra `src/lab13.py` trên máy khác với máy viết code CP1; nhóm rà bản nộp và mỗi thành viên tự nộp link repo trên LMS.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức của lab](../../docs/du_lieu_va_cong_thuc.md)
- [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- [Script tái lập kết quả](../../src/lab13.py)
