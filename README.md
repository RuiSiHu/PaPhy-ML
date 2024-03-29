# PaPhy-ML
PaPhy-ML uses [MAFFT v7.508](https://mafft.cbrc.jp/alignment/software/) (Katoh and Standley, 2013), [HAlign v3.0.0_rc1](http://lab.malab.cn/soft/halign/) (Tang, et al., 2022), [WMSA v0.4.3](https://github.com/malabz/WMSA/) (Wei, et al., 2022), and [MUSCLE v5.1](https://www.drive5.com/muscle/) (Edgar, 2021) as alignment software. In general, MSA results have poorly aligned regions at both ends, which we automatically trimmed using [trimAI v1.4.1](http://trimal.cgenomics.org/trimal) (Capella-Gutierrez, et al., 2009) to remove non-alignment parts. This trimming method has been shown to be particularly suitable for subsequent phylo-genetic analyses. We selected four ML-based phylogenetic programs, namely [RAxML v8.2.12](https://cme.h-its.org/exelixis/web/software/raxml/) (Stamatakis, 2014), [PhyML v3.3.20190909](http://www.atgc-montpellier.fr/phyml/usersguide.php) (Guindon, et al., 2010), [FastTree v2.1.11](http://www.microbesonline.org/fasttree/) (Price, et al., 2010), and [IQ-TREE v2.0.4](http://www.iqtree.org/) (Nguyen, et al., 2015). 

Please use command `python PaPhyML.py -h` for help

# Usage example
```bash
python PaPhyML.py -f test.fas -a halign -t raxmlHPC -n
```

# References

Capella-Gutierrez, S., Silla-Martinez, J.M. and Gabaldon, T. trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses. *Bioinformatics* 2009;25(15):1972-1973.  
Edgar, R.C. Muscle5: High-accuracy alignment ensembles enable unbiased assessments of sequence homology and phylogeny. *Nat Commun* 2022;13(1):6968.  
Guindon, S., et al. New algorithms and methods to estimate maximum-likelihood phylogenies: assessing the performance of PhyML 3.0. *Systematic biology* 2010;59(3):307-321.  
Katoh, K. and Standley, D.M. MAFFT multiple sequence alignment software version 7: improvements in performance and usability. *Mol Biol Evol* 2013;30(4):772-780.  
Nguyen, L.T., et al. IQ-TREE: a fast and effective stochastic algorithm for estimating maximum-likelihood phylogenies. *Mol Biol Evol* 2015;32(1):268-274.  
Price, M.N., Dehal, P.S. and Arkin, A.P. FastTree 2--approximately maximum-likelihood trees for large alignments. *PLoS One* 2010;5(3):e9490.  
Stamatakis, A. RAxML version 8: a tool for phylogenetic analysis and post-analysis of large phylogenies. *Bioinformatics* 2014;30(9):1312-1313.  
Tang, F., et al. HAlign 3: Fast Multiple Alignment of Ultra-Large Numbers of Similar DNA/RNA Sequences. *Mol Biol Evol* 2022;39(8).  
Wei, Y., et al. WMSA: a novel method for multiple sequence alignment of DNA sequences. *Bioinformatics* 2022;38(22):5019-5025.  

