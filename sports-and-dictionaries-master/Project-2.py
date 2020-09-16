def main():

    filename = 'data.txt'
    readFile(filename)
    readFile(filename, True)
    readFile(filename, False)

def readFile(filename, winner = None):

    data = {}
    infile = open(filename, 'r')

    team = infile.readline()
    while team != '':
        
        PPG = infile.readline()
        PAPG = infile.readline()
        RPG = infile.readline()
        FG = infile.readline()
        SPG = infile.readline()
        win = infile.readline()

        team = team.rstrip('\n')
        PPG = PPG.rstrip('\n')
        PAPG = PAPG.rstrip('\n')
        RPG = RPG.rstrip('\n')
        FG = FG.rstrip('\n')
        SPG = SPG.rstrip('\n')
        win = win.rstrip('\n')

        if winner == True:
            if win == 'True':
                data[team] = [float(PPG), float(PAPG), float(RPG),
                              float(FG), float(SPG)]
        elif winner == False:
            if win == 'False':
                data[team] = [float(PPG), float(PAPG), float(RPG),
                              float(FG), float(SPG)]
        else:
            data[team] = [float(PPG), float(PAPG), float(RPG),
                          float(FG), float(SPG)]

        team = infile.readline()

    infile.close()

    if winner == True:
        print('Here is a dictionary of all winning teams: ')
        print()
    elif winner == False:
        print('Here is a dictionary of all nonwinning teams: ')
        print()
    else:
        print('Here is a dictioary of all teams: ')
        print()
        
    for key in data:
        print(key, ':', data[key])

    analyze(data)

def analyze(data):
    # Convert all dictionary values to list.
    stats = list(data.values())
    # Join lists.
    stats_list = sum(stats, [])

    # Convert to separate lists for each stat.
    PPG = stats_list[::5]
    PAPG = stats_list[1::5]
    RPG = stats_list[2::5]
    FG = stats_list[3::5]
    SPG = stats_list[4::5]

    # Calculate average of each stat.
    total = 0.0
    for v in PPG:
        total += v
    PPG_avg = total / len(PPG)

    total = 0.0
    for v in PAPG:
        total += v
    PAPG_avg = total / len(PAPG)

    total = 0.0
    for v in RPG:
        total += v
    RPG_avg = total / len(RPG)

    total = 0.0
    for v in FG:
        total += v
    FG_avg = total / len(FG)

    total = 0.0
    for v in SPG:
        total += v
    SPG_avg = total / len(SPG)

    # Place averages into list and format to correct decimal place.
    avg_list = [PPG_avg, PAPG_avg, RPG_avg, FG_avg, SPG_avg]
    avg_list = ['%.2f' % x for x in avg_list]

    # Print table of min, max, and avg of each statistic.
    print()
    print('Here are the minimum, maximum, and average of each statistic' \
          + '\nfor this set of teams:')
    print('\tPPG\tPAPG\tRPG\tFG\tSPG')
    print('MIN' + '\t' + str(min(PPG)) + '\t' + str(min(PAPG)) + '\t' \
          + str(min(RPG)) + '\t' + str(min(FG)) + '\t' + str(min(SPG)))
    print('MAX' + '\t' + str(max(PPG)) + '\t' + str(max(PAPG)) + '\t' \
          + str(max(RPG)) + '\t' + str(max(FG)) + '\t' + str(max(SPG)))
    print('AVG' + '\t' + (avg_list[0]) + '\t' + (avg_list[1]) + '\t' + \
          (avg_list[2]) + '\t' + (avg_list[3]) + '\t' + (avg_list[4]))
    print()
    
    
    

    
    
    

    
