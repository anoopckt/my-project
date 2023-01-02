# a=[2,4,1,7,5]
# n=len(a)
# b=[]
# # for i in range(n):
# #     for k in range(n-1):
        

# #         print(a[k])
# # #print(b)        
# #     #print(a[i])
# for i in range(0,len(a)):  
#     #print(a[i])
#     for j in range(len(a)-1):  
#         print(a[j])
#         if(a[j]>a[j+1]):   
#                 # here we are not using temp variable  
#             a[j],a[j+1] = a[j+1], a[j]    
#     print(a[j])            
                
# # for i in range(len(a)):
# #     for j in range(len(a)):
# #         if j[i]>[i+1]:
# #             print(a[i])
              
        
# #print(b)
# def bubble_sort(list1):  
#     # Outer loop for traverse the entire list  
#     for i in range(0,len(list1)-1):  
        
#         print(list1[i])
#         # for j in range(len(list1)-1):  
#         #     print(list1[i],list1[j])
#     #         if(list1[j]>list1[j+1]):   
#     #             # here we are not using temp variable  
#     #             list1[j],list1[j+1] = list1[j+1], list1[j]  
#     # return list1  
  
# list1 = [5, 3, 8, 6, 7, 2]  
# print("The unsorted list is: ", list1)  
# # Calling the bubble sort function  
# print("The sorted list is: ", bubble_sort(list1))  
a=[1,4,5,6,2]
n=len(a)
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)       