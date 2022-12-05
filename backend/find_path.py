import heapq
import json

def dijkstra(graph, first, last):
    distance = {node:[float('inf'), first] for node in graph}
    distance[first] = [0, first]
    queue = []

    heapq.heappush(queue, [distance[first][0], first])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node][0] < current_distance:
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node][0]:
                distance[next_node] = [total_distance, current_node]
                heapq.heappush(queue, [total_distance, next_node])

    path = last
    path_output = []
    path_output.append(last)
    while distance[path][1] != first:
        path_output.append(distance[path][1])
        path = distance[path][1]
    path_output.append(first)
    path_output.reverse()
    path_output.insert(0, distance[last][0])
    return path_output

graph1 = {
    '경영관': {'문화관':11, '사회과학관':57, 'QQ':63},
    '과학관': {'D':1, 'B':1},
    '다향관': {'M':5, 'WW':1},
    '만해관': {'법학관':63, '혜화관':54, 'F':33},
    '명진관': {'D':37, 'G':32},
    '문화관': {'경영관':11, '사회과학관':76, '학술관':15},
    '법학관': {'만해관':63, 'P':4},
    '본관': {'K':12, 'S':15},
    '사회과학관': {'경영관':57, '문화관':76, 'PP':1, 'QQ':46},
    '상록원': {'A':1, '대운동장':46},
    '신공학관': {'KK':25},
    '원흥관': {'Q':13, 'R':11, 'II':13},
    '정보문화관': {'VV':5, 'YY':5},
    '중앙도서관': {'H':12, 'Q':50},
    '학림관': {'체육관':56, 'X':50, 'EE':65},
    '학생회관': {'AA':5, 'BB':25},
    '학술관': {'문화관':15},
    '혜화관': {'만해관':54, 'OO':1},
    '혜화문': {'PP':85, 'NN':72},
    '대운동장': {'상록원':46, 'UU':12, 'TT':12},
    '체육관': {'학림관':56, 'W':37},
    '후문': {'EE':14},
    '만해광장': {'XX':1},
    '팔정도': {'F':49, 'P':39, 'O':49, 'N':39, 'L':49, 'K':39, 'J':49, 'G':39},
    'A': {'B':31, '상록원':1},
    'B': {'과학관':1, 'A':31, 'C':16},
    'C': {'B':16, 'D':46, 'H':54},
    'D': {'과학관':1, '명진관':37, 'C':46, 'E':43},
    'E': {'D':43, 'F':61},
    'F': {'E':61, 'G':38, '팔정도':49, 'P':35, '만해관':33, 'UU':110},
    'G': {'명진관':32, 'F':38, '팔정도':39, 'J':38},
    'H': {'C':54, '중앙도서관':12, 'I':16},
    'I': {'H':16, 'J':14},
    'J': {'I':14, 'Q':50, 'K':35, '팔정도':49, 'G':38},
    'K': {'J':35, '본관':12, 'L':35, '팔정도':39},
    'L': {'K':35, 'S':34, 'T':10, 'M':15, '팔정도':49},
    'M': {'L':15, '다향관':5, 'N':23},
    'N': {'팔정도':39, 'M':23, 'O':38},
    'O': {'팔정도':49, 'N':38, 'LL':43, 'P':35},
    'P': {'팔정도':39, 'O':35, '법학관':4, 'F':35},
    'Q': {'R':56, 'J':50, '중앙도서관':50, 'KK':32, '원흥관':13},
    'R': {'Q':56, '원흥관':11, 'JJ':36, 'S':30},
    'S': {'본관':15, 'R':30, 'L':34},
    'T': {'L':10, 'V':35, 'U':10},
    'U': {'T':10, 'WW':10},
    'V': {'T':35, 'XX':49, 'W':39},
    'W': {'V':39, '체육관':37},
    'X': {'학림관':50, 'Y':35},
    'Y': {'X':35, 'Z':20},
    'Z': {'Y':20, 'AA':26},
    'AA': {'학생회관':5, 'Z':26, 'FF':28},
    'BB': {'학생회관':25, 'CC':37},
    'CC': {'BB':37, 'DD':50},
    'DD': {'CC':50, 'EE':20},
    'EE': {'학림관':65, 'DD':20, '후문':14},
    'FF': {'YY':5, 'AA':28, 'GG':20},
    'GG': {'FF':20, 'HH':35},
    'HH': {'II':21, 'GG':35, 'JJ':35},
    'II': {'원흥관':13, 'VV':20, 'HH':21},
    'JJ': {'R':36, 'HH':35, 'XX':49},
    'KK': {'신공학관':25, 'Q':32},
    'LL': {'MM':41, 'O':43},
    'MM': {'LL':41, 'NN':77},
    'NN': {'OO':55, 'MM':77, '혜화문':72},
    'OO': {'혜화관':1, 'NN':55, 'PP':46},
    'PP': {'OO':46, '혜화문':85, '사회과학관':1},
    'QQ': {'경영관':63, 'RR':77, '사회과학관':46},
    'RR': {'QQ':77, 'SS':40},
    'SS': {'RR':40, 'TT':28},
    'TT': {'SS':28, '대운동장':12, 'UU':23},
    'UU': {'대운동장':12, 'TT':23, 'F':110},
    'VV': {'II':20, '정보문화관':5},
    'WW': {'다향관':1, 'U':10},
    'XX': {'만해광장':1, 'V':49, 'JJ':49},
    'YY': {'정보문화관':5, 'FF':5} 
}

