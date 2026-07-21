accuracy=0
while accuracy< 100:
    accuracy+= 10
    print("training ....Accuracy:", accuracy,"%")
    if accuracy >=90:
        print("AI model is ready! Training stopped.")
        break