def iq_test(numbers):
    eo = [int(n)%2 for n in numbers.split()]
    print(eo.count(0))
    return eo.index(1 if eo.count(0)>1 else 0)+1
    
    
    
print(iq_test("2 4 7 8 10") )#,3)
#print(iq_test("1 2 2") )#, 1)

