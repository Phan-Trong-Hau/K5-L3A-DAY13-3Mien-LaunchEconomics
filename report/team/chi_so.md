# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Số liệu tính thử bằng `tinh_chi_so` trong [lab13.py](../../src/lab13.py), từ `src/logix_requests.csv` (1.200 yêu cầu, đọc bằng `keep_default_na=False`). Toàn bộ dữ liệu lab là giả lập; các con số dưới đây mô tả đợt chạy thử của lab.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu có `duoc_xem_lai == 1` | **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | **4,25%** (51 / 1.200) |
| Dùng (đề xuất) | % yêu cầu thuộc nhóm can thiệp được nhân viên mở xem gợi ý trợ lý | Số `request_id` có event `agent_suggestion_shown` chia tổng số `refund_request_created` thuộc nhóm can thiệp trong phạm vi pilot | Không cần tính |
| An toàn (đề xuất) | % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, ca 17) | Số đơn có `so_tien_da_hoan != so_tien_dung` chia tổng số đơn trong `audit_sample_checked` (100 đơn/tuần) | Không cần tính |

**Lưu ý diễn giải:** Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200). Không viết "trợ lý đã nâng chỉ số từ 70% lên 82,83%" vì đợt chạy thử 2 tuần không có nhóm đối chứng.

**Đối chiếu phạm vi CP4 (`noi_dia` + `hang_nang`):** chỉ số chính 906/982 = **92,26%**; sửa/bỏ gợi ý 27/128 = **21,09%**; mở lại 39/982 = **3,97%**. Tỉ lệ mở lại chỉ là chỉ báo thay thế cho lỗi lọt: khách có thể mở lại vì hiểu nhầm, còn lỗi ngầm có thể không bị mở lại; cần đo thêm sai tiền qua hậu kiểm.

**Quy ước đo trong pilot:** chốt nhóm theo phân ngẫu nhiên ban đầu; mỗi yêu cầu chỉ được đếm một lần theo `request_id`. Chỉ số chính xét đóng trong 24 giờ từ lúc tạo, không mở lại trong 7 ngày sau lần đóng đầu; chờ đủ 8 ngày từ lúc tạo để kết luận cohort. Không gán yêu cầu chưa đủ thời gian theo dõi thành “không mở lại”. Đây là quy ước đề xuất của pilot; cần xác nhận cách tạo cột CSV trước khi so lịch sử. Yêu cầu đã xem lại lấy quyết định cuối cùng, không đếm các event bấm lại thành nhiều yêu cầu.

**An toàn khi pilot:** tỉ lệ mở lại = số yêu cầu mở lại trong 7 ngày sau lần đóng đầu / số yêu cầu đã đủ 7 ngày theo dõi sau lần đóng đầu. Báo riêng số chưa đóng và số đóng nhưng chưa đủ theo dõi; ca đóng ngày 4 cần theo dõi đến ngày 11, dù chỉ số chính đã không đạt vì đóng quá 24 giờ. Khi còn ca quá 24 giờ chưa đóng hoặc ca đóng trễ chưa đủ theo dõi, chưa xác nhận an toàn để tăng bước/mở rộng. Cách tính này cần xác nhận tương thích với cột lịch sử, không mặc định 4,25% là baseline cùng cửa sổ.

Ở bước 4/40 hoặc 10/40, mẫu giám sát an toàn chỉ lấy yêu cầu đến nhân viên đã bật cờ trong thời gian bật (kể cả họ không dùng gợi ý), đối chiếu nhóm thủ công đồng thời; không gộp người chưa bật để pha loãng rủi ro. Phân tích chính chỉ dùng giai đoạn bật đủ 20 người theo ITT. Vi phạm ngưỡng an toàn một lần thì giữ bước; đủ 3 lần liên tiếp thì tắt theo CP4.

## Danh sách event

