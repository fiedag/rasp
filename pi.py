import math;
print(math.pi);
ans=0;
sign=-1;
theend=100000000;
for i in range(1,theend):
    sign = -1 * sign;
    ans = ans + sign * 1/(2*i - 1);
    if (i % 10000 == 0):
        print(i, ans*4,math.pi - ans*4);




print("final answer for i=",theend, ans*4,math.pi - ans*4);


    
