"""Print I KNOW BALL ESP32 BLE count notifications (diagnostic only).

Install: python3 -m pip install -r requirements.txt
Run:     python3 ble_monitor.py
"""

import asyncio

from bleak import BleakClient, BleakScanner

DEVICE_NAME = "IKNOWBALL"
COUNT_CHARACTERISTIC = "13d12002-76d1-47aa-9e28-9b4d3c214a10"


async def main():
    print(f"Searching for {DEVICE_NAME}...")
    device = await BleakScanner.find_device_by_filter(
        lambda d, adv: d.name == DEVICE_NAME or adv.local_name == DEVICE_NAME,
        timeout=15.0,
    )
    if device is None:
        print("Sensor not found. Confirm ESP32 is powered and advertising.")
        return

    def on_count(_sender, data):
        # Firmware sends a four-byte unsigned little-endian count.
        if len(data) == 4:
            print(f"Made baskets: {int.from_bytes(data, 'little')}")
        else:
            print(f"Unexpected notification: {data.hex()}")

    print("Connecting...")
    async with BleakClient(device) as client:
        await client.start_notify(COUNT_CHARACTERISTIC, on_count)
        print("Connected. Listening for made-basket notifications. Ctrl+C to stop.")
        while client.is_connected:
            await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDisconnected.")
