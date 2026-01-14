def standard_function(*args, **kwargs):
    for arg in args:
        print(arg ** 2)
    for kwarg in kwargs:
        for key,value in kwargs.items():
            print(f"{key} = {value}")
        pass

standard_function(1,2,3,4,25,operation="sum")