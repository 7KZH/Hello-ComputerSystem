import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.process import Process

def priority_scheduler(procs: list[Process]) -> Process:
    # 实现优先级调度器：选择 priority 最大的，相同时选更靠前的
    return max(procs, key=lambda p: p.priority)