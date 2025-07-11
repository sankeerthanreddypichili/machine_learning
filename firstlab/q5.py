import random
import statistics
def generate(count,high,low):
    return[random.randint(low,high) for i in range(count)]
def calculate(numbers):
    meanval=statistics.mean(numbers)
    medianval=statistics.median(numbers)
    modeval=statistics.mode(numbers)
    return meanval,medianval,modeval
if __name__=="__main__":
    count=100
    low=100
    high=150
    numbers=generate(count,high,low)
    Mean,Median,Mode=calculate(numbers)
    print("generated numbers")
    print(numbers)
    print("\n statistics:")
    print(f"mean:{Mean}")
    print(f"median:{Median}")
    print(f"mode:{Mode}")
    
    