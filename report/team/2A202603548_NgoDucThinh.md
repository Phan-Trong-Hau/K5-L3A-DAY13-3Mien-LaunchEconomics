# Báo cáo cá nhân — NgoDucThinh-2A202603548

## 1. Thông tin thành viên

- Họ tên: Ngô Đức Thịnh
- MSSV: 2A202603548
- Email:
- Vai trong nhóm: Người kiểm số 

## 2. Phần việc phụ trách

- **CP1–CP2 (Kiểm số và điền bảng chi phí):** Tính tay đối chiếu các kết quả A1–A4 và B1–B4, đối soát với output từ `src/lab13.py`, hoàn thiện bảng và câu trả lời trong `report/team/bang_chi_phi.md`.
- **CP4 (Tiếp quản code và thiết kế pilot):** Viết phần tính cỡ mẫu (D1) và tỉ lệ `mo_lai_trong_7_ngay` trong `src/lab13.py`; hoàn thiện toàn bộ `report/team/pilot_plan.yaml` (chú thích D1, D2, đánh đổi MDE 6 điểm, 3 luật dừng và các trường kiểm định).
- **Kiểm tra trước khi nộp:** Chạy lại toàn bộ `src/lab13.py` và kiểm tra cú pháp YAML của `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể
- Đối chiếu độc lập toàn bộ số liệu chi phí từ `src/logix_runs.csv` và `src/logix_requests.csv`: chi phí mỗi việc thành công 4.472 đ (`simulated`, gấp 16,3 lần hóa đơn/yêu cầu 274,7 đ), phân tách 4 loại yêu cầu (loại `quoc_te` 22.515 đ `simulated` = 1,88× và `doi_tac` 10.215 đ `simulated` = 0,85×), tính chi phí cố định 40 triệu đ/tháng (4.599 đ/việc `simulated` ở 45.000 yc/tháng), phân tích độ nhạy 9 kịch bản B1–B2, tổng chi phí hệ thống B3 (tối ưu ở giới hạn 2 lần = 6.901.220 đ `simulated`) và kịch bản xem lại 100% B4 (11.743 đ `simulated` với 9 phút/ca hoặc 12.415 đ `simulated` với 15,3 phút/ca).
- Hoàn thiện phần code CP4 trong `src/lab13.py` bằng `statsmodels` (`NormalIndPower`, `proportion_effectsize`), xác định không đủ 40 nhân viên cho MDE 5 điểm (cần 42 người/nhóm ở `m=75`) nên đề xuất phương án chia theo 20 nhân viên/nhóm với đánh đổi MDE 6 điểm (`n = 859`/nhóm, `m >= 299`, `DE = 6,96`, power còn 0,64 nếu chênh thật 5 điểm).
- Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (4,25% toàn mẫu = 51/1.200; 3,97% trong phạm vi `noi_dia` + `hang_nang`) để làm cơ sở đặt luật dừng an toàn (+2 điểm so với đối chứng, trần 6%) trong `report/team/pilot_plan.yaml`.

## 4. Bằng chứng

- [src/lab13.py](../../src/lab13.py): chạy từ đầu đến cuối in `Ba phép thử đáp án biết trước: ĐẠT`, đầy đủ bảng A1–A4, B1–B4 và D1, D3.
- [report/team/bang_chi_phi.md](bang_chi_phi.md): hoàn thiện đủ các bảng A1–A4, B1–B4, gắn nhãn `simulated` cho mọi con số từ cột `_simulated`.
- [report/team/pilot_plan.yaml](pilot_plan.yaml): vượt qua `yaml.safe_load`, không còn dấu `?` ngoài phần chú thích, có đủ 3 luật dừng theo mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ`.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý lập trình AI (Antigravity) để hỗ trợ viết script đối chiếu số liệu từ CSV, hoàn thiện code tính cỡ mẫu CP4 trong `src/lab13.py` và điền `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`.
- Tự kiểm tra lại bằng cách chạy trực tiếp `python lab13.py` trong `src/`, chạy `yaml.safe_load` trên `pilot_plan.yaml`, đối chiếu từng con số với hướng dẫn và kiểm tra không còn dấu `?` hay từ cấm trong các file báo cáo.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ và đầy đủ các phần việc được giao ở CP1–CP2 và CP4; số liệu khớp với kiểm tra chéo của nhóm và đáp ứng các tiêu chí chấm trong `RUBRIC.md`.
- Cần lưu ý bổ sung email cá nhân (nếu cần), điền thêm phần đóng góp/bằng chứng vào `TEAM.md` khi nhóm chốt commit nộp bài, và tiếp tục tham gia phản biện/chấm chéo ở CP5.
