# Python3 实现推理游戏Bagels
## 一、实验介绍
Bagels 是可以和朋友一起玩的一个推理游戏。你的朋友想到一个随机的、没有重复的3位数字，你尝试去猜测它是什么。每次猜测之后，朋友就会给出3种类型的线索：

Bagels：你猜测的3个数都不在神秘数字中；
Pico：你猜测的是神秘数字中的一个数，但是位置不对；
Fermi：你猜测的是正确位置上的一个正确的数。
本课程将会使用 Python 来实现这个游戏，计算机会提示多条线索，这些线索按照字母顺序排序。如果神秘数字是 456，而玩家的猜测是 546，那么线索就是“fermi pico pico”。6 提供的线索是“fermi”，5 和 4 提供的线索是“pico pico”。

在本实验中，我们将介绍 Python 的一些新的方法和函数。我们将介绍复合赋值操作符和字符串插值。如果之前你不能够做什么事情的话，这些方法和函数也并不能带来什么改变，但是，它们是让编程变得更为简单的快捷方法。

### 1.1 实验内容
在本次实验中，我们将介绍 Python 的一些新的方法和函数。我们将介绍复合赋值操作符和字符串插值。如果之前你不能够做什么事情的话，这些方法和函数也并不能带来什么改变，但是，它们是让编程变得更为简单的快捷方法。

### 1.2 课程来源
本课程源自异步社区的《Python游戏编程快速上手（第4版）》 书籍第 11 章，感谢 异步社区 授权实验楼发布。如需系统的学习本书，请购买《Python游戏编程快速上手（第4版）》。

为了保证可以在实验楼环境中完成本次实验，我们在原书内容基础上补充了一系列的实验指导，比如实验截图，代码注释，帮助您更好得实战。

如果您对于实验有疑惑或者建议可以随时在讨论区中提问，与同学们一起探讨。

### 1.3 实验知识点
random.shuffle() 函数；
复合赋值操作符 +=、-=、*=、/=；
列表方法 sort() 和 join()；
字符串插值；
转换说明符 %；
嵌套循环。
## 二、实验原理
游戏的流程如图所示，下面的流程图描述了在这个游戏中发生了什么以及发生的先后顺序。

![流程图](./wm.jpg)

## 三、实验步骤
### 3.1 导入 random 并定义 getSecretNum()
在程序开始处，导入了 random 模块并设置了一些全局变量。然后定义了一个名为 getSecretNum() 的函数。
```python
import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
  # 返回一个由 NUM_DIGITS 个不重复随机数组成的字符串.
```
我们使用常量 NUM_DIGITS 来表示答案中的数字位数，而不是直接使用整数 3。对于玩家所能够更猜测的次数，也是这样的，我们使用常量变量 MAX_GUESS，而不是整数 10。现在，要修改猜测的次数或神秘数字的位数，将会很容易。只要修改第 3 行或第 4 行的值，而程序的剩下部分不必修改，仍然能够工作。

getSecretNum() 函数生成了只包含独特位数的一个神秘数字。如果神秘数字中没有像 '244' 或 '333' 这样重复的数，Bagels 游戏会更有意思。我们将在 getSecretNum() 函数中使用一些新的 Python 函数来确保这一点。

### 3.2 打乱一组唯一数的顺序
getSecretNum() 函数的头两行将一组不重复的数字打乱了顺序：
```python
  numbers = list(range(10))
  random.shuffle(numbers)
```
list(range(10)) 计算为 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，因此变量 numbers 包含了 0 到 9 这个区间内全部数字。

#### 3.2.1 用 random.shuffle() 函数改变列表项的顺序
random.shuffle() 函数随机修改列表元素的顺序。这个函数没有返回值，而是把传递给它的列表“就地”修改。这有点类似于《Python游戏编程快速上手（第4版）》第11章 Tic Tac Toe 游戏中的 makeMove() 函数，makeMove() 函数把传递给它的列表就地修改，而不是返回修改过的一个新列表。这就是为什么我们没有编写诸如 numbers = random.shuffle(numbers) 这样的代码。

通过在交互式 shell 中输入如下的代码，来尝试体验 random.shuffle() 函数：
```python
>>> import random
>>> spam = list(range(10))
>>> print(spam)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> random.shuffle(spam)
>>> print(spam)
[3, 0, 5, 9, 6, 8, 2, 4, 1, 7]
>>> random.shuffle(spam)
>>> print(spam)
[9, 8, 3, 5, 4, 7, 1, 2, 0, 6]
```
每次在 spam 上调用 random.shuffle() 的时候，spam 列表中的项都会打乱顺序。接下来，你将会看到我们如何使用shuffle()函数来生成一个神秘数字。

