import sys
import time

var =  {"Ignition"      : ["Flage_key_ign"      , "write_key_ign"       , "Read_key_ign"],
        "Engin_State"   : ["Flage_key_eng"      , ""                    , "Read_key_ign"],
        "A_Faults"      : [""                   , ""                    , "Read_key_ign"],
        "Delay"         : None,
    }

class Script(object):
    """"
        Error Code -1 : dev None # Exception rasie Error 구현할까?
    """
    dev = None

    def __init__(self, name):
        print(name)
        pass

    def write(self, name):
        if dev == None:
            return -1
        return Script.dev

class BasicScript(Script):
    def __init__(self, ):
        self.tmp_scripts = {}
        
        super(BasicScript, self).__init__(None)

    def test_add(self, name):  
        self.tmp_scripts[name] = Script(name)

    @classmethod
    def set_dev(cls, test):
        cls.dev = test
        pass
        

if __name__ == "__main__":
    script = BasicScript()

    script.test_add("Ignition")
    
    
    print(script.tmp_scripts["ignition"].write())

    script.set_dev = "Test"

    print(script.tmp_scripts["ignition"].write())

