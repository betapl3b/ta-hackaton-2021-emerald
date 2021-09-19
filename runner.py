import pytest
import shutil
import os
import sys
import threading
from hm_3_page_object.helpers.logger import Logger


def pytest_launch(*args):
    """
    A function that can launch python per thread
    """
    pytest.main([*args])


if __name__ == '__main__':
    # do
    os.environ['LOG_LEVEL'] = 'DEBUG'
    threads_count = int(sys.argv[1])
    report_dir = str(sys.argv[2])
    if len(sys.argv) > 3:
        add_args = sys.argv[3]
    else:
        add_args = ""
    shutil.rmtree(report_dir, ignore_errors=True)
    os.makedirs(report_dir)

    if os.environ.get('LOG_LEVEL'):
        shutil.rmtree('logs', ignore_errors=True)
        os.makedirs('logs')

    for thread_number in range(threads_count):
        pytest_thread = threading.Thread(target=pytest_launch,
                                         args=(f"--threads-count={threads_count}", f"--thread-number={thread_number}",
                                               f"--cucumberjson={report_dir}/results_thread{thread_number}.json",
                                               f"--junitxml={report_dir}/xml_thread{thread_number}.xml", add_args,
                                               "tests"))
        pytest_thread.start()
