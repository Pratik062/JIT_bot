import sys

TOTAL_ROUNDS = 200

round_no = int(sys.argv[1])
prev_res = sys.argv[2] if len(sys.argv) > 2 else "NONE"

if round_no == 1:
    my_res = "YES"
else:
    my_res = prev_res if prev_res != "NONE" else "YES"
print(my_res)
