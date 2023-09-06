from abc import ABCMeta, abstractmethod


class Client(metaclass=ABCMeta):

    @abstractmethod
    def get_weights(self, *args, **kwargs):
        pass

    @abstractmethod
    def set_weights(self, *args, **kwargs):
        pass

    @abstractmethod
    def train(self, *args, **kwargs):
        pass

    @abstractmethod
    def test(self, *args, **kwargs):
        pass