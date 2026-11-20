import os
import gymnasium as gym
import numpy as np

N_EPISODES = 50                    # 50 lượt × 200 bước = 10.000 bộ dữ liệu
env = gym.make("Pendulum-v1")

states, actions, next_states = [], [], []    # 3 danh sách rỗng

for ep in range(N_EPISODES):
    # TODO 1: reset môi trường.
    #   Dùng seed=ep để mỗi lượt bắt đầu ở một vị trí khác nhau
    obs, info = env.reset(seed = ep)

    while True:                    # lặp cho đến khi gặp break
        action = env.action_space.sample()

        # TODO 2: đẩy con lắc. Hứng trạng thái mới vào biến TÊN KHÁC: next_obs
        next_obs, reward, terminated, truncated, info = env.step(action)

        # TODO 3: ghi bộ (s, a, s') vào 3 danh sách
        #   Gợi ý: 3 dòng, mỗi dòng một .append(...)
        #   s là obs, a là action, s' là next_obs

        states.append(obs)
        actions.append(action)
        next_states.append(next_obs)

        

        # TODO 4: cập nhật: trạng thái mới trở thành trạng thái hiện tại
        obs = next_obs

        if terminated or truncated:
            break

env.close()

# TODO 5: biến 3 danh sách thành bảng số (dòng đầu đã viết mẫu)
S = np.array(states, dtype=np.float32)
A = np.array(actions,dtype=np.float32)
S_next = np.array(next_states,dtype=np.float32)

print("S:", S.shape, "| A:", A.shape, "| S_next:", S_next.shape)

os.makedirs("data", exist_ok=True)       # tạo thư mục data nếu chưa có
np.savez("data/pendulum_random.npz", S=S, A=A, S_next=S_next)
print("Đã lưu data/pendulum_random.npz")