import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def welcome():
    print("WELCOME! TO SLARY PEDICTION SYSTEM")
    print("Press any key")
    input()
def checkcsv():
    csv_files=[]
    cur_dir=os.getcwd()
    content_list=os.listdir(cur_dir)
    for x in content_list:
        if x.split(".")[-1]=="csv":
            csv_files.append(x)
    if len(csv_files)==0:
        return " Oops something went wrong  no csv file  there"
    else:
       return csv_files
def display_and_select_csv(csv_files):
    i=0
    for file_name in csv_files:
        print(i,"...",file_name)
        i+=1
    return csv_files[int(input("select any file"))]
def graph(x_train,y_train,regressionObject,x_test,y_test,y_pred):
    plt.scatter(x_train,y_train,color="red",label="Training Data")
    plt.plot(x_tarin,regressionObject.predict(x_train),color="blue",label="BestFit")
    plt.scatter(x_test,y_test,color="green",label="test data")
    plt.scatter(x_test,y_pred,color="black",label="predicted test data")
    plt.title("salary Vs experience")
    plt.xlabel("Years of experience")
    plt.ylabel("Salary")
    plt.legend()
    plt.show()
              
    
                     
    

def main():
    welcome()
    try:
        csv_files=checkcsv()
        if csv_files==" Oops! something went wrong  no csv file  there":
            raise FileNotFoundError("No csv file in the directory")
        csv_file=display_and_select_csv(csv_files)
        print(csv_file,"is selected")
        print("readig cdv file.....")
        print("crearing dataset...")
        dataset=pd.read_csv(csv_file)
        print("Data set created")
        x=dataset.iloc[:,:-1].values
        y=dataset.iloc[:,-1].values
        s=float(input("Enter test data size between ( 0 and 1) "))
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=s)#return 4 values
        print("Model! Creation In progress")
        regressionObject=LinearRegression()
        regressionObject.fit(x_train,y_train)
        print("Model! Is Created")
        print("Press Enter key to predict test data")
        input()
        y_pred=regressionObject.predict(x_test)
        i=0
        print(x-testdata,"....",y-testdata,".....",y-predicted-data)
        while(i<len(x_test)):
              print(x_test[i],"......",y_test[i],".....",y_pred[i])
              i+=1
        print("Press Enter  Key To See Above Result In Graphical Format")
        input()
        graph(x_train,y_train,regressionObject,x_test,y_test,y_pred)
        r2=r2_score(y_test,y_pred)
        print("Our model is %2.2f%% accurate " %(r2*100))
        print("Now You can Predict Salary ")
        print("\n Enter experience in years separated by comma")
        exp=[float(e) for e in input().split(",")]
        ex=[]
        for  x in exp:
              ex.append([x])
        experience=np.array(ex)
        salaries=regressionObject.predict(experience)
              
              
        plt.scatter(experience,salaries,color="balck")
        plt.xlabel("Years Of Experience")
        plt.ylabel("Salaries")
        plt.show()
        d=pd.DataFrame({"Experience":exp,"Salaries":salaries})
        print(d)      
        
        
        
        
                         
            
        
        
        
        
        
    except FileNotFoundError:
        print("No csv file in the directory")
        print("Press Enter Key To Exit")
        input()
        exit()
        




if __name__=="__main__":

    main()
    input()


    
