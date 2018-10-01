print("Hello World!!!")
read_five_times = "No"
count = 0
while read_five_times == "No":
    print ("Reading workshop..")
    count = count + 1
    if(count == 5):
        read_five_times = "Yes"

print ("Good Job ! You understood the workshop.")
