import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
x = pd.read_csv('cwurData.csv')
df = pd.DataFrame(x)
all_x = df['world_rank'].tolist()
all_y = df['quality_of_education'].tolist()
#print(df)
#print(len(all_x))
#print(len(all_y))
#print(all_x)
#print(all_y)

#440 random numbers should be select for test.

randoms = []
def select_rndm(lst,hm,first,last):
    #lst for adding selected random numbers
    #hm is number of how many numbers will be selected
    #first and last variables are specify the intervals for selecting number.
    i= 0
    while (i<hm): 
        r = random.randint(first,last)
        lst.append(r)
        i+=1
        
select_rndm(randoms,20,0,99) #2012
select_rndm(randoms,20,100,199) #2013
select_rndm(randoms,200,200,1199) #2014
select_rndm(randoms,200,1200,2199) #2015
#print (randoms)

#I select the random numbers and I don't want to change these number when every I run the program.
#So,I save the random number to my_random list.
my_random = [76, 93, 66, 60, 89, 49, 59, 32, 75, 78, 42, 72, 1, 54, 65, 12, 58, 91, 29, 83, 155, 182, 121, 177, 123, 124, 161,
             180, 184, 1064, 192, 364, 165, 196, 564, 702, 211, 143, 117, 297, 795, 479, 900, 663, 289, 351, 889, 464, 719, 203,
             604, 200, 666, 332, 665, 1055, 1179, 226, 635, 802, 257, 210, 704, 1188, 932, 579, 645, 268, 1136, 271, 459, 396,
             581, 818, 659, 757, 998, 460, 1054, 880, 1101, 414, 776, 416, 713, 316, 1015, 1121, 910, 791, 721, 939, 1060, 370,
             221, 611, 425, 231, 454, 505, 798, 457, 355, 354, 596, 987, 379, 511, 338, 1143, 1110, 521, 978, 618, 678, 219, 
             577, 1126, 1151, 753, 550, 1152, 657, 918, 641, 832, 1037, 907, 361, 350, 593, 693, 395, 789, 288, 687, 937, 769,
             1018, 844, 909, 320, 1107, 317, 335, 503, 273, 1120, 533, 310, 331, 965, 715, 446, 728, 1190, 614, 835, 428, 913, 
             833, 220, 318, 1075, 1163, 625, 1182, 979, 242, 445, 691, 418, 283, 382, 205, 904, 1006, 1088, 676, 265, 853, 964,
             280, 942, 807, 554, 708, 413, 1100, 967, 1195, 1049, 407, 477, 294, 670, 966, 223, 552, 785, 218, 434, 436, 206,
             411, 1142, 1048, 705, 1153, 525, 334, 863, 631, 1093, 640, 1026, 1004, 400, 300, 613, 698, 510, 936, 847, 284, 342,
             606, 772, 254, 954, 1199, 970, 356, 703, 367, 563, 260, 892, 619, 558, 1381, 1232, 1713, 1786, 2019, 2057, 1904, 
             2028, 2177, 1468, 1771, 1475, 1975, 2178, 1438, 1403, 1773, 1765, 1881, 1818, 2043, 1702, 1833, 1294, 2060, 1266,
             2167, 1694, 1397, 2013, 2077, 1444, 1663, 1416, 1982, 1704, 1448, 2070, 1636, 2012, 1977, 1149, 1497, 1579, 1533,
             1372, 1835, 1309, 1531, 1303, 1918, 1508, 1956, 1477, 1364, 1822, 1960, 1648, 2198, 1725, 2155, 1353, 1654, 1559, 
             409, 1114, 1861, 1138, 1876, 777, 1454, 1817, 1847, 1288, 1709, 1375, 1959, 816, 1491, 1275, 2192, 1872, 2049,
             1890, 1452, 1821, 1949, 1812, 1263, 1810, 1681, 1871, 1458, 1884, 2153, 426, 843, 1038, 1218, 1459, 1642, 2122,
             2124, 1503, 1394, 1234, 1639, 293, 1387, 2126, 1431, 1737, 2120, 1236, 1483, 1718, 1575, 790, 1276, 1673, 1045,
             2027, 1601, 2003, 2097, 1806, 1809, 1509, 1220, 1860, 1405, 2168, 856, 1350, 2111, 1480, 1325, 2197, 1289, 1212,
             662, 1059, 1034, 1522, 1556, 1336, 754, 1609, 304, 422, 1629, 1797, 1843, 1998, 1892, 1279, 497, 1456, 498, 1420,
             2050, 1587, 237, 2163, 2010, 1754, 1210, 1795, 1931, 1971, 1567, 213, 1585, 2136, 2148, 1322, 1247, 1878, 1958, 
             1885, 1573, 1625, 1823, 2006, 1437, 1891, 1680, 1674, 1569, 1162, 1908, 1298, 1536, 874, 1343, 1706, 2119, 2001,
             1635, 1584]
