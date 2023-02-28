kitty = 500
requests = []

# open file and append all lines within file to requests
# while taking away escape character at the end of each line
with open('loan_requests.txt', 'r+') as file:
    for line in file:
        if "\n" in line:
            requests.append(int(line[:-1]))

with open('loan_requests.txt', 'a+') as file:

    file.write('\n')

    for i in range(len(requests)):
        if requests[i] < kitty:
            print(requests[i], '- Paid!')
            file.write('Request of ' + str(requests[i]) + ' paid in full\n')
            kitty = kitty - requests[i]
        elif requests[i] > kitty and kitty > 0:
            print(requests[i], 'cannot be processed in full (Insufficient funds available). Amount paid:', kitty)
            file.write('Request of ' + str(requests[i]) + ' could not be paid in full. Parital payment of ' + str(kitty) + ' made\n')
        else:
            kitty = 0
            print("Request of", requests[i], 'is unpaid')
            file.write('Outstanding Request:'+ str(requests[i]) + '\n')