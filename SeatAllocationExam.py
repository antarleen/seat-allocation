# GRAPHICALLY REPRESENTING A CLASS AS A SET OF EDGES AND NODES
from collections import defaultdict


class Graphs:
    def __init__(self):
        self.graph = defaultdict(list)
        self.allocation_list = defaultdict(int)

    def addEdge(self, origin, destination):
        self.graph[origin].append(destination)

    def makeGraphFromClass(self, bench_seating_columns, bench_seating_rows):
        no_of_seats = bench_seating_rows * bench_seating_columns * 2
        no_of_seats_per_row = bench_seating_rows * 2
        for i in range(1, no_of_seats - no_of_seats_per_row + 2, no_of_seats_per_row):
            for j in range(0, no_of_seats_per_row):
                for k in range(1, no_of_seats + 1):
                    # print(i + j, k)
                    if i + j <= no_of_seats and (i + j + 1 == k or i + j - 1 == k or i + j + no_of_seats_per_row == k or
                                                 i + j - no_of_seats_per_row == k) and i + j != k:
                        if not (((i + j) % no_of_seats_per_row == 0 and i + no_of_seats_per_row == k) or (
                                (i + j) % no_of_seats_per_row == 1 and i - 1 == k)):
                            self.addEdge(i + j, k)

    # NODE COLORING FUNCTION FOR THE GRAPH
    def graphColoring(self, graph_layout, v):
        result = [-1] * v
        result[0] = 0
        available = [False] * v
        for u in range(2, v + 1):
            for i in graph_layout[u]:
                if result[i - 1] != -1:
                    available[result[i - 1]] = True
            clr = 0
            while clr < v:
                if not available[clr]:
                    break
                clr += 1
            result[u - 1] = clr
            for i in graph_layout[u]:
                if result[i - 1] != -1:
                    available[result[i - 1]] = False
        for u in range(1, v + 1):
            self.allocation_list[u] = result[u - 1]

    def addSubject(self, sub, rem):
        sub_list = []
        for i in range(sub):
            if i % 2 == rem:
                sub_list.append(subject[i])
        return sub_list


if __name__ == '__main__':
    subject = []
    roll_no = []
    g1 = Graphs()
    bench_columns = int(input('Enter columns of benches in the class:'))
    bench_rows = int(input('Enter rows of benches in the class:'))
    subjects = int(input('Enter the number of subjects to assign:'))
    for i in range(subjects):
        subject.append(input('Enter the subjects in order to allocate:'))
        roll_no.append(int(input(f'Enter the starting roll no for {subject[i]}:')))
    g1.makeGraphFromClass(bench_rows, bench_columns)
    g1.graphColoring(g1.graph, bench_rows * bench_columns * 2)
    odd_subject_list = g1.addSubject(subjects, 1)
    even_subject_list = g1.addSubject(subjects, 0)
    odd_offset = 0
    even_offset = 0
    print(even_subject_list)
    print(odd_subject_list)
    for key in g1.allocation_list:
        if g1.allocation_list[key] == 0:
            even_offset %= len(even_subject_list)
            print(
                f'SEAT-ID:{key} --- ROLL NO:{roll_no[subject.index(even_subject_list[even_offset])]} --- BRANCH:{even_subject_list[even_offset]}')
            roll_no[subject.index(subject[g1.allocation_list[key] + even_offset])] += 1
            even_offset += 1
        elif g1.allocation_list[key] == 1:
            odd_offset %= len(odd_subject_list)
            print(
                f'SEAT-ID:{key} --- ROLL NO:{roll_no[subject.index(odd_subject_list[odd_offset])]}--- BRANCH:{odd_subject_list[odd_offset]}')
            roll_no[subject.index(subject[g1.allocation_list[key] + odd_offset])] += 1
            odd_offset += 1
