from scipy.stats import ks_2samp
from math import sqrt
import numpy as np

def ks(list_obs, list_poisson, sample_size, confidence, lamb):
    #D, p_value = ks_2samp(list_poisson, list_obs)
    D, p_value = ks_2samp(list_poisson, list_obs)

    a = "The Kolmogorov-Smirnov Test accept the null hypothesis"
    b = "The Kolmogorov-Smirnov Test reject the null hypothesis"

    global teste
    teste = ''

    if lamb > 10:
        teste = b
  
    D_critico = 0
    if confidence == 0.95:
        confidenceL = 1
    elif confidence == 0.99:
        confidenceL = 2
    else:
        confidenceL = 0
    
    s = sqrt(sample_size)
    
    table = np.matrix([[0.202, 0.214, 0.226, 0.237, 0.254],
                  [0.234, 0.242,0.254,0.265,0.281],
                  [0.290,0.3,0.310,0.324,0.334],
                  [0.152,0.166,0.172,0.179,0.185],
                  [0.180,0.188,0.194,0.199,0.206],
                  [0.223,0.234,0.236,0.243,0.249],
                  [0.120,0.132,0.140,0.144,0.149],
                  [0.141,0.151,0.156,0.160,0.165],
                  [0.176,0.185,0.188,0.195,0.197],
                  [0.100,0.112,0.116,0.120,0.124],
                  [0.116,0.125,0.129,0.134,0.140],
                  [0.149,0.154,0.158,0.160,0.168],
                  [0.087,0.097,0.102,0.106,0.110],
                  [0.101,0.108,0.113,0.118,0.122],
                  [0.130,0.135,0.137,0.143,0.146],
                  [0.55/s,0.61/s,0.65/s,0.67/s,0.7/s],
                  [0.64/s,0.69/s,0.72/s,0.75/s,0.77/s],
                  [0.82/s,0.86/s,0.87/s,0.9/s,0.93/s]])
    
    if sample_size < 12:
        if confidenceL == 0:
            if lamb <=1:
                if D <= table[0,0]:
                    teste = a
                    D_critico = table[0,0]
                    
                else:
                    teste = b
                    D_critico = table[0,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[0,1]:
                    teste = a
                    D_critico= table[0,1]
                    
                else:
                    teste = b
                    D_critico= table[0,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[0,2]:
                    teste = a
                    D_critico= table[0,2]
                    
                else:
                    teste = b
                    D_critico= table[0,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[0,3]:
                    teste = a
                    D_critico= table[0,3]
                    
                else:
                    teste = b
                    D_critico= table[0,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[0,4]:
                    teste = a
                    D_critico= table[0,4]
                    
                else:
                    teste = b
                    D_critico= table[0,4]
            
#-----------------------------------------------------------   
        
        elif confidenceL == 1:
            if lamb <=1:
                if D <= table[1,0]:
                    teste = a
                    D_critico= table[1,0]
                    
                else:
                    teste = b
                    D_critico= table[1,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[1,1]:
                    teste = a
                    D_critico= table[1,1]
                    
                else:
                    teste = b
                    D_critico= table[1,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[1,2]:
                    teste = a
                    D_critico= table[1,2]
                else:
                    teste = b
                    D_critico= table[1,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[1,3]:
                    teste = a
                    D_critico= table[1,3]
                    
                else:
                    teste = b
                    D_critico= table[1,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[1,4]:
                    teste = a
                    D_critico= table[1,4]
                    
                else:
                    teste = b
                    D_critico= table[1,4]
#-----------------------------------------------------------
        elif confidenceL == 2:
            if lamb <=1:
                if D <= table[2,0]:
                    teste = a
                    D_critico= table[2,0]
                    
                else:
                    teste = b
                    D_critico= table[2,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[2,1]:
                    teste = a
                    D_critico= table[2,1]
                else:
                    teste = b
                    D_critico= table[2,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[2,2]:
                    teste = a
                    D_critico= table[2,2]
                    
                else:
                    teste = b
                    D_critico= table[2,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[2,3]:
                    teste = a
                    D_critico= table[2,3]
                    
                else:
                    teste = b
                    D_critico= table[2,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[2,4]:
                    teste = a
                    D_critico= table[2,4]
                    
                else:
                    teste = b
                    D_critico= table[2,4]
#-----------------------------------------------------------
    elif sample_size >=12 and sample_size  < 20:
        if confidenceL == 0:
            if lamb <=1:
                if D <= table[3,0]:
                    teste = a
                    D_critico= table[3,0]
                    
                else:
                    teste = b
                    D_critico= table[3,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[3,1]:
                    teste = a
                    D_critico= table[3,1]

                else:
                    teste = b
                    D_critico= table[3,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[3,2]:
                    teste = a
                    D_critico= table[3,2]

                else:
                    teste = b
                    D_critico= table[3,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[3,3]:
                    teste = a
                    D_critico= table[3,3]

                else:
                    teste = b
                    D_critico= table[3,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[3,4]:
                    teste = a
                    D_critico= table[3,4]

                else:
                    teste = b
                    D_critico= table[3,4]
            
#-----------------------------------------------------------
        
        elif confidenceL == 1:
            if lamb <=1:
                if D <= table[4,0]:
                    teste = a
                    D_critico= table[4,0]

                else:
                    teste = b
                    D_critico= table[4,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[4,1]:
                    teste = a
                    D_critico= table[4,1]

                else:
                    teste = b
                    D_critico= table[4,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[4,2]:
                    teste = a
                    D_critico= table[4,2]

                else:
                    teste = b
                    D_critico= table[4,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[4,3]:
                    teste = a
                    D_critico= table[4,3]
                    
                else:
                    teste = b
                    D_critico= table[4,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[4,4]:
                    teste = a
                    D_critico= table[4,4]
                    
                else:
                    teste = b
                    D_critico= table[4,4]
#-----------------------------------------------------------           
        elif confidenceL == 2:
            if lamb <=1:
                if D <= table[5,0]:
                    teste = a
                    D_critico= table[5,0]
                    
                else:
                    teste = b
                    D_critico= table[5,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[5,1]:
                    teste = a
                    D_critico= table[5,1]
                    
                else:
                    teste = b
                    D_critico= table[5,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[5,2]:
                    teste = a
                    D_critico= table[5,2]
                    
                else:
                    teste = b
                    D_critico= table[5,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[5,3]:
                    teste = a
                    D_critico= table[5,3]
                    
                else:
                    teste = b
                    D_critico= table[5,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[5,4]:
                    teste = a
                    D_critico= table[5,4]
                    
                else:
                    teste = b
                    D_critico= table[5,4]
#-----------------------------------------------------------
    elif sample_size  >= 20 and sample_size < 30:
    
        if confidenceL == 0:
            if lamb <=1:
                if D <= table[6,0]:
                    teste = a
                    D_critico= table[6,0]
                    
                else:
                    teste = b
                    D_critico= table[6,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[6,1]:
                    teste = a
                    D_critico= table[6,1]
                    
                else:
                    teste = b
                    D_critico= table[6,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[6,2]:
                    teste = a
                    D_critico= table[6,2]

                else:
                    teste = b
                    D_critico= table[6,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[6,3]:
                    teste = a
                    D_critico= table[6,3]

                else:
                    teste = b
                    D_critico= table[6,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[6,4]:
                    teste = a
                    D_critico= table[6,4]

                else:
                    teste = b
                    D_critico= table[6,4]
#-----------------------------------------------------------
        
        
        elif confidenceL == 1:
            if lamb <=1:
                if D <= table[7,0]:
                    teste = a
                    D_critico= table[7,0]

                else:
                    teste = b
                    D_critico= table[7,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[7,1]:
                    teste = a
                    D_critico= table[7,1]

                else:
                    teste = b
                    D_critico= table[7,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[7,2]:
                    teste = a
                    D_critico= table[7,2]

                else:
                    teste = b
                    D_critico= table[7,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[7,3]:
                    teste = a
                    D_critico= table[7,3]

                else:
                    teste = b
                    D_critico= table[7,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[7,4]:
                    teste = a
                    D_critico= table[7,4]

                else:
                    teste = b
                    D_critico= table[7,4]
#-----------------------------------------------------------
        elif confidenceL == 2:
            if lamb <=1:
                if D <= table[8,0]:
                    teste = a
                    D_critico= table[8,0]

                else:
                    teste = b
                    D_critico= table[8,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[8,1]:
                    teste = a
                    D_critico= table[8,1]

                else:
                    teste = b
                    D_critico= table[8,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[8,2]:
                    teste = a
                    D_critico= table[8,2]

                else:
                    teste = b
            elif lamb > 3 and lamb <=5:
                if D <= table[8,3]:
                    teste = a
                    D_critico= table[8,3]
                    
                else:
                    teste = b
            elif lamb > 5 and lamb <=10:
                if D <= table[8,4]:
                    teste = a
                    D_critico= table[8,4]
                    
                else:
                    teste = b
                    D_critico= table[8,4]
        #-----------------------------------------------------------
    elif sample_size >= 30 and sample_size < 40:
    
        if confidenceL == 0:
            if lamb <=1:
                if D <= table[9,0]:
                    teste = a
                    D_critico= table[9,0]
                else:
                    teste = b
                    D_critico= table[9,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[9,1]:
                    teste = a
                    D_critico= table[9,1]
                    
                else:
                    teste = b
                    D_critico= table[9,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[9,2]:
                    teste = a
                    D_critico= table[9,2]
                    
                else:
                    teste = b
                    D_critico= table[9,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[9,3]:
                    teste = a
                    D_critico= table[9,3]
                    
                else:
                    teste = b
                    D_critico= table[9,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[9,4]:
                    teste = a
                    D_critico= table[9,4]
                else:
                    teste = b
                    D_critico= table[9,4]
            
#-----------------------------------------------------------
        
        elif confidenceL == 1:
            if lamb <=1:
                if D <= table[10,0]:
                    teste = a
                    D_critico= table[10,0]
                    
                else:
                    teste = b
                    D_critico= table[10,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[10,1]:
                    teste = a
                    D_critico= table[10,1]
                    
                else:
                    teste = b
                    D_critico= table[10,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[10,2]:
                    teste = a
                    D_critico= table[10,2]
                    
                else:
                    teste = b
                    D_critico= table[10,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[10,3]:
                    teste = a
                    D_critico= table[10,3]
                    
                else:
                    teste = b
                    D_critico= table[10,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[10,4]:
                    teste = a
                    D_critico= table[10,4]
                    
                else:
                    teste = b
                    D_critico= table[10,4]
#-----------------------------------------------------------
        elif confidenceL == 2:
            if lamb <=1:
                if D <= table[11,0]:
                    teste = a
                    D_critico= table[11,0]
                    
                else:
                    teste = b
                    D_critico= table[11,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[11,1]:
                    teste = a
                    D_critico= table[11,1]
                    
                else:
                    teste = b
                    D_critico= table[11,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[11,2]:
                    teste = a
                    D_critico= table[11,2]
                    
                else:
                    teste = b
                    D_critico= table[11,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[11,3]:
                    teste = a
                    D_critico= table[11,3]
                    
                else:
                    teste = b
                    D_critico= table[11,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[11,4]:
                    teste = a
                    D_critico= table[11,4]
                    
                else:
                    teste = b
                    D_critico= table[11,4]
#-----------------------------------------------------------
    
    elif sample_size == 40:

        if confidenceL == 0:
            if lamb <=1:
                if D <= table[12,0]:
                    teste = a
                    D_critico= table[12,0]

                else:
                    teste = b
                    D_critico= table[12,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[12,1]:
                    teste = a
                    D_critico= table[12,1]

                else:
                    teste = b
                    D_critico= table[12,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[12,2]:
                    teste = a
                    D_critico= table[12,2]

                else:
                    teste = b
                    D_critico= table[12,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[12,3]:
                    teste = a
                    D_critico= table[12,3]

                else:
                    teste = b
                    D_critico= table[12,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[12,4]:
                    teste = a
                    D_critico= table[12,4]

                else:
                    teste = b
                    D_critico= table[12,4]
            
#-----------------------------------------------------------
        
        elif confidenceL == 1:
            if lamb <=1:
                if D <= table[13,0]:
                    teste = a
                    D_critico= table[13,0]

                else:
                    teste = b
                    D_critico= table[13,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[13,1]:
                    teste = a
                    D_critico= table[13,1]

                else:
                    teste = b
                    D_critico= table[13,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[13,2]:
                    teste = a
                    D_critico= table[13,2]

                else:
                    teste = b
                    D_critico= table[13,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[13,3]:
                    teste = a
                    D_critico= table[13,3]

                else:
                    teste = b
                    D_critico= table[13,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[13,4]:
                    teste = a
                    D_critico= table[13,4]

                else:
                    teste = b
                    D_critico= table[13,4]
#-----------------------------------------------------------
        elif confidenceL == 2:
            if lamb <=1:
                if D <= table[14,0]:
                    teste = a
                    D_critico= table[14,0]

                else:
                    teste = b
                    D_critico= table[14,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[14,1]:
                    teste = a
                    D_critico= table[14,1]

                else:
                    teste = b
                    D_critico= table[14,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[14,2]:
                    teste = a
                    D_critico= table[14,2]

                else:
                    teste = b
                    D_critico= table[14,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[14,3]:
                    teste = a
                    D_critico= table[14,3]

                else:
                    teste = b
                    D_critico= table[14,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[14,4]:
                    teste = a
                    D_critico= table[14,4]

                else:
                    teste = b    
                    D_critico= table[14,4]
#-----------------------------------------------------------                    
    elif sample_size > 40:

        if confidenceL == 0:
            if lamb <=1:
                if D <= table[15,0]:
                    teste = a
                    D_critico= table[15,0]
                   
                else:
                    teste = b
                    D_critico= table[15,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[15,1]:
                    teste = a
                    D_critico= table[15,1]
                   
                else:
                    teste = b
                    D_critico= table[15,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[15,2]:
                    teste = a
                    D_critico= table[15,2]

                else:
                    teste = b
                    D_critico= table[15,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[15,3]:
                    teste = a
                    D_critico= table[15,3]

                else:
                    teste = b
                    D_critico= table[15,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[15,4]:
                    teste = a
                    D_critico= table[15,4]

                else:
                    teste = b
                    D_critico= table[15,4]
            
#-----------------------------------------------------------
        
        elif confidenceL == 1:
            if lamb <=1:
                if D <= table[16,0]:
                    teste = a
                    D_critico= table[16,0]

                else:
                    teste = b
                    D_critico= table[16,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[16,1]:
                    teste = a
                    D_critico= table[16,1]

                else:
                    teste = b
                    D_critico= table[16,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[16,2]:
                    teste = a
                    D_critico= table[16,2]

                else:
                    teste = b
                    D_critico= table[16,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[16,3]:
                    teste = a
                    D_critico= table[16,3]

                else:
                    teste = b
                    D_critico= table[16,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[16,4]:
                    teste = a
                    D_critico= table[16,4]

                else:
                    teste = b
                    D_critico= table[16,4]
#-----------------------------------------------------------
        elif confidenceL == 2:
            if lamb <=1:
                if D <= table[17,0]:
                    teste = a
                    D_critico= table[17,0]

                else:
                    teste = b
                    D_critico= table[17,0]
            elif lamb > 1 and lamb <=2:
                if D <= table[17,1]:
                    teste = a
                    D_critico= table[17,1]

                else:
                    teste = b
                    D_critico= table[17,1]
            elif lamb > 2 and lamb <=3:
                if D <= table[17,2]:
                    teste = a
                    D_critico= table[17,2]

                else:
                    teste = b
                    D_critico= table[17,2]
            elif lamb > 3 and lamb <=5:
                if D <= table[17,3]:
                    teste = a
                    D_critico= table[17,3]

                else:
                    teste = b
                    D_critico= table[17,3]
            elif lamb > 5 and lamb <=10:
                if D <= table[17,4]:
                    teste = a
                    D_critico= table[17,4]

                else:
                    teste = b
                    D_critico= table[17,4]    
    return D, teste, D_critico
