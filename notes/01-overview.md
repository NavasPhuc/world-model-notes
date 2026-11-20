# Tổng quan world model qua 8 tầng câu hỏi

> Khung học một lĩnh vực mới: đi từ ngoài vào trong, từ "vì sao" đến "làm thế nào".

---

## Tầng 1: Bức tranh lớn (Why)

**Định nghĩa 1 câu:** world model là một AI học được "luật chơi" của thế giới từ quan sát, để tưởng tượng xem *nếu làm X thì chuyện gì xảy ra tiếp theo*.

**Giải quyết vấn đề gì?** Giúp AI biết trước hậu quả của hành động mà không phải làm thật. Không có nó, robot phải thử và sai ngoài đời: chậm, tốn kém, dễ hỏng phần cứng.

**Trước đây làm thế nào, vì sao chưa đủ?**

| Cách cũ | Hạn chế |
|---|---|
| Control truyền thống (MPC với phương trình tự viết) | Không viết nổi phương trình cho thế giới phức tạp (vải mềm, chất lỏng, cảnh qua camera) |
| Physics engine (MuJoCo, Gazebo, Isaac Sim) | Phải dựng tay mô hình; mô phỏng khác thực tế (sim-to-real gap) |
| Model-free RL | Cần hàng triệu lần thử, không khả thi với robot thật |
| LLM | Hiểu ngôn ngữ nhưng không có cảm nhận vật lý |

**Khác gì với thứ đã biết?**

| So với | Khác |
|---|---|
| LLM | LLM đoán token tiếp theo; world model đoán trạng thái tiếp theo của môi trường khi có action |
| MPC | MPC dùng phương trình do người viết; world model tự học mô hình từ dữ liệu |
| Physics engine | Engine dùng luật vật lý tường minh; world model học xấp xỉ nên có thể sai |
| Model sinh video (Sora) | Video model chỉ "xem"; world model nhận action và phản hồi theo action |

---

## Tầng 2: Từ vựng

| Thuật ngữ | Nghĩa |
|---|---|
| Observation (o) | Dữ liệu cảm biến thô: ảnh, lidar, encoder khớp |
| State (s) | Trạng thái thật đầy đủ của hệ |
| Action (a) | Lệnh điều khiển gửi đi |
| Latent (z) | Vector nén biểu diễn ý nghĩa của observation |
| Encoder / Decoder | Mạng biến o thành z / biến z ngược lại thành ảnh |
| Dynamics model | f(z_t, a_t) → z_{t+1}, "trái tim" của world model |
| Action-conditioned | Dự đoán có phụ thuộc vào action |
| Rollout | Chạy dynamics model nhiều bước liên tiếp "trong đầu" |
| Planning (MPC, CEM) | Tìm chuỗi action tốt nhất dựa trên rollout |
| Policy (π) | Hàm chọn action trực tiếp từ state |
| Model-based RL | RL có dùng world model |
| Self-supervised learning | Tự tạo nhãn từ chính dữ liệu |
| Autoregressive | Sinh từng bước, lấy output bước trước làm input bước sau |
| Compounding error | Sai số nhỏ mỗi bước cộng dồn khi rollout dài |

**Hay nhầm:** observation khác state (một ảnh tĩnh không chứa vận tốc); latent là vector do model tự học, không ai đặt tên cho từng chiều.

---

## Tầng 3: Cơ chế

```
TRAINING:   (o_t, a_t, o_t+1) → Encoder → z_t → Predictor(z_t, a_t) → ẑ_t+1  ↔  loss
INFERENCE:  camera → Encoder → z_t → Planner thử nhiều chuỗi action trong world model
            → chọn chuỗi tốt nhất → làm action đầu tiên → quan sát lại → lặp
```

Chi tiết công thức: xem [`03-mbrl-equations.md`](03-mbrl-equations.md).

---

## Tầng 4: Lịch sử

| Năm | Mốc |
|---|---|
| 1970s–80s | MPC trong công nghiệp |
| 1990–1991 | Schmidhuber (RNN học mô hình môi trường), Sutton (Dyna) |
| 2018 | Ha & Schmidhuber, *World Models* |
| 2019–2020 | PlaNet, Dreamer, MuZero |
| 2022 | LeCun đề xuất kiến trúc JEPA |
| 2023 | DreamerV3, I-JEPA, TD-MPC2 |
| 2024 | Sora và Genie ra mắt cùng tháng 2 |
| 2025 | Cosmos, V-JEPA 2, Genie 3, Marble |
| 2026 | Genie 4, Cosmos 2.5, AMD mua World Labs |

---

## Tầng 5: Trường phái

| Trường phái | Ý tưởng | Đại diện |
|---|---|---|
| Generative ("vẽ lại thế giới") | Dự đoán từng pixel của tương lai | Genie, Cosmos, Sora |
| JEPA ("nén thế giới") | Dự đoán trong latent space, bỏ chi tiết không đoán được | V-JEPA 2, AMI Labs |
| World-action / VLA | Gộp dự đoán và ra quyết định trong một model | Các model policy 4D |

Tranh luận cốt lõi: "hiểu thế giới" có cần vẽ ra được thế giới không?

---

## Tầng 6: Hiện trạng và giới hạn

- **Đã làm được:** robot gắp-thả zero-shot với rất ít dữ liệu robot (V-JEPA 2-AC); sinh mô phỏng cho xe tự lái (Waymo).
- **Chưa giải được:** nhất quán dài hạn (vài phút), vật lý chính xác (benchmark WorldBench cho thấy model chưa nắm tham số vật lý), chưa có thước đo chuẩn cho việc "hiểu".
- **Benchmark:** Physics-IQ, WorldBench, SmallWorld, WoWBench; chỉ số pixel (PSNR, SSIM, FVD) không đo đúng vật lý.

---

## Tầng 7: Liên hệ với robotics

Kiến trúc chia tầng cho cánh tay robot:

```
PC / Jetson (1–10 Hz):     camera → world model → planner → điểm đặt khớp      (System 2)
       ↓ UART / CAN
STM32 (1–10 kHz):          PID → driver → motor ← encoder, công tắc hành trình  (System 1)
```

- System 1 (phản xạ nhanh) chạy trên vi điều khiển; System 2 (lên kế hoạch) chạy trên PC.
- Nguyên tắc an toàn: tầng thấp không bao giờ phụ thuộc tầng cao; luôn clamp điểm đặt và có watchdog.

---

## Tầng 8: Lộ trình

Xem [`../README.md`](../README.md) và [`reading-list.md`](reading-list.md).