#### 3.2.2 从打乱次序的数中获取神秘数字
这个神秘数字将是打乱次序的整数列表的前 NUM_DIGITS 个数字组成的一个字符串。
```python
  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
  return secretNum
```
secretNum 变量一开始是一个空白字符串。紧接着的 for 循环迭代了 NUM_DIGITS 次。在循环的每次迭代中，都会从打乱顺序的列表中获取索引为i的整数，将其转换成一个字符串，并连接到变量 secretNum 的末尾。

例如，如果 numbers 引用列表 [9, 8, 3, 5, 4, 7, 1, 2, 0, 6] ，那么在第 1 次迭代中，将会把 numbers[0]（也就是9）传递给 str() 函数，该函数返回 '9'，会将其连接到变量 secretNum 的末尾。在第 2 次迭代中，对 numbers[1]（也就是 8）做了同样的处理；在第 3 次迭代中，对 numbers[2]（也就是 3）做了同样的处理。最终返回的 secretNum 值是 '983'。

注意，这个函数中的 secretNum 包含了一个字符串，而不是一个整数。这看上去可能有点奇怪，但是记住，我们不能把整数连接到一起。表达式 9 + 8 + 3的结果是 20，而我们想要的是 '9' + '8' + '3'，其结果是 '983'。

### 3.3 复合赋值操作符
第12行的+=操作符是一个复合赋值操作符（augmented assignment operator）。通常，如果想要把一个值增加或者连接到一个变量中，应该使用如下的代码：
```python
>>> spam = 42
>>> spam = spam + 10
>>> spam
52
>>> eggs = 'Hello '
>>> eggs = eggs + 'world!'
>>> eggs
'Hello world!'
```
复合赋值操作符是一种快捷方式，它使得我们不必再重复地输入了变量名称。下面代码做了和上面代码相同的事情：
```python
>>> spam = 42
>>> spam += 10        # 和 spam = spam + 10 等同
>>> spam
52
>>> eggs = 'Hello '
>>>eggs += 'world!'  # 和 eggs = eggs + 'world!' 等同
>>> eggs
'Hello world!'
```
还有一些其他的复合赋值操作符。尝试在交互式shell中输入如下代码：
```python
>>> spam = 42
>>> spam -= 2
>>> spam
40
```
spam −= 2这条语句和 spam = spam – 2是相同的，因此，这个表达式计算为 spam = 42 – 2，然后得到 spam = 40。 乘法和除法也有复合赋值操作符。
```python
>>> spam *= 3
>>> spam
120
>>> spam /= 10
>>> spam
12.0
```
语句 spam = 3和spam = spam 3是相同的。因此，由于spam在前面设置为等于40，整个表达式将会是spam = 40 * 3，这会计算为120。表达式spam /= 10和spam = spam / 10是相同的，并且spam = 120 / 10计算为12.0。注意，spam在进行了除法运算之后，变成了一个浮点数。

### 3.4 计算要给出的线索
getClues()函数将根据参数 guess 和 secretNum，返回线索 fermi、pico 和 bagels 组成的一个字符串。
```python
def getClues(guess, secretNum):
    # 返回一个由 Pico, Fermi 和 Bagels 组成的，用来提示用户的字符串。
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)
```
最显而易见和最简单的步骤是判断猜测是否与神秘数字相等，对应的程序是 guess == secretNum。当玩家的猜测和神秘数字相等的时候，返回 'You got it!'。

如果猜测和神秘数字不相等，代码必须知道要给玩家什么线索。Clue 中的列表最初为空，根据需要来加入 'Fermi' 和 'Pico' 字符串。

程序通过循环遍历 guess 和 secretNum 中每一个可能的索引来做到这一点。因为两个变量中的字符串具有相同的长度，所以既可以使用 len(guess)，也可以使用 len(secretNum)，其效果是一样的。由于 i 的值从 0 变为 1，再变为 2，依次类推，所以紧接着的 geuss[i] == secretNum[i] 会判断guess的第1个字母、第2个字母、第3个字母以及之后的字母是否与secretNum中的相同索引中的数字相等。如果相等，clues.append('Pico') 将把字符串 'Fermi' 加入到 clues 中。

如果不相等，guess[i] in secretNum 将判断 guess 中第 i 个位置的数是否存在于secretNum中。如果存在，我们知道这个数在神秘单词中，但是位置不正确。clues.append('Pico')会把'Pico'添加到clues` 中。

如果循环之后 clue 列表是空的，那么我们就知道 guess中根本没有正确的数。
```python
  if len(clues) == 0:
    return 'Bagels'
