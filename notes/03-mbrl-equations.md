# Model-based RL: 3 công thức cốt lõi của world model

> Ghi chú học tập. Nguồn: survey *Understanding World or Predicting Future? A Comprehensive Survey of World Models* (Ding et al., 2024, arXiv:2411.14499), mục 3.1.1.

---

## 0. Bức tranh lớn

Ba công thức không đứng riêng lẻ. Chúng là **ba khâu của cùng một vòng lặp**:

```
        ┌──────────────── dữ liệu mới ◄────────────────┐
        ↓                                               │
  (1) Học đoán đúng  ──►  (2) Học biết mình chắc ──►  (3) Tưởng tượng, chọn,
      (đoán μ)               đến đâu (đoán σ)             làm 1 bước
```

- **Công thức (1) và (2): HỌC.** Dạy world model đoán tương lai. Thứ được chỉnh là **trọng số θ** của model.
- **Công thức (3): DÙNG.** Dùng world model để chọn hành động. Model giữ nguyên, thứ được chọn là **chuỗi action a**.

Mẹo nhận biết: `min_θ` là đang **học**, `max_a` là đang **dùng**.

### Ngôn ngữ chung: MDP `(S, A, M, R, γ)`

| Ký hiệu | Tên | Nghĩa | Ví dụ cánh tay robot |
|---|---|---|---|
| `S` | State space | Mọi trạng thái có thể | Góc, vận tốc các khớp |
| `A` | Action space | Mọi hành động có thể | Quay khớp −1°, 0°, +1° |
| `M` | Transition dynamics | Luật chuyển trạng thái `(s, a) → s'` | Quay +1° thì góc mới bằng bao nhiêu |
| `R` | Reward | Điểm thưởng mỗi bước | Tay càng gần cốc, điểm càng cao |
| `γ` | Discount factor | Phần thưởng xa trong tương lai được tính ít hơn | 100k hôm nay đáng giá hơn 100k năm sau |

**Ý quan trọng nhất:** `R` do mình tự đặt (mình biết mục tiêu), còn `M` là luật của thế giới mà mình không biết, nên phải **học**. **`M` chính là world model.**

### Bảng ký hiệu dùng trong ghi chú này

| Ký hiệu | Nghĩa |
|---|---|
| `s` | Trạng thái hiện tại |
| `a` | Hành động |
| `s'` | Trạng thái tiếp theo **thật** (đo ngoài đời) |
| `M*` | Luật thật của thế giới (không ai biết, chỉ thu được dữ liệu từ nó) |
| `M_θ` | World model của mình, là một mạng neural có trọng số `θ` |
| `μ`, `σ` | Giá trị model đoán hay xảy ra nhất, và mức "không chắc" |
| `τ` | Horizon: nhìn trước bao nhiêu bước |
| `E[·]` | Kỳ vọng, hiểu đơn giản là **lấy trung bình** |

---

## 1. Công thức (1): học đoán đúng

$$
\min_{\theta}\; \mathbb{E}_{s' \sim M^*(\cdot \mid s,a)}\Big[\, \big\| s' - M_\theta(s,a) \big\|_2^2 \,\Big]
$$

**Đọc thành lời:** chỉnh trọng số `θ` sao cho, trung bình trên dữ liệu thật, **chỗ model đoán gần chỗ thật xảy ra nhất**.

### Từng mảnh, đọc từ trong ra ngoài

| Mảnh | Nghĩa |
|---|---|
| `M_θ(s, a)` | Model nhận `(s, a)`, xuất ra `s'` **dự đoán** |
| `s' − M_θ(s, a)` | Sai số = thật − đoán |
| `‖ · ‖²` | Bình phương: sai số luôn dương, sai càng lớn phạt càng nặng |
| `s' ~ M*(·\|s,a)` | `s'` được lấy từ thế giới thật |
| `E[ · ]` | Trung bình trên toàn bộ dữ liệu |
| `min_θ` | Tìm `θ` làm con số trên nhỏ nhất, tức là **train** |

**Trực quan:** đây là **bài toán hồi quy** bình thường (input `(s, a)`, nhãn `s'`), giống *system identification* trong môn điều khiển. Khác ở chỗ mô hình là mạng neural chứ không phải phương trình tự viết.

### Câu hỏi tiếp theo: làm sao thật sự tìm được θ tốt nhất?

