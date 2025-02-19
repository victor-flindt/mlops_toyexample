# from project_pandora_toy.model import Model
# from project_pandora_toy.data import MyDataset
from random import random

def train():
    # dataset = MyDataset("data/raw")
    # model = Model()
    best_model_score = 0

    for i in range(0,11):
        
        validation_score = random() 

        print(f"Epoch {i} accuracy {validation_score*10}")
        
        best_model_score = validation_score*10 if (validation_score*10 > best_model_score) else best_model_score

        if i==10:
            print(f"model training done saving best model with accruacy {round(best_model_score,3)}")

if __name__ == "__main__":
    train()
