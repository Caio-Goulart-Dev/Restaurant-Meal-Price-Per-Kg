print ("Six SeventotaStore")
purchase_amount = float(input("Please, provide the total value of the costumer's purchase"))
payment_method = int(input("Select the payment method - 1: Credit Card or - 2: cash"))


if payment_method == 1:
    #discount
    total_purchase_with_discount = purchase_amount * 0,95
    print (f"The total cost of the purchase was ${purchase_amount:.2f} got a discount for paying in cash. The costumer will need to pay ${total_purchase_with_discount:.2f}.")


else:
    #installment
    installment = int(input(" specify the desired number of installments"))
    installment_amount = purchase_amount / installment

    print(f"the total value of the purchase ${purchase_amount: .2f} will be paid in{installment} installment of ${installment_amount: .2f}.")
