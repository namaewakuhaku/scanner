from strategy_stub import ScanStrategy

class RunContext():
    def __init__(self, strategy: ScanStrategy = None):
        self._strategy = strategy
        self._reports = list()

    @property
    def reports(self):
        return self._reports

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def run(self):
        self._strategy.scan()
        for report in self._strategy.report():
            self._reports.append(report)
    