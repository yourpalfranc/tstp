##Come up with a regular expression tht matches all the digits in Arizona 209, 501, 870. California
##209, 213, 650.

import re

line = "Arizona 209, 501, 870. California 209, 213, 650."

m = re.findall("\d", line)

print(m)