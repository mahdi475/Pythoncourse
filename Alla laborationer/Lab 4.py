def cheapest_3h(prisen):
    cheapest =  prisen[0] + prisen[1] + prisen[2] 
    cheapest_index = 0
    for i in range(len(prisen) - 2):
        current_3h = prisen[i] + prisen[i+1] + prisen[i+2] 
        print(i)
        print(current_3h)
        
        if current_3h < cheapest:
            cheapest = current_3h
            cheapest_index = i

    return cheapest_index




print(cheapest_3h([143, 167, 124, 112, 96, 102, 129, 190]))
