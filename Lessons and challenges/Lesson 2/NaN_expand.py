def nan_expand(num):
    if num == 0:
        return ""
    message = "Not a " * num
    message += "NaN"
    return message


print(nan_expand(1))

# In most programming languages, NaN stands for Not a Number. If we take a look at
# the following JavaScript code:
# typeof NaN === 'number' // true
#
# We will see that in JavaScript, NaN stands for Not a NaN, which is recursive by nature.
# Implement a Python function, called nan_expand(times), which returns the expansion
# of NaN (In JavaScript terms :P) that many times.
# For example:
# • If we expand NaN once (times=1), we will have "Not a NaN"
# • If we expand NaN twice (times=2), we will have "Not a Not a NaN"
# • If times=3, we have "Not a Not a Not a NaN"
# • And so on ...
