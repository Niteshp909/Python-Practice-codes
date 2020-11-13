 
def findGCDSum(k,a,n): 
	GCDSum = 0; 
	tempGCD = 0; 
	for i in range(n): 
		
		
		for j in range(i, n): 
			
			
			tempGCD = 0; 
			for w in range(i, j + 1): 
				
				 
				tempGCD = __gcd(tempGCD, a[w]); 
				
			
			GCDSum += tempGCD; 

	return GCDSum; 

def __gcd(a, b): 
	return a if(b == 0 ) else __gcd(b, a % b);	 


if __name__ == '__main__': 
	n = 5; 
	
	a = []
	for l in range(n):
	    k = int(input())
	    a.append(k)
	totalSum = findGCDSum(k,a,n); 
	print(totalSum); 

