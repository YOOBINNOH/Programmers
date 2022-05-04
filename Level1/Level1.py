
# 직사각형 별찍기 : 문자열 * 가 아닌 다른 방법으로 풀려다가 시간이 오래 걸렸다.
a, b = map(int, input().strip().split(' '))
for i in range(0,b):
    print("*"*a)


# x만큼 간격이 있는 n개의 숫자 : 다음에는 한줄 풀이 도전해야겠다.   
def solution(x, n):
    answer = []    
    for i in range(1,n+1):
        answer.append(x*i)    
    
    return answer


# 행렬의 덧셈 : zip 을 이용하면 더 간편하게 풀 수 있었다.
def solution(arr1, arr2):
        
    inside = len(arr1[0])
    outside = len(arr1)
    
    answer = [[0]*inside for _ in range(outside)]
    
    for i in range(0,outside):
        for j in range(0,inside):
            answer[i][j]=(arr1[i][j]+arr2[i][j])
    
    
    return answer 


# 핸드폰 번호 가리기 : 한 줄 풀이에 성공했다. [-4: ]으로 하면 더 깔끔했을 것이다.
def solution(phone_number):
    
    return "*"*(len(list(phone_number))-4) + phone_number[len(list(phone_number))-4:len(list(phone_number))]


# 하샤드 수 : list 꼴은 int 가 아닌 str 로 만드는 것이 중요하다.
def solution(x):
    
    total = 0
    
    for i in range(0,len(list(str(x)))):
        total += int(list(str(x))[i])


# 평균 구하기 : 쉬운 문제였다.
def solution(arr):
    return sum(arr)/len(arr)


# 콜라츠 추측 : num가 1 일때를 고려하지 않아 오류가 발생했었다.
def solution(num):
    answer = 1
    if num ==1:
        return 0
    
    while answer<=500:
        if num%2==0:
            num /= 2
        else:
            num = num*3+1
        
        if num==1:
            break
            
            
        answer+=1
    
    if answer>=500:
        return -1
    return answer


# 최대공약수와 최소공배수 : 최대공약수만 구한 후 공식을 이용해 최소공배수를 구했다.
def small(a,b):
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i ==0:
            return i


def solution(n, m):
    
    return [small(n,m),n*m/small(n,m)]


# 짝수와 홀수 : 쉬웠다.
def solution(num):
    if num%2==0:
        return "Even"
    return "Odd"


# 제일 작은 수 제거하기 : remove를 이용해서 최솟값을 제거했다. del 와의 차이점이 중요하다.
def solution(arr):
    arr.remove(min(arr))
    if len(arr)==0:
        return [-1]
    return arr


# 정수 제곱근 판별 : 새로운 방법으로 풀어보았다. ** 는 제곱을 의미하는 것을 알게 되었다.
import math

def solution(n):
    answer = 0
    
    if math.pow(n,0.5)==int(math.pow(n,0.5)):
        return math.pow(pow(n,0.5)+1,2)
    else:
        return -1


# 정수 내림차순으로 배치하기 : 실패, 세 예시에서 런타임 에러가 발생했다. 원인은 join 과 int()를 따로 쓴 것이다. 둘이 한 문장으로 붙여서 쓰면 에러가 발생하지 않았다.
def solution(n):
    a = list(str(int(n)))    
    a.sort(reverse=True)   
    
    return int("".join(a))


# 자연수 뒤집어 배열로 만들기 : map 을 사용하려고 했으나 잘 되지 않았다. reverse 는 객체를 반환하지 않지만 reversed 는 객체를 반환한다는 점을 알게 되었다.
def solution(n):
    a = list(str(n))    
    answer = []
    
    for i in range(len(a)-1,-1,-1):
        answer.append(int(a[i]))
    
    return answer


# 자릿수 더하기 : 쉬웠지만 다른 사람들의 풀이를 보니 map 등 다양한 한 줄 풀이가 많았다.
def solution(n):
    answer = 0
    a = list(str(n))
    for i in range(0,len(a)):
        answer += int(a[i])
    return answer


# 이상한 문자 만들기 : 예전에는 계속 실패했지만 lower() 과 upper()의 사용법을 알고 나서는 쉽게 풀렸다.
def solution(s):
    a = list(s)
    
    check = 0
    
    for i in range(0,len(a)):
        if a[i]==" ":
            check = 0
        else:
            if check%2 !=0:
                a[i]=a[i].lower()
                check += 1
            else:
                a[i]=a[i].upper()
                check += 1
    
    
    return "".join(a)


# 약수의 합 : 쉬웠지만 다른 사람들의 풀이를 보고 반 이상의 값은 계산을 할 필요가 없던 것을 알게 되었다.
def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    
    
    return answer


