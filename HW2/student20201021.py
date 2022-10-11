#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']

row_id = 1;
number = 0;
score = []
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
		score.append(ws.cell(row = row_id, column = 7).value)
		number += 1
	row_id += 1

score.sort()
score.reverse()
grade = [number*0.15, number*0.3, number*0.5, number*0.7, number*0.85]

count = 1;
for s in range(len(score)):
	if s+1 == len(score) or score[s] != score[s+1]:
		row_id = 1;
		for row in ws:
			if ws.cell(row = row_id, column = 7).value == score[s]:
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
	count += 1

wb.save( "student.xlsx" )
