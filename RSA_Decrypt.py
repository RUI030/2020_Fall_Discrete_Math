def rsa_e(m,e,n):
  ans=0
  while e:
    if e%2:
      if ans==0:
        ans=m%n
      else:
        ans*=m
        ans%=n
    e//=2
    m=(m*m)%n
  return ans

def ascii_table(e,n):
  ans=[]
  ans.clear
  for i in range(32,127):
    m=chr(i)
    c=rsa_e(i,e,n)
    ans.append([m,c])
  return ans

def execute():
  str=input()
  str=str.split()
  n=int(str[0])
  e=int(str[1])
  c=str[2]
  c=c.split(',')
  table=ascii_table(e,n)
  for i in c:
    c_=int(i)
    for j in table:
      if c_==j[1]:
        print(j[0],end="")
        break

execute()