#Spliting the dataset as a train and test
test_x = []
test_y = []
x = []
y = []
for i in my_random:
    a = all_x[i]
    b = all_y[i]
    test_x.append(a/1000)
    test_y.append(b/1000)
    
for j in test_x:
    all_x.remove(j*1000)
    
for j in test_y:
    all_y.remove(j*1000)
    
for k in all_x: # normalizing
    x.append(k/1000)
    
for k in all_y:
    y.append(k/1000)

#!!!!!!!!GRADIENT DESCENT ALAGORITHM!!!!!!!
def fill_h_matrix(empty_matrix, num, degree):
    #creating polinomial function matrix of x unknown 
    #for example, degree = 3 so the matrix will be [0, x, x**2, x**3]
    
    for a in range(degree):
        empty_matrix[0,a] = (num**a)
    return empty_matrix

all_coefficient = np.zeros((28,28)) #rows are my polinomial degree and columns are coeficients (wo, w1, w2) of my polinomial functions
step_size = 0.0001
i = 0
empty_list = []
my_h_empty = np.zeros((1,28)) # For each degree, it create empty h matrix that is size degree+1 28x1
my_w = np.zeros((1,28)) # coefficients of a polinomial function
partial = np.zeros((1,28))
for d in range(28): 
    # d for degree, j for coefficients of the degree i for training x values
    z=0 #epoch
    while(z<10):
        for j in range(d+1): # update coefficients untill the degree
            total_rss = 0 # sum of(yi-y^)
            for i in range(1760):
                my_h = fill_h_matrix(my_h_empty,x[i],d+1)# i'ninci indisteki x leri x yerine koyarak h matris oluşturduk.
                my_h_t = my_h.transpose()
                xdot = np.dot(my_w,my_h_t)
                total_rss += my_h[0,j] * (y[i]- xdot)
            partial[0,j] = -2 * total_rss
            my_w[0,j] = my_w[0,j] - step_size*partial[0,j]
            all_coefficient[d,j] = my_w[0,j]
        z+=1

#!!!!!!!!!!!!FINDING Y PREDICTIONS!!!!!!!!!!!!      
empty2_matrix = np.zeros((1,28))
y_prediction = np.zeros((1760,28))
for d in range(28):
    coef = all_coefficient[d,:] 
    y_pred = 0
    for i in range(1760):
        h = fill_h_matrix(empty2_matrix,x[i],d+1)
        hT = h.transpose()
        y_pred = coef.dot(hT)
        y_prediction[i,d] = y_pred

#!!!!!!!!!!!!!FINDING TRAINING ERRORS !!!!!!!!!!!!!!!!!!
training_errors = []
for d in range(28):
    sumRss = 0
    for i in range(1760):
        sumRss += (y[i] - y_prediction[i,d])**2
    training_errors.append(sumRss/1760) #training error = rmse**2/
    
xx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27] #Graph of training error
plt.scatter(xx,training_errors, color = 'red') 
plt.show()
    
#!!!!!!!!!!!!!FINDING TEST ERRORS !!!!!!!!!!!!!!!!!!!
empty3_matrix = np.zeros((1,28))
test_y_pred = np.zeros((440,28))
for d in range(28):
    coef=all_coefficient[d,:] 
    pred = 0
    for i in range(440):
        h = fill_h_matrix(empty3_matrix,test_x[i],d+1)
        hT = h.transpose()
        pred = coef.dot(hT)
        test_y_pred[i,d] = pred
        
test_err = []
for d in range(28):
    summ = 0
    for i in range(440):
        summ += ( test_y[i] - test_y_pred[i,d])
    test_err.append((summ/440))    

plt.scatter(xx,test_err, color = 'red') 
plt.show()