```
在这种情况下，返回字符串 'Bagels' 作为唯一的线索。

### 3.5 列表方法 sort()
列表有一个叫做 sort() 的方法，它按照字母顺序或数字顺序重新排列列表中的元素。sort()方法没有返回一个排序的列表，而是对这个列表进行了所谓的“就地”排序。这就和 reverse()方法的工作方式一样。

我们不想要使用这样的一行代码：return spam.sort()，因为那将会返回一个None值（而这正是sort()所返回的值）。相反，我们想要的是单独的一行spam.sort()，然后是代码行return spam。

在交互式shell中，输入如下的内容：
```python
>>> spam = ['cat', 'dog', 'bat', 'anteater']
>>> spam.sort()
>>> spam
['anteater', 'bat', 'cat', 'dog']
>>> spam = [9, 8, 3, 5.5, 5, 7, 1, 2.1, 0, 6]
>>> spam.sort()
>>> spam
[0, 1, 2.1, 3, 5, 5.5, 6, 7, 8, 9]
```
当排序一个字符串列表的时候，字符串按照字母顺序返回，但是，当排序一个数字列表的时候，数字按照数值顺序返回。

在根据玩家的猜测得到的提示（glues）上使用 sort()：
```python
    clues.sort()
```
我们想要对 clue 列表进行排序的原因是，去除掉线索中和顺序相关的额外信息。如果 clue是['Pico', 'Fermi', 'Pico']，那么这将会告诉玩家猜测的中间数是在正确的位置上。由于另外两个线索都是 Pico，玩家就会知道必须要把神秘数字中的第 1 个数和第 3 个数进行交换。

如果线索总是按照字母先后顺序来排序，那么玩家就无法确认 Fermi 线索指的是哪个数。这使得游戏变得比较难，并且玩起来更有趣。

### 3.6 字符串方法 join()
字符串方法 join()将字符串的列表连接起来，作为一个单个的字符串返回。
```python
    return '  '.join(clues)
```
调用该方法的字符串（' '，这是一个空格字符串' '）会出现在列表中每个字符串之间（即作为分隔符）。例如，在交互式 shell 中输入如下代码：
```python
>>> ' '.join(['My', 'name', 'is', 'Zophie'])
'My name is Zophie'
>>> ', '.join(['Life', 'the Universe', 'and Everything'])
'Life, the Universe, and Everything'
```
所以，返回的字符串，是把 clue 中的各个字符串组合到一起，每个字符串之间会有一个空格。join()就像是与 split()相反的字符串方法。split()方法通过分割字符串而返回一个列表，而 join()方法返回组合列表而得到的一个字符串。

### 3.7 检查字符串中是否只包含数字
isOnlyDigits()函数帮助判断玩家输入的是否是一个有效的猜测。
```python
def isOnlyDigits(num):
    # Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True
