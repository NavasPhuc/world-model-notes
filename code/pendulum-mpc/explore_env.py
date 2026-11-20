import gymnasium as gym
import numpy as np

env = gym.make("Pendulum-v1")

# TODO 1: reset môi trường để lấy observation đầu tiên
#   Gợi ý: env.reset(seed=0) trả về 2 thứ: (obs, info)
obs, info = env.reset(seed=0) 

print("Observation đầu tiên:", obs, "| shape:", obs.shape)
print("Không gian action:", env.action_space)

total_reward = 0.0
for t in range(200):
    # TODO 2: chọn một action ngẫu nhiên
    #   Gợi ý: env.action_space.sample()
    action = env.action_space.sample()

    # TODO 3: thực hiện action
    #   Gợi ý: env.step(action) trả về 5 thứ:
    #   (obs, reward, terminated, truncated, info)
    obs, reward, terminated, truncated, info = env.step(action)

    total_reward += reward
    if t < 5:
        print(f"t={t} | action={action} | obs={np.round(obs, 3)} | reward={reward:.3f}")

    # TODO 4: dừng vòng lặp nếu episode kết thúc
    if terminated or truncated:
            break   

print("Tổng reward sau 200 bước với action ngẫu nhiên:", round(total_reward, 1))
env.close()