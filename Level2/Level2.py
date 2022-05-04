# 가장 큰 수 : 실패, 다양한 경우를 나누어서 해보아도 실패가 나와서 시간 초과를 감수하고 permutation 으로 했다. 당연히 시간초과는 나왔지만 푸는 방법은 맞는 것 같다. 문자열 비교는 첫 문자부터 차례로 비교한다는 것을 알 수 있었다.
from itertools import permutations

def solution(numbers):

    answer = list(permutations(numbers,len(numbers)))

    c = 0

    input =''

    

    for i in range(0,len(answer)):

        for j in range(0,len(answer[0])):

            input += str(answer[i][j])

        if c<int(input):

            c=int(input)

            input=' '

        else:    

            input =''

            

            

    return str(c)


# 소수 찾기: permutations를 이용해서 비교적 쉽게 풀었다. 시간 초과는 나오지 않았다. 하지만 소수 판별 시 for 문의 범위 오류가 있었다. 
from itertools import permutations 

def sosu(n):  

    if n<=1:

        return False

    for i in range(2,int(n/2)+1):

        if n%i == 0:

            return False

    return True    

def solution(numbers):

    answer = 0

    a = [ ]

    b = [ ]

    number = list(numbers)

    

    

    

    for i in range(1,len(numbers)+1):

        a += list(permutations(numbers,i))

    

    for i in range(0,len(a)):

        if int("".join(a[i])) not in b:

            b.append(int("".join(a[i])))

        

    for i in range(0,len(b)):

        if sosu(b[i])==True:

            answer+=1

    

    return answer
 

# 전화번호 목록 : 실패, 두 가지 테스트에서 계속 시간 오류가 나왔다. 다른 사람의 해설을 참고하니 for문을 두번 사용 한 것이 문제였다. 정렬을 하면 for문 하나로도 되는데 두번을 사용해서 시간 오류가 나왔다.
def solution(a):

    answer = True

    a.sort()

    

    for i in range(0,len(a)-1):

        if a[i]==a[i+1][0:len(list(a[i]))]:

            return False

        # for j in range(i+1,len(a)):

        #     if a[i][0]!=a[j][0] or len(list(a[i]))>len(list(a[j])):

        #         break

        #     elif a[i] == a[j][0:len(list(a[i]))]:

        #         return False

        #     else:

        #         continue

    

    

    

    return True
 

# 피보나치 수 : 생각보다 쉽게 풀렸다. 재귀적으로 풀지 않고 더하기를 해줬더니 시간 초과도 나지 않고 쉽게 풀렸다.
def fibo(n):

    a = [0] * (n+1)

    a[0] = 1

    a[1] = 1

    a[2] = 1  

    

    for i in range(3,n+1):

        a[i]=a[i-1]+a[i-2]

    

    return a[n]

def solution(n):   

    return fibo(n)%1234567


# 최솟값 만들기 : 풀이 과정이 기억이 나서 쉽게 풀 수 있었다.
def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    
    for i in range(0,len(A)):
        answer += A[i]*B[len(A)-i-1]

    return answer


