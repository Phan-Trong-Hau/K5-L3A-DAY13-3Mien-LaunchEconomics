"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p if p else math.inf
    return sum((1 - p) ** lan for lan in range(k))


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    runs = runs[runs.request_id.isin(reqs.request_id)]
    if max_lan_chay is not None:
        runs = runs[runs.attempt <= max_lan_chay]
        reqs = reqs[reqs.so_lan_chay <= max_lan_chay]

    token = (runs.tokens_in.sum() * gia_vao + runs.tokens_out.sum() * gia_ra) / 1000
    tool = runs.tool_calls.sum() * gia_tool
    chay_lai = runs[runs.attempt > 1]
    tien_chay_lai = (
        (chay_lai.tokens_in.sum() * gia_vao + chay_lai.tokens_out.sum() * gia_ra) / 1000
        + chay_lai.tool_calls.sum() * gia_tool
    )
    xem_lai = reqs.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = (reqs.ket_qua == 'thanh_cong').sum()
    return dict(token=token, tool=tool, chay_lai=tien_chay_lai, xem_lai=xem_lai,
                lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong if thanh_cong else math.inf)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    hoa_don = (ket_qua['token'] + ket_qua['tool']) / len(reqs)
    print(f'Hóa đơn token + tool/yêu cầu: {hoa_don:,.1f} đ')

    print('A3 · Loại | Yêu cầu | Thành công | Lần chạy/yêu cầu | Chi phí/việc (simulated) | Bội số')
    for loai, nhom in reqs.groupby('loai', sort=False):
        kq = mo_hinh(runs, nhom)
        print(f"{loai} | {len(nhom)} | {kq['thanh_cong'] / len(nhom):.1%} | "
              f"{nhom.so_lan_chay.mean():.2f} | {kq['cps']:,.0f} | {kq['cps'] / BASELINE:.2f}×")
    runs_quoc_te = runs[runs.request_id.isin(reqs.loc[reqs.loai == 'quoc_te', 'request_id'])]
    print('Tỷ lệ lần chạy quốc tế có trạng thái ok:',
          (runs_quoc_te.status == 'ok').groupby(runs_quoc_te.attempt).mean().to_dict())

    pilot = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    kq_pilot = mo_hinh(runs, pilot)
    ty_le_pilot = kq_pilot['thanh_cong'] / len(reqs)
    print('A4 · Yêu cầu/tháng | Việc thành công | Cố định/việc | Chi phí/việc (simulated) | Bội số')
    for khoi_luong in (45000, 22500):
        thanh_cong = khoi_luong * ty_le_pilot
        co_dinh = 40_000_000 / thanh_cong
        cps = kq_pilot['cps'] + co_dinh
        print(f'{khoi_luong:,} | {thanh_cong:,.0f} | {co_dinh:,.0f} | {cps:,.0f} | {cps / BASELINE:.2f}×')
    hoa_von = 40_000_000 / (BASELINE - kq_pilot['cps']) / ty_le_pilot
    print(f'Khối lượng hòa vốn theo mô hình A4 (simulated): {math.ceil(hoa_von):,} yêu cầu/tháng')

    kich_ban = {
        'Token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Tối đa 1 lần chạy': dict(max_lan_chay=1),
        'Token và xem lại cùng gấp đôi (B2)': dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2),
    }
    print('B1–B2 · Kịch bản | Chi phí/việc (simulated) | Thay đổi')
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f"{ten} | {cps:,.0f} | {cps / ket_qua['cps'] - 1:+.1%}")

    print('B3 · Giới hạn | Tổng trợ lý | Không thành công | Cả hệ thống | Chi phí/việc (simulated)')
    for gioi_han in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_thanh_cong * BASELINE
        print(f"{gioi_han} | {kq['tong']:,.0f} | {khong_thanh_cong} | {he_thong:,.0f} | {kq['cps']:,.0f}")

    so_xem_lai = runs.loc[(runs.status == 'ok') & runs.request_id.isin(pilot.request_id),
                         'request_id'].nunique()
    so_lam_lai = (pilot.ket_qua == 'lam_lai').sum()
    phut_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    hoa_don_pilot = kq_pilot['token'] + kq_pilot['tool']
    print(f'B4 · Xem lại {so_xem_lai} yêu cầu, làm lại {so_lam_lai} ca')
    for phut_lam_lai in (9, round(phut_tb, 1)):
        chi_phi_khac = hoa_don_pilot + so_lam_lai * phut_lam_lai * LUONG_PHUT
        cps = (chi_phi_khac + so_xem_lai * 5 * LUONG_PHUT) / kq_pilot['thanh_cong']
        phut_hoa_von = (BASELINE * kq_pilot['thanh_cong'] - chi_phi_khac) / (so_xem_lai * LUONG_PHUT)
        print(f'{phut_lam_lai:g} phút làm lại/ca | {cps:,.0f} đ/việc (simulated) | '
              f'{cps / BASELINE:.2f}× | hòa vốn ở {phut_hoa_von:.2f} phút xem lại')
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
