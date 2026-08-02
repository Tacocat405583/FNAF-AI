import random

class Perceptron:
    def __init__(self,n):

        self.weights = []
        self.learningConstant = .01

        for i in range(n):
            self.weights.append(random.uniform(-1,1))

    def forward(self,inputs:list):

        sum = 0

        for i in range(len(self.weights)):
             sum += inputs[i] * self.weights[i]

        return self.activate(sum)


    def activate(self,value):
        """ 
            Just a ReLu

            Return -1 if value is < 0 
            else
            Return the value
        """

        return -1 if value < 0 else value


    def train(self,inputs,desired):
        guess = self.forward(inputs=inputs)
        error = desired = guess

        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + error * inputs[i] * self.learningConstant

            


    def check(self):
            return self.weights





if __name__ == "__main__":
    p = Perceptron(3)
    print(p.check())

    inputs = [25.0,22.0]

    guess = p.forward(inputs=inputs)

    print(guess)
    

