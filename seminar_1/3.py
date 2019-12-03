
if __name__ == '__main__':
    #conveyor_input = eval(input())
    conveyor_input = ("QWE",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500
    conveyor = []
    for element in conveyor_input:
        if type(element) is tuple:
            for i in element:
                conveyor.append(i)
        elif type(element) is int:
            conveyor_output = ()
            for i in range(element):
                try:
                    last_conveyor_obj = conveyor.pop(0)
                    conveyor_output = (*conveyor_output, last_conveyor_obj)
                except IndexError:
                    print(conveyor_output)
                    quit()
            print(conveyor_output)
        if len(conveyor)==0: quit()
