import time

def runtime_Check(check_Def):
    def warpper_Def(*args, **kwargs):
        start_time = time.time()
        check_def_result = check_Def(*args, **Kwargs)
        end_time = time.time()
        print("Run Time [{}] : {} sec".format(check_Def.__name__, str(end_time - start_time)[:8]))
        return check_def_result
    return warpper_Def

    