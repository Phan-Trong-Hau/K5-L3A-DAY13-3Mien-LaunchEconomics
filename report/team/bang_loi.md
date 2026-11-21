# Bảng lỗi và cách khắc phục · Nhiệm vụ C

**Trạng thái: nhóm đã xác nhận đồng thuận; đã điền Nhãn người 2 theo xác nhận của thành viên.** Chờ nhập bộ nhãn người 1 để ghi kết quả đối chiếu và tỉ lệ đồng thuận. Phân loại bên dưới đối chiếu với hướng dẫn của lab; các ngưỡng phát hiện là đề xuất cho pilot, chưa phải kết quả đo.

Nguồn: [20 ca lỗi trong đề bài](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), mục “Hai mươi ca lỗi”; [hướng dẫn nhiệm vụ C và nhãn tham khảo](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhiệm-vụ-c--bảng-lỗi-và-cách-khắc-phục-30-phút); [quy tắc gắn nhãn độc lập](../../RULES.md#làm-bài-và-liêm-chính).

## Định nghĩa và cách chọn nhãn

Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa. Với bài lab này, lỗi chỉ lộ qua hậu kiểm được xếp **Ngầm**, dù nguyên nhân kỹ thuật có thể là lỗi hệ thống.

| Loại | Dấu hiệu phân biệt |
| --- | --- |
| Do người dùng | Khách nhập sai, chọn sai hoặc xác nhận nhầm; thiếu kiểm tra đầu vào là vấn đề cần khắc phục. |
| Hệ thống | Trợ lý làm sai thiết kế hoặc chính sách; sai sót đã lộ qua phản hồi, đầu ra hoặc bước xem lại. |
| Ngữ cảnh | Trợ lý làm đúng thiết kế/chính sách nhưng giả định về kỳ vọng, cách hiểu hoặc hoàn cảnh của khách không phù hợp. |
| Giới hạn hệ thống | Thiếu dữ liệu, ngoài phạm vi hoặc đầu vào chưa được hỗ trợ khiến trợ lý không thể xử lý. |
| Ngầm | Có sai sót về kết quả, chi phí hoặc dữ liệu nhưng khách và hệ thống không nhận ra trong luồng xử lý; chỉ lộ qua hậu kiểm. |

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Chờ nhóm điền** · Người gắn nhãn 2: **Đã xác nhận bộ nhãn; chờ bổ sung họ tên**.

Cột “Nhãn người 2” ghi bộ nhãn tham khảo đã được thành viên xác nhận sử dụng sau khi nhóm đồng thuận.

Mỗi người gắn đủ 20 ca trong 8 phút, không trao đổi và chưa xem phần tham khảo bên dưới. Giữ nguyên hai bộ nhãn sau khi so; chỉ ghi quyết định thảo luận vào cột “Nhãn thống nhất”. Nếu đã xem đáp án, ghi rõ việc đó; không xác nhận lượt gắn nhãn ấy là độc lập với đáp án.

Trong bảng này, `—` nghĩa là **chưa có dữ liệu**, không phải hai người đã đồng ý.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | — | Do người dùng | — | — |
| 2 | — | Hệ thống | — | — |
| 3 | — | Ngữ cảnh | — | — |
| 4 | — | Giới hạn hệ thống | — | — |
| 5 | — | Ngầm | — | — |
| 6 | — | Do người dùng | — | — |
| 7 | — | Hệ thống | — | — |
| 8 | — | Hệ thống | — | — |
| 9 | — | Do người dùng | — | — |
| 10 | — | Ngữ cảnh | — | — |
| 11 | — | Giới hạn hệ thống | — | — |
| 12 | — | Ngầm | — | — |
| 13 | — | Giới hạn hệ thống | — | — |
| 14 | — | Do người dùng | — | — |
| 15 | — | Hệ thống | — | — |
| 16 | — | Ngữ cảnh | — | — |
| 17 | — | Ngầm | — | — |
| 18 | — | Ngữ cảnh | — | — |
| 19 | — | Giới hạn hệ thống | — | — |
| 20 | — | Hệ thống | — | — |

**Tỉ lệ đồng thuận: chờ nhập bộ nhãn người 1 để tính và ghi số cụ thể.** Sau khi có đủ dữ liệu: số ca có nhãn người 1 bằng nhãn người 2 / 20 × 100%; đạt từ 16/20 = 80%. Tính trên nhãn ban đầu, trước thảo luận, không tính trên cột “Nhãn thống nhất”.

Mỗi ca trùng tương ứng 5 điểm phần trăm; nếu dưới 16 ca, viết lại định nghĩa và lưu phiên bản bổ sung trước khi đi tiếp, không sửa nhãn ban đầu để tăng tỉ lệ. Mức khớp đáp án tham khảo là một phép đối chiếu riêng, không phải tỉ lệ đồng thuận giữa hai người.

## Quy tắc phân biệt cho các ca không trùng

**Nhóm đã xác nhận đồng thuận; chờ bổ sung bộ nhãn người 1 và kết quả đối chiếu từng ca.** Với mỗi ca khác nhãn ban đầu, thêm một dòng theo mẫu: “Ca [số]: người 1 chọn [loại], người 2 chọn [loại]; thống nhất [loại] vì [một câu phân biệt nguyên nhân gốc].”

Các quy tắc tham khảo để xử lý ca dễ lẫn:

- **Ca 1, 6, 9, 14:** đầu vào hoặc thao tác của khách sai là nguyên nhân gốc nên chọn Do người dùng; bổ sung xác thực hay hướng dẫn thuộc phần khắc phục.
- **Ca 2, 15:** dùng sai loại hàng hoặc sai mức hoàn là Hệ thống; ca 15 đã bị nhân viên phát hiện trước khi gửi nên không phải Ngầm.
- **Ca 8:** viện dẫn điều khoản không tồn tại là Hệ thống, dù số tiền đúng; không cần chờ hậu kiểm mới thấy vấn đề trong đầu ra.
- **Ca 4, 11, 13, 19:** thiếu dữ liệu, không hỗ trợ âm thanh hoặc ngoài phạm vi là Giới hạn hệ thống; câu trả lời vòng vo ở ca 13 không thay đổi nguyên nhân gốc.
- **Ca 3, 10, 16, 18:** xử lý đúng thiết kế/chính sách nhưng lệch kỳ vọng, thời điểm hoặc cách hiểu của khách là Ngữ cảnh.
- **Ca 5, 12, 17:** sai tiền, chi phí tăng hoặc bảng giá cũ đều không bị nhận ra trong luồng xử lý nên chọn Ngầm; kết quả đúng ở ca 12 không loại trừ sai sót về chi phí.
- **Ca 7, 20:** thông báo thành công khi ghi sổ thất bại hoặc hoàn trùng do thiếu khóa chống trùng là Hệ thống, theo nhãn tham khảo của lab.

Nếu phải viết lại định nghĩa: **chờ kết quả so nhãn**; ghi định nghĩa cũ, định nghĩa mới, lý do và ca minh họa, giữ lại bằng chứng của lượt gắn nhãn đầu.

## Phân loại tham khảo cho 20 ca

Đây là bộ nhãn đối chiếu từ tài liệu lab, **không phải hai bộ nhãn độc lập của nhóm**. Tình huống và số liệu trong mô tả ca đều là giả lập (`simulated`); phần lý do giải thích cách áp dụng định nghĩa.

| Ca | Tình huống tóm tắt từ đề bài (simulated) | Nhãn tham khảo | Lý do phân loại |
| --: | --- | --- | --- |
| 1 | Khách nhập tài khoản thiếu hai chữ số; ngân hàng báo lỗi. | Do người dùng | Sai đầu vào từ khách dẫn tới lệnh hoàn thất bại. |
| 2 | Đơn nội địa 28 kg được tra như hàng thường; hoàn thiếu 45.000 đ, khách mở lại sau 2 ngày. | Hệ thống | Trợ lý truyền sai tham số loại hàng và sai sót đã được khách phản ánh. |
| 3 | Hoàn về ví LogiX đúng thiết kế trong 5 phút nhưng khách chờ tiền về ngân hàng. | Ngữ cảnh | Kênh nhận tiền đúng thiết kế nhưng khác kỳ vọng của khách. |
| 4 | Chặng do hãng nước ngoài giao không có dữ liệu; trợ lý chuyển nhân viên. | Giới hạn hệ thống | Thiếu dữ liệu để xác minh; chuyển nhân viên là xử lý giới hạn phù hợp. |
| 5 | Hậu kiểm thấy 14 đơn có mã giảm giá được hoàn thừa trung bình 12.000 đ; không ai báo. | Ngầm | Sai số tiền chỉ được phát hiện qua kiểm tra mẫu, không có cảnh báo trước đó. |
| 6 | Khách chọn hoàn do giao trễ nhưng mô tả hàng vỡ; đơn giao đúng hạn nên bị từ chối. | Do người dùng | Khách chọn sai mục khiếu nại là nguyên nhân gốc. |
| 7 | Sổ cái lỗi 503, thử lại 3 lần vẫn thất bại nhưng trợ lý báo đã hoàn. | Hệ thống | Thông báo thành công trái với trạng thái ghi sổ thực tế. |
| 8 | Trích dẫn Điều 7.2 không có trong chính sách hiện hành; số tiền vẫn đúng. | Hệ thống | Căn cứ chính sách do trợ lý đưa ra không tồn tại. |
| 9 | Khách nhập mã đơn sàn thay mã vận đơn; trợ lý báo không hợp lệ rồi dừng. | Do người dùng | Khách nhập sai loại mã; thiếu gợi ý là điểm cần cải thiện. |
| 10 | Từ chối hoàn do bão đúng chính sách nhưng ứng dụng vẫn cam kết giao 24 giờ. | Ngữ cảnh | Chính sách được áp dụng đúng nhưng thông điệp ứng dụng tạo kỳ vọng khác. |
| 11 | Tin nhắn thoại 40 giây không được hỗ trợ; trợ lý yêu cầu nhập chữ. | Giới hạn hệ thống | Dạng đầu vào âm thanh nằm ngoài khả năng xử lý. |
| 12 | Tool D05 thiếu trường, kết quả vẫn đúng nhưng token gấp 3 lần depot khác suốt 3 tuần. | Ngầm | Lãng phí chi phí kéo dài mà không được giám sát phát hiện. |
| 13 | Khách hỏi phí bảo hiểm đối tác ngoài phạm vi; trợ lý trả lời chung về phí vận chuyển. | Giới hạn hệ thống | Sản phẩm bảo hiểm ngoài phạm vi trợ lý; cần thông báo giới hạn rõ hơn. |
| 14 | Khách xác nhận nhầm đã nhận tiền khiến yêu cầu bị đóng. | Do người dùng | Khách thao tác xác nhận sai trạng thái nhận tiền. |
| 15 | Trễ 26 giờ phải hoàn 50% nhưng trợ lý tính 100%; nhân viên bắt lỗi trước khi gửi. | Hệ thống | Trợ lý tính sai chính sách và lỗi đã được phát hiện ở bước xem lại. |
| 16 | Gửi Zalo lúc 2:14 sáng theo thiết kế gửi ngay khi xong; khách bị làm phiền. | Ngữ cảnh | Thiết kế gửi đúng nhưng không phù hợp thời điểm sinh hoạt của khách. |
| 17 | Cache bảng giá cũ sau 01/11; 212 đơn dưới 2 kg lệch 1.000–2.000 đ trong 9 ngày, không ai mở lại. | Ngầm | Dữ liệu giá lỗi thời gây sai tiền mà không bị nhận ra trong luồng xử lý. |
| 18 | Phí 30.000 đ, hoàn đúng 50% = 15.000 đ nhưng không giải thích; khách tưởng thiếu. | Ngữ cảnh | Số tiền đúng, cách trình bày không đáp ứng nhu cầu hiểu cách tính. |
| 19 | Đơn từ 14 tháng trước ngoài cửa sổ truy cập 12 tháng; chuyển nhân viên kèm tóm tắt. | Giới hạn hệ thống | Dữ liệu cần tra ngoài phạm vi truy cập; cách chuyển giao đã phù hợp. |
| 20 | Khách gửi lại sau 10 phút; trợ lý hoàn hai lần vì thiếu khóa chống trùng. | Hệ thống | Thiếu cơ chế chống trùng làm phát sinh hai khoản hoàn cho cùng đơn. |

**Kiểm đếm bộ tham khảo:** Do người dùng 4 ca (1, 6, 9, 14); Hệ thống 5 ca (2, 7, 8, 15, 20); Ngữ cảnh 4 ca (3, 10, 16, 18); Giới hạn hệ thống 4 ca (4, 11, 13, 19); Ngầm 3 ca (5, 12, 17). Tổng 4 + 5 + 4 + 4 + 3 = 20 ca; đây là cơ cấu bộ đề, không phải tỉ lệ lỗi vận hành.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện dưới đây là **đề xuất**: mỗi dòng có event, ngưỡng kích hoạt và tần suất kiểm tra; ngưỡng chưa được kiểm chứng bằng dữ liệu pilot. Event cần ghi `trace_id`, `request_id`, thời điểm và trường liên quan để nối từ phát hiện tới xử lý. Vai trò phụ trách là đề xuất phân công, chờ nhóm xác nhận người đảm nhiệm.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Ghi `input_validation_failed` với `reason=wrong_code_type` cho từng lần nhập sai; kích hoạt hướng dẫn ngay khi có 1 lần sai. Hằng ngày cảnh báo nếu số yêu cầu có lỗi này / tổng yêu cầu có nhập mã > 2%, đếm mỗi yêu cầu một lần. | Nhận diện mã đơn sàn và tra sang mã vận đơn; nếu không tra được, hướng dẫn tìm mã kèm ví dụ và cho nhập lại hoặc chuyển nhân viên. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Ghi `refund_status_sent` và `ledger_write_result`; trước mỗi tin “đã hoàn” phải có bản ghi sổ cái `ok` khớp `trace_id` và mã giao dịch. Đối soát mỗi giờ; từ 1 tin thành công thiếu bản ghi `ok` thì cảnh báo, mức chấp nhận là 0 ca. | Chặn thông báo thành công nếu ghi sổ chưa `ok`; sau 3 lần thử thất bại báo “đang xử lý”, chuyển nhân viên và tra trạng thái giao dịch trước khi ghi lại bằng khóa chống trùng. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Ghi `refund_message_sent` có `original_fee`, `refund_rate`, `refund_amount`, `calculation_shown`; kiểm tra từng tin và cảnh báo ngay khi 1 tin hoàn theo tỉ lệ thiếu cách tính. Hằng tuần đối chiếu `request_reopened` với `reopen_reason=amount_dispute` và `policy_check=correct` để theo dõi tỉ lệ hiểu nhầm. | Dùng mẫu giải thích “Phí giao 30.000 đ × 50% = 15.000 đ” (ví dụ simulated từ ca 18), nêu căn cứ chính sách và kênh nhận tiền; thử mức dễ hiểu với nhân viên CSKH trước khi dùng trong pilot. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Với mỗi lần tra không có dữ liệu chặng nước ngoài, ghi `handoff_to_staff` có `reason=missing_foreign_leg_data` và `summary_attached`. Kiểm tra hằng ngày; từ 1 ca thiếu chuyển giao hoặc thiếu tóm tắt thì cảnh báo, mức chấp nhận là 0 ca. | Giữ thông báo không đủ dữ liệu và chuyển nhân viên kèm tóm tắt; đề xuất loại chặng nước ngoài khỏi phạm vi tự xử lý của pilot, đối chiếu phạm vi với CP1 trước khi chốt. | PM trợ lý hoàn phí |
| 17 | Ngầm | Ghi `refund_calculated` có `tariff_version`, `tariff_effective_date` và `refund_amount`. Mỗi tuần hậu kiểm ngẫu nhiên 100 đơn đã hoàn trong tuần, hoặc toàn bộ nếu ít hơn 100, đối chiếu bảng giá có hiệu lực tại thời điểm áp dụng; từ 1 đơn lệch thì cảnh báo. Với mẫu 100 đơn, ngưỡng này tương ứng ≥ 1%. | Xóa cache khi bảng giá mới có hiệu lực, kiểm tra phiên bản trước khi tính; khi có sai lệch, tạm chuyển nhóm đơn chịu ảnh hưởng sang nhân viên, rà soát và điều chỉnh các khoản hoàn sai. | Kế toán trưởng |

## Việc nhóm cần hoàn tất trước khi chốt CP3

- Bổ sung bộ nhãn người 1; hai người lưu riêng nhãn ban đầu, bổ sung tên người gắn nhãn và thời điểm thực hiện; ghi rõ nếu đã xem tham khảo.
- Đếm số ca trùng, tính tỉ lệ theo công thức trên; thảo luận ca khác nhãn và điền nhãn thống nhất cùng quy tắc một câu cho từng ca.
- Nếu dưới 80%, bổ sung định nghĩa đã sửa; kiểm tra riêng mức khớp đáp án từ 16/20 ca theo rubric.
- Xác nhận vai trò đảm nhiệm 5 phương án khắc phục; các event và ngưỡng ở đây mới là đặc tả đề xuất, chưa được triển khai hoặc đo thử.
