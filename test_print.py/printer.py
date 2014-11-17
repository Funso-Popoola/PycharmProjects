res = ""
for i in range(1, 13):

    for j in range(1, 13):
        output = ""
        
        prdt = i * j
        if(prdt > 9):
            if(prdt > 99):
                output = str(prdt)
            else:
                if(j >= 9):
                    output = " " + str(prdt)
                else:
                    output = str(prdt)
        else:
            if(j >= 9):
                output = "  " + str(prdt)
            else:
                output = " " + str(prdt)

        res += output + " "
    res += "\n"
print res