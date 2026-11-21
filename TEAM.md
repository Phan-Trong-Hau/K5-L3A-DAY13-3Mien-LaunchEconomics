# Team

## Thông tin nhóm

- Tên nhóm: 3Mien
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-3Mien-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phan Trọng Hâu | 2A202603547 | | [Phan-Trong-Hau](https://github.com/Phan-Trong-Hau) | Viết code trước giải lao, kiểm số sau giải lao |
|   2 | Ngô Đức Thịnh | 2A202603548 | | [NgooThinh05](https://github.com/NgooThinh05) | Kiểm số trước giải lao, viết code sau giải lao |
|   3 | Bùi Gia Huy | 2A202603525 | 26ai.huybg2@vinuni.edu.vn | [huy9ai](https://github.com/huy9ai) | Gắn nhãn 1, phụ trách chỉ số |
|   4 | Vũ Quang Thái | 2A202603545 | | [vuThai05](https://github.com/vuThai05) | Gắn nhãn 2, kiêm giữ hồ sơ |

## Phân công theo checkpoint

| Mốc | Phụ trách | Việc cần bàn giao |
| --- | --- | --- |
| CP1–CP2 · Chi phí và độ nhạy | Hâu viết code, Thịnh kiểm số | Hâu làm A1–A4 và B1–B4 trong `src/lab13.py`. Thịnh tính tay ít nhất một kết quả để đối chiếu, điền bảng và câu trả lời vào `report/team/bang_chi_phi.md`. Huy theo dõi điều kiện hoàn thành từng checkpoint. Thái mở hồ sơ launch v0 và điền dần theo kết quả nhóm bàn giao. |
| CP3 · Bảng lỗi | Huy và Thái | Mỗi người tự gắn nhãn đủ 20 ca trong 8 phút, không trao đổi trước khi so. Huy tổng hợp hai bộ nhãn gốc và tính đồng thuận (mục tiêu ít nhất 16/20). Cả hai thống nhất quy tắc cho ca lệch nhãn và điền 5 ca khắc phục, mỗi loại một ca, vào `report/team/bang_loi.md`. Trong lúc gắn nhãn, Thịnh tiếp quản code để chốt CP2, Hâu đối chiếu lại kết quả. |
| CP4 · Thiết kế pilot | Thịnh chủ trì, Hâu kiểm số | Thịnh viết phần D1 trong `src/lab13.py`, tính tỷ lệ mở lại trong 7 ngày và điền `report/team/pilot_plan.yaml`. Hâu đối chiếu cỡ mẫu. Cả nhóm chốt cách chia và trả lời D2. Thịnh kiểm tra YAML đọc được và có đủ ba luật dừng về an toàn, chi phí và mức sử dụng. |
| CP5 · Chỉ số và hồ sơ launch | Huy phụ trách chỉ số, Thái phụ trách hồ sơ | Huy hoàn thiện `report/team/chi_so.md` với ba chỉ số tính thử, hai chỉ số đề xuất và ít nhất sáu event có `trace_id`. Hâu cung cấp số từ bảng độ nhạy cho ít nhất hai rủi ro kinh tế. Thái tổng hợp hồ sơ một trang đủ bảy mục và gửi nhóm hội đồng vào mốc 17:00 theo lịch mẫu. Cả nhóm chốt đề xuất Go, Go có điều kiện hoặc No-go dựa trên kết quả. |
| Duyệt chéo và nộp bài | Thái tổng hợp, Hâu kiểm tra và push | Cả nhóm chấm nhóm được giao. Thái ghi kết quả vào `report/team/phieu_cham.md` và tổng hợp `report/team/group_report.md`. Thịnh chạy lại code trên máy khác với máy đã dùng ở CP1. Hâu rà checklist và push bản nộp. Mỗi người tự làm báo cáo cá nhân, ghi đóng góp và bằng chứng vào `TEAM.md`, rồi tự nộp cùng link repo trên LMS. |

Hâu bàn giao code cho Thịnh sau giờ giải lao. Cả hai tự chạy phần tính chi phí để đối chiếu kết quả trước khi chốt bảng.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## BuiGiaHuy-2A202603525

### Phần việc phụ trách

- CP3 (Nhiệm vụ C): Người gắn nhãn 1 cho 20 ca lỗi theo Google PAIR, tổng hợp kết quả đối chiếu với Vũ Quang Thái, tính tỉ lệ đồng thuận và hoàn thiện bảng khắc phục 5 ca (`report/team/bang_loi.md`).
- CP5 (Nhiệm vụ E1): Tính thử 3 chỉ số từ `src/logix_requests.csv`, đề xuất thêm 2 chỉ số, thiết kế danh sách event có `trace_id` và kiểm tra chéo (`report/team/chi_so.md`).

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi, đối chiếu với Vũ Quang Thái đạt đồng thuận 19/20 (95%), thống nhất quy tắc phân biệt cho Ca 13 (Giới hạn hệ thống) và xây dựng bảng khắc phục 5 ca đủ 5 loại có cách phát hiện đo được và 1 vai trò phụ trách.
- Tính 3 chỉ số thử nghiệm (`82,83%`, `27,12%`, `4,25%`), đề xuất 2 chỉ số mới (tỉ lệ mở gợi ý, tỉ lệ sai tiền qua kiểm tra mẫu), xây dựng 11 event gắn `trace_id` và ánh xạ kiểm tra chéo đầy đủ.

### Bằng chứng

- `report/team/bang_loi.md`
- `report/team/chi_so.md`
- `report/team/2A202603525_BuiGiaHuy.md`

## VuQuangThai-2A202603545

### Phần việc phụ trách

- CP3: người gắn nhãn 2; gắn độc lập 20 ca và đối chiếu với Huy sau khi hoàn thành bộ nhãn riêng.
- CP1–CP5: giữ hồ sơ launch, tổng hợp kết quả, bằng chứng và trạng thái; tổng hợp báo cáo nhóm. Duyệt chéo và bàn giao Hậu push khi đủ đầu vào.

### Đóng góp cụ thể

- Bộ nhãn người 2 đủ 20 ca; đồng thuận ban đầu 19/20 (95%); ca 13 thống nhất Giới hạn hệ thống theo nguyên nhân gốc.
- Tổng hợp hồ sơ launch 7 mục, nhãn `simulated`, bằng chứng và đề xuất Go có điều kiện từ kết quả nhóm.
- Điền báo cáo nhóm CP1–CP5 và báo cáo cá nhân. Phần duyệt chéo ghi chờ hội đồng; chưa có điểm hoặc quyết định chấm nhóm khác.

### Bằng chứng

- [Bảng lỗi](report/team/bang_loi.md)
- [Hồ sơ launch v0](report/team/ho_so_launch_v0.md)
- [Báo cáo nhóm](report/team/group_report.md)
- [Báo cáo cá nhân Vũ Quang Thái](report/team/2A202603545_VuQuangThai.md)
