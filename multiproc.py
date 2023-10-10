import multiprocessing

class MultiProc:
    target = None
    
    process = None
    queue = multiprocessing.Queue()
    function_args = (queue,)
    def __init__(self, target: function = None, function_args : tuple = None) -> None:
        print(multiprocessing.cpu_count)
        self.target = target
        self.function_args += function_args
        