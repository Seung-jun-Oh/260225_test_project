"""
GitHub 동기화 테스트용 스크립트
"""
# 버전 1: 기본 덧셈 함수

def add(a, b):
    return a + b

print(add(1, 2))

import platform
import datetime
import os


def get_system_info():
    """현재 시스템 정보를 반환"""
    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "os_version": platform.version(),
        "python_version": platform.python_version(),
        "user": os.getenv("USERNAME") or os.getenv("USER", "unknown"),
    }


def get_timestamp():
    """현재 시간을 포맷팅하여 반환"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def main():
    print("=" * 50)
    print("  GitHub Sync Test")
    print("=" * 50)

    info = get_system_info()
    print(f"\n[System Info]")
    print(f"  Hostname      : {info['hostname']}")
    print(f"  OS            : {info['os']} {info['os_version']}")
    print(f"  Python        : {info['python_version']}")
    print(f"  User          : {info['user']}")
    print(f"  Timestamp     : {get_timestamp()}")

    print(f"\n[Sync Check]")
    print(f"  This file was pulled/cloned successfully!")
    print(f"  Edit this message on another machine to verify sync.\n")


if __name__ == "__main__":
    main()
