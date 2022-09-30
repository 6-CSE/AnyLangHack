numberOfTimesInputAsked=int(input(""))
i=1
while i<=numberOfTimesInputAsked:
  arr=[int(x) for x in input().split()]
  start=0
  end=len(arr)-1
  while start<=end:
    arr[start],arr[end]=arr[end],arr[start]
    start=start+1
    end=end-1
  for z in arr:
    print(z,end=" ")
  i=i+1
  print()
