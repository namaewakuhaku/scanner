from strategy_stub import ScanStrategy

class DemoScanner(ScanStrategy):
    def scan(self):
        print("demo scanner is running...")

    def report(self):
        return ["Demo Scanner is a mock-only scanner"]