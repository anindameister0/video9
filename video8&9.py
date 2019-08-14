Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1.get(66)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    d1.get(66)
NameError: name 'd1' is not defined
>>> d1={99:a,88:b,77:c}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d1={99:a,88:b,77:c}
NameError: name 'a' is not defined
>>> d1={99:'a',88:'b',77:'c'}
>>> d1.get(66)
>>> x=d1.get(66)
>>> x=d1.get(66);
>>> d1.get(99)
'a'
>>> d1.get(88)
'b'
>>> 'x'=d1.get(66)
SyntaxError: can't assign to literal
>>> 'x'=d1.get(66);
SyntaxError: can't assign to literal
>>> for x in d1:
	print(x)

	
99
88
77
>>> d1[77]['cat']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d1[77]['cat']
TypeError: string indices must be integers
>>> d1[77]='cat'
>>> d1
{99: 'a', 88: 'b', 77: 'cat'}
>>> d1[66]='bull dog'
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> for x in d1:
	print(x,d1[99])

	
99 a
88 a
77 a
66 a
>>> for x in d1:
	print(x,d1.get(99))

	
99 a
88 a
77 a
66 a
>>> for x in d1:
	print(x,d1.get(x))

	
99 a
88 b
77 cat
66 bull dog
>>> for x in d1
SyntaxError: invalid syntax
>>> for x in d1:
	print(x,d1[x])

	
99 a
88 b
77 cat
66 bull dog
>>> d1[55]:'MF'
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> sorted(d1)
[66, 77, 88, 99]
>>> sorted(d1.values())
['a', 'b', 'bull dog', 'cat']
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> d1[55]:'MF'
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> d1[55]:'mf'
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> d1[55]='MF'
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog', 55: 'MF'}
>>> sorted(d1.values())
['MF', 'a', 'b', 'bull dog', 'cat']
>>> d1[44]="mf"
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog', 55: 'MF', 44: 'mf'}
>>> d1[33]="Mf"
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog', 55: 'MF', 44: 'mf', 33: 'Mf'}
>>> sorted(d1.values())
['MF', 'Mf', 'a', 'b', 'bull dog', 'cat', 'mf']
>>> d1[22]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d1[22]
KeyError: 22
>>> d1[22];
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d1[22];
KeyError: 22
>>> d1.popitem()
(33, 'Mf')
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog', 55: 'MF', 44: 'mf'}
>>> (mykey,myvalue)=d1.popitem()
>>> mykey
44
>>> myvalue
'mf'
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog', 55: 'MF'}
>>> (serialnumber:value)=d1.popitem()
SyntaxError: invalid syntax
>>> (serialnumber,value)=d1.popitem()
>>> serialnumber
55
>>> d1.copy
<built-in method copy of dict object at 0x03D88210>
>>> d1.copy()
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> d1
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> d2
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d2
NameError: name 'd2' is not defined
>>> d2=d1.copy()
>>> d2
{99: 'a', 88: 'b', 77: 'cat', 66: 'bull dog'}
>>> d2.popitem(66)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d2.popitem(66)
TypeError: popitem() takes no arguments (1 given)
>>> d2.popitem(66);
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d2.popitem(66);
TypeError: popitem() takes no arguments (1 given)
>>> d1.popitem()
(66, 'bull dog')
>>> d1
{99: 'a', 88: 'b', 77: 'cat'}
>>> d1.pop(77)
'cat'
>>> d1
{99: 'a', 88: 'b'}
>>> d1.keys()
dict_keys([99, 88])
>>> serialnumber=d1.keys()
>>> type(serialnumber)
<class 'dict_keys'>
>>> for a in serialnumber
SyntaxError: invalid syntax
>>> for a in serialnumber:
	print(a)

	
99
88
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')

			
>>> love()
Love comes after true infatuation
>>> love()
Love comes after true infatuation
>>> love();
Love comes after true infatuation
>>> infatuation()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    infatuation()
NameError: name 'infatuation' is not defined
>>> infatuation()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    infatuation()
NameError: name 'infatuation' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
infatuation()
SyntaxError: invalid syntax
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
	infatuation()

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
	infatuation()
	admiration()

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    love()
  File "<pyshell#97>", line 8, in love
    admiration()
NameError: name 'admiration' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
	infatuation()
		admiration()
		
SyntaxError: unexpected indent
>>> 
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
	infatuation();
		admiration();
		
SyntaxError: unexpected indent
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    love()
  File "<pyshell#103>", line 8, in love
    admiration();
NameError: name 'admiration' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
	infatuation();
		admiration();
		
SyntaxError: unexpected indent
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality')
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    love()
  File "<pyshell#107>", line 8, in love
    admiration();
NameError: name 'admiration' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality');
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    love()
  File "<pyshell#110>", line 8, in love
    admiration();
NameError: name 'admiration' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality');
	infatuation();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality');
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    love()
  File "<pyshell#117>", line 8, in love
    admiration();
NameError: name 'admiration' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality');
	infatuation();
		admiration();
		
SyntaxError: unexpected indent
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
		def admiration():
			print('Admiration could be based on beauty or personality');
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    love()
  File "<pyshell#121>", line 8, in love
    admiration();
NameError: name 'admiration' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Admiration could be based on beauty or personality
>>> 
def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty();
			print('Beauty is based on three things: natural, artificial, state of mind');
	infatuation();
	admiration();
	
SyntaxError: invalid syntax
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
	infatuation();
	admiration();
		beauty();
		
