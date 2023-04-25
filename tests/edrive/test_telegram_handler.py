"""Contains tests for MotionHandler class"""
from edcon.edrive.telegram_handler import TelegramHandler
from unittest.mock import Mock


class TestTelegramHandler:
    def test_update_inputs(self):
        telegram = Mock()
        edrive = Mock()
        dut = TelegramHandler(telegram, edrive)
        dut.update_inputs()

        edrive.recv_io.assert_called()

    def test_acknowledge_faults_return_true(self):
        telegram = Mock()
        edrive = Mock()
        dut = TelegramHandler(telegram, edrive)

        telegram.zsw1.fault_present = False
        res = dut.acknowledge_faults(0.1)

        assert res == True

    def test_acknowledge_faults_return_false(self):
        telegram = Mock()
        edrive = Mock()
        dut = TelegramHandler(telegram, edrive)

        telegram.zsw1.fault_present = True
        res = dut.acknowledge_faults(0.1)

        assert res == False
