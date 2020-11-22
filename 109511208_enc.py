def rsa_e(m_,e_,n_):
  ans=0
  while e_:
    if e_%2:
      if ans==0:
        ans=m_%n_
      else:
        ans*=m_
        ans%=n_
    e_//=2
    m_=(m_*m_)%n_
  return ans

def execute():
  str=input()
  str=str.split()
  n=int(str[0])
  e=int(str[1])
  m=str[2]
  a=[]
  a.clear
  for i in m:
    a.append(ord(i))
  count=0
  for i in a:
    print(rsa_e(i,e,n),end='')
    count+=1
    if count!=len(a):
      print(',',end='')
  print()

execute()
