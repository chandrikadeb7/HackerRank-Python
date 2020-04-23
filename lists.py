if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(0, N):
        input_str = input().split(" ")
        command=input_str[0]
        if(command=='insert'):
            L.insert(int(input_str[1]), int(input_str[2]))
        if(command=='remove'):
            L.remove(int(input_str[1]))
        if(command=='append'):
            L.append(int(input_str[1]))
        if(command=='sort'):
            L.sort() 
        if(command=='pop'):
            L.pop() 
        if(command=='reverse'):
            L.reverse() 
        if(command=='print'):
            print(L)