SyntaxError: unexpected indent
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
	infatuation();
	admiration();
	beauty();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Admiration could be based on beauty or personality
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    love()
  File "<pyshell#130>", line 11, in love
    beauty();
NameError: name 'beauty' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
	infatuation();
	admiration();
	beauty();

	
>>> admiration()
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    admiration()
NameError: name 'admiration' is not defined
>>> admiration():
	
SyntaxError: invalid syntax
>>> admiration()
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    admiration()
NameError: name 'admiration' is not defined
>>> infatuation()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    infatuation()
NameError: name 'infatuation' is not defined
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
		beauty();
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Admiration could be based on beauty or personality
Beauty is based on three things: natural, artificial, state of mind
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();

	
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('Created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('This is developed by tremendous human effort over extended period of time')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Admiration could be based on beauty or personality
Beauty is based on three things: natural, artificial, state of mind
Natural beauty is God gifted
Created within a short span of time by tremendous human efforts
This is developed by tremendous human effort over extended period of time
>>> def love():
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('artificial beauty is created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('state of mind is developed by tremendous human effort over extended period of time')
			def personality():
				print('a good personality is developed over an extended period of time by tremendous human effort')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
			personality();
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Admiration could be based on beauty or personality
Beauty is based on three things: natural, artificial, state of mind
Natural beauty is God gifted
artificial beauty is created within a short span of time by tremendous human efforts
state of mind is developed by tremendous human effort over extended period of time
a good personality is developed over an extended period of time by tremendous human effort
>>> print(show.__doc__)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print(show.__doc__)
NameError: name 'show' is not defined
>>> print(love.__doc__)
None
>>> print(beauty.__doc__)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    print(beauty.__doc__)
NameError: name 'beauty' is not defined
>>> print(infatuation.__doc__)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    print(infatuation.__doc__)
NameError: name 'infatuation' is not defined
>>> print(sum.__doc__)
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types.
>>> def love():
	'''Trying to show nested fucntion'''
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('artificial beauty is created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('state of mind is developed by tremendous human effort over extended period of time')
			def personality():
				print('a good personality is developed over an extended period of time by tremendous human effort')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
			personality();
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();

	
>>> print(love.__doc__)
Trying to show nested fucntion
>>> def love():
	'''Trying to show nested fucntion'''
	# Don't try to supercede your Mommy'
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('artificial beauty is created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('state of mind is developed by tremendous human effort over extended period of time')
			def personality():
				print('a good personality is developed over an extended period of time by tremendous human effort')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
			personality();
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();

	
>>> print(love.__doc__)
Trying to show nested fucntion
>>> def love():
	'''Trying to show nested fucntion'''
	# Don't try to supercede your Mommy'
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			'''Dont try to supercede your Mommy'''
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('artificial beauty is created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('state of mind is developed by tremendous human effort over extended period of time')
			def personality():
				print('a good personality is developed over an extended period of time by tremendous human effort')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
			personality();
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();

	
>>> print(beauty.__doc__)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    print(beauty.__doc__)
NameError: name 'beauty' is not defined
>>> def love():
	'''Trying to show nested fucntion'''
	# Don't try to supercede your Mommy'
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			'''Dont try to supercede your Mommy'''
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('artificial beauty is created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('state of mind is developed by tremendous human effort over extended period of time')
			def personality():
				print('a good personality is developed over an extended period of time by tremendous human effort')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
			personality();
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();
	print(beauty.__doc__)

	
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Admiration could be based on beauty or personality
Beauty is based on three things: natural, artificial, state of mind
Natural beauty is God gifted
artificial beauty is created within a short span of time by tremendous human efforts
state of mind is developed by tremendous human effort over extended period of time
a good personality is developed over an extended period of time by tremendous human effort
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    love()
  File "<pyshell#164>", line 27, in love
    print(beauty.__doc__)
NameError: name 'beauty' is not defined
>>> def love():
	'''Trying to show nested fucntion'''
	# Don't try to supercede your Mommy'
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			'''Dont try to supercede your Mommy'''
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('artificial beauty is created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('state of mind is developed by tremendous human effort over extended period of time')
			def personality():
				print('a good personality is developed over an extended period of time by tremendous human effort')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
			personality();
		print(beauty.__doc__)
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();

	
>>> 
>>> love()
Love comes after true infatuation
Infatuation happens after true admiration
Admiration could be based on beauty or personality
Dont try to supercede your Mommy
Beauty is based on three things: natural, artificial, state of mind
Natural beauty is God gifted
artificial beauty is created within a short span of time by tremendous human efforts
state of mind is developed by tremendous human effort over extended period of time
a good personality is developed over an extended period of time by tremendous human effort
>>> def love():
	'''Trying to show nested fucntion'''
	# Don't try to supercede your Mommy'
	print('Love comes after true infatuation');
	def infatuation():
		print('Infatuation happens after true admiration');
	def admiration():
		print('Admiration could be based on beauty or personality');
		def beauty():
			'''DONT TRY TO SUPERCEDE YOUR MOMMY'''
			print('Beauty is based on three things: natural, artificial, state of mind');
			def naturalbeauty():
				print('Natural beauty is God gifted')
			def artificialbeauty():
				print('artificial beauty is created within a short span of time by tremendous human efforts')
			def stateofmind():
				print('state of mind is developed by tremendous human effort over extended period of time')
			def personality():
				print('a good personality is developed over an extended period of time by tremendous human effort')
			naturalbeauty();
			artificialbeauty();
			stateofmind();
			personality();
		print(beauty.__doc__)
		beauty(); #function can be only called inside function and not outside
	infatuation();
	admiration();
