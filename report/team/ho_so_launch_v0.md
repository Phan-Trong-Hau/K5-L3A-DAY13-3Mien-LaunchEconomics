# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm 3Mien · Lớp L3A · Phạm vi đề xuất gồm yêu cầu nội địa và hàng nặng tại 12 depot.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: 4.472 đ trên mỗi việc thành công (978 việc). Trong phạm vi pilot: 4.599 đ/việc sau khi cộng chi phí cố định, ở quy mô 45.000 yêu cầu/tháng. [A2, A4](bang_chi_phi.md) | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Gấp đôi số ca làm lại: +51,8%. Gấp đôi xem lại: +40,7%. Lương tăng 25%: +23,1%. [B1–B2](bang_chi_phi.md#b1--đổi-từng-yếu-tố) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Toàn mẫu, giới hạn hai lần chạy: 6.901.220 đ / 1.200 yêu cầu ≈ 5.751 đ/yêu cầu (~48% của 12.000 đ), đã tính 234 ca nhân viên xử lý thay. [B3](bang_chi_phi.md#b3--giới-hạn-chạy-lại-có-thật-sự-rẻ-hơn) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng và an toàn | Đóng trong 24 giờ và không mở lại trong 7 ngày: 82,83%. Sửa hoặc bỏ gợi ý trong số ca được xem lại: 27,12%. Mở lại trong 7 ngày: 4,25%. [E1](chi_so.md) | Xong, có bằng chứng | Người phụ trách chỉ số |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 19/20 ca (95%). Có cách khắc phục cho 5 loại lỗi. Ưu tiên khóa chống hoàn trùng và đối soát sổ cái. [Bảng lỗi](bang_loi.md) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | 20 nhân viên/nhóm, MDE 6 điểm phần trăm, tối thiểu 299 yêu cầu đủ điều kiện/người, ba luật dừng. Ngày quyết định theo kế hoạch: 05/01/2027. [Kế hoạch pilot](pilot_plan.yaml) | Xong, có bằng chứng | Người viết code sau giải lao |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ/việc thành công trên toàn mẫu. Trong phạm vi pilot, xem lại toàn bộ gợi ý hợp lệ: 11.743–12.415 đ/việc tùy giả định thời gian làm lại. [E2](chi_so.md#e2--rủi-ro-kinh-tế) | Giả lập | Người kiểm số |

Điều kiện và mốc kiểm tra đề xuất, tính theo ngày khởi động pilot thực tế:

- **Ngày khởi động** — Kỹ sư dịch vụ sổ cái xác minh khóa chống hoàn trùng và đối soát giao dịch.
- **Ngày khởi động** — Giám đốc vận hành xác nhận mục tiêu 299 yêu cầu đủ điều kiện/người và chấp nhận MDE 6 điểm.
- **Cuối tuần 1** — Người phụ trách chỉ số kiểm tra các event có `trace_id` và cập nhật mô hình bằng số phút xem lại, làm lại đã đo.
- **Trước bước rollout 50%** — Trưởng nhóm CSKH đối chiếu tỷ lệ mở lại với luật dừng và chốt phương án giảm xem lại theo bậc.

**Đề xuất: Go có điều kiện** cho pilot nội địa và hàng nặng.
