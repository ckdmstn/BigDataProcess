#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']

row_id = 1;
number = 0;
score = {} 
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
		if sum_v not in score:
			score[sum_v] = 1
		else:
			score[sum_v] += 1
		number += 1
	row_id += 1

sorted_score = sorted(score.items(), key = lambda item: item[0], reverse = True)
dictionary = dict(sorted_score)
score_list = list(dictionary.keys())
grade = [int(number*0.15), int(number*0.3), int(number*0.5), int(number*0.7), int(number*0.85)]

count = 0
for i in range(len(score_list)):
	row_id = 1
	score = float(score_list[i])
	count += int(dictionary[score_list[i]])
	for row in ws:
		if ws.cell(row = row_id, column = 7).value == score:
			if count <= grade[0]:
				ws.cell(row = row_id, column = 8).value = "A+"
			elif count <= grade[1]:
				ws.cell(row = row_id, column = 8).value = "A0"
			elif count <= grade[2]:
				ws.cell(row = row_id, column = 8).value = "B+"
			elif count <= grade[3]:
				ws.cell(row = row_id, column = 8).value = "B0"
			elif count <= grade[4]:
				ws.cell(row = row_id, column = 8).value = "C+"
			else:
				ws.cell(row = row_id, column = 8).value = "C0"
		row_id += 1

wb.save( "student.xlsx" )
