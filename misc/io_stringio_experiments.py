'''
The tests use a StringIO buffer. This file explores StringIO a bit.

https://pymotw.com/3/io/

Derrick Warrick's explanation for how it is used in the tests:
"When we call print(), we're actually calling a modified version of
sys.stdout.write()
in order to print things to the console.
This test file is just overridding the normal sys.stdout object 
and replacing it with a StringIO object instead.
Whenever we type print(), instead of writing our answers to the console, 
python now writes the answers inside that StringIO() object. 
That way, the test can store the values that we're printing, 
and check them against the expected answers."
'''

import io
import sys

output = io.StringIO()
output.write("Testing out the StringIO buffer.")
print(" And testing it out with print.", file=output)

print(output.getvalue())

output.close()

try:
    print(output.getvalue())
except:
    print("Can't do an I/O operation on a closed file.")

another = io.StringIO('Initial value ')
print(another.getvalue())
print(another.read())
# Nothing shows up for the line below. I guess you can only read once?
print(another.read())

answer = input("What is your name? ")
another.write(answer)
print(another.getvalue())
print(another.read())

another.close()

# How the tests use it:

stdout_ = sys.stdout  # Keep previous value
sys.stdout = io.StringIO()
print("One more test.")
output = sys.stdout.getvalue()
# Here's where the tests would compare the output with what is expected.
# Test blah
# Test blah again.
print(" Second part.")
output2 = sys.stdout.getvalue()
print(output)  # <- Won't do anything
# Finally, the line below will allow normal printing to occur again.
sys.stdout = stdout_  # Restore stdout
print(output)
print(output2)
