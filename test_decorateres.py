def capital(function):
    def inner(name):
        val = "Mr "+name
        updated_val = function(val)
        return updated_val
    return inner
@capital
def show_name(name):
    print(name)
    return name

show_name('kapricon')