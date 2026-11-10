#What the error message said:
# Traceback (most recent call last):
#   File "C:\Users\18328\Documents\code the dre\python-intro-homework\week-2\assignment-2\warmup4.py", line 4, in <module>
#     print(f"{message} {cause} {fixes}")
#                                ^^^^^
# NameError: name 'fixes' is not defined
#What caused it:
#variable name is actually spelled 'fix' not 'fixes'
#How I fixed it:
#I changed the variable from fixes to fix

message = "What the error message said"
cause = "What caused it"
fix = "How you fixed it"
print(f"{message} {cause} {fix}")