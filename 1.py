# stack 문제

#다음의 조건을 만족하도록 파이썬 코드를 작성하시오.

#변수명 "stack”으로 스택을 초기화하는 코드를 작성하시오.
#초기화한 스택에 원소를 3->4->2->7 순으로 추가한 후
#두번 연속하여 원소를 삭제하는 코드를 작성 하시오.
#스택의 원소를 최하단 부터 출력하는 코드를 작성하시오.
#스택의 원소를 최상단 부터 출력하는 코드를 작성하시오.

stack = []

stack.append(3)
stack.append(4)
stack.append(2)
stack.append(7)
stack.pop()
stack.pop()

print(stack)
print(stack[::-1])
