a = input('请输入1到100之间的数字：')

num = int(a)

#if 1 <= num <= 100:
    #print('你好漂亮^-^')
#else:
    #print('你大爷好丑T_T')

if num in range(1,100):
    print('你好漂亮^-^')
else:
    print('你大爷好丑T_T')
