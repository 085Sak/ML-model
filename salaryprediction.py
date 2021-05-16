#from typing import ValuesView
from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def welcome():
    print("Welcome to Salary Prediction System")
    print("Press Enter key to proceed")
    input()
def checkcsv():
    csv_files=[]
    cur_dir=os.getcwd()#give current directory
    content_list=os.listdir(cur_dir)
    print(content_list)
    csv_files=content_list
    
    return csv_files
def display_and_select_csv(csv_files):
    i=0
    for file_name in csv_files:
        print(i,"....",file_name)
        i+=1
    return csv_files[int(input("Select required csv file :  "))]      
def graph(X_train,Y_train,regressionObject,X_test,Y_test,Y_pred):
    plt.scatter(X_train,Y_train,color="red",label="training data")
  
   # print(Y_train)
    #print(regressionObject.predict(X_train))

   
    plt.plot(X_train,regressionObject.predict(X_train),color="Blue",label="best fit")
    plt.scatter(X_test,Y_test,color='green',label="test data")
    plt.scatter(X_test,Y_pred,color="black",label="preicted test data")
    plt.title("Salary vs Experience")
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.legend()
    plt.show()            
def main():
    welcome()
    #print("helo!")
    try:
        csv_files=checkcsv()# function to check how many csv files are there in directory
        if(csv_files=="NO CSV FILE FOUND!"):
            raise FileNotFoundError("No csv file in the directory")
        csv_file=display_and_select_csv(csv_files)    
        print(csv_file,"is selected")
        print("Reading csv file...")
        print("Creating data set")
        dataset=pd.read_csv(csv_file)
        print("data set created")
        X=dataset.iloc[:,:-1].values
        Y=dataset.iloc[:,-1].values
        s=float(input("enter test data size between 0 and 1:"))#0.1=10 percent
        X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=s)
        print("Model creation in progress....")
        regressionObject=LinearRegression()
        regressionObject.fit(X_train,Y_train)# for regression line on the basis of training data best fit
        print("Model created!")
        print("press Enter key to predict test data")
        input()
        Y_pred=regressionObject.predict(X_test)# predict Y with the help of X predict is a function
        i=0
        print('X_test,"....",Y_test,"....",Y_pred')
        while i<len(X_test):
            print(X_test[i],"....",Y_test[i],"....",Y_pred[i])
            i+=1
        print("Press Enter key to see above result in graphical format")
        input()
        graph(X_train,Y_train,regressionObject,X_test,Y_test,Y_pred)
        r2=r2_score(Y_test,Y_pred)
        print("Our model is %2.2f%%   accurate" %(r2*100))

        print("You can predict salary of an employee ")
        print("enter experience in years of the candidates separated by comma")
        exp=[float(l) for l in input().split(',')]
        ex=[]
        for x in exp:
            ex.append([x])#every elemnt is list
        experience=np.array(ex)
        salaries=regressionObject.predict(experience)
        plt.scatter(experience,salaries,color='black')
        plt.xlabel("years of experience")
        plt.ylabel("Salaries")
        plt.show()
        d=pd.DataFrame({"Experience":exp,"Salaries": salaries})    
        print(d)


              
     
    
    except FileNotFoundError:
        print("NO csv file in the directory")
        print("press enter key to exit")
        input()
        exit()

    
    
if __name__=="__main__":
    main()
    input()
    
    # ek ki press krne pr hi program end ho
    

