words_upto_19 = [' ', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
words_for_tens = [' ', ' ', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']
n = int(input("Enter an integer from 1 to 99:-  "))

if n == 0:
    output = 'ZERO'
elif n<= 19:
    output = words_upto_19[n]
elif n<=99:
    output = words_for_tens[n//10] + ' ' + words_upto_19[n%10]
else:
    print("Please enter values only from 1 to 99")
print(output)
print("THANK YOU!")
