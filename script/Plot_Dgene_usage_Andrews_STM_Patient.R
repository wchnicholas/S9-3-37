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

HDusage_by_subject_bar_plot <- function(table_summary){
  textsize <- 7
  p <-  ggplot(table_summary, aes(Subject, HD39_percent*100)) + 
	  geom_bar(stat="identity",position=position_dodge()) +
	  theme(plot.title=element_text(size=textsize,face="bold"),
		axis.title=element_text(size=textsize,face="bold"),
		axis.text=element_text(size=textsize,face="bold"),
		axis.text.x=element_text(angle = 90, hjust = 0.5,size=textsize, vjust=0.5,face="bold"),
		legend.key.size=unit(0.6,'lines'),
		legend.title=element_blank(),
		legend.text=element_text(size=textsize,face="bold"),
		legend.position='right') +
	  scale_y_continuous(breaks=c(0,20,40,60,80,100),labels=c('0','20','40','60','80','100'),expand=c(0,0),limits=c(0,100)) +
	  scale_fill_manual(values=c('gray30','gray70'),drop=FALSE) +
	  ylab(bquote(bold('D3-9 gene segment usage (%)'))) +
	  xlab(bquote(bold('')))
  ggsave('graph/HD39_Andrews_STM_Patient_usage.png',p,height=2.5,width=3)
  }

table_summary <- read_tsv('result/Dgene_Andrews_STM_Patient_summary.tsv') %>%
                   mutate(HD39_percent=HD39_count/Total_count) %>%
                   mutate(Other_count=HD39_count-ILTG_count-LRYFDWL_count) %>%
                   mutate(Subject=factor(Subject,levels=Subject))
HDusage_by_subject_bar_plot(table_summary)

