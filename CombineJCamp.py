from os import path, listdir

initialfilename = str(input("Enter Initial DX Filename without .DX extension"))+".DX"
seriesname = input("Series name, no .DX, no Xmin")
outputfilename = input("name of .txt file to output without .txt extension")+".txt"

print(initialfilename,seriesname,outputfilename)

initial_file = open(initialfilename, 'r')
old_line0 = ''
read_status = 'closed'
absorbance_matrix = [['Wavelength','0min']]
for line in initial_file:
    line_list = line.split(" ")
    if old_line0 == "##XYDATA=":
        read_status = 'open'
    if read_status == 'open' and line_list[0] == '##END=\n':
        read_status = 'closed'
    if read_status == 'open':
        absorbance_matrix.append([float(line_list[0]),float(line_list[1])])
    old_line0 = line_list[0]
    
pathname = '.'
dirlist = listdir(pathname)
dirlist.sort()
sliceendindex = len(seriesname)
column_index = 1
for filename in dirlist:
    if filename[0:sliceendindex] == seriesname and filename[-1:-4:-1] == 'XD.':
        column_index += 1
        file = open(filename, 'r')
        old_line0 = ''
        read_status = 'closed'
        line_index = 1
        absorbance_matrix[0].append(filename)
        print(file)
        for line in file:
            line_list = line.split(" ")
            if old_line0 == "##XYDATA=":
                read_status = 'open'
            if read_status == 'open' and line_list[0] == '##END=\n':
                read_status = 'closed'
            if read_status == 'open':
#                print(line_index,column_index)
                absorbance_matrix[line_index].append(float(line_list[1]))
                line_index += 1
            old_line0 = line_list[0]

output_file = open(outputfilename, 'w')
for index in range(0,len(absorbance_matrix)):
    for cell in absorbance_matrix[index]:
        output_file.write(str(cell)+' ')
    output_file.write('\n')

#print(absorbance_matrix)



