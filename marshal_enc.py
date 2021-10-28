import os
import marshal

def enc(name_in, name_out):
    file = open(name_in, 'r').read()
    # print(compile(file, "s", "exec"))
    en = marshal.dumps(compile(file, "osyicozy", "exec"))
    open(name_out, 'w').write("import marshal\nexec(marshal.loads("+repr(en)+"))")
    print("\033[36mDone\033[0m")
    
name_in = input("\033[36m[?] Input you'r file? : \033[0m")
name_out = input("\033[36m[?] what the output filename? : \033[0m")

enc(name_in, name_out)
