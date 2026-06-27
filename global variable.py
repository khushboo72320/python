matric_name="accuracy"
def evalute():
    score= 0.09
    print(f"inside function:{matric_name} score is {score}")
    evalute()

#global variable

a=10
def change():    
    a=80
    print("after changing the 'a' variable:",a)
change()
print("original:",a)

#global epoch
epoch_counter=8
def run_epoch():
    global epoch_counterepoch_counter
    epoch_counter += 1
print(f"inside run_epoch: epoch_counter incremented to{epoch_counter}")
