
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import csv

with open('nanai-vowels.csv', encoding='utf-8') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    n_i_f1 = 0
    n_i_f2 = 0
    n_e_f1 = 0
    n_e_f2 = 0
    n_I_f1 = 0
    n_I_f2 = 0
    counter_i = 0
    counter_e = 0
    counter_I = 0
    k_i_f1 = 0
    k_i_f2 = 0
    k_e_f1 = 0
    k_e_f2 = 0
    k_I_f1 = 0
    k_I_f2 = 0
    kcounter_i = 0
    kcounter_e = 0
    kcounter_I = 0
    i_f1, e_f1, I_f1, ki_f1, ke_f1, kI_f1 = 0, 0, 0, 0, 0, 0
    for row in filereader:
        if row[2] == "Dzhuen":
            if row[3] == "i":
                n_i_f1 += float(row[4])
                n_i_f2 += float(row[5])
                counter_i +=1
                if counter_i != 0:
                    i_f1 = n_i_f1/counter_i
                    i_f2 = n_i_f2/counter_i
            elif row[3] == "e":
                n_e_f1 += float(row[4])
                n_e_f2 += float(row[5])
                counter_e +=1
                if counter_e != 0:
                    e_f1 = n_e_f1/counter_e
                    e_f2 = n_e_f2/counter_e
            elif row[3] == "I":
                n_I_f1 += float(row[4])
                n_I_f2 += float(row[5])
                counter_I +=1
                if counter_I != 0:
                    I_f1 = n_I_f1/counter_I
                    I_f2 = n_I_f2/counter_I
        elif row[2] == "Naikhin":
            if row[3] == "i":
                k_i_f1 += float(row[4])
                k_i_f2 += float(row[5])
                kcounter_i +=1
                if kcounter_i != 0:
                    ki_f1 = k_i_f1/kcounter_i
                    ki_f2 = k_i_f2/kcounter_i
            elif row[3] == "e":
                k_e_f1 += float(row[4])
                k_e_f2 += float(row[5])
                kcounter_e +=1
                if kcounter_e != 0:
                    ke_f1 = k_e_f1/kcounter_e
                    ke_f2 = k_e_f2/kcounter_e
            elif row[3] == "I":
                k_I_f1 += float(row[4])
                k_I_f2 += float(row[5])
                kcounter_I +=1
                if kcounter_I != 0:
                    kI_f1 = k_I_f1/kcounter_I
                    kI_f2 = k_I_f2/kcounter_I
print(i_f1, e_f1, I_f1, ki_f1, ke_f1, kI_f1)
print(i_f2, e_f2, I_f2, ki_f2, ke_f2, kI_f2)
X = [1, 2, 3, 1, 2, 3]
Y = [i_f1, e_f1, I_f1, ki_f1, ke_f1, kI_f1]
colors = ['red', 'red', 'red', 'green', 'green', 'green']

marker = ['^', '^', '^', 'o', 'o', 'o']

#plt.scatter(X, Y, s=[60, 60, 60, 60, 60, 60], c=colors)
plt.title('Распределение 1 формант по деревням')
plt.ylabel('Значение форманты')
plt.xlabel('Гласный')

dots = ['Dzhuen',  'Dzhuen', 'Dzhuen',"Naikhin", "Naikhin", "Naikhin"]
plt.xticks(X, ['i', 'e', 'I', 'i', 'e', 'I'])

for x, y, d, n, m in zip(X, Y, dots, colors, marker):
    plt.scatter(x, y, s=200, c=n, marker=m)
    plt.text(x+0.1, y+7, d)
#plt.xticks(X, ['i', 'e', 'I'])

plt.show()

L = ["i", "e", "I", "i", "e", "I"]
M = [i_f2, e_f2, I_f2, ki_f2, ke_f2, kI_f2]
colors = ['red', 'red', 'red', 'green', 'green', 'green']

marker = ['^', '^', '^', 'o', 'o', 'o']

#plt.scatter(X, Y, s=[60, 60, 60, 60, 60, 60], c=colors)
plt.title('Распределение 2 формант по деревням')
plt.ylabel('Значение форманты')
plt.xlabel('Гласный')

dots = ['Dzhuen',  'Dzhuen', 'Dzhuen',"Naikhin", "Naikhin", "Naikhin"]

for x, y, d, n, m in zip(L, M, dots, colors, marker):
    plt.scatter(x, y, s=200, c=n, marker=m)
    plt.text(x, y+5, d)

plt.show()        
  

