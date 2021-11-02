# 利用 methylFASTQ 產生出 read(.fastq file)
'''
python3 methylFASTQ.py -i ../../../data_write_myself/final/ref.fa -o ../../../data_write_myself/final/ --seq paired_end --lib directional --cg 0.5 --chg 0 --chh 0 --read 50 --error 0
'''

# 利用 bwameth 當作 alignmant tool
## .fastq file 和 .ref file 為 input
## .sam file 為 output
'''
bwameth.py index ref.fa
bwa index -a bwtsw ref.fa.bwameth.c2t
bwameth.py --reference ref.fa ref_pe_f50r50_dir_R1.fastq > read.sam
'''

# 自行插入變異(for 實驗)
插入變異

# 利用 smatools 把 .sam file 變成 .bam file 再變成 .sorted.bam file
'''
samtools view -S -b new_read.sam > new_read.bam
samtools sort new_read.bam -o new_read.sorted.bam
samtools index new_read.sorted.bam
'''

# eagle 的執行指令
'''
./eagle/eagle -v data_write_myself/final/DIY.vcf -a data_write_myself/final/new_read.sorted.bam -r data_write_myself/final/ref.fa > data_write_myself/final/output.tab
'''
