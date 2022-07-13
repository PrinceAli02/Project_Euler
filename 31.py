# 200a + 100b + 50c + 20d + 10e + 5f + 2g + h
count = 0
for a in range (2):
    for b in range (3):
        val = 200*a + 100*b
        if val == 200:
            count += 1
            break
        if val > 200:
            break
        for c in range (5):
            val = 200*a + 100*b + 50*c
            if val == 200:
                count += 1
                break
            if val > 200:
                break
            for d in range (11):
                val = 200*a + 100*b + 50*c + 20*d
                if val == 200:
                    count += 1
                    break
                if val > 200:
                    break
                for e in range (21):
                    val = 200*a + 100*b + 50*c + 20*d + 10*e
                    if val == 200:
                        count += 1
                        break
                    if val > 200:
                        break
                    for f in range (41):
                        val = 200*a + 100*b + 50*c + 20*d + 10*e + 5*f
                        if val == 200:
                            count += 1
                            break
                        if val > 200:
                            break
                        for g in range (101):
                            val = 200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g
                            if val == 200:
                                count += 1
                                break
                            if val > 200:
                                break
                            for h in range (201):
                                val = 200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g + h
                                if val == 200:
                                    count += 1
                                    break
                                if val > 200:
                                    break
print (count)