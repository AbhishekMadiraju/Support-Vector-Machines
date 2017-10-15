import numpy as np
from sklearn import svm
def train(dataset):
    j = 0
    sum = 0
    
    ##Performed Cross Validation for better results. Did a 90 - 10 split.
    
    while j < 10:
        print("Cross validating on file ",j)
        reqs = []
        train0 = []
        train1 = []
        noreqs = []
        dict0 = {}
        dict1 = {}
        found = 0
        i = 0
        filename = r"C:\Users\abhis\Desktop\SVM_Final\datasets_v1" + dataset + "\data"
        file1 = open(filename, 'r')

        for line in file1:

            found = 0
            file2 = open(r'C:\Users\abhis\Desktop\SVM_Final\datasets_v1' + dataset + r'\random_class.' + str(j), 'r')
            for lines in file2:
                arr = lines.split()
                if int(arr[1]) == i:
                    reqs.append([float(y) for y in line.split()])
                    train0.append(float(arr[0]))
                    found = 1
            if (found != 1):
                noreqs.append([float(z) for z in line.split()])
            i = i + 1

        file1 = open(r'C:\Users\abhis\Desktop\SVM_Final\datasets_v1' + dataset + r'\trueclass', 'r')
        for line in file1:
            arr = line.split()
            dict0[arr[1]] = arr[0]

        file2 = open(r'C:\Users\abhis\Desktop\SVM_Final\datasets_v1' + dataset + r'\random_class.' + str(j), 'r')
        for line in file2:
            arr = line.split()
            dict1[arr[1]] = arr[0]
        for key in dict0:
            if key not in dict1:
                train1.append(dict0[key])

        X_train = np.array(reqs).astype(float)
        X_test = np.array(noreqs).astype(float)
        y_train = np.array(train0).astype(float)
        y_test = np.array(train1).astype(float)

        ##print(X_train.shape)
        ##print(X_test.shape)
        ##print(y_train.shape)
        ##print(y_test.shape)
        clf = svm.SVC(kernel='linear')
        clf.fit(X_train,y_train)
        score = clf.score(X_test,y_test)
        print(score)
        sum = sum + score
        j = j + 1
    avg = sum/10.0
    print("Average: ",avg)

train(r'\secom')
