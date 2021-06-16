global_var = 1

def my_f():
    local_var = 100
    print(local_var)
    print(global_var)

my_f()
print(global_var)