import time

def run_time_task():
    print("单击 “Enter” 键开始, 每一轮以“Enter”结束，使用 “Ctrl+c” 组合键 结束")
    input()  # 接收键盘的按键，可以是任意键位，但是最终以Enter为 计时开始
    print("start...")
    start_time = time.time()  # 开始计时...
    last_time = start_time  # 第一轮时  结束时间等于开始时间
    lap_num = 1  # 统计圈数
    try:
        while True:  # 死循环
            input()  # 接收下一轮的开始位置，以 Enter
            lap_time = round(time.time() - last_time, 2)  # 计算单轮的间隙时间
            total_time = round(time.time() - start_time, 2)  # 计算总时间
            print(f'Lap #{lap_num}: {total_time} ({lap_time})', end='')  # 打印输出
            print(f'Lap #{str(lap_num).rjust(2)}: {str(total_time).rjust(6)} ({str(lap_time).rjust(6)})', end='')  # 打印输出
            lap_num += 1  # 圈数 + 1
            last_time = time.time()  # 单圈结束时间S
    except KeyboardInterrupt:
        # Handle "Ctrl + c " Exception
        print("\n done")


if  __name__ == "__main__":
    run_time_task()