# 시저 암호 : ord, chr 까지는 구현을 했지만 뒤의 부분은 헷갈려서 대문자와 소문자 두 리스트를 직접 만들었다.
def solution(s, n):
    answer = ''
    l = list(s)
    a=[]
    b=[]
    
    for i in range(65,91):
        a.append(chr(i))
    
    for i in range(97,123):
        b.append(chr(i))
    
    for i in range(0,len(list(s))):
        if l[i] in a:
            f = a.index(l[i])
            l[i]=a[(f+n)%len(a)]
        elif l[i] in b:
            f = b.index(l[i])
            l[i]=b[(f+n)%len(a)]
        else:
            continue
    
    return "".join(l)


# 문자열을 정수로 바꾸기 : 어렵지 않은 문제였다.
def solution(s):
    
    return int("".join(s))


# 수박수박수박수박수박수? : n이 짝수인 경우와 홀수인 경우로 나누어서 풀었다.
def solution(n):
    a = "수박"
    if n%2 == 0:
        return a * int((n/2))
    else:
        return a * int((n/2)) + "수"


# 소수 찾기 : 시간 초과에 계속 걸렸다. import math 후 pow(n,0.5) 를 이용해서 가까스로 통과했다.
import math

def find(n):          
    for i in range(2,int(math.pow(n,0.5)+1)):
        if n%i==0:
            return False
    return True    


def solution(n):
    answer = 0    
    for i in range(2,n+1):
        if find(i)==True:
            answer+=1
            
    return answer


# 서울에서 김서방 찾기 : str의 + 는 str 과만 성립한다.
def solution(seoul):    
    return "김서방은 " +  str(seoul.index("Kim")) +"에 있다"


# 문자열 다루기 기본 : 쉬운 문제였다. isdigit() 함수의 활용이 중요했다.
def solution(s):
    
    return s.isdigit() and (len(list(s))==4 or len(list(s))==6)


# 문자열 내림차순으로 배치하기 : 쉬운 문제였다.
def solution(s):
    a = list(s)
    a.sort(reverse=True)
    return "".join(a)


# 문자열 내 p와 y의 개수 : 쉬웠지만 두 개수 모두 0인 경우 역시 두 개수가 같다는 경우에 포함되기에 따로 구할 필요가 없었다.
def solution(s):
    s = s.lower()
    
    if s.count("p")==s.count("y"):
        return True
    
    return False


# 두 정수 사이의 합 : sum과 range를 병합해서 사용하는 방법을 배웠다.
def solution(a, b):
    answer = 0
    a,b=min(a,b),max(a,b)
    for i in range(a,b+1):
        answer+=i
    return answer


