from multiprocessing.reduction import duplicate


numbers = [5, 5,5,6,3,3,2,1,7,4]
uniques= []
for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)
# print(numbers)
# append,insert,remove, clear,pop(removing last item in a list), index,count,sort(arranging items(print(numbers))), reverse, copy