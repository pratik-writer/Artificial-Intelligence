#lab1 Implementing AND OR and XOR gate using perceptron function
import math,random
weights=[1,1]


def activation(x): #sigmoid function
    value=1/(1+math.exp(-x))
    if value>0.5:
        return 1
    return 0




def train_perceptron(inputs,desire_outputs):
    global w0,w1,b
    w0=random.uniform(-1,1)
    w1=random.uniform(-1,1)
    b=random.uniform(-1,1)
    epochs=100
    learning_rate=0.1
    for epoch in range(epochs):
        total_error=0
        for i in range(len(inputs)):
            A,B=inputs[i]
            target_output=desire_outputs[i]
            predicted=activation(w0*A+w1*B+b)
            error=target_output-predicted

            w0+=error*A*learning_rate
            print("w0:",w0,"\n")
            w1+=error*B*learning_rate
            print("w1:",w1,"\n")
            b+=error*learning_rate
            print("b is",b,"\n")
            total_error+=abs(error)

        if total_error==0:
          print(f"Training Completed in {epoch+1} epochs.")
        
        else:
            print("Maximum epoch reached")



def test_perceptron(input):
    A,B=input
    predicted=activation(w0*A+w1*B+b)
    return predicted


#AND Gate

AND_inputs=[(0,0),(0,1),(1,0),(1,1)]
AND_desired_outputs=[0,0,0,1]

train_perceptron(AND_inputs,AND_desired_outputs)

for i in AND_inputs:
     print(f"Inputs:{i},Predicted Output:{test_perceptron(i)}")







