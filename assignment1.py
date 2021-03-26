from random import randint
output = []
i = 1
while i <= 10000:
    no_times_atleast_one_head = 0
    k = 1
    while k <= 50000: 
        
        j = 1
        while j <= i:

            output.append(randint(0,1))
            j += 1
        m = 0
        sum_ = 0
        while m < i:
            
            sum_ = sum_ + output[m]
            m += 1
        
        k += 1
        if sum_ >= 1:
          no_times_atleast_one_head += 1
        
        output. clear
    prob_atleast_one_head = no_times_atleast_one_head/5000
    i += 1
    if  prob_atleast_one_head > 0.9:
      break   
         
required_no_of_tosses = i
print("the number os tosses required calulated by simulation is :",i)
print("the number of tosses required calculated by theory is 4")
print("the error in calculation by simulation is:",i - 4)
