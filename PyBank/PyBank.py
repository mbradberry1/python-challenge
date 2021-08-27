import os
import csv

filepath = os.path.join('resources', 'budget_data.csv')

inc_month =[""]
dec_month =[""]
previous_val = 0
Total_Months = 1
Total = 0
Average_Change = 0
Greatest_Increase = 0
Greatest_Decrease = 0


with open(filepath, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)
    second_skip = next(csv_reader)
    previous_val = int(second_skip[1])
    Total = previous_val
    for row in csv_reader:
              
        Total_Months = Total_Months +1
        Total = Total + int(row[1])
        Average_Change = Average_Change + (int(row[1])-previous_val)
            
        if int(row[1]) - previous_val > Greatest_Increase:
            Greatest_Increase = int(row[1]) - previous_val
            inc_month = (row[0])
        elif int(row[1]) - previous_val < Greatest_Decrease:
            Greatest_Decrease = int(row[1]) - previous_val
            dec_month = (row[0])
        previous_val = int(row[1])   
    Average_Change = Average_Change/(Total_Months-1)

print("Total:", Total)
print("Total Months:", Total_Months)
print("Average  Change:", round(Average_Change,2))
print("Greatest Increase in Profits:", inc_month,":", Greatest_Increase)
print("Greatest Decrease in Profits:", dec_month,":", Greatest_Decrease)

f = open("Financial Analysis.txt", "w")
f.write("Financial Analysis")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total:"+ str(Total))
f.write('\n')
f.write("Total Months:" + str(Total_Months))
f.write('\n')
f.write("Average Change:" + str(Average_Change))
f.write('\n')
f.write(f"Greatest Increase in Profits: {inc_month}:{Greatest_Increase}")
f.write('\n')
f.write(f"Greatest Decrease in Profits: {dec_month}:{Greatest_Decrease}")