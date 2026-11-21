# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Bùi Gia Huy** · Người gắn nhãn 2: **Vũ Quang Thái** (gắn độc lập trong 8 phút, không trao đổi trước khi so)

| Ca | Nhãn người 1 (Huy) | Nhãn người 2 (Thái) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** **19 / 20 = 95%** (đạt mục tiêu ≥ 80%). Phân bổ 5 loại sau thống nhất: Do người dùng (4 ca: 1, 6, 9, 14) · Hệ thống (5 ca: 2, 7, 8, 15, 20) · Ngữ cảnh (4 ca: 3, 10, 16, 18) · Giới hạn hệ thống (4 ca: 4, 11, 13, 19) · Ngầm (3 ca: 5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

**Ca không trùng (1/20):**
- **Ca 13 (Huy: Hệ thống vs. Thái: Giới hạn hệ thống → Thống nhất: Giới hạn hệ thống):** Gắn nhãn theo nguyên nhân gốc chứ không theo cách trợ lý xử lý kém; hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi năng lực của trợ lý nên thuộc **Giới hạn hệ thống**, còn việc trả lời chung chung thay vì từ chối rõ được xử lý ở bước khắc phục.

**Các quy tắc bổ sung đã thống nhất cho những ca dễ nhầm khác:**

- **Ca 6, 9 → Do người dùng (không phải Hệ thống):** nguyên nhân gốc là khách chọn sai mục hoặc nhập sai loại mã; việc trợ lý chưa gợi ý nằm ở bước khắc phục.
- **Ca 8, 15 → Hệ thống (không phải Ngầm):** lỗi đã lộ ra trực tiếp trong câu trả lời hoặc bị nhân viên xem lại phát hiện trước khi gửi; chỉ gắn Ngầm khi không ai nhận ra cho đến khi kiểm tra mẫu/chi phí.
- **Ca 12 → Ngầm:** câu trả lời đúng nhưng lỗi thiếu trường làm chi phí token tăng gấp 3 suốt 3 tuần mà không ai phát hiện.
- **Ca 18 → Ngữ cảnh:** số tiền hoàn đúng chính sách nhưng thiếu giải thích cách tính nên lệch kỳ vọng khiến khách mở lại.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (mã không đúng định dạng vận đơn); cảnh báo hằng ngày khi vượt **2%** tổng số yêu cầu/ngày | Tự nhận diện định dạng mã đơn sàn TMĐT để tra chéo sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát hằng giờ giữa thông báo "đã hoàn" và event `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; ngưỡng cảnh báo **> 0 ca** | Chỉ gửi thông báo "đã hoàn tiền thành công" sau khi sổ cái trả `ok`; nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hằng tuần tỉ lệ `ticket_reopened` có lý do "hoàn thiếu tiền" nhưng đối chiếu thấy số tiền đúng chính sách; cảnh báo khi vượt **1%** số đơn hoàn | Cập nhật mẫu tin nhắn hoàn phí luôn hiển thị công thức tính rõ ràng (ví dụ: `30.000 đ × 50% = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` thống kê hằng tuần theo cột `loai`; cảnh báo nếu tỉ lệ vượt **10%** trong phạm vi pilot | Giữ luồng chuyển nhân viên kèm tóm tắt ngữ cảnh; loại nhóm yêu cầu `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm tra mẫu **100 đơn/tuần** so với bảng giá hiện hành; ngưỡng cảnh báo khi **> 1%** đơn lệch số tiền | Tự động xoá bộ nhớ đệm (cache invalidation) ngay khi cập nhật bảng giá mới và ghi `price_table_version` vào mọi `trace_id` | Kế toán trưởng |