Công thức (1) chỉ nói **mục tiêu**: "tìm θ cho sai số nhỏ nhất". Nó **không nói cách làm**.

- Không thể thử hết mọi giá trị θ, vì một mạng neural có hàng nghìn đến hàng triệu con số θ.
- Cách làm phổ biến nhất là **gradient descent** ("đi xuống dốc"). Đây chính là thứ chạy bên trong 2 dòng `loss.backward()` và `optimizer.step()` ở phần code bên dưới, và cũng là nút **"Train 1 bước"** trong mô phỏng.

Nói gọn: **công thức (1) = đích đến, gradient descent = cách đi đến đích.**

### Trực quan: người bịt mắt xuống đồi

Tưởng tượng MSE là **độ cao của một ngọn đồi**, còn θ là **vị trí bạn đang đứng**. Bạn bị bịt mắt nhưng muốn xuống chỗ thấp nhất (sai số nhỏ nhất). Bạn làm thế này:
1. Dò chân thử xem **bên nào thấp hơn**.
2. **Bước một bước** về phía đó.
3. Lặp lại cho đến khi không còn chỗ nào thấp hơn.

### Ví dụ tính tay, bước 1: dò chân bằng cách "nhích thử"

World model đơn giản: `Δx = w · a`. Ở đây θ chỉ là một con số `w`. Thế giới thật: `Δx = 1.0 · a`.

Có 2 điểm dữ liệu: `(a = +1, Δx = +1.0)` và `(a = −1, Δx = −1.0)`. Bắt đầu với `w = 0.3`.

- Với `w = 0.3`: model đoán `0.3` và `−0.3`, sai số `0.7` và `−0.7`, nên **MSE = (0.7² + 0.7²) / 2 = 0.49**.
- **Nhích thử** `w` lên một chút, thành `w = 0.31`: sai số còn `0.69`, nên **MSE = 0.69² = 0.4761**.

→ Tăng `w` thì MSE **giảm**. Vậy **tăng w là đúng hướng xuống dốc**.

Độ dốc = "nhích một chút thì MSE thay đổi bao nhiêu":

```
độ dốc ≈ (0.4761 − 0.49) / 0.01 ≈ −1.4
```

Dấu **âm** nghĩa là: đi về phía w lớn hơn thì xuống dốc. Con số này chính là **đạo hàm** `∂MSE/∂w`.

> Ghi chú: thay vì nhích thử, có thể tính đạo hàm bằng công thức. Đạo hàm của `(Δx − w·a)²` theo `w` là `−2a(Δx − w·a)`. Trung bình 2 điểm: `[−2·(1)·(0.7) + (−2)·(−1)·(−0.7)] / 2 = −1.4`, khớp với kết quả nhích thử. PyTorch tự tính phần này trong `loss.backward()`.

### Ví dụ tính tay, bước 2: bước một bước

Quy tắc bước đi:

$$
w \leftarrow w - \eta \cdot \text{độ dốc}
$$

- `η` (learning rate) = **độ dài bước chân**. Ở đây chọn `η = 0.3`.
- Dấu trừ để luôn đi **ngược chiều dốc**: dốc âm thì `w` tăng, dốc dương thì `w` giảm.

Tính:

```
w ← 0.3 − 0.3 · (−1.4) = 0.3 + 0.42 = 0.72
```

Kiểm tra lại: với `w = 0.72`, sai số còn `0.28` và `−0.28`, nên **MSE = (0.28² + 0.28²) / 2 ≈ 0.078**. Giảm từ 0.49 xuống 0.078 chỉ sau 1 bước.

Lặp lại vài bước nữa, `w` sẽ tiến về `1.0`, đúng bằng thế giới thật.

**Lưu ý về η:** bước quá ngắn thì xuống đồi rất lâu; bước quá dài thì có thể **nhảy vọt qua đáy** sang sườn bên kia, và MSE còn tăng lên.

Lặp lại vài bước nữa, `w` sẽ tiến về `1.0`.

### Code PyTorch

```python
pred = model(s, a)                                   # M_θ(s, a)
loss = ((s_next - pred) ** 2).sum(dim=-1).mean()     # ‖·‖² rồi E[·]
optimizer.zero_grad()
loss.backward()                                      # tính đạo hàm
optimizer.step()                                     # θ ← θ − η·đạo hàm
```

