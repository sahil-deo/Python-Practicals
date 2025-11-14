salaries = [10000, 20000, 30000, 22000, 33000, 15000, 54000, 45000, 23000]

def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if salaries[i] > salaries[j]:
                temp = salaries[i]
                salaries[i]=salaries[j]
                salaries[j]=temp
    return l



def selection_sort(l):
    for i in range(len(l)-1):
        min_index = i   
        for j in range(i+1, len(l)):
            if salaries[j] < salaries[min_index]:
                min_index=j
        salaries[i],salaries[min_index]=salaries[min_index],salaries[i]

    return l

sorted_1 = bubble_sort(salaries)
sorted_2 = selection_sort(salaries)
print("Salaries:", salaries)
print("Bubble Sort:", sorted_1)
print("Selection Sort:", sorted_2)
print("Top 5 Salaries:", sorted_1[len(sorted_1)-5:])
