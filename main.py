from Hdisease import hdisease


age = float(input("age: "))
sex  = float(input("sex: "))
cp = float(input("cp: "))
trestbps  = float(input("trestbps: "))
chol = float(input("chol: "))
fbs  = float(input("fbs: "))
restecg = float(input("restecg: "))
thalach  = float(input("thalach: "))
exang = float(input("exang: "))
oldpeak  = float(input("oldpeak: "))
slope = float(input("slope: "))
ca  = float(input("ca: "))
thal  = float(input("thal: "))

HD = hdisease.theNet()
predition = HD.predict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
print("result is : "+predition)

