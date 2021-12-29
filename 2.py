#다음의 조건을 만족하도록 파이썬 코드를 작성하시오.

#변수명 “queue”으로 큐를 초기화하는 코드를 작성하시오.
#초기화한 큐에 원소를 3->4->2->7 순으로 추가한 후
#두번 연속하여 원소를 삭제하는 코드를 작성 하시오.
#큐의 원소를 FIFO 방식으로 출력하는 코드를 작성하시오.
#큐의 원소를 LIFO 방식으로 출력하는 코드를 작성하시오.

from collections import deque 

queue = deque()

queue.append(3)
queue.append(4)
queue.append(2)
queue.append(7)
queue.popleft()
queue.popleft()

print(queue) 

queue.reverse() 
print(queue) 
