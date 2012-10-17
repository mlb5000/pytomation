"""
Interface Device:
"""
from .state import StateDevice
from pytomation.utility import CronTimer

class InterfaceDevice(StateDevice):
    STATES = ['on','off','unknown']
    DELEGATE_PREFIX = 'on_'
    TIME_PREFIX = 'time_'
    ANY_STATE = 'any'

    _state = None
    _delegates = {}
    _times = {}

    def __init__(self, interface=None, address=None):
        self.interface = interface
        self.address = address
        super(InterfaceDevice, self).__init__()

    def __setattr__(self, name, value):
        if name in self.STATES:
            self.interface.command.setattr(name, value)
        super(InterfaceDevice, self).__setattr__(name, value)

    def _set_state(self, state):
        getattr(self.interface, state)(self.address)
        return super(InterfaceDevice, self)._set_state(state)