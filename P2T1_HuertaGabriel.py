#Input, Processing and Output of Sales within a Program
#9/4/19
#CTI-110 P2T1 - Sales Prediction
#Gabriel Huerta

#Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))

