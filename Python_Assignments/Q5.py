
n=int(input("Enter the number of days: "))
prices=[]
for i in range(n):
    prices.append(int(input()))

greatest=prices[1]-prices[0]
buy=0

for i in range(n):
    for j in range(i+1,n):
        if greatest<(prices[j]-prices[i]):
            greatest=prices[j]-prices[i]
            buy=i

print(greatest)
print(buy)