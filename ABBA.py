input_data = open('input.txt', 'r') 
data= input_data.read() 
#-------------------------------------------------------------------------
data = data.split()
ans = str(max(int(data[0]), int(data[1]), int(data[2])))




#-------------------------------------------------------------------------
output_data = open('output.txt', 'w') 
output_data.write(str(ans)) 

input_data.close() 
output_data.close()