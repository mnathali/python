# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

print("%.2d/%.2d/%.4d"% kata[-3::-1], end=' ')
print("%.2d:%.2d"% kata[-2:])