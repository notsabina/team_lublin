


def main():
    n = int(input())
    tab = [[0 for i in range(6)] for i in range(n)]
    #zapisywanie wyników
    for i in range(n):
        dane = input()
        tab[i] = dane.split()

    punkty = [0 for i in range(n)]
    for i in range(n):
        for j in range(1,6):
            punkty[i] = punkty[i] + int(tab[i][j])

    dict = {}
    for i in range(n):
        dict[tab[i][0]] = punkty[i]

    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get,reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = dict[w]

    places = [i+1 for i in range(n)]
    for i in range(1,n):
        if list(sorted_dict.values())[i] == list(sorted_dict.values())[i-1]:
            places[i] = places[i-1]

    for i in range(n):
        print(str(places[i])+" "+str(list(sorted_dict.keys())[i])+" "+str(list(sorted_dict.values())[i]))


        

if __name__ == '__main__':
    main()