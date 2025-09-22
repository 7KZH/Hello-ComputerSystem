import sys
import os

# 将项目根目录加入模块搜索路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def my_run():
    """
    实现一个支持 fork 系统调用的主运行循环。
    本示例使用 os.fork() 演示 fork 的行为。
    """
    print(f"Parent process starting (PID: {os.getpid()})")

    try:
        # 模拟某种条件触发 fork，比如接收到任务
        print("my_run: Running main loop...")

        # 假设在某个时刻需要创建新进程（例如处理新任务）
        input("Press Enter to fork a new process (or Ctrl+C to exit)...\n")

        # ============ FORK 系统调用 ============
        pid = os.fork()

        if pid == 0:
            # 子进程执行的逻辑
            child_main()
        else:
            # 父进程继续运行主循环
            print(f"Parent: forked child with PID {pid}")
            print("Parent: continuing main loop...\n")
            # 可以在这里继续处理其他任务
            my_run()  # 递归调用，允许再次 fork（仅用于演示）

    except KeyboardInterrupt:
        print(f"\nProcess {os.getpid()} exiting.")
    except OSError as e:
        print(f"Fork failed: {e}")
        sys.exit(1)

def child_main():
    """
    子进程的主函数
    """
    print(f"Child process running (PID: {os.getpid()}, Parent PID: {os.getppid()})")
    # 模拟子进程工作
    for i in range(5):
        print(f"Child {os.getpid()}: working... {i}")
        os.sleep(1)
    print(f"Child {os.getpid()}: finished.")
    os._exit(0)  # 子进程正常退出，避免影响父模块

# ================== 运行示例 ==================

if __name__ == "__main__":
    my_run()