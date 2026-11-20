# Toy project: world model + MPC cho con lắc (Pendulum-v1)

> Trạng thái: chưa bắt đầu. Code trong thư mục này sẽ được tự viết từng bước.

## Mục tiêu

Cho con lắc tự đứng thẳng bằng một world model tự train, không dùng phương trình vật lý viết tay.

## Kế hoạch

1. **Thu dữ liệu:** cho môi trường chạy với action ngẫu nhiên, lưu khoảng 10.000 bộ `(s, a, s')`.
2. **Train world model:** MLP nhỏ `f(s, a) ≈ s'`, loss MSE (công thức 1).
3. **Planning:** random shooting MPC, bốc khoảng 500 chuỗi action dài 15 bước, tưởng tượng bằng world model, chọn chuỗi điểm cao nhất (công thức 3).
4. **Chạy:** chỉ thực thi action đầu tiên, quan sát lại, lặp lại.
5. **Lặp vòng MBRL:** thêm dữ liệu mới vào bộ dữ liệu, train lại.
6. **Nâng cấp (tùy chọn):** model xuất μ và σ (công thức 2), planner dùng CEM.

## Yêu cầu

- Python 3.10, `gymnasium`, `torch` (bản CPU), `numpy`, `matplotlib`
- Chạy được trên CPU

## Lý thuyết liên quan

Xem [`../../notes/03-mbrl-equations.md`](../../notes/03-mbrl-equations.md).
