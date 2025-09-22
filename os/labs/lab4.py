import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def my_run():
    print(f"Parent process starting (PID: {os.getpid()})")

    try:
        # 模拟触发
        print("my_run: Running main loop...")

        # 假设创建新进程
        input("Press Enter to fork a new process (or Ctrl+C to exit)...\n")

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


if __name__ == "__main__":
    my_run()
