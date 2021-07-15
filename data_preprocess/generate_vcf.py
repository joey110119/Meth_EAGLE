import random

############################
# input: ref
# output: vcf
# description: A->T
############################
f_in = open("../final/ref.fa", "r")
line = f_in.readline()
line = f_in.readline()
ref = []
while line!='':
    for i in line:
        if i=='A':
            if random.random()>0.7:
                ref.append(1)
            else:
                ref.append(0)
        elif i=='T' or i=='C' or i=='G':
            ref.append(0)
    line = f_in.readline()


f_out = open("../final/DIY.vcf", "w")
f_out.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')
var_happen = []
index = 1
for i in ref:
    if i==1:
        f_out.write('test\t'+str(index)+'\ttest\tA\tT\t1.0\t.\t.\n')
        var_happen.append(index)
    index+=1


############################
# input: var_happen (python3 list), read file
# output: new read file
# description: top strand: A->T; reverse strand: T->A
############################

# f_in2 = open('small/ref_pe_f50r50_dir_R1.fastq', 'r')
# f_out2 = open('small/newread.fastq', 'w')
# while True:
#     line1 = f_in2.readline()
#     if line1=='':
#         break
#     line2 = f_in2.readline()
#     line3 = f_in2.readline()
#     line4 = f_in2.readline()
    
#     # forward or not
#     forward = 0
#     #print( (line1.split(':'))[2][0] )
#     if (line1.split(':'))[2][0] =='f':
#         forward = 1
        
#     # position
#     pos = int((line1.split(':'))[1])

#     f_out2.write(line1)
#     if forward:
#         print('f')
#         for point in line2:
#             if point =='A':
#                 f_out2.write('T')
#             else:
#                 f_out2.write(point)
#     else:
#         print('r')
#         plus = 49
#         for point in line2:
#             if point=='T' and (pos+plus) in var_happen:
#                 f_out2.write('A')
#             else:
#                 f_out2.write(point)
#             plus-=1
#     #f_out2.write('\n') #line2
#     f_out2.write(line3)
#     f_out2.write(line4)