11 event cốt lõi, mọi event đều gắn `trace_id` để nối xuyên suốt với trace của agent và hệ thống vận hành. Trường dùng chung bắt buộc: `event_id`, `event_time` có múi giờ, `request_id`, `trace_id`, `staff_id`, `arm` và `depot`; `event_id` để loại event gửi trùng. Dùng `request_id` nối các lần chạy lại hoặc mở lại, vì một yêu cầu có thể có nhiều trace. Đây là đặc tả event cần triển khai, chưa phải bằng chứng hệ thống đã ghi đủ.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / cổng CSKH | `request_id`, `created_at`, `loai`, `depot`, `so_tien_vnd`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí, ghi cả nhóm can thiệp và đối chứng |
| `input_validation_failed` | Cổng tiếp nhận / Agent | `request_id`, `field_error`, `reason`, `trace_id` | Khi đầu vào của khách sai định dạng (VD: mã đơn sàn TMĐT, thiếu số tài khoản) |
| `agent_run_completed` | Agent | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `price_table_version`, `trace_id` | Sau mỗi lần chạy của agent, kể cả lần chạy lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id` | Khi gợi ý của trợ lý hiển thị trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại yêu cầu bị sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `transaction_id`, `idempotency_key`, `so_tien_da_hoan`, `ket_qua`, `trace_id` | Khi hệ thống ghi lệnh hoàn tiền vào sổ cái; 2 giao dịch thành công cho cùng đơn/khoản hoàn kích hoạt đối soát hoàn trùng |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu trong vòng 7 ngày |
| `audit_sample_checked` | Bộ phận kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `price_table_version`, `checked_at`, `trace_id` | Khi hậu kiểm ngẫu nhiên 100 đơn/tuần, hoặc toàn bộ nếu dưới 100 đơn |

Để thực thi luật CP4 và đối soát ca 7, bổ sung `refund_status_sent` (`message_status`, `transaction_id`) và `request_outcome_recorded` (`ket_qua` theo định nghĩa lab, `matured_at`, `quality_check_source`); cả hai mang đủ trường chung. Chỉ ghi “đã hoàn” khi có ghi sổ `ok`. Kết quả thành công cần đối chiếu trạng thái đóng, mở lại và lỗi tiền đã phát hiện; không suy “thành công” chỉ từ `agent_run_completed.status = ok`.

**Kiểm tra chéo (ánh xạ chỉ số → event):**
- **Chỉ số chính (% đóng trong 24h và không mở lại 7 ngày):** tính từ `refund_request_created` (mốc tạo), lần `ticket_closed` đầu tiên (kiểm tra `closed_at - created_at ≤ 24h`), và `ticket_reopened` (không mở lại trong 7 ngày sau lần đóng đầu, nối theo `request_id`); mẫu số là các yêu cầu đã đủ thời gian theo dõi.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** số yêu cầu có quyết định cuối cùng trong `staff_review_decision` thuộc `{sua, bo}`, chia số yêu cầu đã xem lại; khử trùng theo `request_id`.
- **Chỉ số an toàn (chỉ báo mở lại):** thử trên CSV bằng cột `mo_lai_trong_7_ngay` / 1.200; trong pilot nối `ticket_closed` đầu tiên với `ticket_reopened` theo `request_id`, chỉ chia số yêu cầu đã đủ 7 ngày sau đóng, báo riêng ca đang chờ. Theo dõi từng bước bật cờ như quy ước trên; không dùng cohort chưa trưởng thành để kết luận đạt luật CP4.
- **Chỉ số dùng đề xuất (% mở gợi ý trợ lý):** số `request_id` duy nhất có `agent_suggestion_shown` chia số `request_id` duy nhất của `refund_request_created` thuộc nhóm can thiệp và phạm vi pilot (`arm = treatment`).
- **Chỉ số an toàn đề xuất (% đơn hoàn sai tiền qua kiểm tra mẫu):** tính trực tiếp từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng mẫu kiểm tra).
- *(Ngoài ra, `agent_run_completed`, `staff_review_decision` và `staff_rework_completed` còn giúp đo trực tiếp chi phí thật và thay thế 2 cột `_simulated` sau tuần 1 pilot).*

- **Chi phí/việc thành công cho luật CP4:** cộng token/tool mọi lần chạy và phút xem lại/làm lại thực đo của cùng cohort, chia số `request_id` có `request_outcome_recorded.ket_qua = thanh_cong` đã trưởng thành. Báo riêng chi phí thủ công thay thế và cố định 40 triệu đ/tháng, tránh đếm đôi phút làm lại; không bỏ chi phí của ca lỗi khỏi tử số. Mẫu số bằng 0 thì chưa tính được, giữ bước.

## E2 · Rủi ro kinh tế

Các mức chi phí lấy từ kịch bản B1 và B4 do [lab13.py](../../src/lab13.py) tính. Ngưỡng theo dõi dưới đây là đề xuất để nhóm đối chiếu với kế hoạch pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Từ 4.472 lên 6.787 đ/việc thành công (+51,8%, simulated, toàn bộ mẫu B1) | Tỷ lệ yêu cầu phải làm lại theo tuần đạt gấp đôi mức đầu pilot | Rà các ca làm lại theo loại yêu cầu và xem xét thu hẹp phạm vi | PM trợ lý hoàn phí |
| Khối lượng thành công giảm một nửa | A4: cố định/việc từ 1.185 lên 2.370 đ; chi phí tổng từ 4.599 lên 5.784 đ/việc (simulated) | Khối lượng đủ thời gian theo dõi dưới 50% kế hoạch; rà hằng tuần | Giữ bước, kiểm tra lại chi phí tổng và cách phân bổ cố định trước mở rộng | PM trợ lý hoàn phí |
| Phải xem lại toàn bộ gợi ý hợp lệ | Phạm vi `noi_dia` + `hang_nang`: 11.743 đ/việc nếu làm lại 9 phút/ca, 12.415 đ nếu làm lại 15,3 phút/ca (simulated, B4) | Tỷ lệ xem lại, phút xem lại và phút làm lại thực đo. Ở mức làm lại 15,3 phút, điểm hòa vốn B4 là khoảng 4,80 phút xem lại | Rà thời gian thao tác, đề xuất giảm phạm vi xem lại nếu chỉ số an toàn đạt điều kiện pilot | Trưởng nhóm CSKH |
