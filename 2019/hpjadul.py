def value(string,pos):
	p = string[pos]
	while True:
		if pos+1 < len(string):
			if (string[pos] == string[pos+1]):
				p = p + string[pos+1]
				pos = pos+1
			else: break
		else:
			break
	return p,pos
	
def decoding(elements):
	val,alpha = '', ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
	for i in elements:
		if i == '0':
			val = val+' '
		elif i == ' ':
			pass
		else:
			x = i[0]
			y = alpha[int(x)-2]
			if x in ['7','9']:
				a = 4
			else:
				a = 3						
			z = len(i)%a
			if z == 1:
				val = val+y[0]
			elif z == 2:
				val = val + y[1]
			elif z == 0:
				val = val + y[-1:]
			elif z == 3:
				val = val + y[2]
	return val
	

def main():
	x = raw_input('enter code:  ')
	lisval,c = [],0
	while True:
		no,c = value(x,c)
		lisval.append(no)
		c = c+1
		if c >= len(x):
			break
	string = decoding(lisval)
	print string	
	
if __name__ == '__main__':
	main()
