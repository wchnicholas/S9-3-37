#R code
library(ggplot2)
library(data.table)
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

Dgene_table <- read_tsv('result/Compare_OAS.tsv') %>%
                 mutate(ILTG_freq = ILTG_count/Total_count) %>%
                 mutate(LRYFDWL_freq = LRYFDWL_count/Total_count) %>%
                 select(Sample, ILTG_freq, LRYFDWL_freq) 
Sample_levels <- Dgene_table$Sample
setDT(Dgene_table)
Dgene_table <- melt(Dgene_table, id=c("Sample")) %>%
                 mutate(Sample=factor(Sample,levels=Sample_levels))
print (Dgene_table)
textsize <- 7
colorscale  <- c(brewer.pal(8,"Set3"))[1:3]
p <-  ggplot(Dgene_table, aes(x=Sample, y=log10(value), color=variable, fill=variable)) + 
	geom_point(colour="black",pch=21) +
	theme(plot.title=element_text(size=textsize,face="bold"),
	      axis.title=element_text(size=textsize,face="bold"),
	      axis.text=element_text(size=textsize,face="bold"),
	      axis.text.x=element_text(angle = 90, hjust = 1,size=textsize, vjust=0.5,face="bold"),
	      legend.key.size=unit(0.6,'lines'),
	      legend.title=element_blank(),
	      legend.text=element_text(size=textsize,face="bold"),
	      legend.position='bottom') +
        scale_fill_manual(values=colorscale,drop=FALSE) +
        scale_y_continuous(breaks=c(-4,-3,-2,-1),labels=c('0.01','0.1','1','10'),limits=c(-4.3,-1)) +
	ylab(bquote(bold('Frequency (%)'))) +
	xlab(bquote(bold('')))
ggsave('graph/Compare_OAS.png',p,height=3,width=4)
