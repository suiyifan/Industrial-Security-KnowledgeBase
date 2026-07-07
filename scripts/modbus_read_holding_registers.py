#!/usr/bin/env python3
"""Build a Modbus TCP Read Holding Registers request.

This script prints the raw request bytes. Use it for protocol learning first;
only send traffic to systems you own or have explicit permission to test.
"""

from __future__ import annotations

import argparse
import socket
import struct


def build_request(transaction_id: int, unit_id: int, address: int, quantity: int) -> bytes:
    protocol_id = 0
    function_code = 0x03
    pdu = struct.pack(">BHH", function_code, address, quantity)
    length = len(pdu) + 1
    mbap = struct.pack(">HHHB", transaction_id, protocol_id, length, unit_id)
    return mbap + pdu


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Modbus TCP read holding registers")
    parser.add_argument("--host", help="Target host. If omitted, only print request bytes.")
    parser.add_argument("--port", type=int, default=502)
    parser.add_argument("--unit-id", type=int, default=1)
    parser.add_argument("--address", type=int, default=0)
    parser.add_argument("--quantity", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=2.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    request = build_request(1, args.unit_id, args.address, args.quantity)
    print("request:", request.hex(" "))

    if not args.host:
        return

    with socket.create_connection((args.host, args.port), timeout=args.timeout) as sock:
        sock.sendall(request)
        response = sock.recv(260)
        print("response:", response.hex(" "))


if __name__ == "__main__":
    main()
