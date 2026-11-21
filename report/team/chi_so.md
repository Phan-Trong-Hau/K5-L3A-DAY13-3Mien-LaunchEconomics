# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Các mức chi phí lấy từ kịch bản B1 và B4 do [lab13.py](../../src/lab13.py) tính. Ngưỡng theo dõi dưới đây là đề xuất để nhóm đối chiếu với kế hoạch pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Từ 4.472 lên 6.787 đ/việc thành công (+51,8%, simulated, toàn bộ mẫu B1) | Tỷ lệ yêu cầu phải làm lại theo tuần đạt gấp đôi mức đầu pilot | Rà các ca làm lại theo loại yêu cầu và xem xét thu hẹp phạm vi | PM trợ lý hoàn phí |
| Phải xem lại toàn bộ gợi ý hợp lệ | Phạm vi `noi_dia` + `hang_nang`: 11.743 đ/việc nếu làm lại 9 phút/ca, 12.415 đ nếu làm lại 15,3 phút/ca (simulated, B4) | Tỷ lệ xem lại, phút xem lại và phút làm lại thực đo. Ở mức làm lại 15,3 phút, điểm hòa vốn B4 là khoảng 4,80 phút xem lại | Rà thời gian thao tác, đề xuất giảm phạm vi xem lại nếu chỉ số an toàn đạt điều kiện pilot | Trưởng nhóm CSKH |
