import pytest
import shutil
import os
import sys
import threading


def pytest_launch(*args):
    """
    A function that can launch python per thread
    """
    pytest.main([*args])


if __name__ == '__main__':
    threads_count = int(sys.argv[1])
    report_dir = str(sys.argv[2])
    shutil.rmtree(report_dir, ignore_errors=True)
    os.makedirs(report_dir)

    for thread_number in range(threads_count):
        pytest_thread = threading.Thread(target=pytest_launch,
                                         args=(f"--threads-count={threads_count}", f"--thread-number={thread_number}",
                                               f"--cucumberjson={report_dir}/results_thread{thread_number}"))
        pytest_thread.start()
