# Danh sách đọc cho người mới

⭐ = nên đọc · ○ = đọc thêm

**Lộ trình gọn nhất (6 bài):** 1 → 4 → 5 → 6 → 13 → 14

---

## Bước 1: Survey

| # | Tên | Tác giả, năm | arXiv | Trạng thái |
|---|---|---|---|---|
| 1 ⭐ | Understanding World or Predicting Future? A Comprehensive Survey of World Models | Ding et al., 2024 | 2411.14499 | Đang đọc (xong 1, 2, 3.1.1) |
| 2 ⭐ | A Step Toward World Models: A Survey on Robotic Manipulation | 2025 | 2511.02097 | |
| 3 ○ | Model-based Reinforcement Learning: A Survey | Moerland et al., 2020 | 2006.16712 | |

**Cách đọc survey số 1 (cho hướng robotics):**
- Đọc kỹ: Abstract, 1, 2, 3.1.1, 5.2
- Đọc lướt: 4.1, 6.1, 6.3, 6.6, 7
- Bỏ qua tạm thời: 3.1.2, 3.2, 4.2, 5.1, 5.3, 6.2, 6.4, 6.5

## Bước 2: Paper kinh điển

| # | Tên | Tác giả, năm | arXiv |
|---|---|---|---|
| 4 ⭐ | World Models | Ha & Schmidhuber, 2018 | 1803.10122 |
| 5 ⭐ | Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models (PETS) | Chua et al., 2018 | 1805.12114 |
| 6 ⭐ | Learning Latent Dynamics for Planning from Pixels (PlaNet) | Hafner et al., 2019 | 1811.04551 |
| 7 ⭐ | Dream to Control: Learning Behaviors by Latent Imagination (Dreamer) | Hafner et al., 2020 | 1912.01603 |
| 8 ○ | Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model (MuZero) | Schrittwieser et al., 2020 | 1911.08265 |
| 9 ○ | Mastering Diverse Domains through World Models (DreamerV3) | Hafner et al., 2023 | 2301.04104 |
| 10 ○ | TD-MPC2: Scalable, Robust World Models for Continuous Control | Hansen et al., 2023 | 2310.16828 |

## Bước 3: SOTA

**Nhánh JEPA**

| # | Tên | Tác giả, năm | Nguồn |
|---|---|---|---|
| 11 ⭐ | A Path Towards Autonomous Machine Intelligence | LeCun, 2022 | OpenReview |
| 12 ○ | Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (I-JEPA) | Assran et al., 2023 | arXiv 2301.08243 |
| 13 ⭐ | V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning | Assran et al., 2025 | arXiv 2506.09985 |

**Nhánh generative**

| # | Tên | Tác giả, năm | Nguồn |
|---|---|---|---|
| 14 ⭐ | Genie: Generative Interactive Environments | Bruce et al., 2024 | arXiv 2402.15391 |
| 15 ○ | Video generation models as world simulators (Sora) | OpenAI, 2024 | Technical report |
| 16 ○ | Diffusion Models Are Real-Time Game Engines (GameNGen) | Valevski et al., 2024 | arXiv 2408.14837 |
| 17 ⭐ | Cosmos World Foundation Model Platform for Physical AI | NVIDIA, 2025 | arXiv 2501.03575 |
| 18 ○ | Genie 3: A new frontier for world models | DeepMind, 2025 | Blog |

**Giới hạn và đánh giá**

| # | Tên | Năm | Nguồn |
|---|---|---|---|
| 19 ○ | WorldBench: Disambiguating Physics for Diagnostic Evaluation of World Models | 2026 | arXiv 2601.21282 |

---

## Cách đọc một paper: 3 lượt

1. **Lượt 1 (10 phút):** tiêu đề, abstract, Figure 1, các heading, kết luận. Trả lời: bài này giải quyết vấn đề gì, bằng cách nào?
2. **Lượt 2 (khoảng 1 giờ):** hình, bảng kết quả, phần Method. Bỏ qua chứng minh. Đánh dấu chỗ chưa hiểu.
3. **Lượt 3 (khi cần):** chạy code của tác giả hoặc tự cài lại một phần.

## Template ghi chú cho mỗi paper

```
- Vấn đề:
- Ý tưởng chính (1 câu):
- Input → Output:
- Loss / cách train:
- Dữ liệu:
- Kết quả chính (con số):
- Giới hạn:
- Liên hệ với project của mình:
- Câu hỏi còn thắc mắc:
```

## Mẹo tìm trên Google Scholar

- Đặt cụm từ trong ngoặc kép: `"world model"`
- Chỉ tìm trong tiêu đề: `intitle:"world model"`
- Theo tác giả: `author:"D Hafner"`
- Bấm "Cited by" ở paper kinh điển để thấy các bài phát triển tiếp
- Không có PDF thì tìm tên bài trên arXiv
