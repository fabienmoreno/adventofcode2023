import time
import importlib

min_day=5
max_day=5
part_qty=2

for d in range(min_day, max_day+1):
    d_str=str(d)
    if len(d_str)==1: d_str="0"+d_str
    filename="data/input_"+d_str+".txt"
    
    module_name = "puzzles.p"+d_str
    module = importlib.import_module(module_name)

    for p in range(1,part_qty+1):
        start=time.perf_counter()
        func=getattr(module, "part"+str(p))
        result=func(filename)
        print("Result Day ",d_str," / Part ", str(p)," : ", result, " Duration : ", (time.perf_counter()-start)*1000, " ms")
