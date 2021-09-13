import pdb

def using_pdb():
    pdb.set_trace()

def using_eval():
    _input = 0
    while True:
        _input = input("")
        if _input == "q":
            break
        eval(_input)

if __name__ == "__main__":
    # using_pdb()

    using_eval()

