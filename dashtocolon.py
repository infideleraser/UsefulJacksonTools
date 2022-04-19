def dashtocolon(string):
	a=string.split('-')
	i=0
	ans=''
	while i<len(a):
		ans+=a[i]+':'
		i+=1
	return ans[:-1]


print(dashtocolon(input("mac addy")))