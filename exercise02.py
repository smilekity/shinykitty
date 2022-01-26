

# history_data_list에 담긴 숫자들을 잘 가져와서 카운팅 해보세요.
# 이중 배열이므로 중첩된 for 문이 필요할 수 있고, list comprehension을 활용해봐도 됩니다.
# 카운팅 용 딕셔너리 또는 리스트를 선언하셔야 할 것입니다. 이름은 number_counter라고 하시기 바랍니다.

f=open('lotto999.csv','rt',encoding='utf-8')
    
textline=f.readlines()
num=[[int(text) for text in line.strip().split(',')[1:]] for line in textline[1:]]

# num=[]
# for line in textline[1:] :
#     line=line.strip()
#     content=line.split(',')
#     for text in content[1:] :
#         value=int(text)
        
#         num.append(value)
        
f.close()     
   
number_counter = {}  # 리스트 또는 딕셔너리로 대체하세요.

## list comprehension 결과가 [[]] 형태임.. list comprehension에 문제가 있었나..?
for number in num :
        for number_1 in number :
                number_counter[number_1]=number_counter.get(number_1,0)+1

a=sorted(number_counter.keys())

for i in a :
        print(i,":", number_counter[i])
        

# for ball_num, ball_count in number_counter.items() :
#         print(ball_num,':',ball_count)
        
# 출력하실 때에는 {공번호} : {횟수} 형태로 한줄씩 출력해 보시기 바랍니다.
# 예:
# 1 : 142
# 2 : 135
# ...
# 45 : 138

import numpy as np 
np_counter = np.array(number_counter)

min_k = 0   # 각각 구해보세요.
min_v = 0
max_k = 0
max_v = 0

print(f'가장 많이 나온 공: {max_k} 번공,  횟수: {max_v} 회')
print(f'가장 적게 나온 공: {min_k} 번공,  횟수: {min_v} 회')
