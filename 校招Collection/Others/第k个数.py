# -*- coding:utf-8 -*-
# https://www.nowcoder.com/practice/d5e776441a6e41ae9f9859413bdc1eca

class KthNumber:
    def findKth(self, k):
        # write code here
        a = [1, 3, 5, 7, 9, 15, 21, 25, 27, 35, 45, 49, 63, 75,
             81, 105, 125, 135, 147, 175, 189, 225, 243, 245, 315,
             343, 375, 405, 441, 525, 567, 625, 675, 729, 735, 875,
             945, 1029, 1125, 1215, 1225, 1323, 1575, 1701, 1715,
             1875, 2025, 2187, 2205, 2401, 2625, 2835, 3087, 3125,
             3375, 3645, 3675, 3969, 4375, 4725, 5103, 5145, 5625,
             6075, 6125, 6561, 6615, 7203, 7875, 8505, 8575, 9261,
             9375, 10125, 10935, 11025, 11907, 12005, 13125, 14175,
             15309, 15435, 15625, 16807, 16875, 18225, 18375, 19683,
             19845, 21609, 21875, 23625, 25515, 25725, 27783, 28125,
             30375, 30625, 32805, 33075]

        return a[k]