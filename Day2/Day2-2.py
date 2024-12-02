f = open("C:/dev/AdventOfCode/2024/Day2/input.txt", "r").readlines()

safe_count = 0

for i in range(len(f)):
    f[i] = f[i].replace("\n", "").split(" ")
    for j in range(len(f[i])):
        f[i][j] = int(f[i][j])
    
    report_safe = False

    for removed_index in range(len(f[i])):
        new_f = f[i][:]
        del new_f[removed_index]

        variant_safe = True
        ascending = new_f[0] < new_f[1]
        
        for j in range(len(new_f) - 1):
            if abs(new_f[j] - new_f[j+1]) > 3 or (ascending == True and new_f[j] >= new_f[j+1]) or (ascending == False and new_f[j] <= new_f[j+1]):
                variant_safe = False
                break
        
        if variant_safe:
            report_safe = True
            break
    
    if report_safe == True:
        safe_count += 1
    


print(safe_count)
