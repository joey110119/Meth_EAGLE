# Meth_EAGLE
## Meth_EAGLE Input
* reference file
* read file
* varaint calling file
## Meth_EAGLE Output
* original EAGLE output
    * one file 
    * variant likelihood
* Meth-EAGLE output
    * two files
    * deamination likelihood
## Floder Analysis
### /data
  * ref file (artificial data)
  * vcf file (generated by myself, in 'data_preprocess' floder)
  * bam file (already sorted)
  * sam file (inserted variant information by myself, in 'data_preprocess' floder)
  * .ch3 file (generated by simulator)
  * read file (generated by simulator)
### /data_preprocess
  * generate_vcf.py
    * generate artificial vcf file
  * replace_sam.py
    * inserted variant information into sam file
### /output
  * original EAGLE output
  * Meth-EAGLE outputs (two files)
### /scripts
  * original EAGLE floder

## Detailed Description
### Meth-EAGLE can do:
#### 1. "variant quality scores":
* As the general output of EAGLE, Meth-EAGLE can give "variant quality scores".
#### 2. "methylation quality scores":
* To remove the bias which may be generated by variants, Meth-EAGLE modifies the given reference sequence by the best variant set calculated by the previous procedure.
* Supposing all CpG sites are the potential methylated cites, Meth-EAGLE uses this modified reference sequence to calculate the "methylation quality scores" of all CpG sites.
