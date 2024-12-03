from runcontext import RunContext
from strategies.demostrat import DemoScanner
from strategies.sql_injection import SqlInjectionScanner
from strategies.csrf import CSRFScanner


# this is a registry of types of scan we want to support by the program
# currently we just have a sql injection, csrf and a demo scanner
scanStrategyRegistry = list()

# create demo scanner, nothing much just for testing implementaitons
scanStrategyRegistry.append(DemoScanner())


# create a sql injection scanner for each url given
# this will be taken as commandline args or config later
urls = ["http://demo.owasp-juice.shop/#/login"]
for url in urls:
    scanStrategyRegistry.append(SqlInjectionScanner(url))

# create a csrf scanner for each url given
# this will be taken as commandline args or config later
urls = ["http://demo.owasp-juice.shop/"]
for url in urls:
    scanStrategyRegistry.append(CSRFScanner(url))





# We set a context to collect all the reports from our scans
runnerContext = RunContext()
for strat in scanStrategyRegistry:
    runnerContext.strategy = strat
    try:
        runnerContext.run()
    except Exception as e:
        print("Encountered exception")
        print(e)

print()
print("====================REPORTS=====================")
for report in runnerContext.reports:
    print(f"⚠️\t{report}")
