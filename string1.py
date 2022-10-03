def donuts(count):
  if count>=10 :
    return "Number of donuts: many"
  else:
    res="Number of donuts: "+str(count)
    return res
def both_ends(s):
  f=""
  se=""
  if(len(s)<2):
    return ""
  else:
    for i in range(2):
        f+=s[i]
        se+=s[-(2-i)]
    res=f+se
    return res
def fix_start(s):
  n=len(s)
  f=s[0]
  news=s[1:]
  res=f+news.replace(f,"*")
  return res
def mix_up(a, b):
  n=len(a)
  res=b[0]+b[1]
  for i in range(2,n):
    res+=a[i]
  n=len(b)
  res+=" "+a[0]+a[1]
  for i in range(2,n):
    res+=b[i]
  return res
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
def main():
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')


  print('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), '')
  test(both_ends('xyz'), 'xyyz')

 
 
  print('fix_start')
  test(fix_start('babble'), 'ba**le')
  test(fix_start('aardvark'), 'a*rdv*rk')
  test(fix_start('google'), 'goo*le')
  test(fix_start('donut'), 'donut')

 
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox mid')
  test(mix_up('dog', 'dinner'), 'dig donner')
  test(mix_up('gnash', 'sport'), 'spash gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy perm')
if __name__ == '__main__':
  main()

