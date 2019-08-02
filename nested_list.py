l1=[]
match=[]
score_list=[]
for _ in range(int(raw_input())):
    l=[]
    name = raw_input()
    score = float(raw_input())
    l.append(name)
    l.append(score)
    l1.append(l)
n=len(l1)
for i in range(n):
    score_list.append(l1[i][1])
score_list.sort()
min_score=min(score_list)
diff=[]
for i in range(len(score_list)):
    if(score_list[i]!=min_score):
        d=score_list[i]-min_score
        diff.append(d)
add_min=min(diff)
ans=min_score+add_min
for i in range(n):
    if (l1[i][1]==ans):
        match.append(l1[i][0])
match.sort()
for i in range(len(match)):
    print match[i]
        
