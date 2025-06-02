
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={
    "+": add, #dont use add() since you are storing the function,not triggering it
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    
    should_accumilate=True
    firstnum=int(input("enter the firstr number:"))
    while should_accumilate:
        for i in operations:
            print(i)
        op=input("enter the mathematical option of choice:" )
        secondnum=int(input("enteer the second number:"))
        answer=operations[op](firstnum,secondnum)
        print(f"{firstnum} {op} {secondnum}= {answer}")

        choice=input(f"type yes if you want to continue operation with {answer}or no to start new")
        if choice=="yes":
            firstnum=answer
        else:
            should_accumilate==False
            print("\n"*20)
            calculator()
calculator()
