# [1차] 비밀지도 : 생각보다 시간이 조금 걸렸다. n 의 값에 따라 답이 달라지는 것을 고려하지 않았었다.
def two(n,m):
    answer = [ ]
    while n>=1:
        answer.append(n%2)
        n=(n-(n%2))/2
        
    while len(answer)<m:
        answer.append(0)
        
    answer.reverse()
    
    return answer 

def solution(n, arr1, arr2):
    answer = []
    q=[]
    # 벽: 1  하나라도 1 이면 1.
    a=[]
    b=[]
    length=n
    
    for i in range(0,n):
        a=two(arr1[i],length)
        b=two(arr2[i],length) 
        n=""
        for j in range(0,length):
            if a[j]==b[j]==0:
                n+=" "
            else:
                n+="#"
        q.append(n)
        
    
    
    
    return q


# 실패율 : 실패, 런타임 에러가 나왔다. 마지막 for 문이 문제인 것 같지만 대체할 방법이 안떠올랐다.
def solution(N, stages):
    answer = []
    a = [[0] * 2 for _ in range(N)] 
    stages.sort()
    
    total = 0
    temp=0  
    minus = 0
    # a인 사람 / a 이상인 사람
        
    for i in range(1,N+1):
        a[i-1][1]=i
        a[i-1][0]=(stages.count(i)/(len(stages)-minus))
        minus+=stages.count(i)
        
    a.sort(reverse=True)    
    
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i][0]==a[j][0]:
                temp = a[i][1]
                a[i][1] = a[j][1]
                a[j][1] = temp
    
    for i in range(0,len(a)):
        answer.append(a[i][1])
    
    return answer


# 로또의 최고 순위와 최저 순위 : 생각보다 시간이 좀 걸렸다. 시간 복잡도가 높은 것 같아서 만족스럽지는 않다. rank 를 이용한 풀이도 보였다.
def solution(lottos, win_nums):
    answer = []
    
    good = 0
    bad=0
    zero = lottos.count(0)
    
    for i in range(0,len(lottos)):
        if lottos[i] in win_nums:
            good+=1            
            win_nums.remove(lottos[i])
            
    bad=good        
    
    if zero>=len(win_nums):
        good+=len(win_nums)
    else:
        good+=zero
        
    if 7-good>=6:
        answer.append(6)
    else:    
        answer.append(7-good)
    
    if 7-bad>=6:
        answer.append(6)
    else:    
        answer.append(7-bad)
    
    return answer


# 숫자 문자열과 영단어 : 생각보다 쉽게 풀었다. 시간 초과가 걸리지 않아서 신기했다.
def solution(s):
    answer = 0
    s=s.replace("one","1")
    s=s.replace("two","2")
    s=s.replace("three","3")
    s=s.replace("four","4")
    s=s.replace("five","5")
    s=s.replace("six","6")
    s=s.replace("seven","7")
    s=s.replace("eight","8")
    s=s.replace("nine","9")
    s=s.replace("zero","0")
    
    return int(s)


# 신규 아이디 추천 : 필요없는 문자들을 "@"로 치환한 후 while 문을 통해 삭제하는 방식으로 풀었다. while 문이 많았지만 다행히 시간 초과는 걸리지 않았다. 정규식은 어려워서 정석대로 풀려고 했다. ".." 을 replace를 이용해서 "." 로 바꾸는 방법등을 배웠다.
def solution(new_id):
    a = ['0','1','2','3','4','5','6','7','8','9','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','-','_',"."]
    
    answer = new_id.lower()
    
    answer = list(answer)
    for i in range(len(list(new_id))):
        if answer[i] not in a:
            answer[i]="@"
    
    while "@" in answer:
        answer.remove("@")
    
    for i in range(len(list(answer))-1):
        if answer[i]==answer[i+1]==".":
            answer[i]="@"
    
    while "@" in answer:
        answer.remove("@")
        
    if answer[0]==".":
        answer[0]="@"
    
    if answer[-1]==".":
        answer[-1]="@"
    
    while "@" in answer:
        answer.remove("@")
    
    if len(answer)==0:
        answer.append('a')   
    
    ha = answer
    
    if len(answer)>=16:
        answer=answer[0:15]
         
    if len(answer)==15 and answer[-1]==".":
        del answer[-1]
        
    
        
        
    while "@" in answer:
        answer.remove("@")     
        
    if len(answer)==1:
        answer.append(answer[0])
        answer.append(answer[0])
        
    if len(answer)==2:
        answer.append(answer[1])
        
    answer= "".join(answer)
        
        
    return answer


# 크레인 인형뽑기 게임 : del 할 때 range 오류가 계속 나와서 새로운 def 를 만들어서 해결했다.
def remove(list):
    for i in range(0,len(list)-1):
        if list[i]==list[i+1]:
            del list[i]
            del list[i]
            break
    return list        

def solution(board, moves):
    answer = 0
    a = []
    
    
    pick = len(moves)
    width = len(board)
    
    for i in range(0,pick):
        for j in range(0,width):
            if board[j][moves[i]-1]!=0:
                a.append(board[j][moves[i]-1])
                board[j][moves[i]-1]=0
                break    
    
    origin=len(a)
    
    while True:
        if len(a)==len(remove(a)):
            break
        else:    
            a=remove(a)                       
    
    
    return origin-len(a)


# [1차] 다트 게임 : 실패, 지난 번에 노가다로 풀었던 기억이 있어서 풀지 않았다. 10을 k로 바꾸는 아이디어가 가장 좋아보였다.
def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score)
    
    
    
    
    
    
    return answer


# 키패드 누르기 : 실패, 지난 번에 풀려고 했던 기억이 있어서 풀지 않았다.
def solution(numbers, hand):
    answer = ''
    # Keypad Coordinate: 0123456789*(10)#(11)
    distance = [[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3]]

    # initial position
    left = 10
    right = 11

    for i in numbers:
        # LEFT HAND
        if i in [1,4,7]:
            answer += 'L'
            left = i
        # RIGHT HAND
        elif i in [3,6,9]:
            answer += 'R'
            right = i
        # DISTACNE COMPARISON
        else:
            ldist = abs(distance[i][0] - distance[left][0]) + abs(distance[i][1] - distance[left][1])
            rdist = abs(distance[i][0] - distance[right][0]) + abs(distance[i][1] - distance[right][1])
            if ldist > rdist:
                answer += 'R'
                right = i
            elif ldist < rdist:
                answer += 'L'
                left = i
            # distance equals
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
    return answer


# 신고 결과 받기 : 실패, 어찌어찌 테스트 코드는 통과했지만 당연히 시간초과가 나왔고 정확도도 많이 떨어졌다. 머릿속으로는 대충 알겠지만 실제 코드를 사용하기는 어려웠다.
def solution(id_list, report, k):
    
    answer = [0]*len(id_list)    
    a = list(set(report))
    
    b=[]
    
    for i in range(0,len(a)):
        b += str(a[i]).split(" ")
    
    
    
    c = []
    ban = []
    
    for i in range(0,len(b)):
        if i%2==0:
            continue
        else:
            c.append(b[i])
            
    for i in range(0,len(c)):
        if c.count(c[i])>=k:
            ban.append(c[i])
    
    ban = list(set(ban))
    
    for i in range(0,len(id_list)-1):
        for j in range(0,len(b)):
            if j%2!=0:
                continue
            else:
                if b[j]==id_list[i] and b[j+1] in ban:
                    answer[i]+=1
        
    
    
    
    
    return answer
