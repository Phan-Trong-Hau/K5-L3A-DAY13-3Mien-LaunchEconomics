# Báo cáo nhóm

Báo cáo CP1–CP5 ngày 21/11/2026; phần duyệt chéo chờ hội đồng. Toàn bộ dữ liệu lab là giả lập; chi phí dùng phút `_simulated` được ghi nhãn `simulated`.

## 1. Thông tin nhóm

- Tên nhóm: 3Mien
- Lớp: L3A
- Thành viên và phân công: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đánh giá tính khả thi kinh tế và thiết kế pilot trợ lý hoàn phí LogiX-VN. Nhóm tổng hợp chi phí từ mọi lần chạy, kể cả lần lỗi, rồi chia cho số việc thành công; phân tích độ nhạy, phân loại lỗi độc lập và thiết kế đối chứng trước khi đề xuất Gate 2a.

## 3. Giải pháp

- **A–B:** lập mô hình chi phí, tách loại yêu cầu, tính cố định và độ nhạy; xem [bảng chi phí](bang_chi_phi.md), [code](../../src/lab13.py).
- **C:** Huy và Thái gắn nhãn độc lập 20 ca, đối chiếu và thống nhất ca lệch; lập cách phát hiện, khắc phục cho 5 loại lỗi trong [bảng lỗi](bang_loi.md).
- **D:** đề xuất chia ngẫu nhiên theo nhân viên, có đối chứng, cỡ mẫu và 4 luật dừng trong [pilot plan](pilot_plan.yaml).
- **E:** đặc tả chỉ số, event có `trace_id` và rủi ro kinh tế trong [chỉ số](chi_so.md); tổng hợp 7 mục, trạng thái, vai trò và đề xuất trong [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

- Chi phí toàn mẫu: **4.472 đ/việc thành công** (simulated), gấp **16,3 lần** hóa đơn token và tool chia số yêu cầu. Phạm vi `noi_dia` + `hang_nang` có chi phí gồm cố định **4.599 đ/việc** ở 45.000 yêu cầu/tháng (simulated), so với mốc thủ công 12.000 đ.
- Ba yếu tố nhạy nhất: làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% **+23,1%** (simulated). Xem lại 100% có thể lên **12.415 đ/việc** (simulated), vượt mốc thủ công.
- Bảng lỗi: **19/20 = 95%** đồng thuận ban đầu; ca 13 thống nhất **Giới hạn hệ thống**; có khắc phục cho **5/5 loại**.
- Chỉ số toàn mẫu: đóng 24 giờ, không mở lại 7 ngày **82,83%**; sửa/bỏ gợi ý **27,12%**; mở lại **4,25%**. Đây là số liệu lab, chưa chứng minh tác động của trợ lý.
- Pilot đề xuất **20 nhân viên/nhóm**, **299 yêu cầu/người**, tương đương **5.980 yêu cầu/nhóm**, mẫu hiệu dụng **859,20**; MDE 6 điểm phần trăm, power 0,80.
- **Đề xuất: Go có điều kiện** cho kế hoạch pilot trong phạm vi đã chọn. Trước bật phải kiểm chứng chống hoàn trùng, ghi sổ, event và roster; sau đó đo phút thật, kiểm soát an toàn và chi phí theo các cổng của hồ sơ launch.
- **Duyệt chéo: Chờ hội đồng.** Chưa có điểm, quyết định hoặc phản hồi; [phiếu chấm](phieu_cham.md) chỉ hoàn thiện khi nhận hồ sơ nhóm được giao.

## 5. Khó khăn và cách xử lý

Tối ưu chi phí trợ lý có thể đẩy việc sang nhân viên: giới hạn 1 lần chạy rẻ nhất theo chi phí/việc thành công, nhưng 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ, simulated). Vì vậy nhóm xét cả chi phí chuyển thủ công. Thiết kế hiện tại chỉ có power khoảng 0,64 cho chênh 5 điểm; nhóm ghi rõ đánh đổi thay vì coi MDE 6 điểm là bảo đảm đạt mục tiêu kinh doanh 5 điểm.

## 6. Tổng hợp đóng góp

Hậu phụ trách code trước giải lao, kiểm số sau giải lao và rủi ro kinh tế; Thịnh kiểm số trước giải lao, chủ trì code và pilot sau giải lao; Huy gắn nhãn 1, tổng hợp bảng lỗi và chỉ số; Thái gắn nhãn 2, giữ hồ sơ launch và tổng hợp báo cáo. Chi tiết, bằng chứng xem [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

Phút xem lại/làm lại còn giả lập; ngưỡng an toàn và lịch pilot là đề xuất. CSV chỉ có 20 nhân viên tại 6 depot, chưa chứng minh đủ roster 40 người tại 12 depot. Cần xác nhận nguồn lực, đo phút thật, triển khai event và theo dõi đủ cửa sổ trước kết luận. Chờ Thịnh xác nhận chạy code trên máy khác; Hậu rà bản nộp, commit và push. Mỗi thành viên tự nộp link repo trên LMS.

## 8. Tài liệu tham khảo

- [Đề bài lab](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md).
- [CHECKPOINTS](../../CHECKPOINTS.md), [quy tắc](../../RULES.md), [hướng dẫn nộp](../../SUBMISSION.md) và các file kết quả nhóm dẫn ở trên.
