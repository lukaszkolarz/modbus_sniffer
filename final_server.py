#!/usr/bin/env python3

from pymodbus.server.sync import StartTcpServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

import logging

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s  %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_server():
    # initialize data store
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [17] * 100),
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100))

    context = ModbusServerContext(slaves=store, single=True)
    identity = ModbusDeviceIdentification()
    StartTcpServer(context, identity=identity, address=("127.0.0.1", 5020))


if __name__ == "__main__":
    run_server()
