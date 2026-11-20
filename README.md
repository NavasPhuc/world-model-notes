# World Model Notes

Ghi chú tự học về **world model** trong AI, từ lý thuyết đến code, theo góc nhìn của một sinh viên Robotics & AI.

> World model là một AI học được "luật chơi" của thế giới từ quan sát, để tưởng tượng xem *nếu làm X thì chuyện gì xảy ra tiếp theo*, rồi dùng khả năng đó để lên kế hoạch trước khi hành động thật.

## Nội dung

| File | Nội dung |
|---|---|
| [`notes/01-overview.md`](notes/01-overview.md) | Tổng quan world model qua 8 tầng câu hỏi, thuật ngữ cốt lõi |
| [`notes/02-survey-sec1-2.md`](notes/02-survey-sec1-2.md) | Ghi chú survey Ding et al. (2024), phần 1–2: hai góc nhìn "hiểu thế giới" và "dự đoán tương lai" |
| [`notes/03-mbrl-equations.md`](notes/03-mbrl-equations.md) | 3 công thức cốt lõi của model-based RL: MSE, KL/maximum likelihood, MPC, và cách chúng nối với nhau |
| [`notes/reading-list.md`](notes/reading-list.md) | Danh sách paper theo thứ tự đọc cho người mới, cách đọc paper |
| [`code/pendulum-mpc/`](code/pendulum-mpc/) | Toy project: world model + MPC cho con lắc (đang làm) |

## Lộ trình

- [x] Tuần 0: Tổng quan world model, đọc survey phần 1–2 và mục 3.1.1
- [ ] Tuần 1–2: PyTorch cơ bản, Gymnasium, Sutton & Barto ch.1–3 và ch.8
- [ ] Tuần 3: Toy project Pendulum + world model + MPC (random shooting)
- [ ] Tuần 4: Autoencoder/VAE, đọc Ha & Schmidhuber 2018
- [ ] Tuần 5–6: Planning từ ảnh (pixel), đọc PlaNet và Dreamer
- [ ] Tuần 7: Đọc JEPA, V-JEPA 2, Genie; so sánh hai trường phái
- [ ] Tuần 8: Mô phỏng cánh tay robot 2-DOF điều khiển bằng world model

## Môi trường

- Ubuntu 22.04, Python 3.10
- Toy project chạy trên CPU, không cần GPU

## Nguồn chính

- Ding et al. (2024). *Understanding World or Predicting Future? A Comprehensive Survey of World Models.* ACM Computing Surveys. arXiv:2411.14499
- Ha & Schmidhuber (2018). *World Models.* arXiv:1803.10122
- Chua et al. (2018). *Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models* (PETS). arXiv:1805.12114

## Ghi chú

Ghi chú được soạn trong quá trình tự học, có sự hỗ trợ của trợ lý AI để giải thích và kiểm tra kiến thức. Các phần được viết lại dần bằng lời của mình theo tiến độ học.
