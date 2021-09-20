# import pickle
# model = pickle.load( open('saved_model.pkl','rb'))
# url="naver.com"

# pred=model.predict(url)

# print(pred)

# # 함수로 만들기

# from model_mlp import MLP
import torch
model = torch.load('saved_model.pth')