```
在每次迭代中，i的值将是一个单个的字符。在 for 语句块中，代码判断 i是否不存在于 '0 1 2 3 4 5 6 7 8 9'.split() 返回的列表中（split()的返回值是['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']，只是 split() 更易于输入一些）。如果 i 不存在于列表之中，我们就知道 num 中包含了非数字字符。在这种情况下，返回 False。

如果程序跳过 for 循环往下执行，我们就知道 num 中的每个字符都是一个数字。在这种情况下，返回 True。

### 3.8 游戏的开始
在定义了所有的函数之后，这里是程序真正开始的地方。
```python
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
print('The clues I give are...')
print('When I say:    That means:')
print('  Bagels       None of the digits is correct.')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
```
print()函数调用将告诉玩家游戏的规则，以及线索 Pico、Fermi 和 Bagels所表达的含义。最上面的 print()调用在末尾加入了% (NUM_DIGITS)，并且在字符串中加入了 %s。这种技术叫做字符串插值（string interpolation）。

### 3.9 字符串插值
字符串插值（也称为字符串格式化，string formatting）是编码的一种快捷方式。通常，如果想要在一个字符串中使用一个变量中所包含的另一个字符串值的话，必须使用连接操作符+：
```python
>>> name = 'Alice'
>>> event = 'party'
>>> location = 'the pool'
>>> day = 'Saturday'
>>> time = '6:00pm'
>>> print('Hello, ' + name + '. Will you go to the ' + event + ' at ' +
location + ' this ' + day + ' at ' + time + '?')
Hello, Alice. Will you go to the party at the pool this Saturday at 6:00pm?
```
正如你所看到的，很难把连接多个字符串的代码输入到一行中。相反，可以使用字符串插值，它允许放入像%s 这样的占位符。这样的占位符叫做转换说明符（conversion specifiers）。一旦放入了转换说明符，我们可以在字符串末尾放置所有的变量名称。每个%s 会被代码行末尾的一个变量所替换。例如，下面代码所做的事情和之前的代码相同：
```python
>>> name = 'Alice'
>>> event = 'party'
>>> location = 'the pool'
>>> day = 'Saturday'
>>> time = '6:00pm'
>>> print('Hello, %s. Will you go to the %s at %s this %s at %s?' % (name,
event, location, day, time))
Hello, Alice. Will you go to the party at the pool this Saturday at 6:00pm?
```
注意，第1个变量名用于第1个 %s，第2个变量名用于第2个 %s，以此类推。我们的变量的数目必须和%s转换说明符的数目相同。

使用字符串插值而不是字符串连接的另一个好处是，插值对于任意的数据类型都有效，而不仅仅是对字符串有效。所有值都会自动转换为字符串数据类型。如果连接一个整数和一个字符串，会得到如下的错误：
```python
>>> spam = 42
>>> print('Spam == ' + spam)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```
字符串连接只能把两个字符串组合起来，而 spam 是一个整数。我们必须要记住要使用str(spam)，而不是 spam。但是字符串插值会为我们做这种字符串的转换。尝试在交互式 shell 中输入：
```python
>>> spam = 42
>>> print('Spam is %s' % (spam))
Spam is 42
```
字符串插值也叫做字符串格式化（string formatting）。

### 3.10 游戏循环
while True 开始一个无限 while 循环，条件是 True，所以它会一直循环直到执行一条 break 语句。
```python
while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' % (MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
```
在这个无限循环中，我们通过 getSecretNum() 函数得到一个神秘的数字。把这个神秘数字赋值给 secretNum。记住，secretNum 中的值是一个字符串，而不是整数。

这里的 print 使用字符串插值而不是字符串连接，以告诉玩家总共能够猜测了多少次。guessTaken = 1把变量 guessesTaken 设置为 1，表示这是第 1 次猜测。然后从 while guessTaken <= MAX_GUESS 开始是一个新的 while 循环，只要 guessesTaken 小于或等于 MAX_GUESS，这个循环就一直进行下去。

注意，从 while guessTaken <= MAX_GUESS 开始的 while 循环是在另外一个 while 循环之中，而这个循环是从 while True 开始的。这种循环之中的循环，叫做嵌套循环（nested loop）。任何的 break 或 continue 语句，例如 if geuss==secretNum 后面的 break 语句，只是暂停最内部的循环，或者跳到最内部的循环之外来继续，而不会对最外部循环产生任何影响。

#### 3.10.1 获取玩家的猜测
guess 变量会保存 input() 函数返回的玩家的猜测。这部分代码会一直循环并要求玩家做出猜测，直到玩家输入一个有效的猜测。
```python
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()
```
有效的猜测只包含数字，并且和神秘数字拥有相同的位数。使用 while 循环来检查猜测的有效性。

geuss = ''将 guess 设置为空字符串，所以 while 循环条件在第一次判断时为False，从而确保执行可以进入到从 while 开始的循环中。

#### 3.10.2 根据玩家的猜测给出线索
当执行跳过从第 while len(guess) != NUM_DIGITS or not isOnlyDigits(guess) 开始的 while 循环之后，guess 中包含了一个有效的猜测。把变量 guess 和 secretNum 传递给 getClues() 函数。
```python
        print(getClues(guess, secretNum))
        guessesTaken += 1
```
该函数返回包含线索的一个字符串，print() 函数把该字符串显示给玩家。guessTaken += 1 使用加法复合赋值操作符把 guessesTaken 加 1。

3.10.3 判断玩家的输赢
现在，我们来搞清楚玩家赢得了游戏还是输掉了游戏：
```python
       if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))
```
如果 guess 和 secretNum 的值相同，玩家就正确地猜到了神秘数字，跳出while循环。如果 guess 和 secretNum 的值不相同，就继续执行，它会判断玩家是否用完了猜测次数。

如果玩家还有更多的猜测，执行跳转回该 while 循环开始的地方，这里会让玩家再做一次猜测。如果玩家用完了猜测次数（或使用 break 语句跳出了循环），那么执行跳转将跳到 print('Do you want to play again? (yes or no)') 处。

#### 3.10.4 询问玩家是否再玩一局
来询问玩家是否想再玩一局。
```python
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
```

## 四、总结
就编程来讲，Bagels 是一个简单的游戏，但是想在游戏中获胜却很难。不过如果你一直玩，最终将发现有更好的方法来猜测和使用游戏所提供的线索。这就好像越坚持编程，也会越来越善于编程。

本章介绍了一些新的函数和方法 random.shuffle() 、sort() 和 join()，以及两个方便的快捷方式。当想要修改一个变量的时候，复合赋值操作符减少了输入工作量，例如 spam = spam + 1可以简写为 spam += 1。字符串插值通过在字符串中使用 %s（称为转换说明符）而不是使用多个字符串连接操作，从而让代码更容易阅读。

