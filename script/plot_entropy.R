#R code
library(ggplot2)
library(scales)
library(RColorBrewer)
library(readr)
library(tidyr)
library(reshape)
library(stringr)
library(dplyr)
library(ggrepel)
library(gridExtra)
require(cowplot)

textsize <- 7
entropy_table <- read_tsv('result/Epitope_seq_entropy.tsv')
p <-  ggplot(entropy_table, aes(x=class,y=entropy,color=class,fill=class)) +
        geom_boxplot(color='black',fill='white',coef=500)+
        #geom_jitter(position=position_jitter(0.2),size=0.5, pch=20) +
        geom_point(position=position_jitter(width=0.2),size=0.8, color='black', pch=21) +
        scale_fill_manual(values=c('blue','orange','yellow2')) +
        theme(axis.text=element_text(size=textsize,face="bold",colour = 'black'),
              axis.text.x=element_text(angle=90,hjust=1,vjust=0.5,colour = 'black'),
              axis.text.y=element_text(hjust=0.5,vjust=0.5,colour = 'black'),
              axis.title=element_text(size=textsize,face="bold"),
              axis.line = element_line(colour = 'black', size = 0),
              legend.position="none",
              legend.title=element_blank(),
              panel.border = element_rect(colour = "black", fill=NA, size=1)) +
        xlab('')+
        ylab('Sequence Entropy')
ggsave('graph/entropy_distribution.png', p, height=2.5,width=2)
