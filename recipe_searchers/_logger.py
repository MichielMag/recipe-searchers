class Logger:

    verbose : bool = False

    @classmethod
    def info(cls, msg : str):
        if cls.verbose:
            print(msg)
            
    @classmethod    
    def error(cls, msg : str):
        cls.info(msg)