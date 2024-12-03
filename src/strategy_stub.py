from abc import abstractmethod, ABC

# ABC here just means Abstract-Base-Class
# A python convention for classes without implementaiton

class ScanStrategy(ABC):
    """
    Interface Class that declares an operation common to all supported
    versions of Scanner Algorithms.

    The RunnerContext uses this interface to call the algorithm defined by the Strategies
    """
    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def report(self):
        pass

