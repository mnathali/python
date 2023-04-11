from sys import exit
from os import get_terminal_size
from time import time, sleep

def ft_progress(lst):
	col = get_terminal_size().columns - 60
	print(col)
	stt = time()
	print(stt)
	end = lst.stop - lst.start
	print(end)
	new = range(0, end, lst.step)
	print(new)

	if col < 20:
		print(
			f"[Loading]",
			f"[Failure]",
			f"The terminal is too small.")
		exit()

	for idx in new:
		elp = time() - stt
		per = (abs(idx) + 1) / abs(end)

		eta = (((elp / (per * 100)) * 100) - elp)
		print(
			f"ETA: {eta:5.2f}s",
			f"[{(per * 100):3.0f}%]",
			f"[{('=' * round(per * (col))) + '>':{col}.{col}}]",
			f"{abs(idx) + 1}/{abs(end)} | elapsed time {elp:.2f}s",
			end='\r')
		yield idx


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)