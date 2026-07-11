user=input("ENTER ANYTHING TO CHECK PALINDROME OR NOT:")
lar=len(user)
for i in user:
    if i==user[lar-1]:
        lar=lar-1
    else:
        print( "NOT PALINDROME")
        quit()
print("PALINDROME")