graph2 = {
    '경영관': {'문화관':11, '사회과학관':57, 'QQ':63},
    '과학관': {'D':1, 'B':1},
    '다향관': {'M':5, 'WW':1},
    '만해관': {'법학관':63, '혜화관':54, 'F':33},
    '명진관': {'D':37, 'G':32},
    '문화관': {'경영관':11, '사회과학관':76, '학술관':15},
    '법학관': {'만해관':63, 'P':4},
    '본관': {'K':12, 'S':15},
    '사회과학관': {'경영관':57, '문화관':76, 'PP':1, 'QQ':46},
    '상록원': {'A':1, '대운동장':46},
    '신공학관': {'KK':25},
    '원흥관': {'Q':15, 'R':11, 'II':13},
    '정보문화관': {'VV':5, 'YY':5},
    '중앙도서관': {'H':12, 'Q':50},
    '학림관': {'체육관':71, 'X':50, 'EE':65},
    '학생회관': {'AA':5, 'BB':25},
    '학술관': {'문화관':15},
    '혜화관': {'만해관':54, 'OO':1},
    '혜화문': {'PP':89, 'NN':79},
    '대운동장': {'상록원':64, 'UU':12, 'TT':12},
    '체육관': {'학림관':56, 'W':55},
    '후문': {'EE':17},
    '만해광장': {'XX':1},
    '팔정도': {'F':49, 'P':39, 'O':49, 'N':39, 'L':49, 'K':39, 'J':49, 'G':39},
    'A': {'B':31, '상록원':1},
    'B': {'과학관':1, 'A':31, 'C':16},
    'C': {'B':16, 'D':46, 'H':54},
    'D': {'과학관':1, '명진관':37, 'C':46, 'E':43},
    'E': {'D':43, 'F':61},
    'F': {'E':61, 'G':38, '팔정도':49, 'P':35, '만해관':33, 'UU':110},
    'G': {'명진관':32, 'F':38, '팔정도':39, 'J':38},
    'H': {'C':54, '중앙도서관':12, 'I':16},
    'I': {'H':16, 'J':14},
    'J': {'I':14, 'Q':50, 'K':35, '팔정도':49, 'G':38},
    'K': {'J':35, '본관':12, 'L':35, '팔정도':39},
    'L': {'K':35, 'S':34, 'T':10, 'M':15, '팔정도':49},
    'M': {'L':15, '다향관':5, 'N':23},
    'N': {'팔정도':39, 'M':23, 'O':38},
    'O': {'팔정도':49, 'N':38, 'LL':43, 'P':35},
    'P': {'팔정도':39, 'O':35, '법학관':4, 'F':35},
    'Q': {'R':56, 'J':50, '중앙도서관':50, 'KK':32, '원흥관':13},
    'R': {'Q':56, '원흥관':11, 'JJ':36, 'S':30},
    'S': {'본관':15, 'R':30, 'L':39},
    'T': {'L':15, 'V':35, 'U':10},
    'U': {'T':10, 'WW':10},
    'V': {'T':41, 'XX':49, 'W':39},
    'W': {'V':58, '체육관':37},
    'X': {'학림관':50, 'Y':35},
    'Y': {'X':35, 'Z':20},
    'Z': {'Y':20, 'AA':26},
    'AA': {'학생회관':5, 'Z':26, 'FF':28},
    'BB': {'학생회관':28, 'CC':37},
    'CC': {'BB':40, 'DD':50},
    'DD': {'CC':54, 'EE':20},
    'EE': {'학림관':73, 'DD':22, '후문':14},
    'FF': {'YY':5, 'AA':28, 'GG':21},
    'GG': {'FF':20, 'HH':37},
    'HH': {'II':21, 'GG':35, 'JJ':37},
    'II': {'원흥관':13, 'VV':20, 'HH':21},
    'JJ': {'R':39, 'HH':35, 'XX':55},
    'KK': {'신공학관':25, 'Q':32},
    'LL': {'MM':41, 'O':51},
    'MM': {'LL':43, 'NN':77},
    'NN': {'OO':55, 'MM':101, '혜화문':72},
    'OO': {'혜화관':1, 'NN':55, 'PP':46},
    'PP': {'OO':46, '혜화문':85, '사회과학관':1},
    'QQ': {'경영관':63, 'RR':77, '사회과학관':46},
    'RR': {'QQ':77, 'SS':47},
    'SS': {'RR':40, 'TT':33},
    'TT': {'SS':28, '대운동장':12, 'UU':27},
    'UU': {'대운동장':12, 'TT':23, 'F':125},
    'VV': {'II':20, '정보문화관':5},
    'WW': {'다향관':1, 'U':10},
    'XX': {'만해광장':1, 'V':55, 'JJ':49},
    'YY': {'정보문화관':5, 'FF':5} 
}

node_list = ['경영관', '과학관', '다향관', '만해관', '명진관', '문화관', '법학관', '본관', '사회과학관', '상록원', '신공학관', '원흥관', '정보문화관', '중앙도서관', '학림관', '학생회관', '학술관', '혜화관', '혜화문', '대운동장', '체육관', '후문', '만해광장', '팔정도']

path_all1 = {}
for start in node_list:
    path_start = {}
    for end in node_list:
      path_start[end] = dijkstra(graph1, start, end)
    path_all1[start] = path_start

path_all2 = {}
for start in node_list:
    path_start = {}
    for end in node_list:
      path_start[end] = dijkstra(graph2, start, end)
    path_all2[start] = path_start

file_path1 = "./frontend/src/path1.json"
with open(file_path1, 'w', encoding='utf-8') as outfile:
    json.dump(path_all1, outfile, ensure_ascii=False, indent=4)

file_path2 = "./frontend/src/path2.json"
with open(file_path2, 'w', encoding='utf-8') as outfile:
    json.dump(path_all2, outfile, ensure_ascii=False, indent=4)
