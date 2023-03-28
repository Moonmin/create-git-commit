import random
from datetime import datetime, timedelta

# 生成时间戳
start_time = datetime(2022, 4, 1, 9, 0, 0)
end_time = datetime(2022, 5, 31, 21, 0, 0)
timestamps = []
delta = timedelta(minutes=1)

while start_time <= end_time:
    if start_time.hour >= 9 and start_time.hour < 21:
        # 生成随机秒数
        random_second = random.randint(0, 59)
        # 生成随机时间间隔
        random_delta = timedelta(seconds=random.uniform(0, 60))
        # 创建新的 timedelta 对象，并将其添加到 start_time 对象中
        new_delta = timedelta(seconds=random_second) + random_delta
        # 将新的 timedelta 对象添加到日期时间对象中，并生成时间戳
        ts = int((start_time + new_delta).timestamp())
        timestamps.append(ts)
    start_time += delta

# 随机打乱时间戳的顺序
random.shuffle(timestamps)

# 从中随机选择10个时间戳并排序
random_timestamps = sorted(random.sample(timestamps, k=10))

# 将时间戳转换为日期时间格式
random_date_times = [datetime.fromtimestamp(ts) for ts in random_timestamps]

# 打印随机时间
print("随机时间：", [dt.strftime("%Y-%m-%d %H:%M:%S") for dt in random_date_times])
