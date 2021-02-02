class Logger:
    """ Simple class that can be turned off or on with its verbose property """
    verbose : bool = False

    @classmethod
    def info(cls, msg : str):
        if cls.verbose:
            print(msg)
            
    @classmethod    
    def error(cls, msg : str):
        cls.info(msg)