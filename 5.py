# 재귀구조로 팩토리얼 연산을 수행하는 함수를 구현하시오.


def factorial_recursive(n):        
    if n <= 1: 
        return 1
    
    return n * factorial_recursive(n - 1)