---

## 2. Công thức (2): học biết mình chắc đến đâu

$$
\min_{\theta}\; \mathbb{E}_{s' \sim M^*(\cdot \mid s,a)}\left[ \log \frac{M^*(s' \mid s,a)}{M_\theta(s' \mid s,a)} \right]
$$

### Vì sao cần?

Thế giới có **ngẫu nhiên** (*aleatoric uncertainty*). Cùng một lệnh "quay +1", 5 lần đo có thể ra `0.14, 0.16, 0.15, 0.13, 0.17` do ma sát, rung, nhiễu encoder.

Model của công thức (1) chỉ được trả lời **một số**, nên không nói được "kết quả hay dao động". Công thức (2) cho model trả lời **hai số**:
- `μ`: giá trị hay xảy ra nhất (giống output của công thức 1).
- `σ`: mức không chắc chắn.

Giống dự báo thời tiết: không nói "mai mưa", mà nói "mai 70% mưa".

`μ` và `σ` vẽ ra một **cái chuông Gaussian**. `M_θ(s' | s, a)` là **độ cao của chuông tại điểm s'**, tức là model tin s' xảy ra nhiều hay ít.

### Từ công thức gốc đến thứ thật sự được train

Tách `log(a/b) = log a − log b`:

$$
\mathbb{E}\big[\log M^*(s' \mid s,a)\big] \;-\; \mathbb{E}\big[\log M_\theta(s' \mid s,a)\big]
$$

- Vế đầu chỉ phụ thuộc thế giới thật, chỉnh `θ` thế nào cũng không đổi, nên **bỏ đi**.
- Còn lại:

$$
\min_\theta\; \mathbb{E}\big[-\log M_\theta(s' \mid s,a)\big]
$$

**Đọc thành lời:** làm sao để model **gán xác suất cao cho những gì thực sự xảy ra**. Biểu thức gốc gọi là **KL divergence** (đo hai phân phối khác nhau bao nhiêu). Cách train này gọi là **maximum likelihood**.

### Điểm phạt −log: "đặt cược"

| Model gán xác suất bao nhiêu cho kết quả thật | Điểm phạt −log(p) |
|---|---|
| 0.9 | 0.11 (phạt nhẹ) |
| 0.5 | 0.69 |
| 0.1 | 2.30 |
| 0.01 | 4.61 (phạt nặng) |
| 0 (chắc chắn điều đó không xảy ra, mà nó lại xảy ra) | ∞ |

### Với chuông Gaussian, điểm phạt có dạng cụ thể (bỏ hằng số)

$$
\text{phạt} = \underbrace{\frac{(s' - \mu)^2}{2\sigma^2}}_{\text{phạt đoán sai}} + \underbrace{\log \sigma}_{\text{phạt khai không chắc}}
$$

Ví dụ: kết quả thật `s' = 0.15`.

| Model | μ | σ | Tổng phạt | Nhận xét |
|---|---|---|---|---|
| A | 0.15 | 0.01 | −4.6 | Đúng và tự tin: **tốt nhất** |
| C | 0.10 | 0.05 | −2.5 | Sai nhưng khiêm tốn: tạm được |
| D | 0.15 | 1.00 | 0 | Đúng nhưng luôn khai "không chắc": bị phạt |
| B | 0.10 | 0.01 | 7.9 | **Sai mà tự tin: tệ nhất** |

(Phạt âm là bình thường, chỉ cần nhớ **càng nhỏ càng tốt**.)

**Hai bài học:** sai mà tự tin bị phạt nặng nhất; khai σ thật to để né phạt cũng không được vì vế `log σ`. Model bị ép phải **trung thực** về độ chắc chắn.

### Liên hệ với công thức (1)

Nếu cố định σ (không cho model tự đoán), `log σ` thành hằng số, chỉ còn `(s' − μ)²`. **Công thức (1) là trường hợp đặc biệt của công thức (2).**

### Thuật toán và code

Vẫn là gradient descent như mục 1, chỉ khác là model xuất 2 đầu ra. Trong thực tế, model xuất `log σ` thay vì `σ` để σ luôn dương.

```python
mu, log_sigma = model(s, a)
sigma = log_sigma.exp()
loss = ((s_next - mu) ** 2 / (2 * sigma ** 2) + log_sigma).mean()
```

Công thức này đến từ Chua et al. 2018, paper **PETS**.

---

## 3. Công thức (3): dùng model để chọn hành động (MPC)

$$
\max_{a_{t:t+\tau}}\; \mathbb{E}_{s_{t'+1} \sim p(s_{t'+1} \mid s_{t'},\, a_{t'})}\left[\, \sum_{t'=t}^{t+\tau} r(s_{t'}, a_{t'}) \right]
$$

**Đọc thành lời:** trong mọi chuỗi hành động có thể, chọn chuỗi mà khi **tưởng tượng bằng world model** sẽ cho **tổng điểm trung bình cao nhất**.

Gói gọn: **tưởng tượng nhiều kế hoạch → chấm điểm → chọn kế hoạch tốt nhất.**

Giống chọn đường đi học về: bạn tưởng tượng đường A kẹt xe, đường B đang sửa, đường C thoáng, rồi chọn C. Bạn chưa đi thử đường nào; tưởng tượng được là nhờ **kinh nghiệm**, chính là world model.

### Từng mảnh

| Mảnh | Nghĩa | Ví dụ đi học về |
|---|---|---|
| `a_{t:t+τ}` | Một kế hoạch: chuỗi action từ bước t đến t+τ | Một con đường |
| `p(s_{t'+1} \| s_{t'}, a_{t'})` | World model đã học ở (1)/(2), dùng để tưởng tượng | Kinh nghiệm của bạn |
| `r(s, a)` | Điểm mỗi bước | Thời gian từng đoạn đường (ít là tốt) |
| `Σ` | Cộng điểm cả kế hoạch | Tổng thời gian về nhà |
| `E` | Tưởng tượng vài lần rồi lấy trung bình, vì tương lai không chắc | "Đường C *thường* mất 20 phút" |
| `max` | Chọn kế hoạch tốt nhất | Chọn đường C |

### Ví dụ tính tay (bài toán 1 chiều)

Tay gắp ở `x = 0`, cốc ở `x = 3`. Action `a ∈ {−1, 0, +1}`. World model: `x' = x + a`. Điểm mỗi bước: `r = −|(x + a) − 3|` (đến đúng cốc thì r = 0, cao nhất). `τ = 2`, nghĩa là 3 bước.

| Kế hoạch | Vị trí tưởng tượng | Điểm từng bước | Tổng |
|---|---|---|---|
| [+1, +1, +1] | 0 → 1 → 2 → 3 | −2, −1, 0 | **−3** ← chọn |
| [+1, +1, 0] | 0 → 1 → 2 → 2 | −2, −1, −1 | −4 |
| [+1, 0, +1] | 0 → 1 → 1 → 2 | −2, −2, −1 | −5 |
| [0, 0, 0] | 0 → 0 → 0 → 0 | −3, −3, −3 | −9 |

### Hai chi tiết thuật toán quan trọng

**a) Chỉ làm bước đầu tiên rồi tính lại (receding horizon).**
World model không hoàn hảo. Nếu làm hết cả kế hoạch mà không nhìn lại, sai số mỗi bước sẽ **cộng dồn** (*compounding error*). Vì vậy robot làm action đầu tiên, đo trạng thái thật, rồi lập kế hoạch lại từ đầu. Đây cũng là lý do một model có MSE nhỏ (sai ít trong **1 bước**) vẫn có thể cho kế hoạch tệ khi tưởng tượng **nhiều bước**.

**b) Ngoài đời không thử hết được mọi kế hoạch.**
Ví dụ trên có 3³ = 27 kế hoạch, thử hết được. Robot thật có action liên tục và horizon khoảng 15 bước, nên có vô số kế hoạch. Hai cách tìm phổ biến:

#### Hình dung: đi tìm kho báu trên bãi biển bằng máy dò kim loại

- **Random shooting:** đi **một lượt**, dò ngẫu nhiên 15 chỗ rải khắp bãi, chỗ nào máy kêu to nhất thì đào ở đó. Đơn giản, nhưng nếu kho báu nằm giữa hai chỗ đã dò thì sẽ bị lỡ.
- **CEM (Cross-Entropy Method):** dò **nhiều lượt, mỗi lượt khoanh vùng hẹp lại**.
  - Lượt 1: dò 5 chỗ rải khắp bãi, thấy máy kêu to ở **khu A**.
  - Lượt 2: chỉ dò 5 chỗ **quanh khu A**, thấy kêu to nhất ở một góc của khu A.
  - Lượt 3: dò 5 chỗ **quanh góc đó**, và tìm ra kho báu.

Cùng tổng 15 lần dò, nhưng CEM tìm chính xác hơn vì **dồn các lần dò vào vùng có triển vọng**.

Với robot: "bãi biển" là **tất cả các kế hoạch có thể**, "máy kêu to" là **điểm cao**, còn "dò một chỗ" là **tưởng tượng một kế hoạch bằng world model rồi chấm điểm**.

#### Ví dụ bằng số

Để dễ hình dung, giả sử mỗi kế hoạch chỉ là **1 con số v**: robot đi với tốc độ v trong cả 3 bước. Tay ở `x = 0`, cốc ở `x = 3`, world model `x' = x + v`, nên sau 3 bước tay ở `3v`. Điểm = `−|3v − 3|` (chỉ tính vị trí cuối, cho đơn giản). Đáp án đúng là `v = 1.0`.

**Random shooting: bốc 5 giá trị v ngẫu nhiên trong khoảng [−2, 2], chấm điểm, lấy cái tốt nhất**

| v | Vị trí cuối 3v | Điểm |
|---|---|---|
| −1.4 | −4.2 | −7.2 |
| 0.3 | 0.9 | −2.1 |
| **0.8** | 2.4 | **−0.6** ← tốt nhất |
| 1.6 | 4.8 | −1.8 |
| −0.5 | −1.5 | −4.5 |

→ Chọn `v = 0.8`. Gần đúng, nhưng chưa trúng 1.0, vì không có lần bốc nào rơi đúng vào chỗ tốt.

**CEM: bốc → giữ nhóm tốt nhất → bốc lại quanh nhóm đó → lặp**

| Lượt | Bốc quanh vùng nào | 5 giá trị bốc được | 2 giá trị tốt nhất | Vùng mới cho lượt sau |
|---|---|---|---|---|
| 1 | Tâm 0, rộng ±2 | −1.4, 0.3, 0.8, 1.6, −0.5 | 0.8 (−0.6), 1.6 (−1.8) | Tâm **1.2**, rộng ±0.4 |
| 2 | Tâm 1.2, rộng ±0.4 | 0.9, 1.0, 1.3, 1.5, 1.1 | 1.0 (0), 1.1 (−0.3) | Tâm **1.05**, rộng ±0.05 |
| 3 | Tâm 1.05, rộng ±0.05 | 1.0, 1.02, 1.04, 1.07, 1.09 | 1.0 (0), 1.02 (−0.06) | Đã đủ hẹp, dừng |

→ Chọn `v = 1.0`, trúng đáp án.

Cách lập "vùng mới": **tâm** = trung bình của nhóm tốt nhất, **độ rộng** = nhóm tốt nằm rải rác bao xa. Nhóm tốt càng tụm lại thì vùng càng hẹp. Tâm và độ rộng này thực chất là **μ và σ của một cái chuông Gaussian**, cùng kiểu chuông ở công thức (2), chỉ khác là ở đây chuông dùng để **bốc kế hoạch** chứ không phải để đoán tương lai.

#### So sánh

| | Random shooting | CEM |
|---|---|---|
| Cách làm | Bốc 1 lượt rải khắp nơi | Bốc nhiều lượt, mỗi lượt khoanh vùng hẹp lại |
| Ưu điểm | Rất dễ viết code | Chính xác hơn với cùng số lần thử |
| Nhược điểm | Dễ lỡ chỗ tốt nhất | Phức tạp hơn một chút |
| Ai dùng | Nagabandi et al. | PETS, V-JEPA 2-AC |

Ngoài đời, mỗi kế hoạch là **một chuỗi nhiều con số** (ví dụ 15 bước × số khớp của robot), chứ không phải 1 con số v. Nhưng cách làm vẫn y hệt: bốc nhiều chuỗi, chấm điểm, giữ nhóm tốt, khoanh vùng lại. Với toy project, nên bắt đầu bằng **random shooting** cho dễ, rồi nâng cấp lên CEM sau.

### Pseudocode MPC

```
Lặp mãi:
  1. Đo trạng thái thật s
  2. Bốc N kế hoạch, mỗi kế hoạch dài τ+1 bước
  3. Với mỗi kế hoạch:
       tưởng tượng bằng world model, cộng reward
       (model xác suất: tưởng tượng K lần, lấy trung bình   ← chữ E)
  4. Chọn kế hoạch điểm cao nhất                             ← chữ max
  5. Thực thi CHỈ action đầu tiên trên robot thật
  6. Quay lại bước 1
```

---

## 4. Ba công thức nối với nhau thế nào

| Từ | Sang | Thứ được truyền đi |
|---|---|---|
| (1) | (2) | `μ` mà model đoán ở (1) chính là tâm của cái chuông ở (2) |
| (1), (2) | (3) | World model đã học là "bộ não" để tưởng tượng trong (3) |
| (2) | (3) | `σ` là lý do (3) cần chữ `E`: tương lai dao động nên phải lấy trung bình |
| (3) | (1) | Mỗi bước làm thật sinh ra một điểm dữ liệu `(s, a, s')` mới, đưa về (1) để học tiếp |

### Thuật toán model-based RL đầy đủ

```
0. Cho robot làm hành động ngẫu nhiên, thu dữ liệu ban đầu D = {(s, a, s')}
Lặp:
  1. Train world model trên D bằng công thức (1) hoặc (2)       ← HỌC
  2. Chạy robot vài bước, mỗi bước chọn action bằng MPC (3)    ← DÙNG
  3. Thêm các bước vừa chạy vào D
```

**Một câu để nhớ:** thu dữ liệu → học cách đoán (1, 2) → dùng cách đoán để chọn hành động (3) → làm thật → có dữ liệu mới → học tiếp. Giống học lái xe: tập thì có kinh nghiệm, lái thật thì dùng kinh nghiệm, mỗi chuyến đi lại có thêm kinh nghiệm.

---

## 5. Những chỗ mình từng hiểu sai

- **So sánh hai thứ phải giữ cùng một tiêu chí.** Cả "hiểu thế giới" lẫn "dự đoán tương lai" đều học từ dữ liệu thế giới, nên "học từ đâu" không phải điểm khác. Khác nhau ở **output**: biểu diễn ẩn bên trong và trạng thái/hình ảnh nhìn thấy được.
- **`min_θ` khác `max_a`.** (1)/(2) chỉnh model lúc train. (3) giữ nguyên model, chỉ tìm action lúc chạy.
- **MSE nhỏ chưa chắc robot làm tốt.** Công thức (1) đo sai số **một bước**, còn MPC dùng model **nhiều bước liên tiếp**, nên sai số có thể cộng dồn.

---

## 6. Tự kiểm tra

1. Thật là 0.15, model đoán 0.12. Sai số bình phương bằng bao nhiêu?
2. App X nói "100% nắng", app Y nói "60% nắng". Trời mưa. App nào bị phạt nặng hơn theo công thức (2), vì sao?
3. Cốc ở `x = −2`, tay ở `x = 0`, tưởng tượng 3 bước. Kế hoạch nào tốt hơn: [−1, −1, 0] hay [−1, −1, −1]?
4. Nếu bỏ công thức (1), robot sẽ gặp chuyện gì?

<details>
<summary>Đáp án</summary>

1. `(0.15 − 0.12)² = 0.0009`.
2. App X. Nó gán 0% cho "mưa", nên −log(0) = ∞. App Y gán 40% cho "mưa", chỉ bị phạt −log(0.4) ≈ 0.92. Sai mà tự tin bị phạt nặng nhất.
3. [−1, −1, 0], tổng −1 (vị trí −1 → −2 → −2). Kế hoạch [−1, −1, −1] đi quá cốc, tổng −2.
4. Không có world model để tưởng tượng, nên công thức (3) không chạy được. Robot hoặc phải thử và sai ngoài đời thật (chậm, tốn kém, dễ hỏng phần cứng), hoặc tưởng tượng bằng một model sai và lên kế hoạch sai.

</details>

---

## Nguồn

- Ding et al. (2024). *Understanding World or Predicting Future? A Comprehensive Survey of World Models.* ACM Computing Surveys. arXiv:2411.14499, mục 3.1.1.
- Chua et al. (2018). *Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models* (PETS). arXiv:1805.12114.
- Nagabandi et al. (2018). *Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning.*
