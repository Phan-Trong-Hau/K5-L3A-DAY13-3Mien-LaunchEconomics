# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm 3Mien · Lớp L3A · Chốt hồ sơ 21/11/2026.** Đề nghị duyệt kế hoạch pilot cho `noi_dia` + `hang_nang`; các mốc bên dưới là đề xuất, chưa phải hoạt động đã thực hiện. Toàn bộ dữ liệu lab là giả lập; chi phí dùng phút `_simulated` ghi `simulated`. Trạng thái “Xong, có bằng chứng” xác nhận đã có tài liệu/phép tính, không xác nhận hiệu quả ngoài thực tế.

| Mục | Con số chính và bằng chứng | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.373.585 đ / 978 việc = **4.472 đ/việc** (simulated), gấp 16,3 lần hóa đơn 274,7 đ/yêu cầu; [A2](bang_chi_phi.md). | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi **+51,8% → 6.787 đ**; xem lại gấp đôi **+40,7% → 6.292 đ**; lương +25% **+23,1% → 5.506 đ/việc** (đều simulated); [B1–B2](bang_chi_phi.md). | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Phạm vi chọn: **4.599 đ/việc** gồm cố định ở 45.000 yêu cầu/tháng; nửa khối lượng **5.784 đ**, so với 12.000 đ (simulated). Xem lại 100%: **11.743–12.415 đ/việc** (simulated); loại `quoc_te` 22.515 đ và `doi_tac` 10.215 đ do chi phí/điều khoản; [A3–A4, B4](bang_chi_phi.md). | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng, an toàn | Toàn mẫu: **82,83%** (994/1.200) đóng 24h, không mở lại 7 ngày; **27,12%** (48/177) sửa/bỏ gợi ý; **4,25%** (51/1.200) mở lại. Đây là kết quả chạy thử, chưa chứng minh tăng so với 70%; [chỉ số và event](chi_so.md), [code](../../src/lab13.py). | Xong, có bằng chứng | Người phụ trách chỉ số |
| 5 · Bảng lỗi và cách khắc phục | **19/20 = 95%** đồng thuận ban đầu; ca 13 thống nhất Giới hạn hệ thống; **5/5 loại** có cách phát hiện đo được và vai trò phụ trách. Các biện pháp còn cần triển khai/kiểm chứng; [bảng lỗi](bang_loi.md). | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | **20 + 20 cụm nhân viên**, **299 yêu cầu/người → 5.980/nhóm**, DE **6,96**, hiệu dụng **859,20**; MDE **6 điểm**, power **0,80**, chỉ **0,64** nếu tác động 5 điểm. Giai đoạn chính **21 ngày** (~570 yêu cầu đủ điều kiện/ngày), **4 luật dừng**; pilot dự kiến 30/11/2026, quyết định **26/01/2027** sau theo dõi; [CP4](pilot_plan.yaml). | Xong, có bằng chứng | Người viết code sau giải lao |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi lên **6.787 đ/việc (+51,8%)**; xem lại 100% có thể lên **12.415 đ/việc (1,03× nhân viên)**; giảm nửa khối lượng làm cố định/việc tăng **1.185 → 2.370 đ** (simulated). Đo phút thật và chi phí tổng trước mở rộng; [rủi ro](chi_so.md). | Giả lập | Người kiểm số |

**Điều kiện theo từng cổng quyết định**

- **Trước bật pilot · Kỹ sư trưởng agent · kiểm tra 29/11/2026:** có bằng chứng khóa chống trùng, chỉ báo “đã hoàn” sau ghi sổ `ok`, ghi đủ event có `trace_id` và cơ chế tắt trong 30 phút; chưa đạt thì chưa bật.
- **Trước bật pilot · Giám đốc vận hành · kiểm tra 29/11/2026:** xác nhận roster thật 40 nhân viên tại 12 depot, **kiểm tra log lưu lượng thực tế 4 tuần gần nhất theo từng nhân viên (`noi_dia` + `hang_nang`)** để chứng minh đạt ≥570 yêu cầu đủ điều kiện/ngày (~14,2/người/ngày lịch) và đủ 299 yêu cầu/người trong 21 ngày (nếu thiếu phải chốt kéo dài giai đoạn 50%, ví dụ 28 ngày, trước khi bật), phân ngẫu nhiên 20/20 và ký chấp nhận MDE 6 điểm/power 0,64 ở 5 điểm; CSV chỉ có 20 nhân viên/6 depot (tải mẫu lệch 39–73 yêu cầu/người).
- **Sau tuần 1 và trước tăng bước · Trưởng nhóm CSKH · kiểm tra 06/12/2026, rà lại 13/12 và 27/12:** đo phút thật để thay `_simulated`; cùng kế toán duyệt giảm xem lại theo bậc khi hậu kiểm sai tiền ≤1%, không có sự cố nghiêm trọng và đạt cổng an toàn CP4. Nếu vẫn xem lại 100%, trình lại B4 và chi phí thực trước tăng bước.
- **Trước mở rộng ngoài pilot · Giám đốc vận hành · kiểm tra 26/01/2027:** đủ cỡ mẫu và theo dõi 7 ngày sau đóng kể cả ca đóng trễ, đạt an toàn và chi phí tổng gồm cố định <12.000 đ/việc; chỉ cân nhắc mở rộng nếu cận dưới khoảng tin cậy 95% của mức tăng đạt ≥5 điểm. Nếu chưa đủ bằng chứng thì chưa mở rộng, lập nghiên cứu tiếp theo; MDE 6 điểm không bảo đảm chứng minh được mức tăng tối thiểu 5 điểm.

**Đề xuất: Go có điều kiện** — Gate 2a duyệt kế hoạch pilot `noi_dia` + `hang_nang`; chỉ bật sau khi đạt hai điều kiện trước bật ngày 29/11, tăng bước và mở rộng theo các cổng riêng ở trên. Kết quả duyệt chéo hội đồng chưa có.
