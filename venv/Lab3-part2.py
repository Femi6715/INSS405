score1=input('Enter Score for INS405')
score2=input('Enter Score for BUIS 360')
score3=input('Enter Score for DANL 470 ')

sum= int(score1) + int(score2) + int(score3)
print('sum=',sum)

average= int(sum) /3
print('Average=',average)

if(float(average)>90):
   print('A')
elif (float(average)>=70 and float(average)<=89):
   print('B')
elif (float(average)>=60 and float(average)<=69):
   print('C')
elif (float(average)<50):
   print('D')