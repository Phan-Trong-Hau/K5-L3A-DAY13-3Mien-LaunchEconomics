# Báo cáo cá nhân — Phan Trọng Hâu

## 1. Thông tin thành viên

- Họ tên: Phan Trọng Hâu
- MSSV: 2A202603547
- Email: [Bổ sung trước khi nộp]
- Nhóm 3Mien, lớp L3A
- Vai trò: Viết code trước giải lao, kiểm số sau giải lao.

## 2. Phần việc phụ trách

- CP1–CP2: Viết và chạy mô hình chi phí A1–A4 và phân tích độ nhạy B1–B4.
- CP4–CP5: Đối chiếu cỡ mẫu khi phần D1 có kết quả, cung cấp số liệu cho mục rủi ro kinh tế và rà checklist trước khi nhóm nộp.

## 3. Đóng góp cụ thể

- Tính chi phí token và tool trên mọi lần chạy, kể cả lần lỗi. Cộng chi phí xem lại và làm lại, rồi chia cho số yêu cầu thành công. Kết quả cơ sở là 4.472 đ/việc thành công (simulated) trên 978 việc thành công, gấp khoảng 16,3 lần hóa đơn token và tool tính trên mỗi yêu cầu.
- So sánh bốn loại yêu cầu và tính chi phí cố định cho phạm vi nội địa và hàng nặng. Ở 45.000 yêu cầu/tháng, phần cố định là 1.185 đ/việc thành công, đưa tổng chi phí lên 4.599 đ/việc thành công (simulated).
- Chạy chín kịch bản độ nhạy, một kịch bản kết hợp và so sánh ba giới hạn chạy lại. Giới hạn hai lần có tổng chi phí hệ thống thấp nhất, khoảng 6,90 triệu đồng trên 1.200 yêu cầu (simulated), sau khi cộng chi phí nhân viên xử lý các yêu cầu trợ lý không hoàn tất.
- Bổ sung hai rủi ro kinh tế vào hồ sơ nhóm. Số ca làm lại tăng gấp đôi đẩy chi phí lên 6.787 đ/việc thành công (+51,8%). Xem lại mọi gợi ý hợp lệ trong phạm vi pilot đưa chi phí lên 11.743–12.415 đ/việc thành công theo hai giả định về thời gian làm lại. Các số liệu này đều là simulated.

## 4. Bằng chứng

- [Mã nguồn A1–A4 và B1–B4](../../src/lab13.py)
- [Mục E2 về rủi ro kinh tế](chi_so.md#e2--rủi-ro-kinh-tế)
- Chạy `python3 lab13.py` từ thư mục `src/` với môi trường đã cài pandas. Cả ba phép thử A1 đều đạt (1,20 · 1,25 · 1,25). Các kiểm tra bổ sung xác nhận mức giảm chi phí khi giảm một nửa hệ số xem lại hoặc làm lại bằng một nửa mức tăng tương ứng khi gấp đôi hệ số.

## 5. Công cụ AI đã dùng

Dùng Codex để hỗ trợ triển khai Python, chạy kiểm tra với hai file CSV của lab và soạn bản nháp báo cáo. Kiểm tra đã thực hiện gồm chạy ba phép thử A1, đối chiếu số yêu cầu thành công và chi phí cơ sở, và kiểm tra quan hệ giữa các kịch bản tăng giảm hệ số ở B1.

## 6. Tự đánh giá

Kết quả B3 cho thấy hai cách tính dẫn đến hai lựa chọn khác nhau. Một lần chạy có chi phí thấp nhất trên mỗi việc trợ lý làm xong, còn hai lần chạy rẻ nhất cho cả hệ thống sau khi tính phần nhân viên xử lý. Việc còn lại là đối chiếu cỡ mẫu pilot khi D1 có kết quả và rà checklist trước khi nhóm nộp.
