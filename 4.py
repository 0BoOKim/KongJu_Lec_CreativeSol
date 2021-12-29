# 함수 명이 recursv( ) 일 때, 11번 째 호출에서 종료되는 재귀함수 구조를 갖도록 코드를 작성하시오.

def recursive_function(i):
    
    if i == 11:
        return
    recursive_function(i + 1)
    
recursive_function(1)
