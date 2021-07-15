#############################################
# 讀入 sam file                              #
# 依據 vcf 去直接改 sam file                  #
# 記得 反股 以及 反轉 的事情                    #
#############################################
f_in = open("../final/read.sam", "r")
f_in2 = open('../final/DIY.vcf', 'r')
f_out = open("../final/new_read.sam", "w")
line = f_in.readline()
f_out.write(line)
line = f_in.readline()
f_out.write(line)
line = f_in.readline()
f_out.write(line)
line = f_in.readline()



##############################
# 記下所有 vcf 的 position
# pos = []
##############################
pos = []
line2 = f_in2.readline()
line2 = f_in2.readline()
while line2!='':
    vcf_sp = line2.split('\t')
    pos.append(int(vcf_sp[1]))
    line2 = f_in2.readline()



##############################
# 開始改 sam file
# 產出為: small/new_read.sam
##############################
f = 1
line_number = 1
while line!='':
    print('at'+str(line_number))
    line_number+=1
    sp = line.split('\t')
    words = sp[9]
    replace = ''
    sam_pos = int((sp[0].split(':'))[1])
    if f==1:
        f = 0
        for i in words:
            if i =='A' and sam_pos in pos:
                replace+='T'
            else:
                replace+=i
            sam_pos+=1
    elif f==0:
        f = 1
        for i in words:
            if i =='A' and sam_pos in pos:
                replace+='T'
            else:
                replace+=i
            sam_pos+=1

    for i in range(len(sp)):
        if i!=9:
            f_out.write(sp[i])
        else:
            f_out.write(replace)
        if i!=len(sp)-1:
            f_out.write('\t')
    line = f_in.readline()