def ConvertDollerToTAKA(Dollar, rateOfExchange):
    TAKA = Dollar * rateOfExchange
    return TAKA
print("TOTAL AMOUNT:",ConvertDollerToTAKA(int(input("Enter the amount in Dollar: ")),int(input("Enter the Exchange rate: "))),"TAKA")