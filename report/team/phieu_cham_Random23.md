# Phiếu chấm hội đồng Gate 2a · Nhóm Random23

- **Nhóm được chấm:** Random23 (Lớp L3A)
- **Nhóm chấm (hội đồng):** 3Mien 
- **Đối tượng:** Toàn bộ hồ sơ nhóm trong `report/team/` ([ho_so_launch_v0.md](report/team/ho_so_launch_v0.md), [bang_chi_phi.md](report/team/bang_chi_phi.md), [bang_loi.md](report/team/bang_loi.md), [pilot_plan.yaml](report/team/pilot_plan.yaml), [chi_so.md](report/team/chi_so.md), [group_report.md](report/team/group_report.md)) và mã nguồn [src/lab13.py](src/lab13.py).
- **Thang điểm:** C6–C8, tối đa 30 điểm, theo [RUBRIC.md](RUBRIC.md) và [mẫu phiếu hội đồng](report/team/phieu_cham.md).
- **Phạm vi đối chiếu bằng chứng:** Đã kiểm chứng trực tiếp mã nguồn `src/lab13.py` (3 phép thử A1 ĐẠT, số liệu A2–B4 và D1–D3 khớp dữ liệu CSV gốc) và toàn bộ tệp hồ sơ trong repo. Điểm dưới đây là đánh giá hội đồng cho phần C6–C8, cần xác nhận câu trả lời của đội trình tại phiên duyệt chéo.

| Tiêu chí | Điểm | Lý do có số |
| --- | ---: | --- |
| **C6 · Đề xuất khớp bằng chứng** | **10/10** | Đề xuất **Go có điều kiện** khớp với kinh tế phạm vi chọn: `4.599 đ/việc` (`0,38×`) ở `45.000` yêu cầu/tháng và `5.784 đ/việc` (`0,48×`) ở nửa sản lượng, toàn hệ thống `5.865 đ/yêu cầu` (`0,49×`) so với baseline `12.000 đ` (`simulated`). Hồ sơ nêu thẳng hai con số bất lợi: xem lại 100% đội chi phí lên `11.743 đ – 12.415 đ` (`0,98× – 1,03×`) và power giảm còn `0,64` ở tác động `+5 điểm`, kèm 4 điều kiện xử lý có vai trò và hạn chót cụ thể. |
| **C7 · Số giả lập và phạm vi** | **10/10** | Gắn nhãn `simulated` / trạng thái `Giả lập` ở bảng chi phí, `pilot_plan.yaml` và 4 mục dùng cột `_simulated` trong hồ sơ launch v0 (mục 1, 2, 3, 7). Phạm vi thu hẹp có lý do bằng số: giữ `noi_dia` (`2.696 đ`, `0,22×`, thành công `95,0%`) và `hang_nang` (`8.221 đ`, `0,69×`, `74,1%`); loại `quoc_te` (`22.515 đ`, `1,88×`, `27,3%`) và `doi_tac` (`10.215 đ`, `0,85×`, `54,4%`, điều khoản riêng). Cần bổ sung nhãn `simulated` trực tiếp cạnh các số độ nhạy ở Mục 2 hồ sơ và Mục 3/5 báo cáo nhóm để tránh mất ngữ cảnh khi trích rời. |
| **C8 · Pilot ra được quyết định** | **5/10** | Thiết kế phân cụm hợp lệ: ngẫu nhiên `20/20` nhân viên phân tầng theo depot, khóa seed `20261121`, `m ≥ 299` yêu cầu/người (`5.980`/nhóm), `DE = 6,96`, mẫu hiệu dụng `859,20 ≥ 859` (`MDE = 6 điểm`, `alpha = 0,05`, `power = 0,80`), có 4 luật dừng đủ 4 vế `NẾU–TRONG–THÌ–KHÔNG THÌ` với ngưỡng mở lại (`6%` / `+2 điểm %`) bám sát baseline `4,25%` (`3,97%` phạm vi). Tuy nhiên, `pilot_plan.yaml` vẫn ở trạng thái nháp (`status: draft_pending_team_review`, `predeclared: "Chưa hoàn tất"`, `launch_gate.ready: false`), để trống `decision_date: null`, và đặt trần dừng chi phí ở mức hòa vốn `12.000 đ` (chưa ký duyệt). Chưa đủ điều kiện chốt để đạt mức 10 theo rubric. |
| **Tổng điểm hội đồng** | **25/30** | **Go có điều kiện** cho kế hoạch pilot phạm vi `noi_dia` và `hang_nang`. |

