def update(neurons):
    for i, n in enumerate(neurons):
        if neurons[i] == 1:
            try:
                neurons[i] = 0
                neurons[i+1] = 1
                break
            except IndexError:
                neurons[i] = 0
    return neurons
    
    
def pulse(neurons):
    neurons[0] = 1
    for i in neurons:
        print(np.array(neurons), end="\r")
        update(neurons)
        time.sleep(0.5)
    print(neurons, end="\r")