# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Số liệu tính thử từ `src/logix_requests.csv` (1.200 yêu cầu, đọc bằng `keep_default_na=False`).

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu có `duoc_xem_lai == 1` | **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | **4,25%** (51 / 1.200) |
| Dùng (đề xuất) | % yêu cầu thuộc nhóm can thiệp được nhân viên mở xem gợi ý trợ lý | Số `request_id` có event `agent_suggestion_shown` chia tổng số `refund_request_created` thuộc nhóm can thiệp trong phạm vi pilot | Không cần tính |
| An toàn (đề xuất) | % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, ca 17) | Số đơn có `so_tien_da_hoan != so_tien_dung` chia tổng số đơn trong `audit_sample_checked` (100 đơn/tuần) | Không cần tính |

**Lưu ý diễn giải:** Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200). Không viết "trợ lý đã nâng chỉ số từ 70% lên 82,83%" vì đợt chạy thử 2 tuần không có nhóm đối chứng.

## Danh sách event

11 event cốt lõi, mọi event đều gắn `trace_id` để nối xuyên suốt với trace của agent và hệ thống vận hành.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / cổng CSKH | `request_id`, `loai`, `depot`, `so_tien_vnd`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `input_validation_failed` | Cổng tiếp nhận / Agent | `request_id`, `field_error`, `reason`, `trace_id` | Khi đầu vào của khách sai định dạng (VD: mã đơn sàn TMĐT, thiếu số tài khoản) |
| `agent_run_completed` | Agent | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `price_table_version`, `trace_id` | Sau mỗi lần chạy của agent, kể cả lần chạy lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id` | Khi gợi ý của trợ lý hiển thị trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại yêu cầu bị sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien_da_hoan`, `ket_qua`, `trace_id` | Khi hệ thống ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `audit_sample_checked` | Bộ phận kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `checked_at`, `trace_id` | Khi kiểm tra mẫu định kỳ 100 đơn/tuần |

**Kiểm tra chéo (ánh xạ chỉ số → event):**
- **Chỉ số chính (% đóng trong 24h và không mở lại 7 ngày):** tính từ `refund_request_created` (mốc tạo), `ticket_closed` (kiểm tra `closed_at - created_at ≤ 24h`), và `ticket_reopened` (kiểm tra không có event mở lại trong 7 ngày theo cùng `trace_id`).
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** tính từ `staff_review_decision` (`quyet_dinh` ∈ `{sua, bo}` chia tổng số bản ghi `staff_review_decision`).
- **Chỉ số an toàn (tỉ lệ lỗi lọt đến khách):** tính từ `ticket_reopened` (trong 7 ngày) chia tổng số `refund_request_created`.
- **Chỉ số dùng đề xuất (% mở gợi ý trợ lý):** tính từ số `trace_id` duy nhất có `agent_suggestion_shown` chia tổng `refund_request_created` của nhóm can thiệp (`arm = treatment`).
- **Chỉ số an toàn đề xuất (% đơn hoàn sai tiền qua kiểm tra mẫu):** tính trực tiếp từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng mẫu kiểm tra).
- *(Ngoài ra, `agent_run_completed`, `staff_review_decision` và `staff_rework_completed` còn giúp đo trực tiếp chi phí thật và thay thế 2 cột `_simulated` sau tuần 1 pilot).*

## E2 · Rủi ro kinh tế

Các mức chi phí lấy từ kịch bản B1 và B4 do [lab13.py](../../src/lab13.py) tính. Ngưỡng theo dõi dưới đây là đề xuất để nhóm đối chiếu với kế hoạch pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Từ 4.472 lên 6.787 đ/việc thành công (+51,8%, simulated, toàn bộ mẫu B1) | Tỷ lệ yêu cầu phải làm lại theo tuần đạt gấp đôi mức đầu pilot | Rà các ca làm lại theo loại yêu cầu và xem xét thu hẹp phạm vi | PM trợ lý hoàn phí |
| Phải xem lại toàn bộ gợi ý hợp lệ | Phạm vi `noi_dia` + `hang_nang`: 11.743 đ/việc nếu làm lại 9 phút/ca, 12.415 đ nếu làm lại 15,3 phút/ca (simulated, B4) | Tỷ lệ xem lại, phút xem lại và phút làm lại thực đo. Ở mức làm lại 15,3 phút, điểm hòa vốn B4 là khoảng 4,80 phút xem lại | Rà thời gian thao tác, đề xuất giảm phạm vi xem lại nếu chỉ số an toàn đạt điều kiện pilot | Trưởng nhóm CSKH |