**Quyết định của hội đồng đề xuất:** **Go có điều kiện.** Chỉ cho phép khởi động pilot sau khi chốt dứt điểm trạng thái nháp của `pilot_plan.yaml`, chốt `decision_date`, hoàn tất các điều kiện an toàn tiền khởi động và đồng bộ bằng chứng lỗi/telemetry. Quyết định này chỉ áp dụng cho giai đoạn pilot, không đồng nghĩa với chấp thuận triển khai diện rộng.

## Nhận xét và điều kiện cần chốt

- **Mô hình kinh tế chặt chẽ và kiểm chứng được từ code:** `src/lab13.py` chạy thông suốt, phân biệt rõ hóa đơn token+tool `274,7 đ/yêu cầu` với chi phí thật `4.472 đ/việc` (`16,3×`, giờ nhân viên chiếm `92,5%`, `simulated`), có đủ phân tích chi phí cả hệ thống B3 (`6.901.220 đ` tối ưu ở giới hạn 2 lần chạy) và độ nhạy xem lại 100% B4. Cần thống nhất con số B4 giữa `12.415 đ` (`lab13.py`, `bang_chi_phi.md`, `ho_so_launch_v0.md`) và `12.414 đ` (`chi_so.md`, `group_report.md`).
- **Hoàn tất bản chốt `pilot_plan.yaml` để nâng C8 lên 10/10:** Điền ngày quyết định cụ thể thay cho `decision_date: null`, chuyển các trạng thái bản nháp (`draft_pending_team_review`, `predeclared: Chưa hoàn tất`, `launch_gate.pending` chứa việc nội bộ đã xong) sang bản chốt chính thức, và xem xét hạ ngưỡng dừng chi phí từ mức hòa vốn `12.000 đ` xuống ngưỡng cảnh báo sớm hơn (ví dụ `8.000 đ` so với `4.599 đ – 5.784 đ` ở A4).
- **Chỉnh lại trình tự thời hạn của 4 điều kiện trong hồ sơ launch v0:** Hiện Điều kiện 3 yêu cầu thay phút `simulated` bằng phút đo thật *sau tuần rollout 0.10* trước `2026-12-28`, nhưng Điều kiện 4 (ban hành quy trình giảm xem lại theo bậc) lại có hạn `2027-01-02` (muộn hơn cả tuần chạy đầu tiên). Cần đưa toàn bộ điều kiện tiền khởi động (Điều kiện 1, 2, 4 và bật telemetry) lên trước ngày bắt đầu pilot, còn mốc thay số phút đo thật đặt sau tuần 1.
- **Đồng bộ danh mục event, bảng lỗi và báo cáo nhóm:** Thống nhất số lượng thành **11 telemetry events** và **4 luật dừng** trên toàn bộ tài liệu (hiện `ho_so_launch_v0.md` và `group_report.md` vẫn ghi `10 events` / `3 luật dừng`). Chuẩn hóa lại tên giá trị `reason` và thuộc tính còn thiếu giữa `bang_loi.md` và `chi_so.md` (`sai_loai_ma` vs `invalid_tracking_code`, `khong_hieu_cach_tinh` vs `thac_mac_so_tien`, `thieu_du_lieu_chang` vs `thieu_du_lieu`; bổ sung `loai`, `price_table_version`, `staff_id`, `arm`, `created_at` và sửa đối soát Ca 7 thay vì dùng `agent_suggestion_shown`).
- **Làm rõ tính xác thực của Bộ nhãn 2 trong `bang_loi.md`:** Hiện `bang_loi.md` còn placeholder `(chờ điền họ tên)`, phần hướng dẫn nháp chưa dọn, và đặc biệt Bộ nhãn 2 có `13/20` ca mô tả khác hoàn toàn đề gốc nhưng vẫn trùng nhãn `20/20` (`100%`). Đội cần giải trình minh bạch quá trình gắn nhãn độc lập của TV4 và dọn sạch các mục nháp trước khi chốt bài.
- **Hoàn thiện thủ tục nộp bài:** Bổ sung báo cáo cá nhân còn thiếu của TV3 (`2A202603524_NguyenTrieuDuong.md`), cập nhật báo cáo TV1 cho khớp trạng thái cuối buổi, hoàn thiện `phieu_cham.md` của nhóm, và loại bỏ từ khóa bị cấm còn sót trong câu phủ định ở báo cáo cá nhân của TV2 và TV4 để vượt qua bước kiểm tra tự động.

