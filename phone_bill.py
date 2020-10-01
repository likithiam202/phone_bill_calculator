import math

class bill():

    def bill_calculator(self):
        min_free = 500 #minimum free minutes

        cost_month = 300 #monthly cost
        cost_per_min = 0.50 #cost per minute
        taxes = 5 #additional taxes to be paid

        min_used = int(input("how much mins was telephone used"))
        if min_used < min_free: 
            taxes = cost_month * 5 / 100
            monthly_bill = cost_month + taxes # if the usage is below free limit

        else:
            extra_usage = min_used - min_free
            print(extra_usage)
            extra_cost = extra_usage * cost_per_min
            taxes = (cost_month + extra_cost) * 12.5 / 100
            monthly_bill = cost_month + extra_cost + taxes #calculating the excess usage

        print("ur monthly bill is: ", monthly_bill)


bill.bill_calculator(0)
