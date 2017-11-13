import random as R

R.seed()

def alg(a, b, p=0.7):
	if check(a, b) > p:
		return True
	else:
		return False

def check(a, b):
	if a > b:
		a, b = b, a
	assert b != 0
	return R.randint(a, b)/b

def test_alg(a=1, b=20, p=.7, trials=100):
	l = []
	t = 0
	for _ in range(trials):
		l.append(alg(a, b, p))
	for b in l:
		if b:
			t += 1
	print("true: " + str(t), "false: " + str(len(l) - t))
	return l


