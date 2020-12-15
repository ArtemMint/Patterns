class AbstractTV(object):
    """Abstract TV"""
    def tune_channel(self, channel):
        raise NotImplementedError()


class SonyTV(AbstractTV):
    """TV So"""
    def tune_channel(self, channel):
        print(f'Sony TV: chosen {channel} channel')


class AbstractRemoteControl(object):
    """Abstract remote control"""
    def __init__(self):
        self._tv = self.get_tv()

    def get_tv(self):
        raise NotImplementedError()

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(AbstractTV):
    """Remote control"""
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0

    def get_tv(self):
        return SonyTV()

    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)

def main():
    remote_control = RemoteControl()
    remote_control.tune_channel(3)
    remote_control.next_channel()

    if __name__ == '__main__':
        main()