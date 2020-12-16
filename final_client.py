#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
import time

FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# specify slave to query - UNIT parameter

UNIT = 0x1


def run_sync_client():
    client = ModbusClient('localhost', port=5020)
    client.connect()

    for i in range(5):
        log.debug("Reading Coils")
        client.read_coils(1, 1 + i, unit=UNIT)
        # first param - address: The starting address to read from
        # second param - count: The number of coils to read
        time.sleep(0.1)
        # 100ms przerwy między Reading Coils
        log.debug("Reading Coils")
        client.read_coils(2, 3 + i, unit=UNIT)
        time.sleep(0.1)

        log.debug("Write to a Coil")
        client.write_coils(1, 4, unit=UNIT)
        time.sleep(5)
        # 5s przerwy między write coils
        log.debug("Write to a Coil")
        client.write_coil(4, 3, unit=UNIT)
        time.sleep(5)

    # log.debug("Read discrete inputs")
    # client.read_discrete_inputs(0, 8, unit=UNIT)
    # # first param - The starting address to read from
    # # second param - The number of discretes to read
    #
    # log.debug("Write to a holding register and read back")
    # client.write_register(1, 10, unit=UNIT)
    # # first param - The starting address to write to
    # # second param - The value to write to the specified address
    #
    # log.debug("Read back")
    # client.read_holding_registers(1, 1, unit=UNIT)
    # # first param - The starting address to read from
    # # second param - The number of registers to read

    client.close()


if __name__ == "__main__":
    run_sync_client()
