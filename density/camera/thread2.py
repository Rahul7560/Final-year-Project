import emergency
import comparison

import multiprocessing
for bot in ('emergency','comparison'):
    p = multiprocessing.Process(target=lambda: __import__(bot))
    p.start()
