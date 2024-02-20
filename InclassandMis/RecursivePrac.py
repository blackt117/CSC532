def reverse_string(string):
    if len(string) == 1:
        return string[0]
    else:
        return (string[len(string)-1]) + reverse_string(string[:len(string)-1])

print(reverse_string("he"))


def exp(a,n):
    if n == 0:
        return 1, 0
    if n == 1:
        return a, 0
    if n % 2 == 0:
        ans, count = exp(a * a, n // 2)
        return ans, count + 1
    else:
        ans, count = exp(a * a, n // 2)
        ans = a * ans
        return ans, count + 2

print(exp(3,3))