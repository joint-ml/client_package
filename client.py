from abc import ABCMeta, abstractmethod


class Client(metaclass=ABCMeta):

    @abstractmethod
    def get_weights(self):
        pass

    @abstractmethod
    def set_weights(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def test(self):
        pass