# N개의 최소공배수 : find 함수를 만들어서 풀었다. import를 통해 gcd 모듈을 사용하는 방법도 있었다.
def find(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b ==0:
            return i

def solution(arr):
    answer = find(arr[0],arr[1])
    
    count = len(arr)
    
    for i in range(2,count):
        answer = find(answer,arr[i])
    
    
    return answer


# 최댓값과 최솟값 : 생각보다 시간이 걸렸다. 어떤 식으로 숫자들을 추출할지 고민을 오래 했다. 하지만 split 이 떠올랐고 map 도 이용해서 문제를 풀 수 있었다.
def solution(s):
    answer = []
    a = s.split()
    
    a = list(map(int,a))
    
    
    
    return str(min(a))+" "+str(max(a))


# 다음 큰 숫자 : 생각보다 쉽게 풀었다. 두 테스트가 시간 초과가 걸리는 줄 알았지만 다행히 통과했다.
def solution(n):
    answer = 0
    
    count = list(bin(n)).count('1')
    
    for i in range(n+1, 1000000):
        if count == list(bin(i)).count('1'):
            return i


# 숫자의 표현 : 저번에는 못 풀었었는데 풀려서 신기하다. 실력이 늘었나 보다.
def solution(n):
    answer = 0
    count = 0  
    
    
    for i in range(0,n+1):
        for j in range(i+1,n+1):
            count += j
            if count>n:
                count = 0
                break
            if count == n:
                answer+=1
                count = 0
                break
    
    return answer


# JadenCase 문자열 만들기 : 배열 말고 다른 방식으로 하려고 했는데 생각이 안나서 배열로 풀었다. 변수에 upper() 된 값을 넣어주고 그 값을 다시 대입해주는 방식으로 성공했다.
def solution(s):
    answer = list(s.lower())
    num = [0,1,2,3,4,5,6,7,8,9]      
    
    if answer[0] not in num:  
        k=answer[0].upper()
        answer[0]=k    
    
    for i in range(1,len(list(s))):
        if answer[i-1] == " " and answer[i] not in num:
            k = answer[i].upper()
            answer[i] = k
            
            
    
    
    return "".join(answer)


# 행렬의 곱셈 : 실패, 정말 더럽게 어찌어찌 풀었지만 모든 테스트 코드에서 시간 초과가 나왔다.
def sum(a,b):
    m = 0
    
    for i in range(0,len(a)):        
            m += a[i]*b[i]
    
    return m

def solution(arr1, arr2):
    answer = []
    a = []
    b = []
    temp = []
    
    
    
    for i in range(0,len(arr2)):
        for j in range(0,len(arr2[0])):
            temp.append(arr2[j][i])
    
    length = len(arr2[0])
    
    i=0
            
    while True:        
        a.append(temp[i:i+length])
        i+=length
        if len(a)>=len(arr2):
            break
            
    for i in range(len(arr1)):
        for j in range(len(a)):
            answer.append(sum(arr1[i],a[j]))
    
    j=0
    while True:        
        b.append(answer[j:j+length])
        j+=length
        if len(b)>=len(arr1):
            break         
            
        
    return b


# 짝지어 제거하기 : 실패, while 을 이용해 del 를 했지만 역시나 시간초과에 걸렸다. 새로운 리스트를 생성해서 stack 을 이용한 pop과 push 방법이 유용한 것 같다. 연습이 필요하다.
def solution(s):
    a = list(s)
    if len(a)%2 !=0:
        return 0
    while True:
        k = 0
        for i in range(0,len(a)-1):
            if a[i]==a[i+1]:
                del a[i]
                del a[i]
                k+=1
                break
        if k==0 and len(a)==0:
            return 1
        if k==0 and len(a)!=0:
            return 0


# 더 맵게 : 실패, 테스트 코드는 다 맞았지만 효율성은 다 틀렸다. heapq 를 사용하면 효율성이 더 좋아질 수 있다. 
def solution(a, K):
    answer = 0
    a.sort()
    
    while True:
        a.sort()
        if len(a)==1 and a[0]<K:
            return -1
        
        
        if a[0]>=K:
            return answer
        else:
            a.append(a[0]+a[1]*2)
            answer+=1
            a = a[2:]


# 구명보트 : 실패, 이 역시 모든 효율에서 걸렸다. 깨달은 점은 del 는 생각보다 느리다는 것이고 deque 나 que 가 훨씬 빠른 성능이기에 이를 이용하는 연습이 필요하다. 
def solution(a, limit):
    answer = 0
    
    a.sort(reverse=True)
    
    while True:
        if len(a)<=1:
            if len(a)==1:
                return answer+1
            return answer
        else:
            if a[0]+a[-1]<=limit:
                del a[-1]
                del a[0]
                answer+=1
            else:
                del a[0]
                answer+=1
            
    
    
    
    
    return answer


# 큰 수 만들기 : 실패, 이 역시 시간 초과가 나왔다. pop 을 이용해서 푸는 방법이 있다.
def solution(number, k):
    answer = ''
    a=(list(number))
    
    count = 0
    
    while True:
        if count==k:
            return "".join(a)
        for i in range(0,len(a)):
            if a[i]<a[i+1]:
                del a[i]
                count+=1
                break
        
    return deq


# 가장 큰 정사각형 찾기 : 실패, 방법은 아예 몰랐다. 블로그 글을 보니 이해는 되었다. (x,y) 의 값은 min((x-1,y),(x-1,y-1),(x,y-1))로 두면 만들 수 있는 가장 큰 정사각형의 길이를 구할 수 있다. 동적 방법이라고 한다.


# 카펫 : 오랜만에 성공을 했다. 처음에는 막혔지만 수학적으로 생각을 해보려고 하니 성공을 하게 되었다.
def solution(brown, yellow):
    answer = []
    
    for a in range(3,brown+yellow):
        if (brown+yellow)%a != 0:
            continue
        else:
            b = (brown+yellow)/a
            if (a-2)*(b-2)==yellow and a*b==brown+yellow:
                answer.append(b)
                answer.append(a)
                break
        
    
    
    
    
    return answer


# 프린터 : 시간 초과가 날 줄 알았지만 다행히 성공을 했다. enumerate 와 any, 그리고 2차원 리스트 생성에 대해 알게 되었다.
def solution(a, b):
    answer = 0
    
    # 순위가 앞에, 문서 번호가 뒤에 
    
    list = [[0]*2 for i in range (len(a))]
    
    for i in range(0,len(list)):
        list[i][0]=a[i]
        list[i][1]=i
    
    for i in range(len(list)):
        if list[i][1]==b:
            find = list[i]
            break
    
    while True:
        if find==list[0] and max(list)[0]==find[0]:
            answer+=1
            return answer
        else:
            if list[0][0] == max(list)[0]:
                del list[0]
                answer+=1
            else:
                list.append(list[0])
                del list[0]
                
    
    
    
    return answer




















