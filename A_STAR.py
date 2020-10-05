# -*- coding: utf-8 -*-


"""
Created on Fri Sep 11 10:35:02 2020

@author: ARRAFI
"""
import FILEREAD as F


class a_Star(F.FileRead):

    def __init__(self, path, start, goal):
        self.start = start
        self.goal = goal
        self.wd = dict()
        self.wd = self.readFile(path)
        self.astar()

    def priorityQueue(self, d, que, cost):

        keys = list()
        values = list()
        accost = dict()
        for j in d:
            keys.append(j)
            temp = (d[j][0] + d[j][1])
            values.append(temp)
            accost[temp] = d[j]

        def heapSort(l):
            l1 = list()

            def minHeapify(l):
                for i in range(len(l)):
                    left = 2 * i + 1
                    right = 2 * i + 2
                    if left < len(l) and l[left] < l[i]:
                        l[left], l[i] = l[i], l[left]
                        minHeapify(l)
                    if right < len(l) and l[right] < l[i]:
                        l[right], l[i] = l[i], l[right]
                        minHeapify(l)
                return l

            while len(l) > 0:
                minHeapify(l)
                l[0], l[len(l) - 1] = l[len(l) - 1], l[0]
                l1.append(l.pop())
            l.clear()
            for i in l1:
                l.append(i)
            return l

        heapSort(values)
        que.clear()

        for j in range(len(values)):
            values[j] = accost[values[j]][0]

        for j in values:
            for key, value in d.items():
                if len(que) == len(keys):
                    break
                if value[0] == j:
                    que.append(key)

        if len(que) > 0:
            d.pop(que[0])
        if len(values) > 0:
            cost = values[0]
        return cost

    def astar(self):
        visited = list()
        dtemp = dict()
        que = list()
        path = dict()
        cost = 0
        temp = self.start
        que.append(temp)
        while len(que) > 0:
            temp = que.pop(0)
            if temp == self.goal:
                path[temp] = cost
                break
            if visited.count(temp) == 0:
                if self.wd[temp] is not None:
                    for i in self.wd[temp]:
                        self.wd[temp][i][0] = self.wd[temp][i][0] + cost
                        dtemp[i] = self.wd[temp][i]
                        que.append(i)
                    visited.append(temp)
                else:
                    visited.append(temp)
                path[temp] = cost
                cost = self.priorityQueue(dtemp, que, cost)

        if temp == self.goal:
            print("starting search-->", end=" ")
            for i in path:
                print(i, "-->", end=" ")
            print("reached GOAL")
            print("astar sol: ", cost)

        else:
            print("No path exist")

        return None
