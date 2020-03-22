data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢，總共有', len(data),'筆資料。')

sum_len = 0  #為何要先設定為0?
for d in data:
	sum_len = sum_len + len(d)

print('每筆留言平均長度為', sum_len/len(data),'個字')
# 剩下留言長度加總以及平均長度的計算。
# len是長度，len(d)是d的長度，d是data內的每一筆資料。len(d)為每一筆資料的長度。