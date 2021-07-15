python3 methylFASTQ.py -i ../../../data_write_myself/final/ref.fa -o ../../../data_write_myself/final/ --seq paired_end --lib directional --cg 0.5 --chg 0 --chh 0 --read 50 --error 0

bwameth.py index ref.fa
bwa index -a bwtsw ref.fa.bwameth.c2t
bwameth.py --reference ref.fa ref_pe_f50r50_dir_R1.fastq > read.sam

插入變異

samtools view -S -b new_read.sam > new_read.bam
samtools sort new_read.bam -o new_read.sorted.bam
samtools index new_read.sorted.bam 

./eagle/eagle -v data_write_myself/final/DIY.vcf -a data_write_myself/final/new_read.sorted.bam -r data_write_myself/final/ref.fa > data_write_myself/final/output.tab