## Câu hỏi tại buổi duyệt chéo

1. Trong `pilot_plan.yaml`, `decision_date` đang là `null` và trần dừng chi phí đặt ở mức hòa vốn `12.000 đ/việc` (cao hơn gấp đôi `4.599 đ – 5.784 đ` ở A4) — nhóm chốt ngày quyết định cụ thể là ngày nào, và nếu chi phí thực tế leo lên `9.000 đ – 11.500 đ/việc` trong 2 tuần liên tiếp thì cơ chế nào ngăn pilot tiếp tục đốt tiền?
2. Tại sao trong `bang_loi.md`, Bộ nhãn 2 có tới `13/20` ca mô tả sai khác so với đề gốc nhưng nhãn gắn độc lập vẫn trùng `20/20` (`100%`) với Bộ nhãn 1?

**Câu trả lời của đội trình:**

1. **Về `decision_date` và trần dừng chi phí trong `pilot_plan.yaml`:**
   - Nhóm cập nhật bỏ trạng thái nháp (`draft_pending_team_review`) và chốt `decision_date` cụ thể ngay sau khi hoàn tất 3 bước rollout (`0.10 → 0.25 → 0.50`) cộng đủ cửa sổ theo dõi trưởng thành 8 ngày (24h đóng + 7 ngày mở lại), tức ngày **`2027-01-19`** (hoặc **`2027-01-26`** nếu kéo dài giai đoạn 50% lên 21 ngày để đủ `299` yêu cầu/nhân viên).
   - Với ngưỡng dừng chi phí: thừa nhận mức `12.000 đ/việc` là điểm hòa vốn của nhân viên tự làm nên nếu đợi chạm `12.000 đ` mới dừng sẽ không còn biên an toàn kinh tế so với mức `4.599 đ – 5.784 đ/việc` (`simulated`) ở A4. Nhóm hạ trần luật dừng chi phí biến đổi xuống **`8.000 đ/việc`** (dùng số phút xem lại/làm lại đo thật): *NẾU chi phí mỗi việc thành công vượt `8.000 đ/việc` TRONG 2 tuần liên tiếp THÌ PM trợ lý hoàn phí thu hẹp phạm vi về chỉ `noi_dia` và giới hạn tối đa 2 lần chạy trong vòng 1 ngày KHÔNG THÌ không được mở rộng thêm `hang_nang`*. Nhờ vậy, khi chi phí leo lên vùng `9.000 đ – 11.500 đ/việc`, luật dừng sẽ kích hoạt ngay sau 2 tuần để ngăn tiếp tục tiêu tốn ngân sách.

2. **Về sự sai khác mô tả `13/20` ca của Bộ nhãn 2 trong `bang_loi.md`:**
   - Quá trình gắn nhãn 20 ca theo 5 nhóm lỗi Google PAIR được hai thành viên thực hiện trên 20 ca của đề gốc, nhưng khi tổng hợp sang bảng Markdown của Bộ nhãn 2, thành viên phụ trách đã dùng công cụ tự động tóm tắt/sinh lại cột mô tả ngắn khiến nội dung chữ của 13 ca bị lệch so với văn bản gốc trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`.
   - Nhóm cam kết chuẩn hóa lại cột mô tả của cả 20 ca đúng nguyên văn đề bài gốc, điền đầy đủ họ tên người gắn nhãn, xóa các dòng hướng dẫn nháp còn sót và rà soát lại từng cặp nhãn độc lập để đảm bảo tính minh bạch của tỉ lệ đồng thuận trước khi chốt bản nộp cuối.

---

*Lưu ý về tổng điểm môn: `25/30` là phần điểm hội đồng C6–C8. Chưa cộng `70` điểm C1–C5 do trợ giảng chấm riêng (dù đã kiểm tra `src/lab13.py` đạt A1–B4, D1; nhóm cần đặc biệt xử lý `bang_loi.md` và trạng thái nháp của `pilot_plan.yaml` để không mất điểm ở C3–C4); không quy đổi thành điểm `/100`.*
