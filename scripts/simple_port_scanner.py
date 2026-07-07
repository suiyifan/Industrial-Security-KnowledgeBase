#!/usr/bin/env python3
"""A tiny TCP port scanner for learning socket basics."""

from __future__ import annotations

import argparse
import socket


def is_open(host: str, port: int, timeout: float) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("host", help="Target host, for example 127.0.0.1")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--timeout", type=float, default=0.5, help="Socket timeout")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for port in range(args.start, args.end + 1):
        if is_open(args.host, port, args.timeout):
            print(f"{args.host}:{port} open")


if __name__ == "__main__":
    main()
