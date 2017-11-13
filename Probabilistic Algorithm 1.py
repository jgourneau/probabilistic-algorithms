import random as R

R.seed()

def alg(a, b, p):
	"""Returns True if the probability of a check on a and b is
	greater than a given parameter, p. False otherwise."""
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
	results = []
	trues = 0
	for _ in range(trials):
		l.append(alg(a, b, p))
	for b in l:
		if b:
			t += 1
	print("true: ", trues, "false: ", (len(l) - trues))
	return results

