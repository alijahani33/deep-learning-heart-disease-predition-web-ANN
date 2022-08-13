# for DL modeling
import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd



class theNet(nn.Module):
  """
   Heart disease ANN model
  """ 
  def __init__(self) -> None: 
    super().__init__()
    ### input layer
    self.input = nn.Linear(13,32)
    ### hidden layers
    self.fc1 = nn.Linear(32,64)
    self.fc2 = nn.Linear(64,10)
    ### output layer
    self.output = nn.Linear(10,1)
  # forward pass
  def forward(self,x) -> nn.Linear:
    x = F.relu( self.input(x) )
    x = F.relu( self.fc1(x) )
    x = F.relu( self.fc2(x) )
    return self.output(x)
  def _load_model(self) -> None:
    """
    Loads the trained model
    """
    self.load_state_dict(torch.load("trainmodel.pt"))

  def predict(self, age: float, sex: float, cp: float, trestbps: float , chol: float , fbs: float , restecg: float, thalach: float, exang: float, oldpeak: float, slope: float, ca: float, thal: float) -> str:
    """
    it will predict you have haert disease
    or Not              
    """

    self._load_model()
    d = {'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps], 'chol': [chol], 'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach], 'exang': [exang], 'oldpeak': [oldpeak], 'slope': [slope], 'ca': [ca], 'thal': [thal]}
    data = pd.DataFrame(data=d)
    dataT  = torch.tensor( data.values ).float()
    predictions = self(dataT)
    heartdisease = ["You do not have heart disease","You have heart disease"]
    pred_disease = int(torch.sigmoid(predictions)[0][0].item() > .5)
    return heartdisease[pred_disease]