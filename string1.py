def donuts(count):
  # Check the count is grater than 10
  if count >= 10 :
    return "Number of donuts: many"
  else:
    res = "Number of donuts: " + str(count)
    return res


def both_ends(s):
  fst = ""
  sec = ""
  # Check the length of string, if it is less than 2 return None 
  if(len(s) < 2):
    return ""
  else:
  # Here first two character will store to fst and the last two will be stored to sec variables
    for i in range(2):
        fst += s[i]
        sec += s[-(2-i)]
  # Concat fst and sec and return it
    res = fst+sec
    return res


def fix_start(s):
  n = len(s)          # Store the length of s
  f = s[0]            # Store the first charcter of the string s to f
  new_s = s[1:]       # Store the string expect the first character to new_s
  res = f + new_s.replace(f, "*")       # Replase first character (f) of the string new_s to '*' and concat f and new_s  
  return res


def mix_up(a, b):
  n = len(a)                # n will have length of string a
  res = b[0] + b[1]         # Assign first 2 charecter of string b to res
  for i in range(2, n):     # Add string a to res exept the first two character 
    res += a[i]
  n = len(b)                # n will have length of string b
  res += " " + a[0] + a[1]  # Assign first 2 charecter of string a to res
  for i in range(2, n):     # Add string b to res exept the first two character 
    res += b[i]
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

