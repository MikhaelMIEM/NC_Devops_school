from collections import deque

if __name__ == '__main__':
    #conveyor_input = eval(input())
    conveyor_input = ("QWE",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500
    conveyor = deque()
    for element in conveyor_input:
        if type(element) is tuple:
            for i in element:
                conveyor.append(i)
        elif type(element) is int:
            if len(conveyor) < element:
                output_elements_amount = len(conveyor)
            else:
                output_elements_amount = element
            conveyor_output = tuple(conveyor.popleft() for i in range(output_elements_amount))
            print(conveyor_output)
        if len(conveyor) == 0:
            break