# 나누어 떨어지는 숫자 배열 : 간단한 문제였다.
def solution(arr, divisor):
    answer = []
    
    for i in range(0,len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    
    answer.sort()
    
    if len(answer)==0:
        return [-1]
        
    
    return answer


# 같은 숫자는 싫어 : 쉬운 문제였다. 기존 리스트를 del 하는 것 보다 새 list 에 추가해주는 것이 효율적이었다.
def solution(arr):
    answer = []
    
    for i in range(0,len(arr)-1):
        if arr[i]!=arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer


# 문자열 내 마음대로 정렬하기 : 람다로 푸는 법이 있지만 잘 모르겠어서 나만의 방법대로 풀어보았다. 다행이도 통과가 되었다.
def solution(strings, n):
    
    temp = ""
    
    for i in range(0,len(strings)-1):
        for j in range(i+1,len(strings)):
            if strings[i][n]>strings[j][n]:
                temp = strings[i]
                strings[i] = strings[j]
                strings[j] = temp
            if strings[i][n]==strings[j][n]:
                if max(strings[i],strings[j])==strings[j]:
                    continue
                else:
                    temp = strings[i]
                    strings[i] = strings[j]
                    strings[j] = temp
                    
    
    
    
    return strings


# 가운데 글자 가져오기 : 한줄 코딩 하려고 했지만 부분 오타가 나서 두줄로 바꿨다.
def solution(s):
    k=len(list(s))
    return s[int(k/2)] if k%2!=0 else s[int(k/2)-1:int(k/2)+1]


# 약수의 개수와 덧셈 : 약수의 개수가 홀수인 수는 제곱수인 것을 이용했다.
import math

def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        if math.pow(i,0.5)==int(math.pow(i,0.5)):
            answer -= i
        else:
            answer += i
    
    
    return answer


# 두 개 뽑아서 더하기 : set 함수를 이용하지 않고 not in 을 이용했다. 
def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    
    
    
    return sorted(answer)


# 완주하지 못한 선수 : 두 리스트를 정렬한 후 다른 원소를 return 했다. counter를 이용한 방법도 보였다.
def solution(a, b):
    a.sort()
    b.sort()
    answer = ""
    
    for i in range(0,len(b)):
        if a[i]!=b[i]:
            answer=a[i]
            break
    
    if answer=="":
        answer = a[-1]
    
    return answer


# 나머지가 1이 되는 수 찾기: 쉬운 문제였다.
def solution(n):
    
    
    for i in range(1,n):
        if n%i == 1:
            return i


# 부족한 금액 계산하기 : for 문을 이용해서 간단하게 풀 수 있었다.
def solution(price, money, count):
    total = 0
    
    for i in range(0,count):
        total += (price*(i+1))

    return total-money if total-money>=0 else 0


# 없는 숫자 더하기 : 쉬웠다.
def solution(numbers):
    
    return 45-sum(numbers)


# 내적 : 쉬운 문제였다.
def solution(a, b):
    answer = 0
    
    for i in range(0,len(a)):
        answer += a[i]*b[i]
    return answer


# 음양 더하기 : True, False 는 첫글자가 대문자임에 주의해야 한다.
def solution(a, b):
    answer = 0
    
    for i in range(0,len(a)):
        if b[i]==True:
            answer += a[i]
        else:
            answer -= a[i]
    
    return answer


# K번째수 : 배열의 원소값 숫자가 헷갈려서 조금 시간이 걸렸었다. map 을 이용하는 방법도 있었다.
def solution(a, b):
    answer = []
    li = []
    
    for i in range(0,len(b)):
        li = a[b[i][0]-1:b[i][1]]
        li.sort()
        answer.append(li[b[i][2]-1])
        
    
    
    return answer


# 최소직사각형 : 풀이를 외우고 있어서 금방 풀었다.
def solution(sizes):
    answer = 0
    a = [ ]
    b = [ ]
    
    for i in range(0,len(sizes)):
        a.append(max(sizes[i]))
        b.append(min(sizes[i]))
    return max(a)*max(b)


# 예산 : 어렵지 않게 문제를 풀었다. pop 을 사용한 풀이도 보였다.
def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for i in range(0,len(d)):
        budget -= d[i]
        if budget<0:
            return answer
        answer+=1
    
    
    
    return answer


# 3진법 뒤집기 : 잘 풀었지만 int(a,n) 꼴을 이용한 풀이가 보였다.
import math

def three(n):
    answer = []
    while n>=1:
        answer.append(n%3)
        n = (n-n%3)/3
    
    return answer

def solution(n):
    answer = 0
    a = three(n)
    
    for i in range(0,len(three(n))):
        answer += a[i]*math.pow(3,len(a)-i-1)
    
    
    return answer


# 소수 만들기 : 조합은 시간 초과가 나올것 같아 사용하지 않고 풀었다.
def sosu(n):
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
    return True    

def solution(n):
    a = []
    answer=0
    
    for i in range(0,len(n)-2):
        for j in range(i+1,len(n)-1):
            for k in range(j+1,len(n)):                
                a.append(n[i]+n[j]+n[k])
    
    for i in range(0,len(a)):
        if sosu(a[i])==True:
            answer+=1
    
    return answer


# 모의고사 : 나머지 수를 이용해서 비교적 쉽게 답을 구했다.
def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a=0
    b=0
    c=0
    
    for i in range(0,len(answers)):
        if answers[i]==one[i%5]:
            a+=1
        if answers[i]==two[i%8]:
            b+=1
        if answers[i]==three[i%10]:
            c+=1    
    
    if max(a,b,c)==a:
        answer.append(1)
    if max(a,b,c)==b:
        answer.append(2)
    if max(a,b,c)==c:
        answer.append(3)    
        
        
    
    return answer


# 체육복 : 실패, 분실과 여유분 중복인 학생을 미리 제거하지 않았더니 약간의 오류가 생겼다.
def solution(n, lost, reserve):
    answer = 0          
    lost.sort()
    reserve.sort()
    
    for i in range(0,len(lost)):
        if lost[i] in reserve:            
            reserve.remove(lost[i])
            answer+=1
        if lost[i]-1 in reserve:              
            reserve.remove(lost[i]-1)
            answer+=1    
        elif lost[i]+1 in reserve:              
            reserve.remove(lost[i]+1)
            answer+=1
        else:
            continue
    
    
    
    return n-len(lost)+answer


# 폰켓몬 : 수학적으로 접근하니 그렇게 어렵지 않았다.
def solution(nums):
    answer = 0
    count = len(nums)/2
    a=list(set(nums))
    
    if count<=len(a):
        return count
    else:
        return len(a)
