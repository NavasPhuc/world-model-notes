# Survey Ding et al. (2024): phần 1–2

> *Understanding World or Predicting Future? A Comprehensive Survey of World Models.* ACM Computing Surveys. arXiv:2411.14499

---

## Ý chính

Survey chia world model theo **hai chức năng**:

| | Hiểu thế giới | Dự đoán tương lai |
|---|---|---|
| Model tạo ra gì | Biểu diễn ẩn bên trong (latent), con người không nhìn thấy | Trạng thái hoặc khung hình tương lai, nhìn thấy được |
| Ví dụ | Ha & Schmidhuber 2018, model-based RL, LLM | Sora, Kling, Gen-2 |
| Phần trong survey | Section 3 | Section 4 |

**Điểm chung:** cả hai đều học từ dữ liệu thế giới, và cùng hướng tới việc nắm động lực học của thế giới, tính được trạng thái kế tiếp để hỗ trợ ra quyết định và planning.

**Hình dung:** sinh viên A xem nhiều video bóng rơi, hiểu biết nằm trong đầu, dùng nó để chạy đến bắt bóng. Sinh viên B vẽ ra được 10 tấm ảnh bóng rơi tiếp theo. A là "hiểu thế giới", B là "dự đoán tương lai".

---

## Lịch sử (Section 2)

- **Thập niên 1960:** Minsky đề xuất *frame representation*, nỗ lực sớm để biểu diễn tri thức có cấu trúc về thế giới. Liên quan ý tưởng *mental model* trong tâm lý học.
- **2018:** Ha & Schmidhuber phổ biến lại thuật ngữ "world model" với mạng neural học latent. Agent nhận phản hồi, train model, mô phỏng kết quả trước khi chọn action, rất gần model-based RL.
- **2022:** LeCun đề xuất JEPA, với latent variable giữ thông tin then chốt và lọc phần dư thừa để hỗ trợ planning.
- **Từ 2023:** nhiều nghiên cứu cho thấy LLM chứa tri thức ngầm về không gian và thời gian.
- **2024:** model sinh video (Sora, Kling, Gen-2) mô phỏng được thay đổi động của cảnh.

### System 1 và System 2 (trong khung JEPA)

| | System 1 | System 2 |
|---|---|---|
| Đặc điểm | Phản xạ nhanh, không dùng world model | Suy nghĩ chậm, mô phỏng tương lai |
| Ví dụ | Né một người đang lao tới | Dự đoán chuyện xảy ra trong phòng 10 phút tới |
| Cánh tay robot | PID, dừng khẩn cấp trên STM32 | Lên quỹ đạo gắp vật trên PC |

---

## Hai trục phân loại khác nhau

| | Dự đoán trong latent | Dự đoán từng pixel |
|---|---|---|
| Thiên về hiểu thế giới | Ha 2018, Dreamer | — |
| Thiên về dự đoán tương lai | V-JEPA 2 | Sora, Genie, Cosmos |

- Survey phân loại theo **mục đích** (hiểu hay dự đoán).
- Nhiều tài liệu khác phân loại theo **không gian dự đoán** (pixel hay latent).
- Hai cách không mâu thuẫn. Khi hai nguồn xếp loại khác nhau, hãy hỏi: *họ đang phân loại theo tiêu chí nào?*

---

## Sora có phải world model đầy đủ không?

Chưa. Lý do:
1. Trông giống thật không có nghĩa là đúng vật lý.
2. Sora không nhận action, nên không dùng để planning được.
3. Chính survey cũng đặt câu hỏi này.

Mẹo phản biện: liệt kê các điều kiện cần (đúng vật lý, nhận action, dùng được để planning), rồi kiểm tra từng điều kiện.

---

## Những chỗ mình từng hiểu sai

- So sánh "hiểu" và "dự đoán" theo **input** (học từ đâu) là sai, vì cả hai đều học từ dữ liệu thế giới. Phải so theo **output**.
- "Biểu diễn ẩn" không có nghĩa là bí mật, chỉ là nằm bên trong model dưới dạng các con số con người không đọc được trực tiếp.

---

## Tự kiểm tra

1. Hai góc nhìn chính của survey là gì? Khác nhau ở đâu?
2. Ví dụ "né người đang lao tới" minh họa System 1 hay System 2?
3. Vì sao Sora chưa phải world model đầy đủ?
4. V-JEPA 2 nằm ở đâu trên hai trục phân loại?
