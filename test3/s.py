class SortSh:
    def shellSort(self, list):
        distance = len(list) // 2
        while distance > 0:
            for i in range(distance, len(list)):
                temp = list[i]
                j = i
                while j >= distance and list[j-distance] > temp:
                    list[j] = list[j - distance]
                    j -= distance
                list[j] = temp
            distance = distance // 2
        return list