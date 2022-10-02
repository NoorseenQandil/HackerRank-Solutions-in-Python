regex_pattern = r"[^0-9]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))
